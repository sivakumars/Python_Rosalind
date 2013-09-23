def calcprob(k,m,n):
    tot = k+m+n
    #probability of recessive Phenotype given One parent is 'Tt'
    rm = (m/tot)*( ( (1/4)*((m-1)/(tot-1)) ) + ( (1/2) * (n/(tot-1)) ))
    #probability of recessive Phenotype given one Parent is 'tt'
    rn = (n/tot)*( ( 1 * ((n-1)/(tot-1)) ) + (  (1/2)*(m/(tot-1) ) )                                               )
    
    print (1-(rm+rn))
    

if __name__ == '__main__':
    k,m,n= input('''Enter the population numbers (k,m,n)
                    TT -> Homozygous Dominant
                    Tt -> Heterozygous
                    tt -> Homozygous recessive \n''').split(' ')[:3]
    calcprob(int(k),int(m),int(n))                
