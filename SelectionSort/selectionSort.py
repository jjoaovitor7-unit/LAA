def selectionSort(arr):

    for i in range(0, len(arr) - 1):
        menor = i # índice do menor valor

        # i+1 porque compara c/ o próximo elemento
        for j in range(i+1, len(arr)):
            # se o elemento atual for menor que o elemento menor atual,
            # troca o índice do menor pelo índice do elemento atual
            if arr[j] < arr[menor]:
                menor = j
    
        # caso o índice do menor seja diferente de i,
        # realiza a troca
        if menor != i:
            aux = arr[i]
            arr[i] = arr[menor]
            arr[menor] = aux
    
    return arr
