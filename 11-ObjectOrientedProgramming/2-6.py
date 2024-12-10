class Phone():
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.charging = False
        self.gaming = False
        self.calling = False

    def charge(self):
        self.charging = True

    def discharge(self):
        self.charging = False

    def play_game(self):
        self.gaming = True

    def close_game(self):
        self.gaming = False

    def call(self):
        self.calling = True

    def hang_up(self):
        self.calling = False

    def showproperties(self):
        print(f'Brand: {self.brand}, model: {self.model}, price: {self.price} EUR, is calling: {self.calling}, is charging: {self.charging}, is gaming: {self.gaming}')

def main():
    phone = Phone("Apple", "Iphone 16 PRO MAX", 1600)
    phone.charge()
    phone.call()
    phone.showproperties()

if __name__ == "__main__":
    main()