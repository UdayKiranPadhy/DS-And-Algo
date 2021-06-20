"""
Write a program to merge two sorted Arrays into single sorted Array.The time complexity must be in O(N).

Example:
1 2 3 3
2 4 5 6

Ouput:
1 2 2 3 3 4 5 6

"""

struct Solution {
  void mergeTwoArrays(vector<int> &A, vector<int> &B, vector<int> &C) {
      int a=A.size();
      int b=B.size();
      int i=0,j=0,k=0;
      while(a>i || b>i){
          if(A[i]>B[j]){
              C[k]=B[j];
              j+=1;
          }else{
              C[k]=A[i];
              i+=1;
          }
          k+=1;
      }
      while(i<a){
          C[k]=A[i];
          i+=1;
          k+=1;
      }
      while(j<b){
          C[k]=B[j];
          j+=1;
          k+=1;
      }
      i=0;
  }
};
