class A:
    def __init__(self):
        self.a = 123
    def retorna_valor_a(self):
        return self.a

class B:
    def __init__(self):
        self.b = 234
    def retorna_valor_b(self):
        ba = A()
        ba.a = 555
        rba = ba.retorna_valor_a()
        print("---" + str(rba))

        return self.b

AA = A()
xa = AA.retorna_valor_a()
print(xa)
AA.a = 333
print("AA.a" + str(AA.a))

BB = B()
xb = BB.retorna_valor_b()
print(xb)