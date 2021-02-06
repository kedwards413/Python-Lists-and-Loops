
my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]


#your code go here:
hello = []
for value in my_list:
    if type(value) is list or type(value) is dict:
        hello.append(value)

print(hello)
