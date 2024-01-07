#include <iostream>
#include "algorithms.h"
#include <ctime>

int main() {

    Board test(8, 16);
    clock_t timer;
    timer = clock();

    //Arg 1: Board to Attempt to Solve, Arg 2: X-Position of Starting Square
    //Arg 3: Y-Position of Starting Square Arg 4: Whether or Not to Print Each Step
    divide_and_conquer(&test, 0, 0, true);
    //warnsdorff(&test, 0, 0, true);
    //brute_force(&test, 0, 0, false);

    timer = clock() - timer;
    cout << (float)timer/CLOCKS_PER_SEC << endl;

    return 0;
}
