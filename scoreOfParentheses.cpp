#include<iostream>
#include<string>
#include<cmath>
using namespace std;
class Solution {
public:
    int scoreOfParentheses(string s) {
        int ans=0,depth=0;
        char pre='(',ch;
        for(const char &ch: s)
        {
            if(ch == '(')
            {
                depth++;
            }
            else
            {
                depth--;
                if(pre == '(')
                {
                    ans += pow(2,depth);
                }
            }
            pre = ch ;
        }
        return ans;
    }
};
int main()
{
   string str;
   cin >> str;
   Solution sol;
   cout << sol.scoreOfParentheses(str); 
}