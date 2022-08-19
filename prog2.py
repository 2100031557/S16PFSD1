class Base:
    def display(self):
        print("hello")
class Derived(Base):
    def display(self):
        print("good evening")
ob=Derived()
ob.display()