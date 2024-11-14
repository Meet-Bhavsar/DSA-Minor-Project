#include <iostream>
using namespace std;

struct Node
{
    int floor;
    Node *next;
    Node *prev;
    Node(int f)
    {
        floor = f;
        next = nullptr;
        prev = nullptr;
    }
};

class Elevator
{
private:
    Node *head;    // top floor
    Node *tail;    // bottom floor
    Node *current;    // current floor

public:
    Elevator()
    {
        head = nullptr;
        tail = nullptr;
        current = nullptr;
    }
    void addFloor(int f)
    {
        Node *newNode = new Node(f);
        if (head == nullptr)
        {   // floor added when null headptr is top, bottom and current
            head = newNode;
            tail = newNode;
            current = newNode;
        }
        else
        {   // insert at end
            tail->next = newNode;
            newNode->prev = tail;
            tail = newNode;
        }
    }
    void goToFloor(int f)
    {
        Node *temp = current;
        while (temp != nullptr)
        {
            if (temp->floor == f)
            {
                current = temp;
                break;
            }
            temp = (f > current->floor) ? temp->next : temp->prev;
        }
        if (current != nullptr)
        {
            cout << "Arrived at floor " << current->floor << endl;
        }
        else
        {
            cout << "Floor not found!\n";
        }
    }
};

int main()
{
    Elevator elevator;
    int x;
    char a = true;
    while (a)
    {
        char ch;
        cout << "\nEnter choice : \n\t1) Add Floor \n\t2) Go to a Floor\n";
        cin >> x;
        switch (x)
        {
        case 1:
            int f1;
            cout << "Enter the floor number you want to add : ";
            cin >> f1;
            elevator.addFloor(f1);
            break;
        case 2:
            int f2;
            cout << "Enter the floor number you want to go to : ";
            cin >> f2;
            elevator.goToFloor(f2);
            break;
        default:
            cout << "Enter a possible number.";
            break;
        }
        cout << "Do you want to continue (y/n) ?";
        cin >> ch;
        if (ch == 'y' || ch == 'Y')
        {
            a = true;
        }
        else
        {
            a = false;
        }
    }
    return 0;
}
