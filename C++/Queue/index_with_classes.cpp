#include <iostream>
#include <stdio.h>
#include <algorithm>

using namespace std;

// I want to define the size of the array in the constructor
class Queue
{
private:
    int *items, front, rear, size;

public:
    Queue(int size);
    ~Queue();

    bool isFull()
    {
        if (rear == size)
        {
            return true;
        }

        return false;
    }

    bool isEmpty()
    {
        if (front == -1)
        {
            return true;
        }
        return false;
    }

    void clean(){
        front = -1;
        rear = -1;
    }

    void push(int value)
    {
        if (isEmpty())
        {
            front = 0;
            rear = 0;
        }

        if (isFull())
        {
            cout << "QUEUE IS FULL" << endl;
            return;
        }

        items[rear] = value;
        rear++;
    }

    void pop()
    {
        items[front] = 0;
        front++;

        if(front >= rear){
            clean();
        }
    }

    void print()
    {
        cout << "REAR: " << rear << "\n";
        cout << "FRONT: " << front << "\n";
        printf("Queue: ");
        for (int i = front; i < rear; i++)
        {
            cout << items[i] << " ";
        }

        cout << endl;
    }
};

Queue::Queue(int size) : size(size)
{
    size = size;
    items = new int[size];
    front = -1;
    rear = -1;
}

Queue::~Queue()
{
    delete[] items;
}

bool is_number(const std::string &s)
{
    std::string::const_iterator it = s.begin();
    while (it != s.end() && std::isdigit(*it))
        ++it;
    return !s.empty() && it == s.end();
}

void options(string *ptr)
{
    cout << "OPTIONS: \n";
    cout << "P: POP \n";
    cout << "Q: EXIT\n";
    cout << "Add a number: ";
    cin >> *ptr;
}

int main()
{
    Queue q(10);

    string option;
    string *ptr_opt;
    ptr_opt = &option;

    while (option != "Q")
    {
        system("clear");
        q.print();

        options(ptr_opt);

        if (is_number(option))
        {
            q.push(atoi(option.c_str()));
            continue;
        }

        transform(option.begin(), option.end(), option.begin(), ::toupper);

        if (option == "P")
        {
            q.pop();
        }
    }

    return 0;
}