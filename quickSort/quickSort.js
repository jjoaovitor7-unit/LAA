function quickSort(arr){
    // se o tamanho do array for igual a 0.
    if (arr.length == 0){
        return [];
    }

    // se o tamanho do array for igual a 1.
    else if (arr.length == 1){
        return arr;
    }

    // pivô é o elemento inicial
    let pivo = arr[0];

    // elementos menores que o pivô
    let menoresPivo = arr.filter(n => n < pivo);

    // elementos iguais ao pivô
    let igualPivo = arr.filter(n => n == pivo);
    
    // elementos maiores que o pivô
    let maioresPivo = arr.filter(n => n > pivo);

    // quicksort, pegando os elementos menores que o pivô e concatenando-os
    // c/ os elementos iguais ao pivô e concatenando-os c/ os elementos
    // ordenados e maiores do que o pivô.
    return quickSort(menoresPivo).concat(igualPivo).concat(quickSort(maioresPivo));
}

module.exports = quickSort;
