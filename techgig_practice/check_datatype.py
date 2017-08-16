"""
Exploring Data Types (100 Marks)

This problem is all about various data types available in the languages. 

Task: 
For this challenge, you need to read a line from stdin and check whether it is of type integer, float or string. 
If input is- 
    Integer print 'This input is of type Integer.' to the stdout 
    Float print 'This input is of type Float.' to the stdout 
    String print 'This input is of type string.' to the stdout 
    else print 'This is something else.' to the stdout. 


Input Format: 
A single line to be taken as input as save it to a variable(name of your choice). 

Output Format: 
Print the text according to the data type you get as an input. 


Sample Test Case:
Sample Input:
23

Sample Output: 
This input is of type Integer.



Explanation: 
If the given input is of type integer, then you need to print 'This input is of type Integer.' to the stdout, else if the given input is of type float, then you need to print 'This input is of type Float.' to the stdout, else if the given input is of type string, then you need to print 'This input is of type string' to the stdout, else print 'This is something else' to the stdout.
"""

def main():
 
 # Write code here
 number = input()
 
 try:
     test_var = int(number)
     print("This input is of type Integer.")
 except:
     try:
         test_var = float(number)
         print("This input is of type Float.")
     except:
         print("This input is of type string.")

 if len(number) == 0:
     print("This is something else.")
     
main()
