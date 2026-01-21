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

	var a [5][]rune

	for i := 0; i < 5; i++ {
		var s string
		fmt.Fscan(r, &s)
		a[i] = []rune(s)
	}

	for i := 0; i < 15; i++ {
		for j := 0; j < 5; j++ {
			if i < len(a[j]) {
				w.WriteRune(a[j][i])
			}
		}
	}
}
