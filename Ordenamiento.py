import time
import random
random.seed(51)
arregloInicial=[random.randrange(1,1000000) for _ in range(100000)]
def swap(A,x,y):
    temp=A[x]
    A[x]=A[y]
    A[y]=temp

def burbuja(A): 
    for i in range(1,len(A)):
        for j in range(0,len(A)-i):
            if(A[j]>A[j+1]):
                temp=A[j]
                A[j]=A[j+1]
                A[j+1]=temp
    #print(A)
def insercion(A):
    for i in range(0,len(A)):
        for j in range(i,0,-1):
            if(A[j]<A[j-1]):
                swap(A,j,j-1)
                #temp=A[j]
                #A[j]=A[j-1]
                #A[j-1]=temp
    #print(A)


def seleccion(A):
    
    for i in range(0,len(A)-1):
        jmin=i
        for j in range(i,len(A)):
            if(A[jmin]>A[j]):
                jmin=j
        if(jmin!=i):
            swap(A,i,jmin)
    #print(A)


def quickSort(A,min,max):
    pivote=A[int((min+max)/2)]
    swap(A,max,int((min+max)/2))
    i=min
    j=max
    while(j>i):
        while(A[i]<pivote):
            i+=1
        while(pivote<=A[j]):
            if(j==i):
                break
            j-=1
        if(j>i):
            swap(A,i,j)
    swap(A,max,j)
    if ((max-min)<=1):
        return  
    quickSort(A,min,i-1)
    quickSort(A,i+1,max)
    #escoger pivote 
    
def main():
    times1000=printTimes(1000)
    times10000=printTimes(10000)
    times20000=printTimes(20000)
    print("             1000        10000        20000")
    print("burbuja:   {:6f}     {:6f}     {:6f}".format(times1000["burbuja"],times10000["burbuja"],times20000["burbuja"]))
    print("insercion: {:6f}     {:6f}     {:6f}".format(times1000["insercion"],times10000["insercion"],times20000["insercion"]))
    print("seleccion: {:6f}     {:6f}     {:6f}".format(times1000["seleccion"],times10000["seleccion"],times20000["seleccion"]))
    print("QuickSort: {:6f}     {:6f}     {:6f}".format(times1000["quicksort"],times10000["quicksort"],times20000["quicksort"]))
    #print(arregloInicial)

def printTimes(size):
    print("--------------------burbuja")
    arregloPrueba=[arregloInicial[i] for i in range(size)]
    start, times = time.perf_counter(), {}
    burbuja(arregloPrueba)
    times["burbuja"] = -start + (start := time.perf_counter())

    print("--------------------insercion")
    start = time.perf_counter()
    arregloPrueba=[arregloInicial[i] for i in range(size)]
    insercion(arregloPrueba)
    times["insercion"] = -start + (start := time.perf_counter())
    print("--------------------seleccion")
    arregloPrueba=[arregloInicial[i] for i in range(size)]
    start = time.perf_counter()
    seleccion(arregloPrueba)
    times["seleccion"] = -start + (start := time.perf_counter())
    print("--------------------quickS")
    arregloPrueba=[arregloInicial[i] for i in range(size)]
    start = time.perf_counter()
    quickSort(arregloPrueba,0,len(arregloPrueba)-1)
    times["quicksort"] = -start + (start := time.perf_counter())
    #print(times)
    return times
if __name__ =='__main__':
    main()