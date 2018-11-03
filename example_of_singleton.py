""""# Singleton pattern
# making a Singleton with the nested class
class OnlyOne:
    class __OnlyOne:
        def __init__(self,arg):
            self.val = arg

    instance = None
    def __init__(self,arg):
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne(arg)
        else:
            OnlyOne.instance.val = arg

    def __str__(self):
        return repr(self) + self.val
    def __getattr__(self, arg):
        return getattr(self.instance, arg)

x = OnlyOne('Jon')
print(x)
y = OnlyOne('Iggrit')
print(y)
print(x)"""


# The main objective of sigleton is to have a single state of
# data, so you can create as many objects as you want, but
# they all shall refer to the same state information
# Accomplished by a Borg singleton

"""class Borg:
    _shared_state = {}
    def __init__(self):
        self.__dict__ = self._shared_state

class BorgSingleton(Borg):
    def __init__(self,arg):
        Borg.__init__(self)
        self.val = arg
    def __str__(self):
        return self.val

x = BorgSingleton('Jaime')
print(x)
y = BorgSingleton('Brienna')
print(y)
print(x)"""

# Another way to make a Singleton is to wrap a class, as in the
# decorator case, as it takes a class of interest (thus any)
# and adds functionality to it by wrapping it in another class

class SingletonDecorator:
    def __init__(self, _class):
        self._class = _class
        self.instance = None
    def __call__(self, *args, **kwds):
        if self.instance == self._class(*args, **kwds):
