from WebAddressChanger import WebAddressChanger as wac

address = input("Podaj adres: ")

file_name = wac(address)
file_name.address_generator()
print(file_name)