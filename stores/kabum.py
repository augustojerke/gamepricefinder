from selenium import webdriver
import time

class Kabum:

    def searchProduct(self, searchParam: str, driver: webdriver.Firefox):
        driver.get(url='https://www.kabum.com.br')
        driver.maximize_window()
        driver.find_element("xpath", "//input[@id='input-busca']").send_keys(searchParam)
        driver.find_element("xpath", "//button[@aria-label='Buscar']").click()
        
