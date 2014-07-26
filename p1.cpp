#include <iostream>
#include <unordered_set>
#include <ctime>

using namespace std;
int main(){
    // Obvious method
    clock_t start;
    start = clock();
    int sum = 0, x, y = 5, z = 3;
    for (x = 3;  x < 1000; ++x){
        if ( !(x % 3) || !(x % 5) )
            sum += x;
    }
    cout << sum << endl;
    cout << "Time elapsed: " << (clock() - start) / (double)(CLOCKS_PER_SEC) << " seconds" << endl;


    // Fewer iterations, more memory usage
    start = clock();
    sum = 0;
    unordered_set<int> nums = {};
    for (x = 1; x < 200; ++x)
        nums.insert(y * x);
    for (x = 1; x < 334; ++x)
        nums.insert(z * x);
    for (unordered_set<int>::iterator it = nums.begin(); it != nums.end(); ++it)
        sum += *it;
    cout << sum << endl;
    cout << "Time elapsed: " << (clock() - start) / (double)(CLOCKS_PER_SEC) << " seconds" << endl;
return 0;
}
