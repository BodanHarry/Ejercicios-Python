listaEst = []
resp = "Si"
while resp.upper() != "NO":
    nombres = input("Escriba el nombre del estudiante \n")
    listaEst.append(nombres)
    resp= input("Desea agregar mas? SI - NO")

print(listaEst)

tam = len(listaEst)
print("Elementos guardados: ", tam)

for est in listaEst:
    print(est)