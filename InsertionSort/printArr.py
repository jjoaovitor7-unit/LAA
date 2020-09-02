def printArr(n):
    '''Printar o array.'''

    myit = iter(n)
    for i in range(len(n)):
        print(next(myit), end=" ")
    print()
