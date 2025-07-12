import requests
API_KEY = 'd60c8134-de06-4881-b91c-28b80c7f2b56'

def aplicacion(ciudad):
    url = 'https://graphhopper.com/api/1/geocode'
    params = {
        'q': ciudad,
        'locale': 'es',
        'limit': 1,
        'key': API_KEY
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['hits']:
            lat = data['hits'][0]['point']['lat']
            lng = data['hits'][0]['point']['lng']
            return f"{lat},{lng}"
        else:
            print(f" Ciudad incorrecta: {ciudad}")
            return None
    else:
        print(f" Error {ciudad}: {response.status_code}")
        return None

def datos(origen, destino, transporte):
    url = 'https://graphhopper.com/api/1/route'
    params = {
        'point': [origen, destino],
        'vehicle': transporte,
        'locale': 'es',
        'instructions': 'true',
        'calc_points': 'true',
        'key': API_KEY
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        metros = data['paths'][0]['distance']
        minutos = data['paths'][0]['time'] / 1000
        instrucciones = data['paths'][0]['instructions']

        print(f"Distancia total: {metros / 1000} km / {(metros * 0.000621371)} millas")
        print(f" Duración estimada: {minutos / 60} minutos\n")

        print(" Narrativa :")
        for paso in instrucciones:
            print(f"- {paso['text']}")

    else:
        print(f"Error {response.status_code}")
        print(response.text)

def main():
    while True:
        print("Simulador de viaje usa la letra 's' para salir")

        origen = input("Ciudad de origen: ")
        if origen == 's':
            break
        destino = input("Ciudad de destino: ")
        if destino == 's':
            break

        print("Tipo de transporte:")
        print("1. Auto")
        print("2. Bicicleta")
        print("3. Caminando")
        opcion = input("Elige una opción:")
        
        if opcion == '1':
            vehiculo = 'car'
        elif opcion == '2':
            vehiculo = 'bike'
        elif opcion == '3':
            vehiculo = 'foot'
        else:
            print(" Opción inválida.")
            continue

        origen = aplicacion(origen)
        destino = aplicacion(destino)

        if origen and destino:
            datos(origen, destino, vehiculo)
            
        print ("¿quieres simular otro viaje?")
        print ("1) Si")
        print ("2) No")
        opcion2 = input ("Elige una opcion")
        if opcion2 == '1':
            continue
        elif opcion2 == '2':
            print("Gracias por usar")
            break
if __name__ == "__main__":
    main()
    
    
