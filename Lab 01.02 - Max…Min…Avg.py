"""Lab 01.02 - Max…Min…Avg"""
import json
my_list = json.loads(input())
max_value = my_list[0]
min_value = my_list[0]
for num in my_list:
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num
avg_value = round(sum(my_list) / len(my_list), 2)
result = (max_value, min_value, avg_value)
print(result)
