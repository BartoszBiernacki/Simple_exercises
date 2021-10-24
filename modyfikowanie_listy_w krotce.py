lista = ["raz", "dwa", "trzy"]
krotka = ("Kon", "na", "biegunach", lista)

print(krotka)
lista.append("cztery")
print(krotka)
lista[0] = "Poniedzialek"
print(krotka)
lista[1] = ["a", "b"]
print(krotka)
lista[2] = ("A", "B")
print(krotka)

