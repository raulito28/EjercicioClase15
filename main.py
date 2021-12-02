import persistencia_pickle as pp
import car_class
import random as rd

COCHES = "Coches_obj.txt"
lista_coches = pp.retrieve(COCHES)
if lista_coches == None:
    lista_coches = []
while True:
    marca = input("Marca: ")
    if marca == "fin":
        break
    modelo = input("Modelo: ")
    combustible = input("Combustible: ")
    cilindrada = input("Cilindrada: ")
    ancho = input("Ancho rueda(mm): ")
    rodadura = input("Ancho de rodadura(%): ")
    diametro = input("Diametro llanta(pulgadas): ")

    wheel = car_class.Wheel(ancho, rodadura, diametro)
    coche = car_class.Car(marca, modelo, combustible, cilindrada, wheel)

    lista_coches.append(coche)

    coche.wheel.set_pressure(input("Presión rueda: "))
    coche.move_to(rd.random() * 100, rd.random() * 600)
    print("Posición: ", coche.get_pos())
    coche.move_incr(rd.random() * 10, rd.random() * 60)
    print("Posición", coche.get_pos())
    del (coche)
    del (wheel)
pp.store(lista_coches, COCHES)
lista_coches = []
print(lista_coches)
lista_coches = pp.retrieve(COCHES)
n = len(lista_coches)
for i in range(n-1):
    for j in range(n-1-i):
        if lista_coches[j].marca > lista_coches[j+1].marca:
            aux = lista_coches[j]
            lista_coches[j] = lista_coches[j+1]
            lista_coches[j+1] = aux
for car in lista_coches:
    print("Marca, Modelo, Combustible, Cilindrada: ", \
          car.marca, car.modelo, car.combustible, car.cilindrada)
    print("Rueda: ancho, rodadura, diámetro, presión =>", car.wheel.print_info())
    print("Posición: ", car.get_pos(), "\n")