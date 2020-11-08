# user.py

from library import Base

#how do you make sure self.bar exists?

#2. alternativ assert hasattr(Base, 'bar')
def __buid_class__(*args, **kwargs):
    print('')
class Derived(Base):
    def baz(self):
        return 'baz' + self.bar()



#1. alternativ
    def __init__(self):
        if not hasattr(self, 'bar'):
            raise TypeError()

#3. alternativ unittest (one better alternativ)
