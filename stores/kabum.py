from product import Product
import requests

class Kabum:

    def searchProduct(self, searchParam: str):
        print("KABUM:")
        response = requests.get(f"https://servicespub.prod.api.aws.grupokabum.com.br/catalog/v2/products?query={searchParam}&context=search")
        json = response.json()
        print(json["data"][0]["attributes"]["title"])
        
        
