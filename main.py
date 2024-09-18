from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import FirefoxOptions
from stores.kabum import Kabum
from stores.amazon import Amazon
import time
import json

opt = FirefoxOptions()
# opt.add_argument("--headless")
opt.binary_location = '/geckodriver-v0.35.0-win32/geckodriver'

searchParam = "Playstation 5"

class GamePriceFinder:

    def __init__(self):
        self.driver = webdriver.Firefox(options=opt)
    
    def searchKabum(self):
        kabum = Kabum()
        kabum.searchProduct(searchParam, self.driver)
    
    def searchAmazon(self):
        amazon = Amazon()
        amazon.searchProduct(searchParam, self.driver)

if __name__ == '__main__':
    gamePriceFinder = GamePriceFinder()
    gamePriceFinder.searchKabum()
    gamePriceFinder.searchAmazon()