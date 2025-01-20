from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from fpdf import FPDF



# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# go to exmaple page
driver.get("https://manuxxrsb-portafolio.web.app/")

print(driver.title)

#Mostramos el titulo de la pagina web

#time.sleep(2)

button = driver.find_element(by=By.LINK_TEXT, value="Proyectos")

# text_box.send_keys("Selenium") # Send keys to search box

button.click()

time.sleep(1)

class Caja_Unica:
    def __init__(self):
        self.titulo = driver.find_element(by=By.CSS_SELECTOR, value="h3").text
        self.descripcion = driver.find_element(by=By.CSS_SELECTOR, value="p").text

    def mostrar_informacion(self):
        print("Titulo: ", self.titulo)
        print("Descripcion: ", self.descripcion)
        print("")

Primera_Caja = Caja_Unica()

print(button.text)

Primera_Caja.mostrar_informacion()
time.sleep(5)

driver.quit()

pdf = open("Example.pdf", "w")
pdf.write("Titulo: " + "Primera_Caja.titulo" + "\n")
pdf.write("Descripcion: " + "Primera_Caja.descripcion" + "\n")

pdf.close()

print("PDF creado con exito")
