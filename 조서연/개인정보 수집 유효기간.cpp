#include <string>
#include <string.h>
#include <vector>
#include <cstring>
#include <iostream>

using namespace std;

vector<int> solution(string today, vector<string> terms, vector<string> privacies) {
    vector<int> answer;
     
    int todayWhen=stoi(today.substr(0,4))*12*28+stoi(today.substr(5,2))*28+stoi(today.substr(8,2));
    for(int i=0;i<privacies.size();i++){
        int pWhen=stoi(privacies.at(i).substr(0,4))*12*28+stoi(privacies.at(i).substr(5,2))*28+stoi(privacies.at(i).substr(8,2));
        for(int j=0;j< terms.size();j++){
            if(terms.at(j).at(0)==privacies.at(i).at(11)){
                pWhen+=stoi(terms.at(j).substr(2,3))*28;
                if(pWhen<=todayWhen) answer.push_back(i+1);
                
            }
        }
    }
    return answer;
}
