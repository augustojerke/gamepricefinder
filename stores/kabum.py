from selenium import webdriver
from product import Product
import time

class Kabum:

    def searchProduct(self, searchParam: str, driver: webdriver.Firefox):
        print("KABUM:")
        driver.get(url='https://www.kabum.com.br')
        driver.maximize_window()
        driver.find_element("xpath", "//input[@id='input-busca']").send_keys(searchParam)
        driver.find_element("xpath", "//button[@aria-label='Buscar']").click()
        time.sleep(2)
        articles = driver.find_elements("css selector", "article.sc-14d01a9f-7.drCLho.productCard")[:3]
        self.__getProductInfos(driver, articles[0])
        self.__getProductInfos(driver, articles[1])
        self.__getProductInfos(driver, articles[2])
    
    def __getProductInfos(self, driver: webdriver.Firefox, articleProduct):
        p = Product()        
        product = articleProduct.find_element("tag name", "a")
        p.title = product.find_element("tag name", "img").get_attribute("title")
        p.urlImage = "https://kabum.com.br" + product.find_element("tag name", "img").get_attribute("src") 
        p.oldPrice = product.find_element("tag name", "div").find_elements("tag name", "div")[1].find_elements("tag name", "span")[0].text
        p.newPrice = product.find_element("tag name", "div").find_elements("tag name", "div")[1].find_elements("tag name", "span")[1].text
        p.printProducts()
        print("-------------")       
        
