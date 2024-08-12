ventas = [
    {"fecha": "2024-01-01", "producto": "A", "cantidad": 10, "precio": 5.0},
    {"fecha": "2024-01-02", "producto": "B", "cantidad": 5, "precio": 15.0},
    {"fecha": "2024-01-03", "producto": "A", "cantidad": 2, "precio": 5.0},
    {"fecha": "2024-01-04", "producto": "C", "cantidad": 7, "precio": 20.0},
    {"fecha": "2024-01-05", "producto": "B", "cantidad": 3, "precio": 15.0}   
]

ventas_filtradas = list(filter(lambda x: x["cantidad"] > 5, ventas))
print(ventas_filtradas)

ventas_precio_mayor_a_10 = [venta for venta in ventas if venta["precio"] > 10.0]
print("Ventas con precio mayor a 10.0:", ventas_precio_mayor_a_10)