// Queue implementation in C++

#include <stdlib.h>
#include <iostream>

using namespace std;

#define MAX 10

typedef struct Queue
{
    int items[MAX];
    int top;
    int head;
};

void createEmptyQueue(Queue *qu)
{
    qu->top = -1;
    qu->head = -1;
}

bool isFull(Queue *qu)
{
    if (qu->top == MAX - 1)
    {
        return true;
    }

    return false;
}

bool isEmpty(Queue *qu)
{
    if (qu->top == -1)
    {
        return true;
    }

    return false;
}

void push(Queue *qu, int item)
{
    if (isFull(qu))
    {
        printf("STACK FULL \n");
    }
    else
    {
        qu->top++;
        qu->items[qu->top] = item;

        if (isEmpty(qu))
        {
            qu->head = 0;
        }
    }
}

void pop(Queue *qu)
{
    if (isEmpty(qu))
    {
        printf("STACK IS EMPTY \n");
    }
    else
    {
        qu->items[qu->head] = NULL;
        qu->head++;
        qu->top--;
    }
}

void printQueue(Queue *qu)
{
    printf("Queue: ");
    for (int i = qu->head; i < qu->top; i++)
    {
        cout << qu->items[i] << " ";
    }
    cout << endl;
}

int main()
{
    Queue *q = (Queue *)malloc(sizeof(Queue));

    createEmptyQueue(q);

    push(q, 1);
    push(q, 2);
    push(q, 3);
    push(q, 4);
    push(q, 5);
    push(q, 6);
    push(q, 7);
    push(q, 8);
    push(q, 9);
    push(q, 10);

    printQueue(q);
}
