word = 'Football, Basketball, Skate'
print(len (word))   # Число символов в етой строке
print(word.count('!'))  #сколько символов у переменной ворд
print(word.upper()) # к верхнему регистру
print(word.lower()) #к нижниму регистру
print(word.capitalize()) # первая буква каждого слова к верхнему регистру
print(word.find('a'))  #  поиск определьоних символов mesto indiksa
hobby  = (word.split(', ')) #Разбитие строки по определьонному символу
print(hobby[1])
Year = int(input("Введите то сколько ви етим занимаетесь:"))
if Year >= 1:
    print("Good Job")
elif Year == 0:
    print("Ще все попереду")

