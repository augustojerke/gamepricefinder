from selenium import webdriver
from product import Product
import time

class Amazon:
      
     def searchProduct(self, searchParam: str, driver: webdriver.Firefox):
          print("AMAZON:")
          driver.get(url='https://www.amazon.com.br/?&tag=hydrbrabk-20&ref=pd_sl_7rwd1q78df_e&adgrpid=155790195778&hvpone=&hvptwo=&hvadid=677606588104&hvpos=&hvnetw=g&hvrand=4276392996863892716&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1001690&hvtargid=kwd-10573980&hydadcr=26346_11691057&gad_source=1')
          driver.find_element("xpath", "//input[@name='field-keywords']").send_keys(searchParam)
          try: driver.find_element("xpath", "//input[@id='nav-search-submit-button']").click()               
          except: driver.find_element("xpath", "//input[@value='Ir']").click()               
          time.sleep(1)
          for i in range(1, 4): self.__getProductInfos(driver, i)
               
     def __getProductInfos(self, driver: webdriver.Firefox, i):
          p = Product()
          p.urlImage = driver.find_element("xpath", f"//img[@data-image-index='{i}']").get_attribute("src")
          p.title = driver.find_elements("xpath", "//span[@class='a-size-base-plus a-color-base a-text-normal']")[i-1].text
          p.newPrice = driver.find_elements("xpath", "//span[@class='a-price-whole']")[i-1].text
          p.oldPrice = ""
          p.printProducts()
          print("----------")         