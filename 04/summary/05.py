txt = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""

txt = txt.replace(',', '')
txt = txt.lower()
words = txt.split()

words_counter = {}
print((words))
for word in words:
    if word in words_counter:
        words_counter[word] += 1
    else:
        words_counter[word] = 1

for k, v in words_counter.items():
    print(f'- {k} : {v}')