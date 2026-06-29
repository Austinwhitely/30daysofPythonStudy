from functools import reduce


countries_list = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland', 'Ethiopia', 'Ireland' ]
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print([country for country in countries_list ])
print([name for name in names ])
print([number for number in numbers ])

def upper_list(list):
    return list.upper()

upper_name_map = map(upper_list, names)

print(list(upper_name_map))

def has_land(country):
    if "land" in country:
        return False
    else:
        return True

new_country_map = filter(has_land, countries_list)
print(list(new_country_map))

def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers)
print(total)

def get_strings_list(list):
    return str(list)

print(get_strings_list(numbers))

def countries_by_letter(countries):
    
    letter_counts = {}

    for country in countries_list:
        first_letter = country[0].upper()

        if first_letter in letter_counts:
            letter_counts[first_letter] += 1
        
        else:
            letter_counts[first_letter] = 1

    return letter_counts
    

print(str(countries_by_letter(countries_list)))