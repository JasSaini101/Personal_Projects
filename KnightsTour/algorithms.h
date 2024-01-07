// This file contains all of our functions
// Along with functions that solve for the Knights Tour
// are helper functions that we used to make the code easier

#ifndef KNIGHTSTOUR2_ALGORITHMS_H
#define KNIGHTSTOUR2_ALGORITHMS_H

#endif //KNIGHTSTOUR2_ALGORITHMS_H

#include "iostream"
#include "Board.h"
#include <vector>
#include <stack>
#include <ctime>

using namespace std;

int coordinates_to_index(int x, int y, int num_rows){   //converts coordinates on a board to an index in the Board array
    return(y + x * (num_rows));
}

stack<int> possibleMoves(Board *B, int x, int y){  //returns stack w/ all the legal moves for given Square on given Board
    stack<int> answer;
    for(int i = -2; i < 3; i++){
        for(int j = -2; j < 3; j++){
            int index = coordinates_to_index(x + i, y + j, B->get_rows());
            if (i != 0 && j != 0 && abs(i) != abs(j) && x + i > -1 && y + j > -1 &&
                x + i < B->get_cols() && y + j < B->get_rows() &&
                B->get_Squares()[index] < 1) {
                answer.push(index);
            }
        }
    }
    return(answer);
}

void print(Board *B , int currSquare){
    int moveDown = 0;
    cout << "# # # # # # # # #" << endl << "#"; //top of the board
    for(int i = 0; i < B->get_cols() * B->get_rows(); i++){
        if(i / B->get_rows() == moveDown){
            if(i == currSquare){
                cout << "K| ";
            }
            else if(B->get_Squares()[i] < 1){
                cout << "O| ";
            }
            else{
                cout << "X| ";
            }
        }
        else{
            cout << "#" << endl;
            cout << "#";
            if(i == currSquare){
                cout << "K| ";
            }
            else if(B->get_Squares()[i] < 1){
                cout << "O| ";
            }
            else{
                cout << "X| ";
            }
            moveDown++;
        }
    }
    cout << "#" << endl << "# # # # # # # # #" << endl << endl << endl << endl;
}

void brute_force(Board *B, int x, int y, bool p){ //The Brute_Force Function
    int failedMove = 0;
    int startingIndex = coordinates_to_index(x,y, B->get_rows());

    stack<int> moves;
    B->Squares[startingIndex] = 1;
    moves.push(startingIndex);
    stack<int> nextSquare = possibleMoves(B,x,y);

    while(moves.size() != (B->get_cols() * B->get_rows()) - 1){
        while (!nextSquare.empty() && moves.size() != (B->get_cols() * B->get_rows()) - 1) {

            int checkSquare = nextSquare.top();
            stack<int> checkSquareMoves = possibleMoves(B, checkSquare / B->get_rows(), checkSquare % B->get_cols());
            if (checkSquareMoves.empty()) {
                nextSquare.pop();
                if (nextSquare.empty()) { //none of the next moves can move again
                    failedMove = moves.top();
                    B->get_Squares()[failedMove] = 0;
                    moves.pop();
                    nextSquare = possibleMoves(B, moves.top() / B->get_rows(), moves.top() % B->get_cols());
                    while (nextSquare.top() != failedMove) {
                        nextSquare.pop();
                    }
                    nextSquare.pop();
                }
            }
            else {
                B->get_Squares()[nextSquare.top()] = 1;
                moves.push(nextSquare.top());
                while(!nextSquare.empty()){
                    nextSquare.pop(); //clearing this stack to save space
                }
                nextSquare = checkSquareMoves;
            }
        }
        //Our Move left us at a dead end so now we have to go back on moves stack
        while(nextSquare.empty() && moves.size() != (B->get_cols() * B->get_rows()) - 1) {
            failedMove = moves.top();
            B->get_Squares()[failedMove] = 0;
            moves.pop();

            if(moves.empty()){ //Solution was not found with the given starting square
                cout << "No Possible Solution" << endl;
                return;
            }

            nextSquare = possibleMoves(B, moves.top() / B->get_rows(), moves.top() % B->get_cols());
            while (nextSquare.top() != failedMove) {
                nextSquare.pop();
            }
            nextSquare.pop();
        }
    }

    if(p){
        stack<int> reverseMoves;
        moves.push(nextSquare.top());
        while(!moves.empty()){
            reverseMoves.push(moves.top());
            moves.pop();
        }
        nextSquare.pop();

        cout << "Starting Index: " << reverseMoves.top() << endl;
        cout << "Coordinate: (" << reverseMoves.top() / B->get_rows() << "," << reverseMoves.top() % B->get_rows() << ") " << endl;


        reverseMoves.pop();

        while(!reverseMoves.empty()) {
            cout << "Next Index: " << reverseMoves.top() << endl;
            cout << "Next Move: (" << reverseMoves.top() / B->get_rows() << "," << reverseMoves.top() % B->get_rows() << ") " << endl;

            reverseMoves.pop();
        }
    }
    else
        cout << "Solved!!!" << endl;

    //This final bit is to reverse the move order because our answer stack has it backwards technically

}



void warnsdorff(Board *B, int x, int y, bool p){  //Function that uses the Warnsdorff Rule (pure algorithm no data structure)
    int startingIndex = coordinates_to_index(x,y,B->get_rows());
    //cout << "Starting Index: " << startingIndex << endl;

    //cout << "Coordinate: (" << startingIndex / B->get_rows() << "," << startingIndex % B->get_rows() << ") " << endl;

    if(p){
        cout << "Coordinate: (" << startingIndex / B->get_rows() << "," << startingIndex % B->get_rows() << ") " << endl;
        print(B,startingIndex);
    }

    B->get_Squares()[startingIndex] = 1;
    int squaresTouched = 1;

    while(1) {
        vector<int> allMoves;
        for (int j = -2; j < 3; j++) {
            for (int i = -2; i < 3; i++) {
                int index = coordinates_to_index(x + i, y + j, B->get_rows());
                if (i != 0 && j != 0 && abs(i) != abs(j) && x + i > -1 && y + j > -1 && x + i < B->get_cols() &&
                    y + j < B->get_rows() && B->get_Squares()[index] < 1) {
                    allMoves.push_back(coordinates_to_index(x + i, y + j, B->get_rows()));
                }
            }
        }
        int minNeighbors = 8;
        int countNeighbors;
        int nextIndex = -1;

        for (int test: allMoves) {
            x = test / B->get_cols();
            y = test % B->get_rows();
            countNeighbors = 0;
            for (int j = -2; j < 3; j++) {
                for (int i = -2; i < 3; i++) {
                    int index = coordinates_to_index(x + i, y + j, B->get_rows());
                    if (i != 0 && j != 0 && abs(i) != abs(j) && x + i > -1 && y + j > -1 &&
                        x + i < B->get_cols() && y + j < B->get_rows() && B->get_Squares()[index] < 1) {
                        countNeighbors++;
                    }
                }
            }
            if (countNeighbors <= minNeighbors && B->get_Squares()[test] != 1) {
                minNeighbors = countNeighbors;
                nextIndex = test;
            }
        }
        squaresTouched++;

        //cout << "Next Move: (" << nextIndex / B->get_rows() << "," << nextIndex % B->get_cols() <<") " << endl;
        if(p){print(B,nextIndex);}

        if (nextIndex == -1) {
            cout << "No Possible Solution" << endl;
            return;
        }
        else if (squaresTouched == B->get_rows() * B->get_cols()){
            cout << "Solved!!!" << endl;
            return;
        }
        x = nextIndex / B->get_rows(); //cols
        y = nextIndex % B->get_rows(); //rows
        B->get_Squares()[nextIndex] = 1;
    }

}

