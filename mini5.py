# Project name: Car showroom system ( using file handling )
# Developer Name : Rohit Vijay Jadhav
# Created date : 21 / 09 / 2021
# Updated date : 08 / 09 / 2021

# ----------------------------------------------------------------------------------------------------------------------
print()
print("Car Showroom System")


class Showroom:
    def __init__(self):
        self.type = ''
        self.color = ''
        self.price = 0

    def add_car(self):
        try:
            self.type = input('Enter vehicle type: ')
            self.color = input('Enter vehicle color: ')
            self.price = int(input('Enter vehicle price: '))
            return True
        except ValueError:
            print('Please try entering car details properly')
            return False

    def __str__(self):
        return '\t'.join(str(a) for a in [self.type, '-', self.color, '-', self.price])


class Access:
    def __init__(self):
        self.detail = []
        self.var1 = ''

    def add_car1(self):
        cars = Showroom()

        if cars.add_car() is True:
            self.detail.append(cars)
            for self.var1 in user.detail:
                pass
            print()
            print('\nDetails has been added successfully, Thank you\n')


user = Access()               # created object for Access class

while True:

    print()
    print('Choice 1: Add car detail')
    print('Choice 2: Delete car detail')
    print('Choice 3: Available cars')
    print('Choice 4: Quit')
    User_Choice = input('\nPlease Enter your Choice: ')

    if User_Choice == "1":
        # add the car
        user.add_car1()
        file = open('car_data.txt', 'a+')
        file.write(f'{user.var1}\n')
        file.close()

    elif User_Choice == '2':
        # delete a vehicle
        file = open('car_data.txt', 'r')
        if len(file.read()) < 1:
            print('\nSorry there are no car details')
            file.close()
        else:
            file = open('car_data.txt', 'r')
            print(file.read())
            file.close()
            Products = int(input('\nPlease enter the id of the car: '))
            with open(r"car_data.txt", 'r+') as fp:
                # read an store all lines into list
                lines = fp.readlines()
                # move file pointer to the beginning of a file
                fp.seek(0)
                # truncate the file
                fp.truncate()

                # start writing lines
                # iterate line and line number
                for number, line in enumerate(lines):
                    # note: list index start from 0
                    # fp.write(f'{number+1}\t')
                    if number not in [Products-1]:
                        fp.write(line)

                print()
                print('\nThis car data has been removed')
    elif User_Choice == '3':
        # list all the vehicles
        file = open('car_data.txt', 'r')
        if len(file.read()) < 1:
            print('\nSorry there are no car details')
            file.close()
        else:
            print()
            file = open('car_data.txt', 'r')
            print(file.read())
            file.close()

    elif User_Choice == '4':
        # exit the loop
        print('See you again,Bye!')
        break
    else:
        # invalid user input
        print('Please try again, Type properly!')
