#include <iostream>

using namespace std;
int main(){
    int fib1 = 1, fib2 = 2, sum = 2;
    int tmp = fib1;
    while (fib1 + fib2 < 4000000){
        if ( !( (fib1 + fib2) % 2 ) )
            sum += fib1 + fib2;
        tmp = fib1;
        fib1 = fib2;
        fib2 = tmp + fib2;
    }
    cout << sum << endl;
return 0;
}
