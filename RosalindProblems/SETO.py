


if __name__ == '__main__':
    n = int(input('Enter the Size of Universal set(n)\n').strip())
    setA =  input('Enter the values of set(A)\n').strip()
    setB =  input('Enter the values of set(B)\n').strip()
   
    A = set([int(x) for x in setA.split(',')])
    B = set([int(x) for x in setB.split(',')])
    print('{%s}' % ', '.join([str(x) for x in A | B]))
    print('{%s}' % ', '.join([str(x) for x in A & B]))
    print('{%s}' % ', '.join([str(x) for x in A - B]))
    print('{%s}' % ', '.join([str(x) for x in B - A]))
    print('{%s}' % ', '.join([str(x) for x in set(range(1, n+1)) - A]))
    print('{%s}' % ', '.join([str(x) for x in set(range(1, n+1)) - B]))