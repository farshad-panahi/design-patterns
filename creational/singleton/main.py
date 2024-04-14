class SingletonMeta(type):
  _instances = {}

  def __call__(cls, *args, **kwargs):
    if cls not in cls._instances:
      cls._instances[cls] = super().__call__(*args, **kwargs)
    return cls._instances[cls]
  
  

class Config(metaclass=SingletonMeta): pass

s1 = Config()
s2 = Config()

print(id(s1) == id(s2))