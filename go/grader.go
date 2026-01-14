package main

import (
	"bytes"
	"context"
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
	"runtime"
	"strings"
	"time"

	"github.com/pmezard/go-difflib/difflib"
)

// ANSI Colors
const (
	HEADER = "\033[95m"
	BLUE   = "\033[94m"
	GREEN  = "\033[92m"
	RED    = "\033[91m"
	RESET  = "\033[0m"
	BOLD   = "\033[1m"
	YELLOW = "\033[93m"
)

// --- 파일 처리 및 파싱 함수 ---

func readFile(path string) string {
	b, err := os.ReadFile(path)
	if err != nil {
		if os.IsNotExist(err) {
			fmt.Printf("%s[Error] 파일을 찾을 수 없습니다: %s%s\n", RED, path, RESET)
			os.Exit(1)
		}
		fmt.Printf("%s[Error] 파일 읽기 실패: %s (%v)%s\n", RED, path, err, RESET)
		os.Exit(1)
	}

	s := string(b)
	s = strings.ReplaceAll(s, "\r\n", "\n")
	s = strings.ReplaceAll(s, "\r", "\n")
	return s
}

func parseCases(content string) []string {
	parts := strings.Split(content, "---")
	cases := make([]string, 0, len(parts))
	for _, p := range parts {
		c := strings.TrimSpace(p)
		if c == "" {
			continue
		}
		cases = append(cases, c)
	}
	return cases
}

func cleanLinesForCompare(s string) []string {
	s = strings.ReplaceAll(s, "\r\n", "\n")
	s = strings.ReplaceAll(s, "\r", "\n")
	s = strings.TrimSpace(s)

	if s == "" {
		return []string{}
	}

	lines := strings.Split(s, "\n")
	for i := range lines {
		lines[i] = strings.TrimRight(lines[i], " \t")
	}
	return lines
}

// --- 비교 로직 (수정됨: 줄바꿈 강제 처리) ---

func compareResults(expected, actual string) (bool, []string) {
	exp := cleanLinesForCompare(expected)
	act := cleanLinesForCompare(actual)

	// 완전히 동일한지 먼저 체크
	if len(exp) == len(act) {
		same := true
		for i := range exp {
			if exp[i] != act[i] {
				same = false
				break
			}
		}
		if same {
			return true, nil
		}
	}

	// [중요 수정] difflib가 줄을 합치지 못하도록 각 줄 끝에 강제로 \n을 붙입니다.
	// 그리고 UnifiedDiff의 Eol을 빈 문자열로 설정하여 중복 개행을 막습니다.
	// 이렇게 하면 difflib는 무조건 각 내용을 별도의 줄로 인식합니다.
	expWithNL := make([]string, len(exp))
	for i, v := range exp {
		expWithNL[i] = v + "\n"
	}
	actWithNL := make([]string, len(act))
	for i, v := range act {
		actWithNL[i] = v + "\n"
	}

	ud := difflib.UnifiedDiff{
		A:        expWithNL,
		B:        actWithNL,
		FromFile: "Expected",
		ToFile:   "Actual",
		Context:  3,
		Eol:      "", // 각 줄에 이미 \n이 있으므로 Eol은 비워둡니다.
	}

	diffText, _ := difflib.GetUnifiedDiffString(ud)

	// 결과 정제
	diffText = strings.ReplaceAll(diffText, "\r\n", "\n")
	diffText = strings.ReplaceAll(diffText, "\r", "\n")

	// Split을 할 때 마지막 빈 줄이 생길 수 있으므로 처리
	lines := strings.Split(diffText, "\n")
	var finalLines []string
	for _, l := range lines {
		// 줄바꿈만 있는 빈 줄이나, 공백만 있는 줄은 제외하되
		// diff 내용이 있는 경우는 보존
		if strings.TrimSpace(l) == "" {
			continue
		}
		finalLines = append(finalLines, l)
	}

	if len(finalLines) == 0 {
		return false, []string{}
	}
	return false, finalLines
}

// --- 빌드 및 실행 구조체 ---

type BuildResult struct {
	BinPath  string
	BuildLog string
	Duration time.Duration
	OK       bool
	Cleanup  func()
}

func buildMainGo(folderPath string) BuildResult {
	start := time.Now()

	tmpDir, err := os.MkdirTemp("", "grader-solution-*")
	if err != nil {
		return BuildResult{
			OK:       false,
			BuildLog: fmt.Sprintf("임시 폴더 생성 실패: %v", err),
			Duration: time.Since(start),
		}
	}

	cleanup := func() { _ = os.RemoveAll(tmpDir) }

	binName := "solution_bin"
	if runtime.GOOS == "windows" {
		binName += ".exe"
	}
	binPath := filepath.Join(tmpDir, binName)

	cmd := exec.Command("go", "build", "-o", binPath, "main.go")
	cmd.Dir = folderPath

	var buf bytes.Buffer
	cmd.Stdout = &buf
	cmd.Stderr = &buf

	err = cmd.Run()
	dur := time.Since(start)

	if err != nil {
		return BuildResult{
			OK:       false,
			BuildLog: buf.String(),
			Duration: dur,
			Cleanup:  cleanup,
		}
	}

	return BuildResult{
		OK:       true,
		BinPath:  binPath,
		BuildLog: buf.String(),
		Duration: dur,
		Cleanup:  cleanup,
	}
}

type RunResult struct {
	Stdout    string
	Stderr    string
	ExecTime  time.Duration
	Completed bool
}

func runSolution(binPath, workDir, inputData string, timeout time.Duration) RunResult {
	ctx, cancel := context.WithTimeout(context.Background(), timeout)
	defer cancel()

	cmd := exec.CommandContext(ctx, binPath)
	cmd.Dir = workDir
	cmd.Stdin = strings.NewReader(inputData + "\n")

	var outBuf, errBuf bytes.Buffer
	cmd.Stdout = &outBuf
	cmd.Stderr = &errBuf

	start := time.Now()
	err := cmd.Run()
	elapsed := time.Since(start)

	if ctx.Err() == context.DeadlineExceeded {
		return RunResult{Stdout: "", Stderr: "Timeout (5s Limit)", ExecTime: elapsed, Completed: false}
	}

	if err != nil {
		stderr := strings.TrimSpace(errBuf.String())
		if stderr == "" {
			stderr = err.Error()
		}
		return RunResult{Stdout: "", Stderr: stderr, ExecTime: elapsed, Completed: false}
	}

	return RunResult{Stdout: outBuf.String(), Stderr: errBuf.String(), ExecTime: elapsed, Completed: true}
}

// --- 메인 채점 로직 ---

func grade(folderPath string) {
	inputPath := filepath.Join(folderPath, "input.txt")
	outputPath := filepath.Join(folderPath, "output.txt")
	mainGoPath := filepath.Join(folderPath, "main.go")

	if _, err := os.Stat(mainGoPath); err != nil {
		fmt.Printf("%s[Error] main.go가 없습니다: %s%s\n", RED, folderPath, RESET)
		return
	}
	if _, err := os.Stat(inputPath); err != nil {
		fmt.Printf("%s[Error] input.txt가 없습니다: %s%s\n", RED, inputPath, RESET)
		return
	}
	if _, err := os.Stat(outputPath); err != nil {
		fmt.Printf("%s[Error] output.txt가 없습니다: %s%s\n", RED, outputPath, RESET)
		return
	}

	rawInput := readFile(inputPath)
	rawOutput := readFile(outputPath)

	inputCases := parseCases(rawInput)
	outputCases := parseCases(rawOutput)

	if len(inputCases) != len(outputCases) {
		fmt.Printf("%s[Warn] 입력 케이스(%d개)와 정답 케이스(%d개)의 수가 다릅니다.%s\n", YELLOW, len(inputCases), len(outputCases), RESET)
		fmt.Printf("%s가능한 쌍까지만 채점을 진행합니다.%s\n\n", YELLOW, RESET)
	}

	numCases := len(inputCases)
	if len(outputCases) < numCases {
		numCases = len(outputCases)
	}

	br := buildMainGo(folderPath)
	if br.Cleanup != nil {
		defer br.Cleanup()
	}
	if !br.OK {
		fmt.Printf("%sBuild Failed (%.3fs)%s\n", RED, br.Duration.Seconds(), RESET)
		fmt.Printf("%sBuild Log:%s\n%s%s%s\n", RED, RESET, RED, br.BuildLog, RESET)
		return
	}
	fmt.Printf("%s🔨 Build OK (%.3fs)%s\n", BLUE, br.Duration.Seconds(), RESET)

	fmt.Printf("%s🔥 Warm-up (OS 캐싱)...%s ", YELLOW, RESET)
	runSolution(br.BinPath, folderPath, "", 1*time.Second)
	fmt.Printf("Done.\n\n")

	fmt.Printf("%s🚀 채점 시작: 총 %d개의 테스트 케이스%s\n\n", BLUE, numCases, RESET)

	passed := 0

	for i := 0; i < numCases; i++ {
		caseInput := inputCases[i]
		caseExpected := outputCases[i]

		fmt.Printf("%s[Case %d]%s ", HEADER, i+1, RESET)

		rr := runSolution(br.BinPath, folderPath, caseInput, 5*time.Second)

		if strings.TrimSpace(rr.Stderr) != "" && strings.TrimSpace(rr.Stdout) == "" {
			fmt.Printf("%sRuntime Error (%.3fs)%s\n", RED, rr.ExecTime.Seconds(), RESET)
			fmt.Printf("%sError Log:%s\n%s%s%s\n", RED, RESET, RED, rr.Stderr, RESET)
			fmt.Println(strings.Repeat("-", 50))
			continue
		}

		ok, diffLines := compareResults(caseExpected, rr.Stdout)
		if ok {
			fmt.Printf("%s✅ Passed (%.3fs)%s\n", GREEN, rr.ExecTime.Seconds(), RESET)
			passed++
			continue
		}

		fmt.Printf("%s❌ Failed (%.3fs)%s\n", RED, rr.ExecTime.Seconds(), RESET)
		fmt.Printf("\n%s🔍 틀린 상세 내용 (Case %d)%s\n", BOLD, i+1, RESET)
		fmt.Printf("%s--- Input (입력값) ---%s\n", YELLOW, RESET)
		fmt.Println(caseInput)
		fmt.Printf("%s--- Diff (차이점) ---%s\n", YELLOW, RESET)

		// ---------------------------------------------------------------------
		// [수정됨] 병합 로직 제거 및 한 줄씩 출력 보장
		// ---------------------------------------------------------------------
		for j := 0; j < len(diffLines); j++ {
			line := diffLines[j]

			// Diff 헤더 색상 처리
			if strings.HasPrefix(line, "---") || strings.HasPrefix(line, "+++") || strings.HasPrefix(line, "@@") {
				if strings.HasPrefix(line, "---") {
					fmt.Printf("%s%s%s\n", RED, line, RESET)
				} else if strings.HasPrefix(line, "+++") {
					fmt.Printf("%s%s%s\n", GREEN, line, RESET)
				} else {
					fmt.Printf("%s%s%s\n", BLUE, line, RESET)
				}
				continue
			}

			// 내용 색상 처리 (-: Red, +: Green, 그 외: 기본)
			// Printf에 \n을 명시하여 무조건 개행되도록 합니다.
			if strings.HasPrefix(line, "+") {
				fmt.Printf("%s%s%s\n", GREEN, line, RESET)
			} else if strings.HasPrefix(line, "-") {
				fmt.Printf("%s%s%s\n", RED, line, RESET)
			} else {
				fmt.Println(line)
			}
		}
		// ---------------------------------------------------------------------

		fmt.Println(strings.Repeat("-", 50))
	}

	fmt.Println()
	fmt.Println(strings.Repeat("=", 30))
	if passed == numCases {
		fmt.Printf("%s%s🎉 All Accepted! (%d/%d)%s\n", GREEN, BOLD, passed, numCases, RESET)
	} else {
		fmt.Printf("%s%s🔥 Some Failed. (%d/%d passed)%s\n", RED, BOLD, passed, numCases, RESET)
	}
	fmt.Println(strings.Repeat("=", 30))
}

func main() {
	// go run grader.go <폴더 경로>
	targetFolder := "."
	if len(os.Args) > 1 {
		targetFolder = os.Args[1]
	}

	if _, err := os.Stat(targetFolder); err != nil {
		fmt.Printf("%s폴더가 존재하지 않습니다: %s%s\n", RED, targetFolder, RESET)
		return
	}

	grade(targetFolder)
}
