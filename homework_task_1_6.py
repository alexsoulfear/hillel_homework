import math
a_1 = 2
b_1 = 4
c_1 = 8
result_1 = round(a_1 + b_1 * (c_1 / 2))
print ("Результат задания номер 1 (a + b * (c / 2)), при взятых произвольно значениях: a = %d , b = %d , c = %d равен %d"
       %(a_1, b_1, c_1, result_1))




a_2 = 5
b_2 = 7
result_2 = round((a_2**2) + (b_2**2) / 2)
print("Результат задания номер 2 ((a^2 + b^2) / 2), при взятых произвольно значениях: a = %d , b = %d равен %d"
      %(a_2, b_2, result_2))


a_3 = 7
b_3 = 9
c_3 = 6
result_3 = round((a_3 + b_3) / 12 * c_3 % (4+ b_3))
print("Результат задания номер 3 ((a + b) / 12 * c / 4 + b), при взятых произвольно значениях: a = %d, b = %d, c = %d примерно равен %d"
      %(a_3, b_3, c_3, result_3))



a_4 = 7
b_4 = 3
c_4 = 2
result_4 = round((a_4 - b_4 * c_4) / (a_4 + b_4) // c_4)
print("Результат задания номер 4 ((a - b * c) / (a + b) // c), при взятых произвольно значениях: a = %d, b = %d, c = %d примерно равен %d"
      %(a_4, b_4, c_4, result_4))


a_5 = 1
b_5 = 6
c_5 = 9
result_5 = round(abs(a_5 - b_5) / ((a_5 + b_5)**3) - (math.cos(c_5)))
print("Результат задания номер 5 (|a - b| / (a + b)^3 - cos(c)), при взятых произвольно значениях: a = %d, b = %d, c = %d примерно равен %d"
      %(a_5, b_5, c_5, result_5))


a_6 = 7
b_6 = 8
c_6 = 1
result_6 = round(((math.log1p (1 + c_6) / -(b_6))**4) + abs(a_6))
print("Результат задания номер 6 ((ln(1 + c) / -b)^4 + |a|), при взятых произвольно значениях: a = %d, b = %d, c = %d примерно равен %d"
      %(a_6,  b_6, c_6, result_6))
