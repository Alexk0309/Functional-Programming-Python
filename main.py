"""
1- 
2- 
3- Create a list of functions and use that list
4- 
5- 
6- 
7- 
8- Reducing
9- 
10- List Comprehensions
11- Recursion

"""

from functools import reduce 

# Sample data of address book 
# 1. Separaring functions and data 
address_book = [
    {
    'name': 'Anita Dick',
    'number': '73',
    'street': 'Jln 3/23A',
    'street2': 'Danau Kota',
    'post': '53300',
    'city': 'Kuala Lumpur',
    'state': 'Wilayah Persekutuan'
    }, {
    'name': 'Ligma Johnson',
    'number': '39B',
    'street': 'Jalan Tun Razak',
    'street2': 'Empire Tower 182',
    'post': '50400',
    'city': 'Kuala Lumpur',
    'state': 'Wilayah Persekutuan'
    }, {
    'name': 'Bendoverson',
    'number': '11A',
    'street': 'Jln 6/23E',
    'street2': 'Danau Kota',
    'post': '53300',
    'city': 'Kuala Lumpur',
    'state': 'Wilayah Persekutuan'
    }, {
    'name': 'Harry Cox',
    'number': '35',
    'street': 'Jln Camar 5',
    'street2': 'Taman Perling',
    'post': '81200',
    'city': 'Johor Bahru',
    'state': 'Johor'
    }, {
    'name': 'Martha Fokker',
    'number': '27',
    'street': 'Jalan Tpj 3',
    'street2': 'Taman Perindustrian Jaya',
    'post': '47200',
    'city': 'Petaling Jaya',
    'state': 'Selangor'
    }     
]


def filtered_address(x):
    # 7. Filtering 
    return list(filter(lambda i: i['state'] == x or i['city'] == x or i['name'] == x or i['post'] == x, address_book)) # 9. Lambdas

# 4. Passing function as arguments 
def get_address(func): 
    
    def get_filtered_address(x):
        return func(x)
    
    def view_list(y):
        # def list_type(z):
        #     match z:
        #         case "name":
                    
        get_list = list(map(lambda i: i['name'], func(y))) # 6. Mapping
        return get_list
    
    return get_filtered_address, view_list # 5. Return functions 

address_filter, address_names  = get_address(filtered_address) # 2. Assigning function to a variable 

# def add_address(book, x):
#     book.append(x)
#     print('Address added')

# add = reduce(add_address, address_book)


# Test program
stop = False
while(not stop):
    address_input = input("Type something:")
    if (address_input == '0'):
        stop = True 
    else:
        list_address = address_filter(address_input)
        print(list_address)