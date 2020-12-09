def rotLeft(l, r):
    d = [0 for i in range(len(l))]
    for i in range(r):
        for j in range(len(l)):
            if j + 1 == len(l):
                d[j] = l[0]
                continue
            d[j] = l[j + 1]
        l = d[:]
    return d


"""
That did not gave me the solution , thought that copying the list of d in l might be time consuming
So went for in place algorithm
"""


def rotLeft(l, r):
    r = r % len(l)
    for i in range(r):
        temp = l[0]
        for j in range(len(l)):
            if j + 1 == len(l):
                l[j] = temp
                continue
            l[j] = l[j + 1]
    return l


"""
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main() {
    int n; 
    int k; 
    
    scanf("%d %d",&n,&k);
    
    int *a = malloc(sizeof(int) * n);
    int *a_out = malloc(sizeof(int) * n);
    
    for(int a_i = 0; a_i < n; a_i++){
       scanf("%d",&a[a_i]);
    }
/*    
    for(int i = 0; i < k; i++){
        int buf = a[0];
        
        for (int j = 0; j < n-1; j++) {
            a[j] = a[j+1];
        }
            
        a[n-1] = buf;
    }
*/    
    for (int i = 0; i < n; i++) {
        a_out[(i+n-k)%n] = a[i];
    }
    for(int a_i = 0; a_i < n; a_i++){
       printf("%d ", a_out[a_i]);
    }   
    printf("\n");
    
    free(a);
    return 0;
}


"""