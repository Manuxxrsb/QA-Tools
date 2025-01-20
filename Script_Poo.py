from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from fpdf import FPDF

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()
driver.get("https://manuxxrsb-portafolio.web.app/")

button = driver.find_element(by=By.LINK_TEXT, value="Proyectos")
button.click() 

time.sleep(1)

class Caja_Objetos:
    def __init__(self):
        self.titulo = driver.find_elements(by=By.CSS_SELECTOR, value="h3")
        self.descripcion = driver.find_elements(by=By.CSS_SELECTOR, value="p")

    def mostrar_informacion(self):
        for i in range(len(self.titulo)):
            print("Titulo: ", self.titulo[i].text)
            print("Descripcion: ", self.descripcion[i].text)
            print("\n")

    def crear_pdf(self):
        pdf = open("Listado_cajas.pdf", "w")
        for i in range(len(self.titulo)):
            pdf.write("----------------------------------\n")
            pdf.write("\t1)Titulo: " + self.titulo[i].text,)

            pdf.write("Descripcion: " + self.descripcion[i].text,)
            pdf.write("----------------------------------\n")
        pdf.close()

Cajas = Caja_Objetos()
Cajas.crear_pdf()
