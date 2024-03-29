from functools import reduce 

# Sample data of address book 
# 1. Separating functions and data 
address_book = [
    {
    'name': 'Lim Kah Hoe',
    'age': 20,
    'number': '73',
    'street': 'Jln 3/23A',
    'street2': 'Danau Kota',
    'post': '53300',
    'city': 'Kuala Lumpur',
    'state': 'Selangor'
    }, {
    'name': 'Davina Rao',
    'age': 65,
    'number': '39B',
    'street': 'Jalan Tun Razak',
    'street2': 'Empire Tower 182',
    'post': '50400',
    'city': 'Kuala Lumpur',
    'state': 'Selangor'
    }, {
    'name': 'Chia Xin Yi',
    'age': 45,
    'number': '11A',
    'street': 'Jln 6/23E',
    'street2': 'Danau Kota',
    'post': '53300',
    'city': 'Kuala Lumpur',
    'state': 'Wilayah Persekutuan'
    }, {
    'name': 'Ali Abdul',
    'age': 22,
    'number': '35',
    'street': 'Jln Camar 5',
    'street2': 'Taman Perling',
    'post': '81200',
    'city': 'Johor Bahru',
    'state': 'Johor'
    }, {
    'name': 'Jessica Jones',
    'age': 34,
    'number': '27',
    'street': 'Jalan Tpj 3',
    'street2': 'Taman Perindustrian Jaya',
    'post': '47200',
    'city': 'Petaling Jaya',
    'state': 'Selangor'
    }     
]

def printingInfo():
    print("==========================================================\n")
    print("People Available in This Address Book : \n")
    print("1. Lim Kah Hoe\n2. Davina Rao\n3. Chia Xin Yi\n4. Ali Abdul\n5. Jessica Jones\n")
    print("==========================================================\n")
    print("Choose the type of search you wish to perform : \n")
    print("Basic Search returns all the info of a field search in the address book \n")

def filtered_address(x):
    # 7. Filtering 
    return list(filter(lambda i: i['state'] == x or i['city'] == x or i['name'] == x or i['post'] == x, address_book)) # 9. Lambdas

# 4. Passing function as arguments 
def get_address(func): 
    
    def get_filtered_address(x):
        return func(x)
    
    def get_address_list(y): 
        def list_type(z):
            
            def print_obj(i, obj_list): # 11. Recursion
                maximum = len(obj_list)
                index = i + 1
                if i >= maximum:
                    return
                else:
                    print()
                    print(f"{index}. {obj_list[i]}")
                    print_obj(i + 1, obj_list)
                print()
            
            match z:
                case 1: # Show names only 
                    # List of student names 
                    names = list(map(lambda i: i['name'], func(y))) # 6. Mapping
                    return print_obj(0, names)
                case 2: # Show address only
                    # List of addresses
                    addresses = [([v for k,v in i.items() if k != 'name']) for i in func(y)] # List comprehension 
                    return print_obj(0, addresses)
                case _:
                    return "Invalid input"
        return list_type
    
    return get_filtered_address, get_address_list # 5. Return functions 

address_filter, address_filter_special  = get_address(filtered_address) # 2. Assigning function to a variable & Passing functions as arguments 

function_list = [address_filter, address_filter_special] # 3. Create a list of functions and use that list 

#For Reduce
def get_all_age(address_book):
    return list(map(lambda i:i['age'], address_book))

def get_sum_age(acc,i):
    return acc + i


# TEST PROGRAM
stop = False
printingInfo()
while(not stop):
    print("0 - Basic\n1 - Special\n2 - Get Average Age\n3 - End program")
    function_type = int(input("\nSelect function:"))
    match function_type:
        case 0:
            address_input = input("Search address book:")
            list_address = function_list[function_type](address_input)
        case 1: 
            print("\n1 - Name only\n2 - Address only")
            filter_type = int(input("Select Type:"))
            address_input = input("Search address book:")
            list_address = function_list[function_type](address_input)(filter_type)
        case 2:
            age_Average = get_all_age(address_book)
            avg = reduce(get_sum_age, age_Average) / len(age_Average)
            list_address = avg
        case 3:
            stop = True
            break
    print(f"{list_address}\n")