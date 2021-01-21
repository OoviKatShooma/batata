import math

#f(a, b, c) = (-b + - squar(b² - 4 * a * c)) / 2 * a

def baskara(a, b, c):
    delta = math.pow(b,2) - 4*a*c
    parte_de_cima_positiva = -b + math.sqrt(delta)
    parte_de_cima_negativa = -b - math.sqrt(delta)
    parte_de_baixo = 2 * a
    

    x1 = parte_de_cima_positiva / parte_de_baixo
    x2 = parte_de_cima_negativa / parte_de_baixo

    return [x1, x2]


print(baskara(10, 4, -1))
