#Cuantas horas tardaria en leer un libro

paginas = int(input("Cuantos minutos al dia necesitas para terminar en x dias.\n\nCuantas paginas?: "))

average = int(input("Ingresa en cuanto tiempo lees una pagina en segundos: "))
segundos = paginas * average

dias = int(input("En cuantos dias lo quieres acabar?: "))

horas = ((segundos / 60) / 60) / dias
minutos = horas * 60




print(f"Tardas: {round(minutos)} minutos al dia ")