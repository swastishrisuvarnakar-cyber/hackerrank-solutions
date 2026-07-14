# Find the String 
Problem Statement : The user enters a string and a substring. You have to print the number of times that the substring occurs in the given string.

## Concept I Learned  :

1.Strip()  function – it is used to remove the starting and trailing whitespaces or specific character 
Their types – 1. Rstrip() - removes from right side  2. Lstrip()– removes from left side
2. range function of for loop 
3. I understood the reason behind the generation of String index out of range error
4. the concept of String Slicing

## Solution:
'''
def count_substring(string, sub_string):
    count = 0
    i = 0
    sub_len = len(sub_string)
    length = len(string) - len(sub_string)
    length = length+1

    for i in range(0, length):
        if(string[i:i+ sub_len] ==sub_string):
            count+=1
    i +=1
    return count
string = input("enter:").strip()
substring = input("enter:").strip()
count = count_substring(string, substring)
print(count)
'''
## Initial Approaches:
'''
1.	if(string[i]==substring[0]):
            if(string[i+1]==substring[1]):
                if(string[i+2]==substring[2]):
                               count+=1

here I was trying to compare every character of the main string with the substring first character and if it match then it moves to match next character 
but here I got an error regarding String Index out of range 
to solve that I used the second approach
'''

2.
'''
    length = len(string) - len(substring)
    length = length+1

    for i in range(0, length):
        k = 0
        if(string[i]==substring[0]):
            if(string[i+1]==substring[1]):
                if(string[i+2]==substring[2]):
                    count+=1
    i +=1
  '''

    here by subtracting the length of substring from the main string and by adding 1 to it I got the exact length I needed 
how :
ex:
main _string = abcdcdc   length = 7
substring = cdc    length = 3
actually length calculated = 7-3 = 4

Here's why I thought this way :
because in the earlier approach I was getting an error whenever the program reach to the last index after that when we do i+1 there was nothing in the string that’s why  I was getting the string index out of range error.
So to solve this I first calculated the exact length where I have to stop 
But if you look closely you will see that I have added 1 after calculating the length
That was because when I will run the for loop so the range function actually takes the parameter like (0 ,n-1) so if I give it 4 it will stop at 3 
So I added 1 to the length so that it will stop at exact length we want
But this approach was not enough because it is not applicable for every input given because current program consider that the length of substring is only 3 but it could be different to solve this I used the another approach which actually succeed


## The Final Successful Approach:
'''
  if(string[i:i+ sub_len] ==sub_string):
  '''
I have used the concept of string slicing here to access the proper index
main _string = abcdcdc   substring = cdc    	
consider this input 
(string[i:i+ sub_len] – this actually make sure that the string is as long as the substring and then is checked whether it match or not this done for every character in the string 


## What I Understood

This problem taught me that solving a problem is not only about getting the correct output. Initially, I solved the problem by comparing characters manually, but while debugging I understood why the "String Index Out of Range" error occurs. Later, I learned how string slicing makes the solution more general because it works for substrings of any length instead of assuming the length is always 3.

## Status

- Problem Solved: ✅
- Concepts Revised:
  - String Slicing
  - String Indexing
  - strip()
  - range()
- Confidence Level: ⭐⭐⭐⭐☆ (4/5)
            


 


