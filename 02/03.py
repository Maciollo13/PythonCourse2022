quote = 'Honesty is the first chapter in the book of wisdom.'
# counts lenght of the quote
print(len(quote))
# Print wisdom
print(quote[-7:-1:])
# print first halgf of quote
mid_id = len(quote)//2
print(quote[0:mid_id+1])
# print only dot
print(quote[-1])
# print from half of quote every third letter
print(quote[mid_id::3])
# print Hnsyi h is hpe ntebo fwso.
print(quote[0::2])
# print quote inversely
print(quote[::-1])
# change Wisdom to friendship
new_quote = quote.replace('wisdom', 'friendship')
print(new_quote)