# path = "C:\Users\Girfet\Desktop\new_file.txt"
path1 = "C:/Users/Girfet/Desktop/new_file.txt"
print(path1)
path2 = "C:\\Users\\Girfet\\Desktop\\new_file.txt"
print(path2)
path3 = r"C:\Users\Girfet\Desktop\new_file.txt"
print(path3)

file = open('C:\Users\Girfet\Documents\python_project\работа_с_файлами\text.txt', 'r', encoding='UTF-8')

print(file.read())