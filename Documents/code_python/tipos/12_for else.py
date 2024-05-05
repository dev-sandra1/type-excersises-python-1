buscar = 3
 
for i in range(5):
    print(i)
    if i == buscar:
        print("Encontrado",buscar)
        break
        
else:
    print("No encontrado",buscar)