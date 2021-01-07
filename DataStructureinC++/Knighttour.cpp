#Nisarg Patel
#CS-280
#PROJECT 1
#include<iostream>
#define size 8
using namespace std;


typedef struct knights_move
{
    int x,y;                    // creating a structure for chess moves
}knights_move;


void knights_path(int path[size][size])
{
    int i,j;
    for (i = 0; i < size; i++)
    {
        for (j = 0; j < size; j++)
        {                                           // initialize the n*n matrix with 0 for refrence.

            cout<<path[i][j]<<"\t";
        }
        cout<<endl;
    }
}


bool Possiblemove(knights_move next_move, int path[size][size])
{
    int i = next_move.x;            // check if the next move (as per knight's constraints) is possible
    int j = next_move.y;
    if ((i >= 0 && i < size) && (j >= 0 && j < size) && (path[i][j] == 0))
    {
        return true;
    }
    else
    {
        return false;
    }
}



bool find_path(int path[size][size], knights_move move_Knight[], knights_move current_move, int move_count)
{
    int i;
    knights_move next_move;
    if (move_count == size*size-1)         // if the Knight tour is completed return true
    {
        return true;
    }

    for (i = 0; i < size; i++)
    {

        next_move.x = current_move.x + move_Knight[i].x;
        next_move.y = current_move.y + move_Knight[i].y;

        if (Possiblemove(next_move, path))
        {
            path[next_move.x][next_move.y] = move_count+1;      
                                                                          // recursive function to find a knight tour
            if (find_path(path, move_Knight, next_move, move_count+1) == true) 
            {
                return true;
            }
            else
            {
            path[next_move.x][next_move.y] = 0;
            }
        }
    }
    return false;
}

void knight_Tour()
{
    int path[size][size];
    int i,j;
                                                     // displayingthe knight's tour solution
    for (i = 0; i < size; i++)
    {
        for (j = 0; j < size; j++)
        {
            path[i][j] = 0;
        }
    }

                                                       // all possible moves that knight can take
    knights_move move_Knight[8] = { {2,1},{1,2},{-1,2},{-2,1},{-2,-1},{-1,-2},{1,-2},{2,-1} };
    knights_move curr_move = {0,0};
  
    if(find_path(path, move_Knight, curr_move, 0) == false)
    {
        cout<<"\nKnight path does not exist";
    }
    else                                                 // find that tour is possible then proceed.
    {
        cout<<"\npath exist ...\n";
        knights_path(path);
    }
}


int main()
{
    knight_Tour();
    cout<<endl;
    return 0;
}
