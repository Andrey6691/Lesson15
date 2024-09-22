def print_params(a = 1, b = 'kolbasa', c = True):
    print(a, b, c)

value_list = ['banan', 10, [20, 30, 40]]
value_dict = {'a':[100, 200, 300], 'b':'robot', 'c':400}
value_list_2 = ['korova', 90]
# value_list = [10, 20]
# value_list_2 = {'a' : 10, 'b' : 20, 'c' : 30}
# value_list_dict = {'b' : 100, 'c' : 200}
# value_list_2 = ('makaron', 4, [7, 8, 9])
print_params()
print_params(b = 25, c = [1, 2, 3])
print_params(*value_list)
print_params(**value_dict)
print_params(*value_list_2, 42)
# print_params(*value_list, 500)
#print_params(*value_list, **value_dict)
# print_params(value_list_2)
