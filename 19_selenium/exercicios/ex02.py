from selenium.webdriver import Firefox
from time import sleep

url = "https://curso-python-selenium.netlify.app/exercicio_02.html"

browser = Firefox()
browser.get(url)
sleep(1)

body_regras = browser.find_elements_by_tag_name("p")
text_nr_exp = body_regras[-1].text
split_text_nr_exp = text_nr_exp.split()

while True:
    browser.find_element_by_id("ancora").click()
    body_regras = browser.find_elements_by_tag_name("p")
    text_nr = body_regras[-1].text
    split_text_nr = text_nr.split()
    print(f"o número experado é {split_text_nr_exp[-1]} e o número clicado é {split_text_nr[-1]}")
    if split_text_nr_exp[-1] == split_text_nr[-1]:
        print(text_nr)
        break
