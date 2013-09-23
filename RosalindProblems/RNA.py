

if __name__ == '__main__':
    dnaSeq = input('Enter a DNA sequence to be transcribed to RNA:\n').strip()
    #rnaSeq = bytes.maketrans(b'T', b'U') #version 3.3 maketrans doesn't work for string in 2.7
    #print(string.translate(rnaSeq))
    print(dnaSeq.replace('T', 'U'))
    