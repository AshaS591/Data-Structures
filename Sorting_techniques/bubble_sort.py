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


collection = [2,3,1,1,8,9,4,6,8,4,6,3,2,6]
output={}
for num in collection:
    if num not in output:
        output[num]=1
    else:
        output[num]+=1
for key in output:
    if output[key]==1:
        print(key)
        break
