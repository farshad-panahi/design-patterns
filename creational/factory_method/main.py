from __future__ import annotations
import abc

# first we need to define our service Interface
class ICreator(abc.ABC):
  @abc.abstractmethod
  def factory_method(self,): pass
  def some_operation(self):
      product =self.factory_method()
      return product.operation()

# then we define each service that we want to be created at the end
# needs to inherit from service interface
class CCreator1(ICreator):
    def factory_method(self) -> IProduct:
      return CProduct1()

class CCreator2(ICreator):
    def factory_method(self) -> IProduct:
      return CProduct2()
    
# product interface
class IProduct(abc.ABC):
   @abc.abstractmethod
   def operation(self): pass

# products
class CProduct1(IProduct):
  def operation(self,):
    return 'operation product 1'

class CProduct2(IProduct):
  def operation(self,):
    return 'operation product 2'

# at the end client only choose their Factory, no matter what we code in between!
def client(creator: ICreator):
   return creator.some_operation()


print(client(CCreator2 ()))