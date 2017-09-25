#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;
 
int main()
{
int withdraw = 0;
double balance = 0;
 
cin >> withdraw >> balance;
 
if(balance < (withdraw + 0.5)) {
cout << std::fixed << setprecision(2) << balance;
}
else if ((withdraw % 5) != 0) {
cout << std::fixed << setprecision(2) << balance;
}
else{
balance = balance - (withdraw + 0.5);
cout << std::fixed << setprecision(2) << balance;
}
return 0;
}