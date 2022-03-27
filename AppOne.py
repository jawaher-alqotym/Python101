#phone guide

Phone_dictionary = {'Amal':'1111111111', 'Mohammed':'2222222222', 'Khadijah':'3333333333',
                    'Abdullah':'4444444444'}

def AddNumber(key, val):

    if(villedNumber(val) and key.isalpha()):
      Phone_dictionary[key] = val
      print(key +'\n'+ Phone_dictionary[key])
      return True
    else:
        return False

def FinedeCallerName(number):
    #take a phone number thean give the oner name
    for i, j in Phone_dictionary.items():
        if(number == j ):
            return i
            break

    return None



def FinedNumber(name):
    #take a name then give the their number
    for i, j in Phone_dictionary.items():
        if(i == name):
            return j
    return None

def villedNumber(val):
    if(val.isdigit() and len(val) == 10):
        return True
    else:
        print('invaled number')
        return False




op = input('Enter 1 to fined a caller name, or 2 to fined their phone number and 0 to add a number:')

if(op == '0' ):

    NewName = input('Enter the name:')
    NewPhoneNumber = input('Enter number: ')
    isTrue = AddNumber(NewName, NewPhoneNumber)
    if(isTrue):
        print('successful')
    else:
        print('inter a coreact name with only alphabitcal letters and a corect phone number')


elif(op == '1'):
    number = input("Enter the phone numbre: ")
    if (villedNumber(number)):
     name = FinedeCallerName(number)
     if(name != None):
      print('The owner of this number is: '+name)
     else:
      print('Sorry, the owner is not found')



elif(op == '2'):
    Name = input('Enter a name: ')
    Number = FinedNumber(Name)
    if(Number != None):
        print('The caller phone is: '+Number)
    else:
     print('Sorry, the number is not found')


else:
    print(op+' is not a vilde input')