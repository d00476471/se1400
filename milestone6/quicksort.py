from pyscript import display
import time

def bubbleSort(A):
    F = len(A)
    for i in range(F):
        for j in range(0,F-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]

def main():
    list1 = [3,5,1,6,5,2,9,0,4,6]
    bubbleSort(list1)
    display(list1, target="quicksort-output", append=True)

main()