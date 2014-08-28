'''
Created on Aug 23, 2014

@author: miguel
'''
class Product:

    dailyProfit = 0
    totalProducts = 0
    product_list = []
    product_refill = {}

    def __init__(self, name, price, id, quantity):
        self.price = price
        self.name = name
        self.id = id
        self.quantity = quantity
        Product.product_refill[self.name] = 0
#        print 'Product name: %s, id: %d, price: %.2f euros, quantity: %d was added to stock.' % (self.name, self.id, self.price, self.quantity)
        
    def buyFromStock(self, quantity):
        self.quantity -= quantity
        Product.totalProducts += quantity
        print 'There are %d of that product left.' % self.quantity
    
    def checkQuantity(self):
        return self.quantity
    
    def addStock(self, quantity):
        self.quantity += quantity
        
    def changePrice(self, newPrice):
        self.price = newPrice
        return self.price
    
    def checkPrice(self):
        return self.price
    
    @staticmethod
    def checkStock():
        for product in Product.product_list:
            print '%s: %d units.' % (product.name, product.quantity)
#################################################################################################################
def main():
    
    def findProduct(name):
        for product in Product.product_list:
                    if product.name == name:
                        prod = product
                        break
        return prod
    
    def newDay():
        rice = Product('Rice', 2.99, 12345, 600)
        bread = Product('Bread', 1.99, 54321, 300)
        cocacola = Product('CocaCola', 4.99, 73578, 800)
        Product.product_list.append(bread)
        Product.product_list.append(rice)
        Product.product_list.append(cocacola)
    
    def addProduct(name, price, id, quantity):
        product = Product(name, float(price), int(id), int(quantity))
        Product.product_list.append(product)
    
    def buyProduct(quantity, productName):
        for product in Product.product_list:
            if product.name == productName:
                if product.quantity < quantity:
                    return 'Not enough in stock.'
                else:
                    product.buyFromStock(int(quantity))
                    Product.product_refill[product.name] += int(quantity)
                    Product.dailyProfit += int(quantity) * product.price
                    return 'You successfully bought %d of %s' % (int(quantity), product.name)
        return 'Item not in stock.'

    def checkProducts(*args):
        options = args
        try:
            prod = findProduct(options[1])
            if options[0] == 'quantity':
                print prod.checkQuantity()
                
            elif options[0] == 'price':
                print prod.checkPrice()
        except:
            if options[0] == 'stock':
                Product.checkStock()
            else:
                print 'Wanted item is currently not in stock.'
                
    def closeUp():
        print 'Profit of the day is %.2f euros with a total of %d items sold.' % (Product.dailyProfit, Product.totalProducts)
        print 'Products needed to be restocked:'
        for item in sorted(Product.product_refill):
            print '%s: %d' % (item, Product.product_refill[item])
    
    # Commands:
    # Buy x Product.name
    # Add Product.name Product.price Product.id Product.quantity
    # Check quantity Product.name
    # Check price Product.name
    # Check stock
    # Change price Product.name

#    createWindow()
    newDay()
    while 1:
        print 'Choices Available: "Add", "Buy", "Check", "Change", "Close Shop"'
        choice = raw_input().split()
        
        # Add product to stock
        if choice[0] == 'Add':
            addProduct(choice[1], choice[2], choice[3], choice[4])
        
        # Buy product from stock
        elif choice[0] == 'Buy':
                print buyProduct(int(choice[1]), choice[2])
#                createWindow()

        # Check prices, quantity, stock
        elif choice[0] == 'Check':
            try:
                checkProducts(choice[1], choice[2])
            except:
                checkProducts(choice[1])
            
        # Change price of item in stock
        elif choice[0] == 'Change':
            try:
                prod = findProduct(choice[2])
                print prod.changePrice(float(choice[3]))
            except:
                print 'Wanted item is currently not in stock.'
            
        # Close Shop
        elif choice[0] == 'Close':
            closeUp()
            break
#################################################################################################################        
if __name__ == '__main__':
    main()