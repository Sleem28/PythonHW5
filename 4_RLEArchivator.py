# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#
# Входные и выходные данные хранятся в отдельных текстовых файлах.
import os


#-------------------------------------------------Читаем---------------------------------------------------------------+
def reader(path: str) -> str:
    with open(path, 'r') as read:
        data = read.readline()
        return data


#-------------------------------------------------Пишем----------------------------------------------------------------+
def writer(path: str, text: str):
    with open(path, 'w') as write:
        data = write.write(text)


#------------------------------------------------Архивируем------------------------------------------------------------+
def archive(text: str) -> str:
    counter = -1
    symbol  = ''
    out_str = ''
    for item in text:
        if item != symbol:
            if counter == -1: # старт расчета
                symbol = item
                counter = 1
            else:
                out_str += str(counter) + symbol
                symbol = item
                counter = 1
        else:
            counter += 1
    out_str += str(counter) + symbol
    return out_str


#----------------------------------------------Разархивируем-----------------------------------------------------------+
def dearch(arch_text: str) -> str:
    out_text = ''
    for i in range(0, len(arch_text), 2):
        result = arch_text[i+1] * int(arch_text[i])
        out_text += result
    return out_text

#-----------------------------------------------Main()-----------------------------------------------------------------+
input_path = os.path.join('MyLibrary', 'InputText.txt')
arch_path  = os.path.join('MyLibrary', 'Archive.txt')
res_path   = os.path.join('MyLibrary', 'RestoreText.txt')

data_to_archive = reader(path=input_path)
print(f'Это инфа из файла. {data_to_archive}')
arch = archive(text=data_to_archive)
print(f'Это заархивированная инфа. {arch}')
writer(path=arch_path, text=arch)
de_arch = dearch(arch_text=arch)
print(f'Это разархивированная инфа. {de_arch}')
writer(path=res_path, text=de_arch)

