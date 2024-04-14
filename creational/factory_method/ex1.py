import abc

class IShipping(abc.ABC):
  @abc.abstractmethod
  def calc_the_cost(self, weight, distance): ...

class CStandardShipping(IShipping):
  def calc_the_cost(self, weight, distance):
    return weight * 2 + distance * 2

class CExpressShipping(IShipping):
  def calc_the_cost(self, weight, distance):
    return weight * 4 + distance * 4


class IShippingFactory(abc.ABC):
  def create_shipping(self): ...

class CStandardShippingFactory(IShippingFactory):
  def create_shipping(self):
    return CStandardShipping()
class CExpressShippingFactory(IShippingFactory):
  def create_shipping(self):
    return CExpressShipping()

class ShopCart:
    def __init__(self):
        self._products = []
        self.factory_method: IShippingFactory = None  #shipping method!

    def add_product(self, product):
        self._products.append(product)

    def set_factory_method(self, factory):
        self.factory_method = factory

    def get_products(self):
        return self._products

    def checkout(self):
        if not self.factory_method:
            raise ValueError("shipping method must be set!")
        total_weight = sum([p["weight"] for p in self._products])
        total_distance = sum([p["distance"] for p in self._products])
        method = self.factory_method.create_shipping()

        return f"shipping cost: ${method.calc_the_cost(total_weight, total_distance)}"

my_cart = ShopCart()        
my_cart.add_product({"name": "apple mac m3 max", "weight": 1.5, "distance": 600})
my_cart.add_product({"name": "iphone 14 pro max", "weight": 0.200, "distance": 600})

my_cart.set_factory_method(CStandardShippingFactory())
# my_cart.set_factory_method(CExpressShippingFactory())

print(my_cart.checkout())
