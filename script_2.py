def combined_dict(dict1, dict2):
    combineddict = {}
    for key in dict1.keys():
        if key in dict2:
            combineddict[key] = dict1[key] + dict2[key]
    return combineddict

my_dict_1  = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2  = {'b': 4, 'c': 9, 'd': 10, 'e': 1}
print(combined_dict(my_dict_1, my_dict_2))