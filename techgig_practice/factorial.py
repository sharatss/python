"""
Loop your world (100 Marks)

This challenge will help you in clearing your loop fundamentals in your favorite programming language. 

Task: 
For this challenge, you need to take an integer value as input from stdin, calculate its factorial and print the result to the stdout. 


Input Format: 
A single integer value to be taken as input from stdin and stored it in a variable of your choice. 

Output Format: 
Print the value which you will get after calculating the factorial of the input. 


Sample Test Case:
Sample Input: 
5

Sample Output: 
120


Explanation: 
For a number, we will calculate its factorial by multiplying the number with the numbers which comes between 1(inclusive) and the number itself. 
For input as 5, its factorial will be 1*2*3*4*5 = 120. 
factorial of n (n!) = 1*2*3*4....n
"""

def main():
 
 # Write code here 
 number = int(input())
 fact = 1

 for i in range(1,number+1):
     fact = i * fact
 print(fact)
 
main()
