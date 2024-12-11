def precio_stats(precios):
    total = 0
    num_productos = len(precios)
    for precio in precios.values():
        total += precio
        media = total / num_productos
    xi = {}
    for precio in precios.values():
        xi.update({precio: (precio - media)})

    xi2 = {}
    for valor, desviacion in xi.items():
        xi2.update({valor: desviacion**2})

    sumaxi2 = sum(xi2.values())
    varianza = sumaxi2 / (num_productos)
    return (media, varianza)
