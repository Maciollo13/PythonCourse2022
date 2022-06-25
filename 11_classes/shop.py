class Shop:
    def __init__(self, product, size, price, color):
        self.product = product
        self.size = size
        self.price = price
        self.color = color

    def product_show(self):
        print(self.product.title(), self.size , self.color.title() , self.price)

    def product_buy(self, money):
        return "Sold" if money >= self.price else "Its too expensive"

    def product_try_on(self, size):
        return "It fits" if size == self.size else "Its not for you"



def main():
    t_shirt = Shop("tshirt","M",39,"pink")
    print(t_shirt.product_buy(60))
    print(t_shirt.product_buy(20))
    t_shirt.product_show()
    print(t_shirt.product_try_on("M"))

if __name__ == "__main__":
    main()