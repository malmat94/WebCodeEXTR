from selenium import webdriver
from address_fixer import AddressFixer

options = webdriver.ChromeOptions()
options.add_argument("--headless") #It prevent web browser window from appearing
driver = webdriver.Chrome(executable_path="C:/Users/Maliccy/AppData/Local/Programs/chromedriver.exe", chrome_options = options)

url = input("Podaj adres strony: ")
driver.get(url)
fixed_url = AddressFixer(url).address_converter()

site_source = driver.page_source
save_file_path = "D:/Użytkownicy/Maliccy/Dokumenty/Mateusz/PROGRAMOWANIE/Python/Projekty/BrowserAutomat/Sites codes/site_source_of_" + str(fixed_url) + ".txt"
print(save_file_path)

with open(save_file_path, "w", encoding="utf-8") as ss_file:
    ss_file.write(str(site_source))

