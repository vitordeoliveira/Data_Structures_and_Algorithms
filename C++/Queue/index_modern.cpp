#include <iostream>
#include <queue>

using namespace std;

void print(queue<int> copy)
{
    while (!copy.empty())
    {
        cout << copy.front() << " ";
        copy.pop();
    }

    cout << endl;
}

int main()
{
    queue<int> numbers;

    numbers.push(1);
    numbers.push(2);
    numbers.push(3);
    numbers.push(4);

    print(numbers);
}