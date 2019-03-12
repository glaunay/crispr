
    
"""
    Translate a dictionary of constant-length CRISPR motifs into an ordered set of integer
    Usage:
        wordIntegerIndexing.py <pickledDictionary> [--out=<outFile> --length=<wordLength>]
    
    Options:
        -h --help                               Show this screen
        -o <outFile>, --out <outFile>           Name of the output file [default : ./inputFile.index]
      
"""

#  -l <wordLength>, --length <wordLength>  Length of the CRISPR motifs [default : 20]


from docopt import docopt

import os, pickle

def indexPickle(filePath, targetFile):
    pData = pickle.load( open( filePath, "rb" ) )
    wordList = list(pData.keys())
    data = sorted([ weightWord(w, ["A", "T", "C", "G"], len(wordList[0])) for w in wordList ])

    with open(targetFile, "w") as fp:
        fp.write(str(len(data)) + "\n")
        for l in data:
            fp.write(str(l) + "\n")
    
    return len(data)
    #print(, 'in', targetDir + "/" + targetFile)
    
def weightWord(word, alphabet, length=None) :
    rank = 0
    if length:
        if length != len(word):
            raise ValueError ("Irregular word length " + str(len(word)) + " (expected " + str(length) + ")") 
    for n,c in enumerate(word[::-1]):
        wei = alphabet.index(c)
        base = len(alphabet)
        rank += wei * pow(base,n)
    return rank

if __name__ == "__main__":
    arguments = docopt(__doc__, version='wordIntegerIndexing 1.0')
    targetFile = '.'.join(os.path.basename(arguments['<pickledDictionary>']).split('.')[0:-1]) + '.index'
    if arguments['--out']:
        targetFile = arguments['--out']

    total = indexPickle(arguments['<pickledDictionary>'], targetFile)

    print ("Successfully indexed", total, "words\nfrom:", arguments['<pickledDictionary>'], "\ninto:", targetFile)
    