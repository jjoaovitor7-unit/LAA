def insertionSort(arr):
    '''Insertion Sort'''

    # laço de repetição, para i in range de 1 ao tamanho do array
    for i in range(1, len(arr)):
        aux = arr[i] # aux recebe o valor atual do array
        j = i-1 # p/ fazer o laço de repetição
                # para os elementos anteriores

        while j >= 0 and arr[j] > aux:
            """enquanto j for positivo (maior ou igual a 0)
                e o elemento atual for maior que o aux
                faça
            """

            arr[j + 1] = arr[j] # o elemento atual substitui o próximo elemento
                                # caso seja maior que o aux

            j -= 1 # decrementa j para ir pegando os elementos anteriores

        arr[j + 1] = aux # caso seja menor o próximo elemento é o aux

    return arr
