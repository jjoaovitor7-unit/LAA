#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import printArr as p
import insertionSort as iS

# declaração do array
n = [9, 10, 11, 24, 1,
     2, 56, 32, 0, 90]

# printar o array desordenado
print("Array desordenado:")
p.printArr(n)

# printar o array ordenado
print("Array ordenado:")
p.printArr(iS.insertionSort(n))
