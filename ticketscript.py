class ticket:
    def _int_(self, name, base_price) :
        self._name = name
        self.base_price = base_price
    def get_name (self) :
        return self._name
    
    def price (self) :
        return self.base_price


concert = Ticket("Concert", 200)
museum = Ticket("Museum", 150)
print(concert.get_name(), concert.price())
print (museum.get_name(), museum.price())
    
    
