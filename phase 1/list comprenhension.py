

double = [x * 2 for x in range(1, 11)]
triples = [x * 3 for x in range(1, 11)]
squares = [x * x for x in range(1, 11)]


#fruits = ["apple", "banana", "cherry", "orange", "kiwi"]
#upper_fruits = [fruit.upper() for fruit in fruits]
#fruits_chart= [fruit[0]for fruit in fruits]

#print(fruits_chart)

numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
positives_numb = [number for number in numbers if number >= 0]
negative_numb =  [number for number in numbers if number < 0]
even_numb =  [number for number in numbers if number % 2 == 0]
odds_numb =  [number for number in numbers if number % 2 == 1]



grades = [80, 90, 75, 100, 85, 92, 88, 78, 94, 83]
passing_grades = [grade for grade in grades if grade >= 70]
print(passing_grades)

