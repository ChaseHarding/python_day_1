def hello():
    
    print("Hello from inside the file!")
hello()


def pack(arg1, arg2, arg3):
    return [arg1, arg2, arg3]

result = pack(1, "hello", [6, 7, 8])
print(result)

def eat_lunch(food_list):
    if not food_list:
        print("My lunchbox is empty!")
    else: print("First I eat", food_list[0])
    for food in food_list[1:]:
        print("Next I eat", food)

eat_lunch(['sandwhich', 'fruit', 'stringcheese'])
    