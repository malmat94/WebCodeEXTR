from WebAddressChanger import WebAddressChanger as wac

address = input("Podaj adres: ")

file_name = wac(address)
fixed_address = file_name.address_generator()

print(fixed_address)