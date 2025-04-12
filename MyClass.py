class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self._storage = storage  
        self.__battery_level = 100  
    def charge(self, amount):
        self.__battery_level = min(100, self.__battery_level + amount)
        print(f"{self.model} charged to {self.__battery_level}%.")
    def use(self, amount):
        if amount > self.__battery_level:
            print(f"{self.model} has insufficient battery.")
        else:
            self.__battery_level -= amount
            print(f"{self.model} used {amount}%, remaining battery: {self.__battery_level}%.")
    def get_battery_level(self):
        return self.__battery_level

class CameraPhone(Smartphone):
    def __init__(self, brand, model, storage, camera_megapixels):
        super().__init__(brand, model, storage)
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        if self.get_battery_level() < 5:
            print(f"{self.model} has insufficient battery to take a photo.")
        else:
            self.use(5)
            print(f"{self.model} took a photo with {self.camera_megapixels}MP camera.")
