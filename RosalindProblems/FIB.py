
def fib(n,k):
    a, b = n, k
    finalResult = [n,k]
    while len(finalResult) < n:
        a, b = b, a+b
        finalResult.append(b)
    #print(finalResult[-1:])
    print(b)

if __name__ == '__main__':    
    n, k = input('Enter the No of months and Pairs (n,k):\n').split(',')[:2]
    fib(int(n),int(k))
    