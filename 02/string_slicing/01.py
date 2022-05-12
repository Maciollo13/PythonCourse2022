word = 'dlugieslowo'
mid_index = len.word//2
prev_id = mid_index - 1
next_id = mid_index + 1
word[prev_id] + word[mid_index] + word[next_id]
# Albo
word[prev_id:next_id + 1]
