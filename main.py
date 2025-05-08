from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

time.sleep(2)
nombre = driver.find_element(By.ID,"firstName")
nombre.send_keys("Daniel")

time.sleep(2)
apellido = driver.find_element(By.ID,"lastName")
apellido.send_keys("Pacheco")
    
time.sleep(2)
email = driver.find_element(By.ID,"userEmail")
email.send_keys("danielpacosta93@gmail.com")

time.sleep(2)
movil = driver.find_element(By.ID,"userNumber")
movil.send_keys("3105816209")

time.sleep(2)
temas = driver.find_element(By.ID,"subjectsInput")
temas.send_keys("automatizaciones con selenium")

time.sleep(2)
direccion = driver.find_element(By.ID,"currentAddress")
direccion.send_keys("calle 161 #16d-10")

entregar = driver.find_element(By.ID, "submit")
entregar.click()


time.sleep(5)
driver.quit()

