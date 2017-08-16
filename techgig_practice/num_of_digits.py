"""
How Much Big Is Your Number (100 Marks)

This challenge will help you in getting familiarity with division operator and the while loop which will be helpful when you will solve further problems on Techgig. 

Task: 
For this challenge, you will take an integer input from stdin, store it in a variable and  calculate the number of digits in the number using division operator. 


Input Format: 
A single integer value to be taken as input from stdin and stored it in a variable of your choice. 

Output Format: 
Print the value which you will get after calculating the number of digits. 


Sample Test Case:
Sample Input: 
34567

Sample Output: 
5


Explanation: 
Every time you divide the input number by 10, one digit get reduced and you need to maintain a count of that until the input number reduced to 0. The count value is your answer. 
34567/10 = 3456   count = 1 
3456/10 = 345       count = 2 
345/10 = 34           count = 3 
34/10 = 3               count = 4 
3/10 = 0                 count = 5
"""

def main():
 
 # Write code here 
 number = int(input())
 count = 0
 
 while(number>0):
     number = number // 10
     count = count + 1
 
 print(count)
 
main()
