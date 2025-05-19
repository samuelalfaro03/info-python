hotel = {
    "name": "Hotel Uvita",
    "Stars": 4,
    "bedrooms": [
        {
            "number": 1,
            "floor": 1,
            "price_night": "$87"
        },
        {
            "number": 2,
            "floor": 1,
            "price_night": "$89"
        },
        {
            "number": 3,
            "floor": 2,
            "price_night": "$97"
        },
        {
            "number": 4,
            "floor": 2,
            "price_night": "$105"
        },
        {
            "number": 5,
            "floor": 3,
            "price_night": "$120"
        }
    ]
}
        
print(f"Nombre del hotel: {hotel['name']}")
print(f"Número de estrellas: {hotel['Stars']}")
print("Habitaciones:")

    
for bedroom in hotel["bedrooms"]:



    print(f"  - Habitación {bedroom['number']} en el piso {bedroom['floor']} con un precio por noche de {bedroom['price_night']}")

