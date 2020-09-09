def printArr(arr):
    '''Printar o array.'''

    myit = iter(arr)
    for i in range(len(arr)):
        print(next(myit), end=" ")
    print()
