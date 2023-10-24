from Motocycle import Motocycle 

mi_moto = Motocycle(
    color="Rojo",
    license_plate="ABC123",
    brand="Honda",
    model="Estrellita",
    manufacture_date="2022-01-15",
    top_speed=150,
    weight=200
)

mi_moto2 = Motocycle(
    color="Verde",
    license_plate="ACB423",
    brand="Honda",
    model="Lunita",
    manufacture_date="2002-01-15",
    top_speed=450,
    weight=250
)

mi_moto.start_motor()
mi_moto.start_motor()
mi_moto.stop_motor()
mi_moto.stop_motor()

mi_moto.price = 15000
mi_moto.ask_price()
mi_moto2.price = 25200
mi_moto2.ask_price()


#print(f"El precio de la motocicleta {mi_moto.brand} {mi_moto.model} es de ${mi_moto.price}")