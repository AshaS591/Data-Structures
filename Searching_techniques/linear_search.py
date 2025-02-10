def search_element(collection,element):
    for val in collection:
        if val == element:
            print(f"{element} present at index {collection.index(element)}")
collection = [10,23,78,90,56,34]
element = 90
search_element(collection,element)

def search_item(collection,string):
    for val in collection:
        if val == element:
            print(f"{string} present at index {collection.index(string)}")
collection = ['orange','apple','kiwi','dragon']
string = 'apple'
search_element(collection,string)