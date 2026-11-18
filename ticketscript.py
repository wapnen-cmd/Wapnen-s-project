class ticket:
    def _int_(self, name, base_price) :
        self._name = name
        self.base_price = base_price
    def get_name (self) :
        return self._name
    
    def price (self) :
        return self.base_price


class StudentTicket (Ticket):
    def price (self):
        return super ().price()*0.5
class GroupTicket (Ticket):
    def _init_(self, name, base_price, people):
        super ()._init_(name, base_price)
        self._people = people
    
    
