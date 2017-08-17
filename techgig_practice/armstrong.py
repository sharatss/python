"""
Is your Number Armstrong? (100 Marks)

This challenge wants that you have familiarity with following topics in order to solve this problem - 
Loops - while or do-while 
functions 
operators like division and mod. 
pre-defined functions like that of power or you can create on your own 

Task: 
For this challenge, you need to take an integer input and store it in a variable of your choice and checks whether this number is an Armstrong number or not. If yes print 'True' else print 'False'. 


Input Format: 
A single integer value to be taken as input from stdin and stored it in a variable. 

Output Format:
print 'True' if your number is Armstrong otherwise print 'False' to the stdout. 


Sample Test Case:
Sample Input: 
153

Sample Output: 
True


Explanation:
First of all, what is a Armstrong Number? 
An Armstrong number of three digits is an integer such that the sum of the cubes of its digits is equal to the number itself. 

For example, take the number 153 
153 = 1^3 + 5^3 + 3^3 
So, this is a Armstrong Number. 

Take Another Example, now the number is 372 
372 != 3^3 + 7^3 + 2^3
"""

def main():
 
 # Write code here 
 
 number = int(input())
 remain = number
 sum = 0
 
 while remain > 0:
     digit = remain % 10
     sum = sum + digit **3
     remain = remain // 10
 
 if sum == number:
     print("True")
 else:
     print("False")
     
main()
