class persegi:
    def sisi(self):
        pass

class segitiga(persegi):
    def luas(self):
        pass

_persegi = persegi()
_segitiga = segitiga()

print(type(_segitiga)==segitiga)
print(type(_segitiga)==persegi)
print(isinstance(_persegi,persegi))
print(isinstance(_segitiga,segitiga))