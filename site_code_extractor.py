from selenium import webdriver
from WebAddressChanger import WebAddressChanger as wac

options = webdriver.ChromeOptions()
options.add_argument("--headless") #It prevent web browser window from appearing
driver = webdriver.Chrome(executable_path="C:/Users/Maliccy/AppData/Local/Programs/chromedriver.exe", chrome_options = options)
# driver = webdriver.Chrome()

url = input("Podaj adres strony: ")
driver.get(url)
fixed_url = wac(url).address_generator()

site_source = driver.page_source
save_file_path = "D:/Użytkownicy/Maliccy/Dokumenty/Mateusz/PROGRAMOWANIE/Python/Projekty/WebCodeEXTR/Sites_codes/site_source_of_" + str(fixed_url) + ".txt"
print(save_file_path)

with open(save_file_path, "w", encoding="utf-8") as ss_file:
    ss_file.write(str(site_source))

