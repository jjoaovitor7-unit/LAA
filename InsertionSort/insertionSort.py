def insertionSort(vet):
    
    # laço de repetição para i em um alcance
    for i in range(len(vet)):
        j = i # j = i para percorrer os elementos anteriores ao vetor
        aux = vet[i] # o auxiliar para pegar o elemento "atual" do vetor

    while j > 0 and (vet[j-1] > aux):
        """enquanto j > 0, ou seja, enquanto j for positivo
           e vet[j-1] maior que aux, ou seja, maior que o elemento atual,
           faça
        """

        vet [j] = vet[j-1] # substitui o valor atual pelo anterior se condições satisfeitas
        j -= 1 # e decrementa

    vet[j] = aux # substitui o valor atual se condições satisfeitas, ex. 25 é menor que 56.

    return vet # retorna o vetor
