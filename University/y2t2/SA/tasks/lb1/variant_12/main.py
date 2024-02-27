"""
- Розробити програму яка виділяє всі слова, що зустрічаються у файлі, обчисює кількість входжень кожного слова. Регістр при цьому не враховувати. Відсортувати перелік слів з файлу в алфавітному порядку та вивести даний перелік на екран із зазначенням кількості входження кожного слова
"""

# read all words in a file
# count each word
# sort words
# print words with given frequency

arr = "heading wash tank region transportation vote spider drove keep mistake smaller made eye magnet slowly enjoy substance body purpose catch loss elephant western effect"
arr = [word for word in arr.split()]
for word in arr:
    print(f"{word}: {arr.count(word)}")
