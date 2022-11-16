"""
1- 
2- 
3- 
4- 
5- 
6- 
7- 
8- Reducing
9- 
10- 
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
    
    def get_address_list(y): # Not sure if this applicable 
        def list_type(z):
            match z:
                case 1: # Show names only 
                    return list(map(lambda i: i['name'], func(y))) # 6. Mapping
                case 2: # Show address only
                    return [([v for k,v in i.items() if k != 'name']) for i in func(y)] # List comprehension 
                case _:
                    return "Invalid input"
        return list_type
    
    return get_filtered_address, get_address_list # 5. Return functions 

address_filter, address_filter_special  = get_address(filtered_address) # 2. Assigning function to a variable 

function_list = [address_filter, address_filter_special] # 3. Create a list of functions and use that list 


# TEST PROGRAM
stop = False
while(not stop):
    print("0 - Basic\n1 - Special\n2 - End program")
    function_type = int(input("Select function:"))
    match function_type:
        case 0:
            address_input = input("Search address book:")
            list_address = function_list[function_type](address_input)
        case 1: 
            print("\n0 - Full Detail\n1 - Name only\n2 - Address only")
            filter_type = int(input("Select Type:"))
            address_input = input("Search address book:")
            list_address = function_list[function_type](address_input)(filter_type)
        case 2:
            stop = True
            break
    print(list_address)