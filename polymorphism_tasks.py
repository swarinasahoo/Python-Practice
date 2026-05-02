# def display(value):
#     if isinstance(value, int):
#         print(f'Square Root of {value**2}')
    
#     elif isinstance(value, str):
#         print(f'Upppercase : {value.upper()}')
    
#     else:
#         print('Unsupported Type')
                
# display(5)
# display('hello')
# display(True)

# TASK 2


# class bird:
#     def sound(self):
#         print('Chirp')

# class lion:
#     def sound(self):
#         print('Roar')
        
# b = bird()
# l = lion() 

# b.sound()
# l.sound()

# TASK 3 

# List addition 
# list_1 = [1, 2]
# list_2 = [3, 4]

# print(list_1 + list_2)

# # String addition 
# str_1 = 'Hello '
# str_2 = 'World'
# print(str_1 + str_2)

# Task 4 

# def check_type(value):
#     print(f'Type is : {type(value)}')
    
# check_type(10) 
# check_type('Python')
# check_type([1, 2, 3])
# check_type({1 : 1, 
#             2 : 2})
    

# Task 5 
class upi:
    def pay(self):
        print('Processing UPI payment')

class card: 
    def pay(self):
        print('Processing card payment')
        
def make_payment(method):
    method.pay()
    
    
u = upi() 
c = card() 

make_payment(u)
make_payment(c)


























