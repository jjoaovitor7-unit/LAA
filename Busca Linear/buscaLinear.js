function buscaLinear(arr, element){
    for(let i=0; i < arr.length; i++){
        if(arr[i] == element){
            return i;
        }
    }
}

module.exports = buscaLinear;
