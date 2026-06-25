from random import *
import string

characters: str = string.ascii_letters + string.digits
empty_array: list = {}



def random_user_id():

    len: int = int(input('enter user id length: '))
    num: int = int(input('enter number of user ids: '))
 
    for number in range(num): 
          print(''.join(choice(characters) for _ in range(len)))
    

def rgb_color_gen():
    color: int = randint(0, 255)
    color1: int = randint(0, 255)
    color2: int = randint(0, 255)
    rgb: tuple = (color, color1, color2)
    print(rgb + "/n")

def generate_colors(type: str, num: int):
    
    if type.lower() == 'rgb':
        for number in range(num): 
           
             rgb: list = [randint(0,255) for i in range(3)]
             print("rgb({}, {}, {}) " .format(*rgb))

    elif type.lower() == 'hex':
        for number in range(num): 
           
             hex: list = [''.join(choice(characters) for i in range (6))]
             print("#{} " .format(*hex))        
             
             
def shuffle_list(array: list):
       array: list = [randint(0,9) for i in range(7)]
       return array

def main():
     type: str = input('enter color type: ')
     num: int = int(input('enter number of colors: '))

     generate_colors(type, num)
     rgb_color_gen()
     random_user_id()
     print(shuffle_list(empty_array))
     