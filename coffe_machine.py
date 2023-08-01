MENU = {
    "espresso": {
        "ingredientes": {
            "agua": 50,
            "cafe": 18,
        },
        "costo": 54,

    },
    "latte": {
        "ingredientes": {
            "agua": 200,
            "leche": 150,
            "cafe":24,
        },
        "costo": 76,
    },
    "cappuccino": {
        "ingredientes": {
            "agua": 150,
            "leche": 100,
            "cafe": 24,
        },
        "costo": 82,
    }
}

recursos = {
    "agua": 20000,
    "leche": 8000,
    "cafe": 1000,
}

ganancias = 0

# Creación de funciones

def recursos_suficientes(ingredientes_de_bebida):
    for item in ingredientes_de_bebida:
        if ingredientes_de_bebida[item] > recursos[item]:
            print(f'Lo siento no hay suficiente {item}.')
            return False
    return True

def ingreso_monedas():
    print('Por favor inserta las monedas. ')
    total = int(input('¿Cuántas de $1? ')) * 1
    total += int(input('¿Cuántas de $2? ')) * 2
    total += int(input('¿Cuántas de $5? ')) * 5
    total += int(input('¿Cuántas de $10? ')) * 10
    return total

def transaccion(dinero_recivido, precio_bebida):
    if dinero_recivido >= precio_bebida:
        cambio = (dinero_recivido - precio_bebida)
        print(f"Tu cambio es ${cambio}")
        global ganancias
        ganancias += precio_bebida # ganancias = ganancias + precio_bebida
        return True

def hacer_cafe(nombre_bebida, ingredientes_de_bebida):
    for item in ingredientes_de_bebida:
        recursos[item] -= ingredientes_de_bebida[item]
    print(f'Disfruta de tu {nombre_bebida}.')

# Main
esta_encendido = True
while esta_encendido:
    elegir = input ('¿Qué deseas pedir? (espresso/latte/cappuccino): ')
    if elegir == 'apagar':
        esta_encendido = False
    elif elegir == 'reporte':
        print(f"Agua: {recursos['agua']} ml")
        print(f"Leche {recursos['leche']} ml")
        print(f"Café: {recursos['cafe']} g")
        print(f"Ganancias: {ganancias}")
    else:
        bebida = MENU[elegir]
        if recursos_suficientes(bebida['ingredientes']):
            pago = ingreso_monedas()
            if transaccion(pago,bebida['costo']):
                hacer_cafe(elegir, bebida['ingredientes'])   