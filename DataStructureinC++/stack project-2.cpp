//Nisarg Patel
//CSC-214
//stack project.

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
    nodetype *top;
public:
    //constructor
    Inventory()
    {
        top = nullptr;
    }

    ~Inventory();

    void push();
    void pop();
    void display();

};

Inventory::~Inventory()
{
    nodetype *nodeptr;
    nodeptr = top;
    while(nodeptr)
    {
        nodeptr = top;
        top = top->link ;
        delete nodeptr;
    }
}

void Inventory::push()
{
    nodetype *newnode, *nodeptr ;

    newnode = new nodetype;

    cout<<"Enter the Serial Number. \n";
    cin>>newnode->serialNum;

    cout<<"Enter the Manufacturing Date. \n";
    cin>>newnode->manufactDate;

    cout<<"Enter the Lot Number. \n";
    cin>>newnode->lotNum;

    if(!top)
    {
        top = newnode;
        newnode->link = nullptr;
    }

    else
    {
        newnode->link = top;
        top = newnode;
    }

}

void Inventory::pop()
{
    nodetype *nodeptr;

    if(!top)
    {
        cout<<"The Stack is EMPTY! \n";
        return;
    }

    nodeptr = top;
    top = top->link;
    delete nodeptr;
    cout<<"Top node has been deleted. \n";


    if(!top)
    {
        cout<<"The Stack is EMPTY! \n";
        return;
    }

    else
    {
        nodeptr = top;

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

    if(!top)
    {
        cout<<"The Stack is EMPTY! \n";
        return;
    }

    else
    {
        nodeptr = top;

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
        A.push();

    else if(input == 2)
        A.pop();

    else if(input == 3)
        A.display();

    }while(input > 0 && input < 4);

    cout<<"\n\n\n----------------------THE FINAL OUTPUT---------------------\n";
    A.display();

    return 0;

}
