from selenium.webdriver import Firefox
from time import sleep

# url = "https://curso-python-selenium.netlify.app/exercicio_01.html"
url = "file:///C:/Users/alexa/Documents/BitsBytes/tutorial/19_selenium/exercicios/Exerc%C3%ADcio%2001.htm"

browser = Firefox()
browser.get(url)
sleep(1)

textos = browser.find_elements_by_tag_name('p')
attritute = {element.get_attribute('atributo'):element.text for element in textos}

result = {browser.find_element_by_tag_name('h1').text : attritute}
