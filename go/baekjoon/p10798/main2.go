// 10798번: 세로읽기
package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	r := bufio.NewReader(os.Stdin)
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()

	// []rune 대신 string 배열 사용 (메모리 절약)
	var lines [5]string
	maxLen := 0

	// 입력 처리: Fscan을 사용하여 공백/개행 단위로 문자열을 읽음
	for i := 0; i < 5; i++ {
		fmt.Fscan(r, &lines[i])

		if len(lines[i]) > maxLen {
			maxLen = len(lines[i])
		}
	}

	for i := 0; i < maxLen; i++ {
		for j := 0; j < 5; j++ {
			if i < len(lines[j]) {
				// 문제 자체에 영어 대소문자, 숫자만 입력이 되므로 WriteByte도 문제 없음.
				w.WriteByte(lines[j][i])
			}
		}
	}
}
