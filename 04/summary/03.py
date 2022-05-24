n = 3

tab = [['-', '-', '-'],
  ['-', '-', '-'],
  ['-', '-', '-']]
for i in tab:
  print(*i)
for row in tab:
  for i in row:
    print(i, end=' ')
  print()