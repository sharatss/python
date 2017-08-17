"""
Count the letters (100 Marks)

This challenge will help you in getting familiarity with strings which will be helpful when you will solve further problems on Techgig. 

Task: 
For this challenge, you need to take a string as an input from the stdin, count the number of uppercase and lowercase letters and print them to the stdout. 


Input Format: 
A single line of string to be taken as an input and store it in a variable of your choice. 

Output Format: 
print the number of uppercase letters on one line and number of lowercase letters on another side. 


Sample Test Case:
Sample Input: 
Techgig Is The Best Coding Platform.

Sample Output: 
6 
24


Explanation: 
For the above string which is taken as input, it has 6 uppercase letters which is displayed on one line and 24 lowercase letters which is displayed on another line.
"""

def main():
 
 # Write code here 
 string = input()
 upper_case, lower_case = 0, 0

 for character in string:
     if character.isupper():
         upper_case += 1
     elif character.islower():
         lower_case += 1

 print(upper_case)
 print(lower_case)
main()
