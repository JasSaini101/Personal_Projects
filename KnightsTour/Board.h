//
// Created by andre on 12/7/2023.
//

#ifndef KNIGHTSTOUR2_BOARD_H
#define KNIGHTSTOUR2_BOARD_H

#endif //KNIGHTSTOUR2_BOARD_H

class Board{

public:
    int num_rows;
    int num_cols;
    int *Squares;

    Board(int x, int y){
        num_rows = y;
        num_cols = x;
        Squares = new int[num_rows * num_cols];

        for(int i = 0; i < x * y; i++){ //initialize all squares to 0 (not touched)
            Squares[i] = 0;
        }

    }

    int get_rows(){
        return num_rows;
    }

    int get_cols(){
        return num_cols;
    }

    int* get_Squares(){
        return Squares;
    }

    void set_Squares(int *sqs){
        Squares = sqs;
    }
};