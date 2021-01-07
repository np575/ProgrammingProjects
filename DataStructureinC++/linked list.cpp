//Nisarg Patel
//CSC-214
//linked list project

#include<iostream>

using namespace std;

struct nodeType
{

    int info;
    nodeType *link;
};




int main()
{
   nodeType *first, *newNode, *last;
int num;

    cout << "Enter a list of integers ending with -999."
    << endl;

    cin >> num;

    first = NULL;
    while (num != -999)
    {
        newNode = new nodeType;
        newNode->info = num;
        newNode->link = NULL;

        if (first == NULL)
        {
            first = newNode;
            last = newNode;
        }
        else
        {
            last->link = newNode;
            last = newNode;
        }
        cin >> num;
    } //end while

    cout<<"Output : \n";

    cout<<first->info<<endl;
    cout<<first->link->info<<endl;
    cout<<first->link->link->info<<endl;



    return 0;
} //end buildListForward
