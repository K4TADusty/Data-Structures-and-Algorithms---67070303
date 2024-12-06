"""Lab 01.02 - Max…Min…Avg"""
import json
my_list = json.loads(input())
highest_value = my_list[0]
least_value = my_list[0]
for num in my_list:
    if num > highest_value:
        highest_value = num
    if num < least_value:
        least_value = num
avg_value = round(sum(my_list) / len(my_list), 2)
result = (highest_value, least_value, avg_value)
print(result)
