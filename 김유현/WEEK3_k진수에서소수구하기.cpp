#include<string>
#include<vector>
#include<stack>
#define ll long long

bool is_prime(ll val){
   if(val == 1)
      return false;
   
   // for(ll i = 2; i * i < val; ++i) 해서 WA 2 개 나와서 헤맴
   for(ll i = 2; i * i <= val; ++i)
      if(val % i == 0)
         return false;

   return true;
}

int solution(int n, int k) {
   int ans = 0;
   ll N = n, K = k;
   ll tmp;
   std::stack<ll> stk;
   std::vector<ll> vec;

   while(N){
      stk.push(N % K);
      N /= K;
   }
   while(!stk.empty()){
      vec.push_back(stk.top());
      stk.pop();
   }
   tmp = 0;

   for(int i = 0; i < vec.size(); ++i){
      if(vec[i] == 0){
         if(tmp && is_prime(tmp))
            ++ans;
         tmp = 0;
         continue;
      }
      tmp *= 10;
      tmp += vec[i];
   }
   if(tmp && is_prime(tmp))
      ++ans;

   return ans;
}
