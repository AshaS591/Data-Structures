def binary_search(collection,element): 
    start ,end = 0, len(collection)-1
    while start<=end:
        mid=(start+end)//2
        if collection[mid] == element:
            print(f"{element} is present")
            break
        elif collection[mid] < element:
            start=mid-1
        elif collection[mid] > element:
            end=mid-1
collection=[12,3,4,67,88,90]
element=67
binary_search(collection,element)