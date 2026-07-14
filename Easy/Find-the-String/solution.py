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
count = count_substring(string, sub_string)
print(count)
