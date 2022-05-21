from fileinput import filename


def countWordsFromFile():
    filename=input("enter the file name:-")
    
    numberOfWords=0
    f=open(filename,'r')
    for line in f:
        words=line.split()
        numberOfWords=numberOfWords+len(words)
    print("numberOfWords:-")
    print(numberOfWords)
countWordsFromFile()
