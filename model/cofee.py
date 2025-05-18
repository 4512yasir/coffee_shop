class Coffee:
    def __init__(self,name):
        self.__name = name
        self.orders = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,coffeename):
        if isinstance (coffeename, str)and len(coffeename) >= 3:
            self.__name = coffeename
        else:
            raise ValueError("Coffee name must be a string and has more than 3 characters")


    def orders(self):
         return self.orders

    def customers(self):
        unique_customer = []
        for order in self.orders:
            customer = order.customer

            if customer not in unique_customer:
                unique_customer.append(customer)

        return unique_customer
            
