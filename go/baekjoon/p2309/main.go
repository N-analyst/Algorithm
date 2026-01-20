// 2309번: 일곱 난쟁이
package main

import (
	"fmt"
	"sort"
)

func main() {
	const N int = 9
	var heights [N]int
	var sum int

	for i := range N {
		fmt.Scan(&heights[i])
		sum += heights[i]
	}

Loop:
	for i := 0; i < N-1; i++ {
		for j := i + 1; j < N; j++ {
			if sum-heights[i]-heights[j] == 100 {
				heights[i], heights[j] = 0, 0
				break Loop
			}
		}
	}

	sort.Ints(heights[:]) // 실제 메모리 할당하지 않고, 기존 배열을 가리키는 slice 생성

	for _, height := range heights {
		if height != 0 {
			fmt.Println(height)
		}
	}
}
