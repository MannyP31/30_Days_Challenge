<img src="https://media-exp1.licdn.com/dms/image/C4E03AQFDuHx-TrxMNg/profile-displayphoto-shrink_200_200/0/1614907425476?e=1627516800&v=beta&t=6j8PxnUIH5UvyKuhwCJ498EiPLUzgu_c_h-HHor8dVc" align="right" width="100" height="100"/>

# 30 Days Challenge Month-I

[![](https://img.shields.io/badge/CWC-ITER-gray.svg?style=for-the-badge&colorB=0000f&logo=github)](https://elastic-bose-ed6583.netlify.app/)

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
