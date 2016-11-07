import string
import random


def passwordgen():
   password = ""
   for i in range(0, random.randint(8, 15)):
       for x in range(1, 5):
            if x == 1:
               password += str(return_lowerc())
            elif x == 2:
                password += str(return_upperc())
            elif x == 3:
                password += str(return_number())
            elif x == 4:
                password += str(return_symbol())

   return password


def return_lowerc():
   x = string.ascii_lowercase
   c = x[random.randint(0, 25)]
   return c


def return_upperc():
   x = string.ascii_uppercase
   c = x[random.randint(0, 25)]
   return c


def return_number():
   num = random.randint(0, 9)
   return num


def return_symbol():
   sym = "!@#$%^&*()?"
   s = sym[random.randint(0, 10)]
   return s


def main():
   return


if __name__ == '__main__':
   main()
