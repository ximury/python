# from datetime import time
import time

my_dict = {1: "a", 2: "b"}
print(my_dict.items())
print(dict.items(my_dict))
for key, value in dict.items(my_dict):
    print(key, value)
    time.sleep(2)
