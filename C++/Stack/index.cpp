// Stack implementation in C++

#include <stdlib.h>
#include <iostream>

// using namespace std;

#define MAX 10

// Creating a stack

typedef struct Stack
{
  int items[MAX];
  int top;
};

void createEmptyStack(Stack *st)
{
  st->top = -1;
}

// Check if the stack is full
bool isFull(Stack *st)
{
  if (st->top == MAX - 1)
  {
    return true;
  }
  return false;
}

// Check if the stack is empty
bool isEmpty(Stack *st)
{
  if (st->top == -1)
  {
    return true;
  }
  return false;
}

// Add elements into stack
void push(Stack *st, int item)
{
  if (isFull(st))
  {
    printf("STACK FULL \n");
  }
  else
  {
    st->top++;
    st->items[st->top] = item;
  }
}

// Remove element from stack
void pop(Stack *st)
{
  if (isEmpty(st))
  {
    printf("STACK IS EMPTY \n");
  }
  else
  {
    st->items[st->top] = NULL;
    st->top--;
  }
}

// Print elements of stack
void printStack(Stack *st)
{
  printf("Stack: ");
  for (int i = 0; i < st->top + 1; i++)
  {
    std::cout << st->items[i] << " ";
  }
  std::cout << std::endl;
}

// Driver code
int main()
{
  // int ch;
  Stack *s = (Stack *)malloc(sizeof(Stack));

  createEmptyStack(s);

  push(s, 1);
  push(s, 2);
  push(s, 3);
  push(s, 4);
  push(s, 5);
  push(s, 6);
  push(s, 7);
  push(s, 8);
  push(s, 9);
  push(s, 10);

  printStack(s);

  pop(s);
  pop(s);
  pop(s);
  pop(s);
  pop(s);

  
  std::cout << "\nAfter popping out\n";
  printStack(s);
}