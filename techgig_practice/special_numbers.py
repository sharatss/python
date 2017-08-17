"""
Count special numbers between boundaries (100 Marks)

This challenge will help you in getting familiarity with functions which will be helpful when you will solve further problems on Techgig. 

Task:
For this challenge, you are given a range and you need to find how many prime numbers lying between the given range. 


Input Format: 
For this challenge, you need to take two integers on separate lines. These numbers defines the range. 

Output Format: 
output will be the single number which tells how many prime numbers are there between given range. 


Sample Test Case:
Sample Input: 
3 
21

Sample Output: 
7


Explanation: 
There are 7 prime numbers which lies in the given range. 
They are 3, 5, 7, 11, 13, 17, 19
"""

def main():
 
 # Write code here 
 
 lower_bound = int(input())
 upper_bound = int(input())
 count = 0
 
 for number in range(lower_bound, upper_bound+1):
     if number > 1:
         for i in range(2, number):
             if (number % i) == 0:
                 break
         else:
             count = count + 1

 print(count)
 
main()
