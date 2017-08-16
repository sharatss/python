"""
Play with operators (100 Marks)

This problem is all about using various types of arithmetic operators available in the language. 

Task: 
For this challenge, you will be given the values of principal, interest and year. You need to calculate the simple interest, round it to the nearest integer and print it. 


Input Format: 
There will be 3 lines of numeric input - 
principal which is of type double. 
interest which is of type integer. 
year which is again of type integer. 

Output Format: 
Just print the simple interest value after performing the calculation using the formula to the stdout. The result should be an integer. 


Sample Test Case:
Sample Input: 
100 
3 
2

Sample Output: 
6


Explanation: 
Given the value of principal, interest and year. You can calculate the simple interest using the formula 
Sample Interest = (principal * interest * year)/100 
Round the value to the nearest integer and print it.
"""

def main():
 
 # Write code here 
 principal = float(input())
 interest = int(input())
 year = int(input())
 
 simple_interest = (principal * interest * year)/100
 round_off = int(simple_interest)
 print(round_off)
 
main()
