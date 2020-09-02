#!/usr/bin/env python3

import printArr as p
import insertionSort as iS

# declaração do array
n = [56, 25, 32, 11, 10]

# printar o array desordenado
print("Array desordenado:")
p.printArr(n)

# printar o array ordenado
print("Array ordenado:")
p.printArr(iS.insertionSort(n))
