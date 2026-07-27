import math
import os
import sys
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))

from objetos import Objeto2D, crear_cuadrado
from transformaciones import Transformador


def assert_matriz_cercana(actual, esperado, nombre, tolerancia=1e-6):
    if not np.allclose(actual, esperado, atol=tolerancia):
        raise AssertionError(
            f"{nombre} no coincide.\nActual:\n{actual}\nEsperado:\n{esperado}"
        )


def imprimir_resultado(titulo, objeto_original, objeto_transformado, matriz):
    print()
    print("=" * 70)
    print(titulo)
    print("=" * 70)
    print(f"Objeto original:     {objeto_original}")
    print("Matriz utilizada:")
    print(np.round(matriz, 6))
    print(f"Objeto transformado: {objeto_transformado}")
    print("Coordenadas transformadas:")
    print(np.round(objeto_transformado.puntos, 6))


print("=" * 70)
print("TESTS — ALEJANDRO: Módulo de Transformaciones")
print("=" * 70)

transformador = Transformador()
cuadrado = crear_cuadrado(lado=2.0, origen=(0.0, 0.0))
puntos_originales = np.copy(cuadrado.puntos)

trasladado, matriz_t = transformador.trasladar(cuadrado, dx=3.0, dy=-1.0)

matriz_t_esperada = np.array([
    [1.0, 0.0, 3.0],
    [0.0, 1.0, -1.0],
    [0.0, 0.0, 1.0],
])

puntos_t_esperados = np.array([
    [3.0, 5.0, 5.0, 3.0],
    [-1.0, -1.0, 1.0, 1.0],
])

assert_matriz_cercana(matriz_t, matriz_t_esperada, "Matriz de traslación")
assert_matriz_cercana(trasladado.puntos, puntos_t_esperados, "Puntos trasladados")
assert_matriz_cercana(cuadrado.puntos, puntos_originales, "El objeto original no debe modificarse")
imprimir_resultado("CASO 1: Trasladar cuadrado dx=3, dy=-1", cuadrado, trasladado, matriz_t)

rotado, matriz_r = transformador.rotar(cuadrado, angulo=45.0)

c = math.sqrt(2) / 2
matriz_r_esperada = np.array([
    [c, -c],
    [c,  c],
])

puntos_r_esperados = np.array([
    [0.0, 2.0 * c, 0.0, -2.0 * c],
    [0.0, 2.0 * c, 4.0 * c, 2.0 * c],
])

assert_matriz_cercana(matriz_r, matriz_r_esperada, "Matriz de rotación 45 grados")
assert_matriz_cercana(rotado.puntos, puntos_r_esperados, "Puntos rotados 45 grados")
imprimir_resultado("CASO 2: Rotar cuadrado 45 grados", cuadrado, rotado, matriz_r)

escalado, matriz_s = transformador.escalar(cuadrado, sx=2.0)

matriz_s_esperada = np.array([
    [2.0, 0.0],
    [0.0, 2.0],
])

puntos_s_esperados = np.array([
    [0.0, 4.0, 4.0, 0.0],
    [0.0, 0.0, 4.0, 4.0],
])

assert_matriz_cercana(matriz_s, matriz_s_esperada, "Matriz de escalamiento")
assert_matriz_cercana(escalado.puntos, puntos_s_esperados, "Puntos escalados")
imprimir_resultado("CASO 3: Escalar cuadrado por factor 2", cuadrado, escalado, matriz_s)

figura_ref = Objeto2D([(1.0, 2.0), (3.0, 4.0), (-2.0, 5.0)], nombre="FiguraRef")
ref_x, matriz_ref_x = transformador.reflejar(figura_ref, eje="x")

matriz_ref_x_esperada = np.array([
    [1.0, 0.0],
    [0.0, -1.0],
])

puntos_ref_x_esperados = np.array([
    [1.0, 3.0, -2.0],
    [-2.0, -4.0, -5.0],
])

assert_matriz_cercana(matriz_ref_x, matriz_ref_x_esperada, "Matriz reflexión eje x")
assert_matriz_cercana(ref_x.puntos, puntos_ref_x_esperados, "Puntos reflejados eje x")
imprimir_resultado("CASO 4: Reflejar respecto al eje x", figura_ref, ref_x, matriz_ref_x)

ref_y, matriz_ref_y = transformador.reflejar(figura_ref, eje="y")

matriz_ref_y_esperada = np.array([
    [-1.0, 0.0],
    [0.0, 1.0],
])

puntos_ref_y_esperados = np.array([
    [-1.0, -3.0, 2.0],
    [2.0, 4.0, 5.0],
])

assert_matriz_cercana(matriz_ref_y, matriz_ref_y_esperada, "Matriz reflexión eje y")
assert_matriz_cercana(ref_y.puntos, puntos_ref_y_esperados, "Puntos reflejados eje y")
imprimir_resultado("CASO 5: Reflejar respecto al eje y", figura_ref, ref_y, matriz_ref_y)

ref_diag, matriz_ref_diag = transformador.reflejar(figura_ref, eje="y=x")

matriz_ref_diag_esperada = np.array([
    [0.0, 1.0],
    [1.0, 0.0],
])

puntos_ref_diag_esperados = np.array([
    [2.0, 4.0, 5.0],
    [1.0, 3.0, -2.0],
])

assert_matriz_cercana(matriz_ref_diag, matriz_ref_diag_esperada, "Matriz reflexión y=x")
assert_matriz_cercana(ref_diag.puntos, puntos_ref_diag_esperados, "Puntos reflejados y=x")
imprimir_resultado("CASO 6: Reflejar respecto a la recta y=x", figura_ref, ref_diag, matriz_ref_diag)

rot_30, matriz_r30 = transformador.rotar(cuadrado, 30.0)
esc_15, matriz_s15 = transformador.escalar(rot_30, 1.5)
seq_final, matriz_t_seq = transformador.trasladar(esc_15, 2.0, 1.0)

theta = math.radians(30.0)
R3 = np.array([
    [math.cos(theta), -math.sin(theta), 0.0],
    [math.sin(theta),  math.cos(theta), 0.0],
    [0.0, 0.0, 1.0],
])
S3 = np.array([
    [1.5, 0.0, 0.0],
    [0.0, 1.5, 0.0],
    [0.0, 0.0, 1.0],
])
T3 = np.array([
    [1.0, 0.0, 2.0],
    [0.0, 1.0, 1.0],
    [0.0, 0.0, 1.0],
])

matriz_compuesta = T3 @ S3 @ R3
puntos_h = np.vstack([cuadrado.puntos, np.ones((1, cuadrado.n))])
puntos_seq_esperados = (matriz_compuesta @ puntos_h)[:2, :]

assert_matriz_cercana(seq_final.puntos, puntos_seq_esperados, "Transformaciones consecutivas")

print()
print("=" * 70)
print("CASO 7: Transformaciones consecutivas")
print("=" * 70)
print("Orden aplicado: Rotar 30° -> Escalar 1.5 -> Trasladar (2,1)")
print("Matriz rotación 30°:")
print(np.round(matriz_r30, 6))
print("Matriz escalamiento 1.5:")
print(np.round(matriz_s15, 6))
print("Matriz traslación:")
print(np.round(matriz_t_seq, 6))
print("Matriz compuesta homogénea T * S * R:")
print(np.round(matriz_compuesta, 6))
print(f"Resultado final: {seq_final}")
print(np.round(seq_final.puntos, 6))

try:
    transformador.reflejar(cuadrado, eje="z")
    raise AssertionError("Se esperaba ValueError al usar eje='z'")
except ValueError:
    print()
    print("[OK] Caso 8: reflejar() rechaza ejes no soportados")

print()
print("=" * 70)
print("TODOS LOS TESTS DE TRANSFORMACIONES PASARON")
print("=" * 70)
