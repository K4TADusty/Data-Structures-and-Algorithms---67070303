"""Lab 01.02 - Max…Min…Avg"""
import json
my_list = json.loads(input())
max_value = max(my_list)
min_value = min(my_list)
avg_value = round(sum(my_list)/len(my_list),2)
result = (max_value,min_value,avg_value)
print(result)