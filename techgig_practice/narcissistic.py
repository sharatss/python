"""
Is Your Number Narcissistic? (100 Marks)

This challenge wants that you have familiarity with following topics in order to solve this problem - 
Loops - while or do-while 
functions 
operators like division and mod. 
pre-defined functions like that of power function or you can create on your own.(Yeah, at this stage you can create your own functions CONGRATULATIONS!!!) 

Task: 
For this challenge, you will take an integer input and store it in a variable and checks whether the input number is a Narcissistic number or not. If it is, then print 'True' else print 'False'. 


Input Format: 
A single integer value to be taken as input from stdin and stored it in a variable of your choice. 

Output Format: 
print 'True' if your number is Narcissistic otherwise print 'False' to the stdout. 


Sample Test Case:
Sample Input: 
1634

Sample Output: 
True


Explanation: 
First of all, what is a Narcissistic Number? 
An n-digit number that is the sum of the nth powers of its digits is called an n-narcissistic number. 

For example, take the number 1634 

1634 = 1^4 + 6^4 + 3^4 + 4^4 
So, this is a Narcissistic Number. 

Take Another Example, now the number is 372 
372 != 3^3 + 7^3 + 2^3
"""

def main():

 # Write code here 

 number = int(input())
 remain = number
 sum = 0
 power = len(str(number))
 
 while remain > 0:
     digit = remain % 10
     sum = sum + digit ** power
     remain = remain // 10

 if sum == number:
     print("True")
 else:
     print("False")

main()
