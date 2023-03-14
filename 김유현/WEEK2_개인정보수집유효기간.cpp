#include <string>
#include <vector>

int term_arr[30];

int day_to_int(std::string str){
    int ret = 0;
    
    ret += (std::stoi(str.substr(0, 4)) - 2000) * 28 * 12;
    ret += std::stoi(str.substr(5, 2)) * 28;
    ret += std::stoi(str.substr(8, 2));

    return ret;
}

std::vector<int> solution(std::string today, std::vector<std::string> terms, std::vector<std::string> privacies) {
    std::vector<int> answer;
    int day_crit = day_to_int(today);
    
    for(int i = 0; i < terms.size(); ++i){
        term_arr[terms[i][0] - 'A'] = std::stoi(terms[i].substr(2, terms[i].size() - 2));
    }

    for(int i = 0; i < privacies.size(); ++i){
        int cur_day = day_to_int(privacies[i].substr(0, 10));

        if(day_crit - cur_day >= term_arr[privacies[i][privacies[i].size() - 1] - 'A'] * 28){
            answer.push_back(i + 1);
        }
    }
    return answer;
}
