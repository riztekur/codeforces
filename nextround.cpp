// https://codeforces.com/problemset/problem/158/A

#include <iostream>
using namespace std;

int main(){
    int m,n,count=0;
    cin>>m>>n;

    int arr[m];
    for(int i=0;i<m;i++){
        cin>>arr[i];
    }

    for(int i=0;i<m;i++){
        if(arr[i]>0 && arr[i]>=arr[n-1]){
            count++;
        }
    }
    cout<<count;
    return 0;
}