

if __name__ == '__main__':
    str1, str2 = input("Enter Sequences separated by commas:\n").split(',')[:2] 
    str1, str2 = str1.strip(),str2.strip() 
    s = 0;
    for s1, s2 in zip(str1, str2):
        if(s1 != s2):
            s+=1
    print (s)   
    