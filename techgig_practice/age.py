"""
Decide yourself with conditional statement (100 Marks)

This challenge will help you in clearing your fundamentals with if-else conditionals which are the basic part of all programming languages. 

Task: 
For this challenge, you need to read a integer value(default name - age) from stdin, store it in a variable and then compare that value with the conditions given below - 
    - if age is less than 10, then print 'I am happy as having no responsibilities.' to the stdout. 
    - if age is equal to or greater than 10 but less than 18, then print 'I am still happy but starts feeling pressure of life.' to the stdout. 
    - if age is equal to or greater than 18, then print 'I am very much happy as i handled the pressure very well.' to the stdout. 


Input Format: 
A single line to be taken as input and save it into a variable of your choice(Default name - age). 

Output Format: 
Print the sentence according to the value of the integer which you had taken as an input. 


Sample Test Case:
Sample Input: 
10

Sample Output:
I am still happy but starts feeling pressure of life.


Explanation:
The value of the variable is 10 and it comes under the condition that it equal to or greater than 10 but less than 18.
"""

def main():
 
 # Write code here 
 age = int(input())
 
 if age < 10:
     print("I am happy as having no responsibilities.")
 elif (age >=10 and age < 18):
     print("I am still happy but starts feeling pressure of life.")
 else:
     print("I am very much happy as i handled the pressure very well.")
     
main()
