from pyscript import display

def quickSort(A, low, high):
    if (low >= high):
        return
    lmgt = low+1
    for i in range(low+1, high+1):
        if(A[i] < A[low]):
            A[i],A[lmgt] = A[lmgt], A[i]
            lmgt+=1
    pivot = lmgt-1
    A[low],A[pivot] = A[pivot],A[low]
    quickSort(A, low, pivot-1)
    quickSort(A, pivot+1, high)

def run_quicksort():
    list1 = [3,5,1,6,5,2,9,0,4,6]
    quickSort(list1,0,9)
    result = (str(list1)[1:-1])
    display(result, target="quicksort-output", append=False)