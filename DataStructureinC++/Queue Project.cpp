//Nisarg Patel
//csc-214
//Queue project.

#include<iostream>
#include<string>

using namespace std;

class Inventory
{
private:
    struct nodetype
    {
        int serialNum;
        string manufactDate;
        int lotNum;
        nodetype *link;
    };
    nodetype *front, *rear;
public:
    //constructor
    Inventory()
    {
        front = nullptr;
        rear = nullptr;
    }

    ~Inventory();

    void enqueue();
    void dequeue();
    void display();

};

Inventory::~Inventory()
{
    nodetype *nodeptr;
    nodeptr = front;
    while(nodeptr)
    {
        nodeptr = front;
        front = front->link ;
        delete nodeptr;
    }
}

void Inventory::enqueue()
{
    nodetype *newnode, *nodeptr ;

    newnode = new nodetype;

    cout<<"Enter the Serial Number. \n";
    cin>>newnode->serialNum;

    cout<<"Enter the Manufacturing Date. \n";
    cin>>newnode->manufactDate;

    cout<<"Enter the Lot Number. \n";
    cin>>newnode->lotNum;

    newnode->link = nullptr;
    if(!front)
    {
        front = newnode;
        rear = newnode;
    }

    else
    {
        rear->link = newnode;
        rear = newnode;
    }

}

void Inventory::dequeue()
{
    nodetype *nodeptr;

    if(!front)
    {
        cout<<"The Queue is EMPTY! \n";
        return;
    }

    nodeptr = front;
    front = front->link;
    delete nodeptr;
    cout<<"First node has been deleted. \n";


    if(!front)
    {
        cout<<"The Queue is EMPTY! \n";
        return;
    }

    else
    {
        nodeptr = front;

        cout<<"***********************************************************\n";
        cout<<"          C-O-N-T-E-N-T     R-E-M-A-I-N-I-N-G               \n";
        cout<<" Serial #:       Manufacturing Date:     Lot #: \n";

        while(nodeptr)
        {
            cout<<nodeptr->serialNum<<"             "<<nodeptr->manufactDate<<"               "<<nodeptr->lotNum<<endl;
            nodeptr = nodeptr->link;
        }
        cout<<"***********************************************************\n";
    }

}

void Inventory::display()
{
    nodetype *nodeptr;

    if(!front)
    {
        cout<<"The Queue is EMPTY! \n";
        return;
    }

    else
    {
        nodeptr = front;

        cout<<"***********************************************************\n";
        cout<<"               C-O-N-T-E-N-T                    \n";
        cout<<" Serial #:       Manufacturing Date:     Lot #: \n";

        while(nodeptr)
        {
            cout<<nodeptr->serialNum<<"             "<<nodeptr->manufactDate<<"               "<<nodeptr->lotNum<<endl;
            nodeptr = nodeptr->link;
        }
        cout<<"***********************************************************\n";
    }
}

int main()
{
    Inventory A;
    int input;

    cout<<"***********************************************************\n";
    cout<<"----------------------W-E-L-C-O-M-E------------------------\n";
    cout<<"***********************************************************\n\n\n";

    do{
    cout<<"***********************************************************\n";
    cout<<"Please select one of the choices to proceed.\n";
    cout<<"Enter 1 to add to Inventory. \n";
    cout<<"Enter 2 to remove from inventory. \n";
    cout<<"Enter 3 to Display the Results. \n";
    cout<<"Enter 0 to quit the program. \n";
    cout<<"***********************************************************\n";
    cin>>input;
    while(input < 0 || input > 3)
    {
        cout<<"Entered Input is INVALID. please ENTER the correct option. \n";
        cin>>input;
    }

    if(input == 1)
        A.enqueue();

    else if(input == 2)
        A.dequeue();

    else if(input == 3)
        A.display();

    }while(input > 0 && input < 4);

    cout<<"\n\n\n----------------------THE FINAL OUTPUT---------------------\n";
    A.display();

    return 0;

}
