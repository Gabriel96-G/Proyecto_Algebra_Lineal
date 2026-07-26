import numpy as np
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from objetos import (
    Objeto2D,
    crear_cuadrado,
    crear_triangulo,
    crear_rectangulo,
)

print("=" * 60)
print("TEST: Caso 1 - Crear cuadrado y verificar coordenadas")
print("=" * 60)

cuad = crear_cuadrado(lado=2.0, origen=(0.0, 0.0))
print(cuad)

xs, ys = cuad.obtener_xy()
print(f"xs = {xs}")
print(f"ys = {ys}")

assert cuad.n == 4, f"El cuadrado debe tener 4 puntos, tiene {cuad.n}"
assert cuad.nombre == "Cuadrado"
assert xs[0] == 0.0 and ys[0] == 0.0
assert xs[1] == 2.0 and ys[1] == 0.0
assert xs[2] == 2.0 and ys[2] == 2.0
assert xs[3] == 0.0 and ys[3] == 2.0

print("[OK] Caso 1: Cuadrado creado correctamente")

print()
print("=" * 60)
print("TEST: Caso 2 - Clonar triangulo y verificar copia independiente")
print("=" * 60)

tri = crear_triangulo(base=4.0, altura=3.0, origen=(1.0, 1.0))
copia = tri.clonar()

print(f"Original: {tri}")
print(f"Copia:    {copia}")

tri.puntos[0, 0] = 999.0

assert copia.puntos[0, 0] != tri.puntos[0, 0], (
    "La copia no debe modificarse al cambiar el original"
)
assert copia.puntos[0, 0] == 1.0, (
    f"El primer x de la copia debe seguir siendo 1.0, pero es {copia.puntos[0, 0]}"
)
assert tri.nombre == "Triangulo"
assert copia.nombre == "Triangulo_copia"

print("[OK] Caso 2: Clonacion funciona, copia independiente del original")

print()
print("=" * 60)
print("TEST: Caso 3 - Crear objeto desde lista de tuplas")
print("=" * 60)

lista_tuplas = [(10.0, 20.0), (30.0, 40.0), (50.0, 60.0)]
obj = Objeto2D(lista_tuplas, nombre="ListaTest")
print(obj)

assert obj.n == 3
assert obj.puntos.shape == (2, 3)
assert obj.puntos[0, 0] == 10.0
assert obj.puntos[1, 0] == 20.0
assert obj.puntos[0, 1] == 30.0
assert obj.puntos[1, 1] == 40.0
assert obj.puntos[0, 2] == 50.0
assert obj.puntos[1, 2] == 60.0

tuplas_devueltas = obj.to_lista_tuplas()
assert tuplas_devueltas == lista_tuplas, (
    f"to_lista_tuplas() debe devolver {lista_tuplas}, pero devolvio {tuplas_devueltas}"
)

print(f"Matriz interna (2xN):\n{obj.puntos}")
print(f"to_lista_tuplas(): {tuplas_devueltas}")
print("[OK] Caso 3: Lista de tuplas convertida correctamente a matriz 2xN")

print()
print("=" * 60)
print("TEST: Verificaciones adicionales")
print("=" * 60)

rect = crear_rectangulo(ancho=5.0, alto=3.0, origen=(-1.0, -1.0))
print(rect)
assert rect.n == 4
assert rect.nombre == "Rectangulo"
xs, ys = rect.obtener_xy()
assert xs[2] - xs[1] == 0.0

print(f"__len__: {len(rect)}")

print("[OK] Todas las verificaciones adicionales pasaron")

print()
print("=" * 60)
print("TODOS LOS TEST PASARON")
print("=" * 60)
