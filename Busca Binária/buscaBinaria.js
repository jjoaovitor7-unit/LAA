function buscaBinaria (element, arr){
    let primeiro = 0; // 1º elemento
    let ultimo = arr.length - 1; // último elemento

    while(primeiro <= ultimo ){
        let meio = Math.floor((primeiro+ultimo)/2); // elemento meio

        if (element == arr[meio]){
            return meio;
        } else if (element < arr[meio]) {
            ultimo = meio - 1; // remove a parte direita do vetor
        } else if (element > arr[meio]) {
            primeiro = meio + 1; // remove a parte esquerda do vetor
        }
    }
    return "Elemento não existe.";
}

module.exports = buscaBinaria;
