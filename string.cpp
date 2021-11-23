#include<bits/stdc++.h>
using namespace std;
int main(){
    string s;
    cin>>s;
    int n=s.size();
    int c=0;
    for(int i=0;i<n;i++){
         if(s[i]=='0' && s[i+1]=='1'){
             i+=2;
             int j=i;
             while(s[j]!='0'){
                i++;
                j++;
                if(s[j]=='0'){
                    c++;
                }
             }
        }
    }
    cout<<c;
    return 0;

}