package main

import "fmt"

type Stack []int16

func (s *Stack) IsEmpty() bool {
	return len(*s) == 0
}

func (s *Stack) push(item int16) {

	*s = append(*s, item)
}

func (s *Stack) pop() {
	if s.IsEmpty() {
		fmt.Println("Stack is empty")
	} else {
		index := len(*s) - 1
		element := (*s)[index]
		*s = (*s)[:index]
		fmt.Println("Pop:", element)
	}
}

func (s *Stack) printStack() {
	fmt.Print("Stack: ")
	for i := 0; i < len(*s); i++ {
		fmt.Print((*s)[i], " ")
	}
	fmt.Println()
}

func main() {
	var stack Stack

	stack.push(1)
	stack.push(2)
	stack.push(3)

	stack.printStack()

	stack.pop()
	stack.pop()

	stack.printStack()

}
