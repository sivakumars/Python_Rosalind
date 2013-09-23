

if __name__ == '__main__':
    dnaStr = input('Enter the DNA Sequence:\n').strip();
    a=t=g=c=0
    for n in dnaStr:
        if(n.lower() == 'a'):
            a+=1
        elif(n.lower() == 't'):
            t+=1
        elif(n.lower() == 'g'):
            g+=1
        elif(n.lower() == 'c'):
            c+=1            
    print (a, t, g, c)