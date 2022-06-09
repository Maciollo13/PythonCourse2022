l1 = ["rope", 'shoes', 'hat']
with open("hiking.txt","w") as f:
    for i in l1:
        f.write(i + "\n")