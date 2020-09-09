function bubbleSort(arr) {
    // Função para realizar o BubbleSort

    // laço externo para controlar o limite de posição final a ser percorrida
    // -1 porque não pode comparar o último c/ outro próximo elemento,
    // compara até o penúltimo e o último.
    for (let i=0; i < arr.length-1; i++) {

        for (let j=0; j < arr.length-1; j++) {
            // laço interno para fazer as comparações

            if (arr[j] > arr[j+1]) {
               // se o elemento atual for maior que o elemento anterior, faça

                let aux=arr[j]; //auxiliar recebe elemento atual
                arr[j] = arr[j+1]; // elemento atual recebe o próximo elemento
                arr[j+1] = aux; // o próximo elemento recebe o elemento atual
            }
        }
    }
    return arr;
}

module.exports = bubbleSort;
