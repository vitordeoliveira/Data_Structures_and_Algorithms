// Stack implementation in Java

class Stack {
  private int arr[];
  private int top;
  private int size;

  // Creating a stack
  Stack(int size){
    this.size = size;
    arr = new int[size];
    top = -1;
  }

  // Add elements into stack
  public void push(int x){
    if(isFull()){
      System.out.println("OverFlow\nProgram Terminated\n");
      System.exit(1);
    }

    System.out.println("Inserting " + x);
    arr[++top]=x;
  }

  // Remove element from stack
  public void pop(){
    if(isEmpty()){
      System.out.println("STACK EMPTY");
      System.exit(1);
    }

    System.out.println("pop " + arr[top]);
    top--;
  }
 
  // Check if the stack is empty
  private Boolean isEmpty(){
    return top == -1;
  }

  // Check if the stack is full
  private Boolean isFull(){
    return top == size - 1;
  }

  public void printStack() {
    for(int i=0; i<=top; i++){
      System.out.println(arr[i]);
    }
  }

  public static void main(String[] args) {
    Stack stack = new Stack(5);

    stack.push(1);
    stack.push(2);
    stack.push(3);
    stack.push(4);

    stack.pop();
    stack.pop();
    System.out.println("\nAfter popping out");

    stack.printStack();

  }
}