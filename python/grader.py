import os
import sys
import subprocess
import time
import difflib


# 터미널 컬러 출력을 위한 클래스
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    YELLOW = '\033[93m'


def read_file(path):
    """파일을 읽어서 내용을 반환합니다."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"{Colors.RED}[Error] 파일을 찾을 수 없습니다: {path}{Colors.RESET}")
        sys.exit(1)


def parse_cases(content):
    """
    파일 내용을 '---' 구분자로 나누어 리스트로 반환합니다.
    공백만 있는 케이스는 제외합니다.
    """
    # --- 로 분리하고, 앞뒤 공백 제거
    cases = content.split('---')
    # 내용이 있는 것만 필터링 (strip() 적용)
    cleaned_cases = [c.strip() for c in cases if c.strip()]
    return cleaned_cases


def run_solution(script_path, input_data):
    """
    문자열 형태의 input_data를 받아 script_path를 실행합니다.
    """
    start_time = time.time()
    timeout = 10

    try:
        process = subprocess.run(
            [sys.executable, script_path],
            input=input_data + "\n",  # 입력 끝에 줄바꿈 추가 (EOF 처리 안전성)
            text=True,
            capture_output=True,
            timeout=timeout  # 넉넉히 timeout 10초 이후 조절
        )
        end_time = time.time()
        execution_time = end_time - start_time

        return process.stdout, process.stderr, execution_time

    except subprocess.TimeoutExpired:
        return None, f"Timeout ({timeout}s Limit)", timeout
    except Exception as e:
        return None, str(e), 0.0


def compare_results(expected, actual):
    """예상 결과와 실제 결과를 비교합니다."""
    # 비교를 위해 줄 단위로 분리하고 공백 제거
    expected_lines = expected.strip().splitlines()
    actual_lines = actual.strip().splitlines()

    # 줄 끝 공백 제거 후 비교 (엄격함 조절 가능)
    clean_exp = [l.rstrip() for l in expected_lines]
    clean_act = [l.rstrip() for l in actual_lines]

    if clean_exp == clean_act:
        return True, []

    # 다르다면 diff 생성
    diff = difflib.unified_diff(
        clean_exp,
        clean_act,
        fromfile='Expected',
        tofile='Actual',
        lineterm=''
    )
    return False, list(diff)


def grade(folder_path):
    """채점 메인 함수"""
    input_path = os.path.join(folder_path, 'input.txt')
    output_path = os.path.join(folder_path, 'output.txt')
    script_path = os.path.join(folder_path, 'main.py')

    if not os.path.exists(script_path):
        print(f"{Colors.RED}[Error] main.py가 없습니다: {folder_path}{Colors.RESET}")
        return

    # 1. 파일 읽기 및 파싱
    raw_input = read_file(input_path)
    raw_output = read_file(output_path)

    input_cases = parse_cases(raw_input)
    output_cases = parse_cases(raw_output)

    # 케이스 개수 확인
    if len(input_cases) != len(output_cases):
        print(
            f"{Colors.YELLOW}⚠️ 경고: 입력 케이스({len(input_cases)}개)와 정답 케이스({len(output_cases)}개)의 수가 다릅니다.{Colors.RESET}")
        print(f"{Colors.YELLOW}가능한 쌍까지만 채점을 진행합니다.{Colors.RESET}\n")

    num_cases = min(len(input_cases), len(output_cases))
    print(f"{Colors.BLUE}🚀 채점 시작: 총 {num_cases}개의 테스트 케이스{Colors.RESET}\n")

    passed_count = 0

    # 2. 케이스별 루프 실행
    for i in range(num_cases):
        case_input = input_cases[i]
        case_expected = output_cases[i]

        print(f"{Colors.HEADER}[Case {i + 1}]{Colors.RESET}", end=" ")

        # 코드 실행
        actual_output, error, exec_time = run_solution(script_path, case_input)

        # 런타임 에러 처리
        if error and not actual_output:
            print(f"{Colors.RED}❌ Runtime Error ({exec_time:.3f}s){Colors.RESET}")
            print(f"{Colors.RED}Error Log:\n{error}{Colors.RESET}")
            print("-" * 50)
            continue

        # 정답 비교
        is_correct, diff_lines = compare_results(case_expected, actual_output)

        if is_correct:
            print(f"{Colors.GREEN}✅ Passed ({exec_time:.3f}s){Colors.RESET}")
            passed_count += 1
        else:
            print(f"{Colors.RED}❌ Failed ({exec_time:.3f}s){Colors.RESET}")

            # 틀렸을 때 상세 정보 출력
            print(f"\n{Colors.BOLD}🔍 틀린 상세 내용 (Case {i + 1}){Colors.RESET}")
            print(f"{Colors.YELLOW}--- Input (입력값) ---{Colors.RESET}")
            print(case_input)
            print(f"{Colors.YELLOW}--- Diff (차이점) ---{Colors.RESET}")

            for line in diff_lines:
                if line.startswith('+'):
                    print(f"{Colors.GREEN}{line}{Colors.RESET}")
                elif line.startswith('-'):
                    print(f"{Colors.RED}{line}{Colors.RESET}")
                elif line.startswith('^'):
                    print(f"{Colors.BLUE}{line}{Colors.RESET}")
                else:
                    print(line)
            print("-" * 50)

    # 3. 최종 결과 요약
    print("\n" + "=" * 30)
    if passed_count == num_cases:
        print(f"{Colors.GREEN}{Colors.BOLD}🎉 All Accepted! ({passed_count}/{num_cases}){Colors.RESET}")
    else:
        print(f"{Colors.RED}{Colors.BOLD}🔥 Some Failed. ({passed_count}/{num_cases} passed){Colors.RESET}")
    print("=" * 30)


if __name__ == "__main__":
    target_folder = sys.argv[1] if len(sys.argv) > 1 else "."

    if not os.path.exists(target_folder):
        print(f"{Colors.RED}폴더가 존재하지 않습니다: {target_folder}{Colors.RESET}")
    else:
        grade(target_folder)