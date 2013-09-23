
if __name__ == '__main__':
    dnaSeqStrand = input('Enter a DNA Strand sequence:\n').strip()
    complementarySeq = bytes.maketrans(b'GTCA', b'CAGT')
    dnaSeqStrand = dnaSeqStrand[::-1]
    print(dnaSeqStrand.translate(complementarySeq))