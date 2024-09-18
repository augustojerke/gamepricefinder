class Product:
     title = ""
     urlImage = ""
     oldPrice = ""
     newPrice = ""

     def printProducts(self):
          for attr, value in self.__dict__.items():
            print(f"{attr}: {value}")