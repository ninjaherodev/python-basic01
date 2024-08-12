import re
contactos = {
    "ana": "56532565",
    "jose": "562253325",
    "carlos":"56417253"
}
contactos['paola'] = '3524244242'
contactos.update({"maria:":"89654122",
                  "pedro":"32512255"})

print(contactos)
print(contactos['carlos'])
print(contactos.get('carlos'))

contactos_encontrados = {}
for nombre, numero in contactos.items():
    if numero.startswith("3"):
        contactos_encontrados[nombre] = numero

print("Contactos con números que empiezan con 3:", contactos_encontrados)


contactos_encontrados2 = {}
patron = re.compile(r"^3")
for nombre, numero in contactos.items():
    if patron.match(numero):
        contactos_encontrados2[nombre] = numero

print("Contactos con números que empiezan con 3:", contactos_encontrados2)