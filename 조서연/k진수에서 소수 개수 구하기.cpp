#include <iostream>
#include <vector>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

bool isPrime(long num) {
    if(num < 2) return false; 
    for(int i=2; i<=sqrt(num); ++i) {
        if(num % i == 0) return false;
    }
    return true;
}
int solution(int n, int k) {
    int answer = 0;
    string str = "";
    while(n > 0) {
        str += to_string(n % k);
        n /= k;
    }
    reverse(str.begin(), str.end());
    string tmp = "";
    for (char c : str) { 
        if (c == '0') { 
            if (!tmp.empty() && isPrime(stoll(tmp))) {
                answer++; 
            } 
            tmp = ""; 
        } 
        else tmp += c; 
    }
    
    if (!tmp.empty() && isPrime(stoll(tmp))) {
        answer++;
    } 
    return answer;
}
