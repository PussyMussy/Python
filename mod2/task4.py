def get_hex_dict():
    return { 
        10:'a', 
        11:'b', 
        12:'c', 
        13:'d', 
        14:'e', 
        15:'f' 
    } 

def get_dif_system_for_dec(dec_number, basis):
    if basis > 16:
        raise ValueError("Базис > 16 не допускается")
    result = ''
    hex_dictionary = dict() if basis < 10 else get_hex_dict()
    while dec_number != 0:
        remains = dec_number % basis
        result = f"{remains if remains < 10 or basis < 10 else hex_dictionary[remains]}{result}";
        dec_number = int(dec_number / basis);
    return result

def main():
    number = int(input())
    if number <= 0:
        print("Неверный ввод!")
        exit()
    try:
        binary = get_dif_system_for_dec(number, 2);
        octal = get_dif_system_for_dec(number, 8);
        hexadecimal = get_dif_system_for_dec(number, 16);
        print(f"{binary}, {octal}, {hexadecimal}");
    except ValueError as e:
        print(e)

main()