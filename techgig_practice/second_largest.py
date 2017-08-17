"""
Who's the second largest? (100 Marks)

This challenge will help you in getting familiarity with arrays which will be helpful when you will solve further problems on Techgig. 

Task: 
For this challenge, you need to take number of elements as input on one line and array elements as an input on another line and find the second largest array element and print that element to the stdout. 


Input Format: 
In this challenge, you will take number of elements as input on one line and array elements which are space separated as input on another line. 

Output Format: 
You will print the second largest element to the stdout. 


Sample Test Case:
Sample Input: 
5 
23 11 24 13 55

Sample Output:
24


Explanation: 
Of all the given elements, search the second largest element.
"""

def main():
 
 # Write code here 
 
 number = int(input())
 elements = input()
 element = elements.split()
 array = list(map(int, element))
 first = max(array)
 array_without_first = list()
 
 for i in range(len(array)):
     if first != array[i]:
         array_without_first.append(array[i])
 
 second = max(array_without_first)
 print(second)

main()
