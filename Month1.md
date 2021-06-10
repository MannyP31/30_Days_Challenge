<img src="https://media-exp1.licdn.com/dms/image/C4E03AQFDuHx-TrxMNg/profile-displayphoto-shrink_200_200/0/1614907425476?e=1627516800&v=beta&t=6j8PxnUIH5UvyKuhwCJ498EiPLUzgu_c_h-HHor8dVc" align="right" width="100" height="100"/>

# 30 Days Challenge Month-I

[![](https://img.shields.io/badge/CWC-ITER-gray.svg?style=for-the-badge&colorB=0000f&logo=github)](https://elastic-bose-ed6583.netlify.app/)

## Coding Wizard Club welcomes you to the 30 Days Problem Solving Challenge.

<ol>
  <li>This Repo contains set of 100 questions.</li>
  <li>First of all you are required to signup to <b><a href="https://bitbucket.org/">Bitbucket</a></b> so that you can upload your solution there.</li>
  <li>You are supposed to solve atleast 90 questions out of 100 mentioned below and share the repo link of Bitbucket in the google form attached. <b><a href="https://forms.gle/jFCWAzcED6BpvgDB9">Form Link</a></b></li>
  <li>For the time period of 30 days from 10th June 10:00 pm to 10th July 10:00 pm, the challenge will remain active.</li>
  <li>Those who will successfully complete the challenge (fulfill 2nd point) will get a recognition certificate from CWC.</li>
  <li>And the top 3 performers will get a certificate of achievement from the placement cell.</li>	
</ol>

<h2>Happy Coding 👨‍💻 </h2>

<h2>Questions are</h2>

> 1. From a set of permutations for a given number n find the number of elements such hat no element appears in its original position.
<pre>
Input:
n = 4
Output: 9

Input:
n = 10
Output: 1334961
</pre>

> 2. Write a program to find partial sums of the terms of the Fibonacci sequence.

> 3. Given two long integers numbers min and max find and print a typical part n/d to such an extent that min<=d<=max and |n/d-pi| is negligible
if there are a few divisions having an insignificant distance to pi pick the one with the littlest denominator. 
<pre>
Input:
n = 1 10
Output: 22/7 

Explanation:- You must check all fractions with denominators from min to max.
</pre>

> 4. Given four points in the plane, write a program to check if they are the vertices of a rectangle.

> 5. Program to check if two rectangles, not necessarily aligned with the X and Y axes, intersect.

> 6. Program to swap bits with O(1) time complexity.

> 7. Calculate the area of a Circle inscribed in a Square.

> 8. A truck can transport a maximum of 10000 kgs. Assume a heap of load containing 41 boxes should be shipped through the truck. The box weight of this sort of cargo follows a distribution with a mean of 210 kgs 
and standard deviation of 15 kgs. What is the probability that all 41 boxes can be loaded into the truck and transported?

> 9. Find the sum of the digits in the number 100!

> 10. Write a program that has three numbers a, b, c where a < b < c and a^2 + b^2 = c^2. There exists only one solution where it satisfies the following equation for a+ b + c = 1000. Find the product abc.

> 11. Xonas is residing in Albert’s House and he wants to go outside such that he can reach the pizza store in minimum time. You have to find the shortest distance between the store and Albert’s House so that Xonas have to do least effort for a pizza. Xonas is very good in mathematics and he anyhow manages to find the X and Y coordinates of the destination and initial position. 
<pre>
Input Constraints: Xi, Yi, Xf, Yf.
Input: Enter the total no. of paths you want to compare for : 2
	Enter the constraints for 1st path:
	Enter X and Y coordinates of Initial position: 3 2
	Enter X and Y coordinates of Final position: 9 7
           
	Enter the constraints for 2nd path:
	Enter X and Y coordinates of Initial position: 4 1
	Enter X and Y coordinates of Final position: 8 4

Output: 7.81 Units Distance will be covered in path 1.
        5 Units Distance will be covered in path 2.
        You should go with path 2.      
</pre>

> 12. Write a Program that will convert an integer to to it’s corresponding 2’s Complement in binary representation. 
<pre>
Input: Enter an Integer no.: 5
Output: 2’s complement for the no. is  1011 in binary representation.
</pre>

> 13. A member of CWC asks a random question from different coordinators of the club. The member of the club gets an answer from xyz kumar. Write a code that will keep track of question asked by and answer given by in the corresponding index. 
<pre>
Input: Enter the total no. of questions asked: 3
	  Enter asker’s and coordinator’s name for 1st one: Jubin Pulkit
	  Enter asker’s and coordinator’s name for 2nd one: Apul Rohit
	  Enter asker’s and coordinator’s name for 3rd one: Surat Ami
Output: ----------------------------------------------------------------------------------------
		Asker                                       Query Solved by
		-----------                          -----------------------------
		Jubin						Pulkit
		Apul						Rohit
		Surat 						Ami
     -------------------------------------------------------------------------------------------
</pre>

> 14. Write a program to print the series : 1, 2, 3, 4, 5,6 ,7, 8 ,9 ,10 , 12 , 21, 23,32,34, 43, ……. The following series will depend upon upto how many numbers user want to print the series. 
<pre>
Input: Enter the range of numbers : 5
Output: Series Generated: 1 ,2 ,3 ,4, 5
</pre>

> 15. Given a pole of length n and a rundown of costs of poles of length I, where 1 <= I <= n, track down the ideal method to cut the pole into more modest poles to augment benefit.
<pre>
length[] = [1, 2, 3, 4, 5, 6, 7, 8]
price [] = [1, 5, 8, 9, 10, 17, 17, 20]

Rod length: 4
 
Best: Cut the rod into two pieces of length 2 each to gain revenue of 5 + 5 = 10
 
Cut           Profit
4                9
1, 3            (1 + 8) = 9
2, 2            (5 + 5) = 10
3, 1            (8 + 1) = 9
1, 1, 2         (1 + 1 + 5) = 7
1, 2, 1         (1 + 5 + 1) = 7
2, 1, 1         (5 + 1 + 1) = 7
1, 1, 1, 1      (1 + 1 + 1 + 1) = 4
</pre>

We are given an array price[], where the rod of length i has a value price[i-1]. The idea is simple – one by one, partition the given rod of length n into two parts: i and n-i. Recur for the rod of length n-i but don’t divide the rod of length i any further. Finally, take the maximum of all values. This yields the following recursive relation:
<pre>
rodcut(n) = max { price[i – 1] + rodCut(n – i) } where 1 <= i <= n.
</pre>

> 16. Write a program to differentiate an equation and integrate it back to prove the differentiation. Also ask the user if he/she wants to solve the differentiated equation for any values of x. If yes then print the value else terminate the program.
<pre>
Input: Enter the equation to find the differentiation: 3X^2+5y
Output: Derivative of the given equation: 6x+5
	After integration we got 3X^2+5y, hence proved.
Input: Do you Want to solve the differential equation for any value of X and Y?  Yes
	Enter the value of X and Y:  2    3 

Output: Value of the differential equation : 12
</pre>

> 17. Design a pizza counter management system which will take the order from the user and present the bill after calculating the quantity and price of each item ordered by user.
<pre>
Price list of all items:
	      1.Cheese Pizza : Rs. 350
	      2.Chicken Burst Pizza :  Rs. 420
	      3.Double Cheese Mixed Pizza: Rs. 440
	      4.Mushroom Grilled Cheese Burst Pizza: Rs. 510
	      5.Coke (300ml) : Rs. 35
	      6.Mineral Water:  Rs. 40
</pre>

<pre>
Input: Enter the item no. those you want to take : 2 5 6
       Enter the corresponding quantity: 1 2 2
Output : Thanks for visiting here’
         Bill Generated…
         Please pay Rs. 570 through any mode of payment.
</pre>

> 18. Alex and jenny begin playing another game. Alex composes 2 numbers - N and K. She requests that jenny discover a whole number which is N digits long to such an extent that the supreme contrast in the adjoining digits is not exactly or equivalent to K. Jenny understands that a ton of numbers fulfill this condition. Would you be able to assist jenny with tracking down the complete number of N digit numbers which fulfill the condition set by Alex?
<pre>
Input:
2 1
0 0

Output:
26

Constraints
T(1 <= T <= 1000) - Number of test cases.
2 <= N <= 10^9
0 <= K <= 9
</pre>

> 19. 10 persons are working on a Machine Learning model and they want to make a program which will find the array’s least complexity for different elements for processing that array to be used in the ML model.The program will display the no. of operations , Cost/ scalar multiplications for each of the sequences.
<pre>
Hint: Use Matrix Chain Multiplication algorithm.

Input: 	How many numbers you want to store for the matrix chain multiplication?
5
How many sequences you want to check to find the optimised one?
3
For Sequence No. 1
---------------------------------------------------
Enter the elements 2
Enter the elements 3
Enter the elements 4
Enter the elements 5
Enter the elements 6
---------------------------------------------------

For Sequence No. 2
---------------------------------------------------
Enter the elements 6
Enter the elements 4
Enter the elements 5
Enter the elements 3
Enter the elements 2
---------------------------------------------------

For Sequence No. 3
---------------------------------------------------
Enter the elements 5
Enter the elements 4
Enter the elements 2
Enter the elements 3
Enter the elements 6
---------------------------------------------------
Output:
All the sequences with their operations are [124, 118, 136] and among them.
Best sequence for the ML model that runs in least time will be the sequence no : 2 and the no of operations will be 118
</pre>

> 20. Program to print a statement without using the print statement. 

> 21. Write a program which returns all distinct non attacking placements of n Queens on an n x n chessboard, where n is an input to the program. 

> 22. Multiply two numbers with using only Bitwise Operators.

> 23. Write a function to merge two arrays in following fashion.
<pre>
Input :
P = 1 4 6 8
Q = 11 19 10 7
Output: 1 11 4 19 6 10 8 7
</pre>

> 24. Write a function to move all the even elements to the starting of List and odd to the end of the List.

> 25. Write a program to toggle a paritucular bit using bitwise operators.
 
> 26. Write a program to input a number and check and print whether it is a Pronic number or not. (Pronic number is the number which is the product of two consecutive integers).

> 27. Given an unsorted array arr[] which contains both positive and negative numbers.Your task is to find the first positive missing numbers.

> 28. Write a program to calculate the sum of series. S= 1^n + 2^n-1 + 3^n-2 +…………+ n^1.

> 29. Display the following series. Also calculate its sum 0.5 +0.55 + 0.555 + ---------- + n terms.

> 30. Write a program accept N numbers in an array then shift the positive numbers towards the left and negative elements towards the right without altering the original sequence.
<pre>
Input : -3, 22, -45 , 67, 8,10, 9, -2, -5
Output : 22, 67, 8, 10 ,9, -3, -45, -2, -5
</pre>

> 31. Write a java program to accept numbers in a matrix of size 4 x 4 by using Scanner class then calculate and display sum of bordered elements.
<pre>
Input :
4 5 6 3
2 3 2 5
6 1 2 7
4 5 3 2
Output : Sum =52
</pre>

> 32. Binomial co-efficient can be calculated by using the following formula : nCm = n!/m!(n–m)! (where ! sign represents the factorial of a number) 
WAP in java to calculate and print the binomial co-efficient of the given expression, taking the value n and m as input . Make use of the function int fact( int k ), which returns the factorial of a number k. 

> 33. Seema is a teacher.She has got the job to arrange N number of papers in ascending order by there marks. There are T number of sections. Help her do the work.
<pre>
Input: 2
       4
       65 76 65 34 
       3 
       56 54 65

Output:34 65 65 76 
       54 56 65 

Time Complexity: O(n^2) 
Auxiliary Space: O(1)
</pre>

> 34. You are given two integer arrays a and b of length n. You can reverse at most one subarray (continuous subsegment) of the array a. Your task is to reverse such a subarray that the sum ∑i=1nai⋅bi is maximized.
<pre>
Input
The first line contains one integer n (1≤n≤5000).

The second line contains n integers a1,a2,…,an (1≤ai≤107).

The third line contains n integers b1,b2,…,bn (1≤bi≤107).

Output
Print single integer — maximum possible sum after reversing at most one subarray (continuous subsegment) of a.

Examples

input
5
2 3 2 1 3
1 3 2 4 2
output 
29

input 
2
13 37
2 4
output 
174

input 
6
1 8 7 6 3 6
5 9 6 8 8 6
output 
235
</pre>

> 35. Find the n th fibonacci number
<pre>
Time complexity:O(logn)
Space Complexity:O(1)
</pre>

> 36. Write a program to display all the N numbers of a Catalan Number sequence.
<pre>
Time Complexity: O(n^2)
</pre>

> 37. The Gray code is a well-known concept. One of its important properties is that every two adjacent numbers have exactly one different digit in their binary representation.
In this problem, we will give you n non-negative integers in a sequence A[1..n] (0<=A[i]<2^64), such that every two adjacent integers have exactly one different digit in their binary representation, similar to the Gray code.
Your task is to check whether there exist 4 numbers A[i1], A[i2], A[i3], A[i4] (1 <= i1 < i2 < i3 < i4 <= n) out of the given n numbers such that A[i1] xor A[i2] xor A[i3] xor A[i4] = 0.
<pre>
Input
First line contains one integer n (4<=n<=100000). Second line contains n space seperated non-negative integers denoting the sequence A.

Output
Output “Yes” (quotes exclusive) if there exist four distinct indices i1, i2, i3, i4 such that A[i1] xor A[i2] xor A[i3] xor A[i4] = 0. Otherwise, output "No" (quotes exclusive) please.

Example
Input:
5
1 0 2 3 7
Output:
Yes
</pre>

> 38. You are given a multiset of N integers. Please find such a nonempty subset of it that the sum of the subset's elements is divisible by N. Otherwise, state that this subset doesn't exist.
<pre>
Input
The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test consists of a single integer N - the size of the multiset.
The second line of each test contains N single space separated integers - the multiset's elements.

Output
For each test case output:

  ->  -1 if the required subset doesn't exist
  ->  If the required subset exists, output two lines. Output the size of the subset on the first line and output the list of indices of the multiset's element that form the required subset. Of course, any number can be taken in the subset no more than once.
  ->   If there are several such subsets, you can output any.

Constraints
  ->	1 <= The sum of N over all the test cases <= 105
  ->	Each element of the multiset is a positive integer, not exceeding 109.
  ->	1 <= N <= 15   
  ->	1 <= N <= 1000 
  ->	1 <= N <= 105 
Example

Input:
1
3
4 6 10

Output:
1
2
</pre>

> 39. Peter wants to generate some prime numbers for his cryptosystem. Help him! Your task is to generate all prime numbers between two given numbers!
<pre>
Input
The input begins with the number t of test cases in a single line (t<=10). In each of the next t lines there are two numbers m and n (1 <= m <= n <= 1000000000, n-m<=100000) separated by a space.

Output
For every test case print all prime numbers p such that m <= p <= n, one number per line, test cases separated by an empty line.

Example
Input:
2
1 10
3 5

Output:
2
3
5
7

3
5
</pre>

> 40. In this problem Sereja is interested in number of arrays A[1], A[2], ..., A[N] (1 ≤ A[i] ≤ M, A[i] - integer) such that least common multiple (LCM) of all its elements is divisible by number D.
Please, find sum of answers to the problem with D = L, D = L+1, ..., D = R. As answer could be large, please output it modulo (10^9 + 7).
<pre>
Input
  ->	First line of input contain integer T - number of test cases.
  ->	For each test case, only line of input contain four integers N, M, L, R.
Output
   ->	For each test case, output required sum modulo (109 + 7).
Constraints
   ->	1 ≤ T ≤ 10
   ->	1 ≤ N ≤ 5*106
   ->	1 ≤ L ≤ R ≤ M ≤ 1000
Example
Input:
2
5 5 1 5
5 5 4 5
Output:
12310
4202
</pre>

> 41. You are given a sequence of numbers a1, a2, ..., an, and a number m. Check if it is possible to choose a non-empty subsequence aij such that the sum of numbers in this subsequence is divisible by m.
<pre>
Input
The first line contains two numbers, n and m (1 ≤ n ≤ 106, 2 ≤ m ≤ 103) — the size of the original sequence and the number such that sum should be divisible by it.

The second line contains n integers a1, a2, ..., an (0 ≤ ai ≤ 109).

Output
In the single line print either "YES" (without the quotes) if there exists the sought subsequence, or "NO" (without the quotes), if such subsequence doesn't exist.

Examples
input 
3 5
1 2 3
output 
YES
input 
1 6
5
output 
NO
input 
4 6
3 1 1 3
output 
YES
input 
6 6
5 5 5 5 5 5
output 
YES
</pre>

> 42. Print the following pattern
<pre>
				5				
			4		6			
		3		5		7		
	2		4		6		8	
1		3		5		7		9
</pre>

> 43. Program to convert Decimal to Binary,Octal,HexaDecimal numbers. (Within Single Function).

> 44. WAP to check if the binary representation of a number is palindrome.

> 45. WAP to Minimize given integer by swapping pairs of unequal bits(0,1) in its binary representation.

> 46. WAP to find roots of any quadratic equation.
<pre>
Input:
5
2.5
3
Output:
root1 = -0.25+0.73i
root2 = -0.25-0.73i
</pre>

> 47. WAP to check if a number is Armstrong number or not.

> 48. Compute x^y using only bit-wise operators.
<pre>
Test Case:
2.0
3
Output:8.0
</pre>

> 49. WAP to print following triangle:
<pre>
        *
      * *
    * * *
  * * * *
* * * * *
</pre>

> 50. Write a program to find the maximum number of distinct prime factors a number has in a given range and print the max number of factors.
<pre>
Example:
Input first integer:  5
Input second integer:  25
</pre>

> 51. Write a java program to find next smallest palindrome number.
<pre>
Example: 
Input the number:  121
Next smallest palindrome:131
</pre>

> 52. Write a program to print the following pattern:
<pre>
     CWC
    C W C
   C  W  C
  C   W   C
 C    W    C
</pre>

> 53. Write a program to print this series:
<pre>
1,1,4,8,9,27,16,64,.... Upto n terms
</pre>

> 54. WAP to Print the pattern given below:
<pre>
*****
 ***
  *
 ***
*****
</pre>

> 55. Given two complex numbers, write a program to add two numbers.

> 56. Write a program to display whether a number is magic number or not. A magic number is a number whose sum of the digits when added gives result 1.
<pre>
Test case 1: 19 
Output: Magic number
Explanation: 1+9=10. 10=1+0=1.
Test Case 2: 28
Output: Magic number
Explanation: 2+8=10. 10=1+0=1.
</pre>

> 57. Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
<pre>
Note:
•	Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
•	In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.
•	Example 1:
•	Input: n = 00000000000000000000000000001011
•	Output: 3
•	Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
•	Example 2:
•	Input: n = 00000000000000000000000010000000
•	Output: 1
•	Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
•	Example 3:
•	Input: n = 11111111111111111111111111111101
•	Output: 31
•	Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
</pre>

> 58. Write a program covert roman to integer. 

> 59. Write a program to create a array of size N. Then perform a number of right circular rotations and return the values of the elements at the given indices.
<pre>
Input Format
The first line contains 3 space-separated integers, n, p, and  q. Where n is the number of elements in the integer array, p is the rotation count and q is the number of queries. The second line contains n space-separated integers, where each integer i describes array element 

Input
N=3 p= 2 q=3
A[]= {1 ,2 ,3}
q1 = 0
q2 = 1
q3 = 2
Output
2
3
1
Explanation 
After the first rotation, the array is  [3,1,2]
After the second (and final) rotation, the array is [2,3,1].
We will print this final query indices
</pre>

> 60. Write a program to input two matrices then display the product of those two matrices. 

> 61. Write a program to display square root of a N numbers using newton’s method.

> 62. Write a program to take N numbers as input. Then display only prime - palindromes using method overloading concept.
<pre>
Example of prime palindromes are 2,3,5,7,11,101, and so on.
</pre>

> 63. Calculate the total fare of your ride in taxi. The taxi has a base fee of P40.00 for the first 250 meters. An additional P2.50 is added for every succeeding 200 meters. Compute and print the total fare that you would need to pay.
<pre>
Input Format:
A single line containing the total distance traveled.
Input Sample:
250
Output Format:
A single line containing the total cost of the ride.
Output Sample:
P40.00
</pre>

> 64. William planned to choose a four digit lucky number for his car. His lucky numbers are 3,5 and 7. Help him find the number, whose sum is divisible by  3 or 5 or 7.
Provide a valid car number, Fails to provide a valid input then display that number is not a valid car number. 
<pre>
Note : The input other than 4 digit positive number[includes negative and 0] is considered as invalid.
Sample Input 1:
Enter the car no:1234
Sample Output 1:
Lucky Number
Sample Input 2:
Enter the car no:1214
Sample Output 2:
Sorry its not my lucky number
Sample Input 3:
Enter the car no:14
Sample Output 3:
14 is not a valid car number
</pre>

> 65. The number will be unique if it is positive integer and there are no repeated digits in the number. In other words, a number is said to be unique if and only if the digits are not duplicate. For example, 20, 56, 9863, 145, etc. are the unique numbers while 33, 121, 900, 1010, etc. are not unique numbers 
<pre>
O/p: Enter the number you want to check: 13895
The number is unique.
</pre>

> 66. Find the 15th term of the series.
<pre>
0,0,7,6,14,12,21,18,28,…	
</pre>

> 67. WAP that given three arrays sorted in non-decreasing order, print all common elements in these arrays.
<pre>
Input: 
ar1[] = {1, 5, 10, 20, 40, 80} 
ar2[] = {6, 7, 20, 80, 100} 
ar3[] = {3, 4, 15, 20, 30, 70, 80, 120} 
Output: 20, 80
</pre>

> 68. WAP that given array and split it from a specified position, and move the first part of the array add to the end. 
<pre>
Input : arr[] = {12, 10, 5, 6, 52, 36}
            k = 2
Output : arr[] = {5, 6, 52, 36, 12, 10}
</pre>

> 69. WAP that given a number n, the task is to find the even factor sum of a number.
<pre>
Input : 30
Output : 48
Even dividers sum 2 + 6 + 10 + 30 = 48
</pre>

> 70. WAP that given a number, find minimum sum of its factors.
<pre>
Input : 12
Output : 7
Explanation: 
Following are different ways to factorize 12 and
sum of factors in different ways.
12 = 12 * 1 = 12 + 1 = 13
12 = 2 * 6 = 2 + 6 = 8
12 = 3 * 4 = 3 + 4 = 7
12 = 2 * 2 * 3 = 2 + 2 + 3 = 7
Therefore minimum sum is 7
</pre>

> 71. Given an integer N, the task is to generate a matrix of dimensions N x N using positive integers from the range [1, N] such that the sum of the secondary diagonal is a prefect square
<pre>
Input: N = 7
Output:
1 2 3 4 5 6 7
2 3 4 5 6 7 1
3 4 5 6 7 1 2
4 5 6 7 1 2 3
5 6 7 1 2 3 4
6 7 1 2 3 4 5
7 1 2 3 4 5 6
Explanation:
The sum of secondary diagonal = 3 + 3 + 3 = 9(= 3^2).
</pre>

> 72. Write a program Given two integer arrays of same size, “arr[]” and “index[]”, reorder elements in “arr[]” according to given index array. It is not allowed to given array arr’s length.
<pre>
Input:  arr[]   = [50, 40, 70, 60, 90]
        index[] = [3,  0,  4,  1,  2]
Output: arr[]   = [40, 60, 90, 50, 70]
        index[] = [0,  1,  2,  3,   4]
</pre>

> 73. Write a program to evaluate the function sin(x) as defined by the infinite series expansion.
<pre>
sin (x) = x- x 3 /3! + x5 /5! - x 7 /7! +…
The acceptable error for computation is 10^-6 
</pre>

> 74. Write a program to compute the harmonic mean.

> 75. WAP that show double factorial
<pre>
Input: 6
Output: 48
Note that 6*4*2 = 48
</pre>

> 76. Maya celebrated her birthday party. After the completion of cake cutting ceremony, Maya’s mom cuts the cake into various pieces inorder to distribute it to all her friends.Given an integer n denoting the number of cuts that can be made on a birthday cake. Write a code to find the maximum number of pieces that can be formed by making n cuts.
<pre>
 Example :
 Input:  N = 6
 Output: 22
 Explanation: 22 pieces can be formed by making 6 cuts
</pre>

> 77. Given an array a[] of size n and a number num ,write a program to find if there exists a pair of elements in the array whose difference is num.
<pre>
Example:
Input: n = 6 , num = 78
a[ ] = { 5, 3, 2, 80, 20, 5 }
Output:1
Explanation: (2, 80) have difference of 78.
</pre>

> 78. Given an array a[ ]  of size n, swap the p th element from beginning with p th  element from end.
<pre>
Example:
Input: n = 8, p = 3 
a[ ] = {1, 2, 3, 4, 5, 6, 7, 8}
Output: 1 2 6 4 5 3 7 8
Explanation: pth element from beginning is 3 and from end is 6
</pre>

> 79. Print the following pattern.
<pre>
        1
        2    3
        4    5    6
        7     8    9     10
</pre>

> 80. Given two numbers m and n , you are required to check whether they are anagram of each other or not in binary representation?
<pre>
Example:
Input:
m = 8, n = 4 
Output: True 
Explanation: Binary representation of both numbers have same 0s and 1s
</pre>

> 81. Given an array of even size N, task is to find minimum value that can be added to an element so that array become balanced. An array is balanced if the sum of the left half of the array elements is equal to the sum of right half.
<pre>
Example:
Input:  n = 4 
a[ ] = { 1, 5, 3, 2}
Output: 1
Explanation: 
Sum of right half of the array = 3 + 2 = 5
Sum of left half of the array = 1 + 5 = 6
To make the array balance we need to add 1
</pre>

> 82. Given a sorted array containing only 0s and 1s, find the transition point. Note: return -1 if there is no transition point.
<pre>
Example: 
Input: n = 5
arr[ ] = { 0, 0, 0, 0, 1}
Output: 4
Explanation: 4 is the transition point from where 1 starts
Input : n = 4
arr[ ] = {1, 1, 1, 1}
Output: -1
Explanation: -1 because there is no transition point
</pre>

> 83. Given an array arr of positive integers. Your task is to find the leaders in the array. An element of array is leader if it is greater than or equal to all the elements to its right side. The rightmost element is always a leader. 
<pre>
Hint: Traverse all the elements from right to left in array and check whether the current element is greater than the maximum stored till now.
Example:
Input: n = 6
arr[ ] = { 16, 17, 4, 3, 5, 2}
Output: 17  5  2
</pre>

> 84. Print the following pattern.
<pre>
                     1
                 1      2
            1       2       3
       1        2       3      4
   1       2       3       4      5
</pre>

> 85. Print the following pattern.
<pre>
      1   2   3   4   
          1   2   3   
              1   2   
                  1
</pre>

> 86. Write a program to generate and show all Kaprekar numbers less than 1000.
<pre>
Expected Output :
1       1         0 + 1                                  
9       81        8 + 1                                  
45      2025      20 + 25                                
55      3025      30 + 25                                
99      9801      98 + 01                                
297     88209     88 + 209                               
703     494209    494 + 209                              
999     998001    998 + 001                              
8 Kaprekar numbers.  
</pre>

> 87. Write a program to accept a float value of number and return a rounded float value.
<pre>
Sample data:
Input a float number: 12.51
The rounded value of 12.510000 is: 13.00
Input a float number: 12.49999
The rounded value of 12.499990 is: 12.00
</pre>

> 88. Write a program to generate random integers in a specific range.

> 89. Write a program to generate a magic square of order n (all row, column, and diagonal sums are equal).

> 90. Write a program to reverse an integer number.

> 91. The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143.

> 92. Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

> 93. 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.What is the sum of the digits of the number 2^1000.

> 94. 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20.

> 95. The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum of all the primes below two million.

> 96. Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

> 97. In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:
<pre>
1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:
1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
</pre>

> 98. Find the sum of all numbers which are equal to the sum of the factorial of their digits.

> 99. Program to calculate circular primes below one million?

> 100. Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
