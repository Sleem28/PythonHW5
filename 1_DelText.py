#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
some_text = 'Абв ттдт ттабв оилир оомо д оиоабволило ваб лилоб олдльабв'

print(' '.join(list(filter(lambda word: not word.__contains__('абв'), some_text.split()))))
