chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    #Your code go here:
    new_list = []
    for name in list1:
        new_list.append(name)
    for name in list2:
        new_list.append(name)
    return new_list
print(merge_list(chunk_one, chunk_two))
