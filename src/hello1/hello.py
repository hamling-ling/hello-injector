from injector import Injector, inject

class Inner:
    def __init__(self):
        pass

    def print(self):
        print("Inner class")

class Outer:
    @inject
    def __init__(self, inner: Inner):
        self.inner = inner

    def print(self):
        print("Outer class")
        self.inner.print()

def main():
    injector = Injector()
    outer = injector.get(Outer)
    outer.inner.print()
    #outer.print()

main()
