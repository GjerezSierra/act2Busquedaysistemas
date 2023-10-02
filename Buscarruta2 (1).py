import networkx as nx

# Definir una base de conocimiento directamente en Python
base_conocimiento = {
    ("Estación A", "Estación B"): 5,
    ("Estación B", "Estación C"): 3,
    ("Estación B", "Estación D"): 4,
    ("Estación C", "Estación E"): 2,
    ("Estación D", "Estación E"): 3
}

# Información sobre estaciones en obras
estaciones_en_obras = {
    "Estación C": "2023-12-01",
    "Estación D": "2023-11-15"
}

# Función para encontrar la mejor ruta utilizando el algoritmo de Dijkstra en Python
def encontrar_mejor_ruta_con_obras(base_conocimiento, estaciones_en_obras, punto_a, punto_b):
    G = nx.Graph()

    # Agregar nodos (estaciones)
    estaciones = set()
    for conexion, _ in base_conocimiento.items():
        estaciones.add(conexion[0])
        estaciones.add(conexion[1])
    G.add_nodes_from(estaciones)

    # Agregar conexiones con distancias desde la base de conocimiento
    for conexion, distancia in base_conocimiento.items():
        G.add_edge(conexion[0], conexion[1], weight=distancia)

    try:
        mejor_ruta = nx.shortest_path(G, source=punto_a, target=punto_b, weight='weight')
        
        # Eliminar estaciones en obras de la ruta
        ruta_sin_obras = [estacion for estacion in mejor_ruta if estacion not in estaciones_en_obras]
        
        distancia_total = nx.shortest_path_length(G, source=punto_a, target=punto_b, weight='weight')
        return ruta_sin_obras, distancia_total
    except nx.NetworkXNoPath:
        return None, None

# Ejemplo de uso
punto_a = "Estación A"
punto_b = "Estación E"

ruta_python, distancia_python = encontrar_mejor_ruta_con_obras(base_conocimiento, estaciones_en_obras, punto_a, punto_b)

if ruta_python:
    print("Ruta y distancia encontrada usando Python (NetworkX):")
    print(f"Ruta: {ruta_python}")
    print(f"Distancia: {distancia_python}")
else:
    print(f"No se encontró una ruta desde {punto_a} hasta {punto_b} o la ruta pasa por estaciones en obras.")
