n_register = int(input('AGREGAR CANTIDAD DE USUARIOS A REGISTRAR:  '))

file = open('usuarios.txt', 'a')

for i in range(n_register):
    nombre =input('Ingresar su nombre de usuario: ')
    edad  = input ("Ingresar su edad:  "))
    file.write(nombre + ' ' + edad + '/n' )

file.close()

file = open('usuarios.txt')

print(file.read())



