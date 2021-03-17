# Task 2
# в файлі task2 збережений список, відкрийте цей файл, прочитайте вміст, і знайдіть середнє арифметичне чисел що знаходяться в списку
import pickle


with open("./task2", "rb") as readfile:
    read_list = pickle.load(readfile)
average = 0
if len(read_list):
    average = sum(read_list) / len(read_list)
print(average)
