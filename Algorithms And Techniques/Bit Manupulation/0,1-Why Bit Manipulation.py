

"""
link :-https://leetcode.com/discuss/study-guide/1151183/TIPS-or-HACKS-WHICH-YOU-CAN'T-IGNORE-AS-A-CODER

In competitive coding or a live coding round it is very important to 
write the code which is time and space optimised. BIT MANIPULATION is 
the very important topic, the code written by using bit concepts / 
tricks / hacks is reliable and fast in execution if we talk about 
competitive coding it provide us a lot of advantage.

SUPPOSE AN EXAMPLE OF CHECKING WHETHER A NUMBER IS POWER OF 2 or NOT :-

There are a lot of ways to solve it

BY USING CEIL() AND FLOOR() :-
Time complexity :- O(log2(n))
Space complexity :- O(1)

BY USING % and / OPERATOR :-
Time complexity :- O(log2(n))
Space complexity :- O(1)

BY USING BIT MANIPULATION :-
Time complexity :- O(1)
Space complexity :- O(1)

So from the above example we can see that how BIT MANIPULATION tricks 
reduces the time complexity. There are lot of problems which can be 
solved in a lot of ways but selecting the best way is the identity 
of a good coder.

BIT MANIPULATION covers approx 4% of leetcode problems. In this 
article we will see all about BIT MANIPULATION and some cool bit 
manipulation tips / hacks and tricks (which we can apply in our 
coding) with proper and detailed explanation with example.

NOTE :- IN EACH HACK I HAVE DEFINED HOW A PARTICULAR TRICK IS 
WORKING WITH PROPER TIME COMPLEXITIES. NO NEED TO MEMORISE ANYTHING.

CONTENT OF THIS ARTICLE

1. BASIC BITS OPERATORS.
2. BITS HACKS / TRICKS WITH DETAILED EXPLANATION AND COMPLEXITY.
3. MOSTLY ASKED FILTERED QUESTIONS ACCORDING TO LEETCODE.
4. INTERVIEW RELATED QUESTIONS.

PART 1 :- BASIC BITS OPERATORS

There are basically 6 type of operators which we can use over bits.

BITWISE AND (&) operator : It is a binary operator. It takes two 
numbers as an operands. The result of AND is 1 only if both bits are 1. otherwise 0.
BITWISE OR (|) operator : It is a binary operator. It takes two 
numbers as an operands. The result of OR is 0 only if both bits 
are 0. otherwise 1.
BITWISE XOR (^) operator : It is a binary operator. It takes two 
numbers as an operands. The result of XOR is 1 only if two bits are different. otherwise 0.
BITWISE LEFT SHIFT (<<) operator : It is a binary operator. The 
left shift operator (<<) shifts the first operand the specified 
number of bits to the left. Excess bits shifted off to the left 
are discarded. Left shift is equivalent to multiplying the bit 
pattern with pow(2,k) ( if we are shifting k bits ).
1 << 1 = 2 = pow(2,1) = (00010)
1 << 2 = 4 = pow(2,2) = (00100)
1 << 3 = 8 = pow(2,3) = (01000)
1 << 4 = 16 = pow(2,4) = (10000)
…
1 << n = pow(2,n)
BITWISE RIGHT SHIFT (>>) operator : It is a binary operator. The right 
shift operator (>>) shifts the first operand the specified number of 
bits to the right. Excess bits shifted off to the right are discarded. 
Right shift is equivalent to dividing the bit pattern with pow(2,k) 
( if we are shifting k bits ).
4 >> 1 = 4/pow(2,1) = 2
6 >> 1 = 6/pow(2,1) = 3
5 >> 1 = 5/pow(2,1) = 2
16 >> 4 = 16/pow(2,4) = 1
BITWISE NOT (~) operator : It is a unary operator. It takes one number 
and inverts all bits of it.

NOTE :- The left shift and right shift operators should not be used for negative numbers.

PART 2 :- BITS HACKS AND TRICKS WITH PROPER APPROACH AND COMPLEXITIES

BITS HACKS AND TRICKS :

Multiplication by power of 2. ✨🎩
Division by power of 2. ✨🎩
To check number is odd or even? ✨🎩
Swapping of 2 numbers. ✨🎩
To check ith bit is set or not of a number. ✨🎩
To flip ith bit of a number. ✨🎩
To turn on ith bit of a number. ✨🎩
To turn off ith bit of a number. ✨🎩
To check if a number is the power of 2 or not. ✨🎩
Upper case letter to lower case letter. ✨🎩
Lower case letter to upper case letter. ✨🎩
To find min/max of two numbers ✨🎩
Count all set bits of a Number ✨🎩
Count leading zeros ✨🎩
Count trailing zeros ✨🎩
1. MULTIPLICATION BY POWER OF 2 :-

      num = num << i;    //multiplication  by pow(2,i)
Approach :-
suppose an example

5= 101(binary)
5*pow(2,1)=10 = 1010 (shifed all bits one position to left if we compare with 101)=5<<1 (left shift by 1)
5*pow(2,2)=20 = 10100 (shifted all bits two position to left if we compare with 101 )=5<<2 (left shift by 2)
TIME COMPLEXITY O(1)

2. DIVISION BY POWER OF 2 :-

      num = num >> i;  //division by pow(2,i)
Approach :-
suppose an example

8= 1000(binary)
8/pow(2,1)=4 = 0100 (shifed all bits one position to right if we compare with 1000)=8>>1 (right shift by 1)
8/pow(2,2)=2 = 0010 (shifted all bits two position to right if we compare with 1000 )=8>>2 (right shift by 2)
TIME COMPLEXITY O(1)

3. TO CHECK WHETHER NUMBER IS ODD OR EVEN :-

   	  if((num & 1) == 0)
      cout << "Even number";  
      else
      cout << "Odd number";  
Approach :-

9=(1001)
11=(1011)
99=(1100011)
From the above figures we can easily figure out that the right most bit of odd number is 1
So if we perform & with odd number we got 1. 1001 & 0001 = 0001
And if we perform & with even number we got 0 1000 & 0001 = 0000
TIME COMPLEXITY O(1)

4. TO SWAP TWO NUMBERS :-

      x = x ^ y; 
      y = x ^ y; 
      x = x ^ y; 
Approach :-

x = x ^ y -------------------------- eq. 1
y = x ^ y --------------------------eq. 2
x = x ^ y ---------------------------eq. 3
put the value of x from eq. 1 to eq. 2 we got
y = (x ^ y) ^ y = x ^ (y ^ y) = x ^ 0 = x ..... we got y = x ----------eq 4
put the value of y from eq. 4 and x from eq. 1 to eq. 3 we got
x = (x ^ y) ^ x = (x ^ x) ^ y = 0 ^ y = y ...... we got x = y -----------eq 5
according to eq 4 and eq 5
y = x
x = y
hence x and y are swapped
TIME COMPLEXITY O(1)

NOTE :- there are a lot of cons of using xor for swapping. Avoid this 
technique if x and y are pointers or references to objects, and both 
point to the same location.
In some instances it may work slower than the swapping by using third value.

5. TO CHECK ith BIT IS SET OR NOT OF A NUMBER :-

     x = num & (1 << (i-1));
     if(x) cout<<"set"<<endl;
     else cout<<"not set"<<endl;
Approach :-

suppose we want to check the second bit of 10 (1010) which is 1 (bits counting always start from right )
10 & (1<<1)
so 1<<1 corresponds to 1*pow(2,1)=2=0010(binary)
10 & 2
1010 & 0010 = 2 if we get non zero no. means ith bit is set so here we got 2 means our ith means 2nd bit is set.
TIME COMPLEXITY O(1)

6. TO FLIP ith BIT OF A NUMBER :-

     x = num ^ (1 << (i-1)); 
Approach :-

suppose we want to flip the second bit of 10 (1010) 1 to 0 (bits counting always start from right )
10 ^ (1<<1)
so 1<<1 corresponds to 1*pow(2,1)=2=0010(binary)
10 ^ 2
1010 ^ 0010 = 1000 and here in both operand our second bit is 1 and according to ^ properties when two bits are same then resultant is 0 so in this way second bit of 10 flips to 0 from 1.
TIME COMPLEXITY O(1)

7. TO TURN ON ith BIT OF A NUMBER :-

     x = num | (1 << (i-1));
Approach :-

suppose we want to turn on the first bit of 10 (1010) (bits counting always start from right )
10 | (1<<0)
so 1<<0 corresponds to 1*pow(2,0)=1=0001(binary)
10 | 1
1010 | 0001 = 1011 so here if we notice we found that (i<<(i-1)) part set a bit to 1 at the ith place and if we perform | with the num then we get 1 everytime at the ith position in the num due to the | property. because when we | any bit with 1 then we got 1.
TIME COMPLEXITY O(1)

8. TO TURN OFF ith BIT OF A NUMBER :-

     x = num & ~(1 << (i-1));
Approach :-

Same as above one try to understand by yourself
TIME COMPLEXITY O(1)

9. TO CHECK IF A NUMBER IS POWER OF 2 OR NOT :-

     x = num & (num - 1);
     if(!x) cout<<"power of 2"<<endl;
     else cout<<"not a power of 2"<<endl;
Approach :-

8=(1000) , 7=(0111)
16=(10000), 15=(01111)
32=(100000), 31=(011111)
from the above cases we can easily notice that , the number which is power of 2 (say n) has only one bit set.
and for n-1 all the bits are set except the one which is set in the n. because Subtracting 1 from a decimal number flips all the bits after the rightmost set bit(which is 1) including the rightmost set bit.
so if we perform n&(n-1)
n=8 , 1000 & 0111 we got 0 in case of power of 2 otherwise 1
TIME COMPLEXITY O(1)

10. TO CONVERT UPPERCASE TO LOWERCASE LETTER :-

     ch = ch | ' '; 
Approach :-

The difference between the ASCII value of a lower case letter and its corresponding upper case letter is 32 and 32 is the ASCII value of ‘ ’ (space).
So if we notice that for converting A (65) to a(97) so for this we have to set the fifth bit of A. after setting the fifth bit we got 65+32=97 (a).
By the help of | operator we can set the fifth bit.
TIME COMPLEXITY O(1)

11. TO CONVERT LOWERCASE LETTER TO UPPERCASE LETTER :-

     ch = ch & '_'; 
Approach :-

we have just need to off the 5th bit of lowercase letter to convert it into upper case.
NOTE:-

    //for both lower to upper and upper to lower.
     ch = ch ^ (1 << 5)
TIME COMPLEXITY O(1)

12. TO FIND MIN MAX OF TWO NUMBERS :-

     minimum = y ^ ((x ^ y) & -(x < y)); // min(x, y) 

     maximum = x ^ ((x ^ y) & -(x < y)); // max(x, y) 
Approach :-

if x < y holds, then -(x < y) will be -1 which is all ones(11111….)
so minimum = y ^ ((x ^ y) & (111111…)) = y ^ x ^ y = x.
And if x>y holds , then-(x<y) will be -(0) i.e -(zero) which is zero
so maximum = x^((x^y) & 0) = x^0 = x.
TIME COMPLEXITY O(1)

13. TO COUNT ALL SET BITS OF AN NUMBER :-

       int count = 0;
       while (num) {
           num &= (num - 1);
           count++;
       }
       return count;
   	
   	//or
   	
      cout<< __builtin_popcount(num) ; 
Approach :-

Subtracting 1 from a decimal number flips all the bits after the rightmost 
set bit(which is 1) including the rightmost set bit.
for example : 10 in binary is 00001010, 9 in binary is 00001001
So if we subtract a number by 1 and do bitwise & with itself (n & (n-1)), 
we unset the rightmost set bit. If we do n & (n-1) in a loop and count the 
no of times loop executes we get the set bit count.
TIME COMPLEXITY O(k) k is the number of 1s

14. TO COUNT LEADING ZEROS :-

   int count_zeros(int num)
   {
   unsigned y;
   int n = 32;
   y = num >> 16;
   if (y != 0) {
       n = n - 16;
       num = y;
   }
   y = num >> 8;
   if (y != 0) {
       n = n - 8;
       num = y;
   }
   y = num >> 4;
   if (y != 0) {
       n = n - 4;
       num = y;
   }
   y = num >> 2;
   if (y != 0) {
       n = n - 2;
       num = y;
   }
   y = num>> 1;
   if (y != 0)
       return n - 2;
   return n - num;
  }
   
   // or
   
   __builtin_clz (x)
Approach :-

The approach of this one is very simple.
we have to simply divide the number if our number is suppose that >= 16 so 
it is confirmed that the number will require more than 4 bits because by 
using 4 bits we can create a number in the range 0 to 15.
so each time we are dividing the number ith power of 2 (num>>i) if we got 
quotient(y) !=0 means digits will atleast required i bits so we are 
substracting the i bits from our 32 bits sets.
update num, num=y and repeat.
EXAMPLE :- num=16, 16>>4 we got y=1, ans=32-4=28.....then our num will be updated to num=y=1; num=1 ,1>>2 we got y==0, for 1>>1 we got 0 again so return ans-num=28-1 return 27

TIME COMPLEXITY O(1)

15. TO COUNT TRAILING ZEROS :-

   int count = 0;
   while ((x & 1) == 0)
  {
       x = x >> 1;
       count++;
  }
  return count;
   
   // or
   
   __builtin_ctz (x)
Approach :-

just traversing bits from LSB (Least Significant Bit) and increment count while bit is 0.
PART 3 :- FILTERED PROBLEMS ACCORDING TO LEETCODE

MOSTLY ASKED BIT MANIPULATION PROBLEMS :- (Follow the order)

1178. Number of Valid Words for Each Puzzle
78. Subsets
169. Majority Element
1239. Maximum Length of a Concatenated String with Unique Characters
393. UTF-8 Validation
187. Repeated DNA Sequences
1611. Minimum One Bit Operations to Make Integers Zero
371. Sum of Two Integers
268. Missing Number
1290. Convert Binary Number in a Linked List to Integer

PART 4 :- INTERVIEW QUESTIONS

THE MAGICS WHICH WE CAN DO BY USING BIT HACKS | INTERVIEW QUESTIONS:-

Find the missing number in an array without using any extra space ✨🎩
Compute modulus division without division and modulo operator ✨🎩
Reverse bits of an integer ✨🎩
Find the odd occurring element in an array ✨🎩
Swap adjacent bits of a number ✨🎩
Print all distinct subsets of a given set ✨🎩
Swap two bits at a given position in an integer ✨🎩
Add binary representation of two integers ✨🎩
Find two duplicate elements in a limited range array (using XOR) ✨🎩
Generate binary numbers between 1 to n ✨🎩
Find the missing number and duplicate elements in an array ✨🎩
Round up to the previous power of 2 ✨🎩
Round up to the next highest power of 2 ✨🎩
Find XOR of two numbers without using the XOR operator ✨🎩
Detect if two integers have opposite signs or not ✨🎩


"""
