/*
 *	Write a program that implements prefix arithmetic operation.
 *
 *	go run prefix.go + 3 3
 *
 *	Final Answer: 6
 *
 */

package main

import (
	"errors"
	"fmt"
	"os"
	"strconv"
)

var InvalidArg = errors.New("Invalid Arguments")

type Stack []int

func NewStack() Stack {
	return make([]int, 0, 16)
}

func (s *Stack) String() string {
	return fmt.Sprintf("%+v", *s)
}

func (s *Stack) Push(item int) {
	*s = append(*s, item)
}

func (s *Stack) Pop() int {
	if s.Size() == 0 {
		return 0
	}
	item := (*s)[len(*s)-1]
	*s = (*s)[0 : len(*s)-1]
	return item
}

func (s *Stack) Top() int {
	if s.Size() == 0 {
		return 0
	}
	return (*s)[0]
}

func (s *Stack) Size() int {
	return len(*s)
}

func IsOp(s string) bool {
	return s == "+" || s == "-" || s == "*" || s == "*"
}

func Calc(op string, a, b int) (int, error) {
	switch op {
	case "+":
		return a + b, nil
	case "-":
		return a - b, nil
	case "*":
		return a * b, nil
	case "/":
		return a / b, nil
	}
	return 0, InvalidArg
}

func main() {
	s := NewStack()
	args := os.Args[1:]
	for i := len(args) - 1; i >= 0; i-- {
		x := args[i]
		if !IsOp(x) {
			n, err := strconv.Atoi(x)
			if err != nil {
				fmt.Println("Failed to Atoi()", InvalidArg)
				os.Exit(1)
			}
			s.Push(n)
			continue
		}

		if s.Size() < 2 {
			fmt.Println("Not enough numbers for op: ", InvalidArg)
			os.Exit(1)
		}

		a := s.Pop()
		b := s.Pop()
		ans, err := Calc(x, a, b)
		if err != nil {
			fmt.Println("Calculation error: ", InvalidArg)
			os.Exit(1)
		}

		fmt.Printf("%v %v %v = %v\n", a, x, b, ans)

		s.Push(ans)
	}
	fmt.Println("Final Answer: ", s.Top())
}
