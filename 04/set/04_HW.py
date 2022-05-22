list1 = [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]
list1.reverse()
third_index = len(list1) // 3
sixth_index = third_index * 2
list2 = list1[:third_index]
list3 = list1[third_index:sixth_index]
list4 = list1[sixth_index:]
print(list2)
print(list3)
print(list4)