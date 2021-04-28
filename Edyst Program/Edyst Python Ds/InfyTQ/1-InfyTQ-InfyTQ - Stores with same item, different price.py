"""
Given two list A and B of different length.
Each item of a list is associated with its name and its price.

Count the number of items which are in both the lists but with different prices.

Example :

Input :

Aname: [ "code", "fode", "mode" ]
Aprice: [3, 2, 1]
 
Bname: [ "code", "fode", "mode", "load" ]
Bprice: [4, 2, 2, 2]
Output :
2
"""

class Solution:
    def countItems(self, Aname, Aprice, Bname, Bprice):
        count=0
        l=list(set(Aname) & set(Bname))
        for i in l:
            index1=Aname.index(i)
            index2=Bname.index(i)
            if Aprice[index1] != Bprice[index2]:
                count+=1
        return count