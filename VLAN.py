VLAN=int(input("Ingrese el numero de VLAN: "))
if VLAN in range(1, 1005):
    print("Esta VLAN es estandar")
elif VLAN in range(1006, 4094):
    print("Esta VLAN es extendida")
else:  
    print("Ingrese un numero valido")