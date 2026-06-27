import string
#Filter only negative and zero in the list using list comprehension
numbers: list[int] = [-4, -3, -2, -1, 0, 2, 4, 6]

neg_list: list[int] = [number for number in numbers if number <=0 ]
print(neg_list)

#Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat_list: list[int] = [number for row in list_of_lists for number in row]
print(flat_list)

#Using list comprehension create the following list of tuples:
square_tup = [( i , *(i**j for j in range (0,6))) for i in range (11)]
print (square_tup)

#Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

country_city = [(country.upper(),country[:3].upper(), city.upper()) for row in countries for country, city in row]
print (country_city)

#Change the following list to a list of dictionaries:
country_for_city = [{'Country': country, 'City': city} for row in countries for country, city in row]
print(country_for_city)

#Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concat_names = [' '.join(name) for row in names for name in row]
print (concat_names)

#Write a lambda function which can solve a slope or y-intercept of linear functions.
y_int = lambda x1,y1,x2,y2: (y2-y1)/(x2-x1)

x1 = int(input("enter x1 coordinate "))
y1 = int(input("enter y1 coordinate "))
x2 = int(input("enter x2 coordinate "))
y2 = int(input("enter y2 coordinate "))

print(y_int(x1,y1,x2,y2))
