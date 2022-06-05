def quick_sort(arr,left,right):
    if arr==[] or arr==None:
        raise Exception("array empty or None")
    if  right >= len(arr):
        raise Exception("index errors")
    if left < right:
        position = partition(arr,left,right)
        quick_sort(arr,left,position-1)
        quick_sort(arr , position+1,right)
        return arr



def partition(arr,left,right):
    pivot = arr[right]
    low = left-1
    for i in range(left,right):
        if arr[i] <= pivot:
            low+=1
            swap(arr,i,low)
    swap(arr,right,low+1)
    return(low+1)


def swap(arr,i,low):
    arr[i],arr[low]=arr[low],arr[i]



if __name__=="__main__":
    arr=[8,4,23,42,16,15]
    print(quick_sort(arr,0,5))