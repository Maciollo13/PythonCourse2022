days = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sept': 30}
list1 = []
set1 = {}
set1 =set(days.values())
list1 = list(set1)
print(list1)