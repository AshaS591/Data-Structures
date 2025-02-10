def sort_elements(collection):
    length=len(collection)
    for val in range(1,length):
        for index in range(length-val):
            if collection[index]>collection[index+1]:
                collection[index],collection[index+1]=collection[index+1],collection[index]
            index+=1
    return collection
collection = [90,0,-20,5,9,2]
print(sort_elements(collection))
