// Queue Manual implementation in C++

#include <stdlib.h>
#include <iostream>
#include <ctype.h>
#include <stdio.h>
#include <cstdint>
#include <string>
#include <typeinfo>
#include <algorithm>

using namespace std;

#define MAX 10

struct Queue
{
    mutable int items[MAX];
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
    if (qu->head == -1 || qu->head > qu->top)
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
        cin.ignore();
        cin.ignore();
    }
    else
    {
        if (isEmpty(qu))
        {
            qu->head = 0;
        }
        qu->top++;
        qu->items[qu->top] = item;
    }
}

void pop(Queue *qu)
{

    if (qu->head == qu->top)
    {
        qu->head = -1;
        qu->top = -1;
    }
    if (isEmpty(qu))
    {

        int test;
        printf("STACK IS EMPTY \n");
        std::string temp;
        cin.ignore();
        cin.ignore();
    }
    else
    {
        qu->items[qu->head] = 0;
        qu->head++;
    }
}

void printQueue(Queue *qu)
{
    cout << "TOP: " << qu->top << "\n";
    cout << "HEAD: " << qu->head << "\n";
    printf("Queue: ");
    for (int i = qu->head; i <= qu->top; i++)
    {
        cout << qu->items[i] << " ";
    }
    cout << endl;
}

void showOptions(Queue *qu)
{
    cout << "OPTIONS: \n";
    cout << "P: POP \n";
    cout << "Q: EXIT\n";
}

bool is_number(const std::string &s)
{
    std::string::const_iterator it = s.begin();
    while (it != s.end() && std::isdigit(*it))
        ++it;
    return !s.empty() && it == s.end();
}

int main()
{
    Queue *q = (Queue *)malloc(sizeof(Queue));

    createEmptyQueue(q);

    string option;
    while (option != "Q")
    {
        system("clear");
        printQueue(q);
        showOptions(q);
        cout << "Add a number: ";
        cin >> option;

        if (is_number(option))
        {
            push(q, atoi(option.c_str()));
            continue;
        }

        transform(option.begin(), option.end(), option.begin(), ::toupper);

        if (option == "P")
        {
            pop(q);
        }
    }
}
