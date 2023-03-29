class Contactos:
    def __init__(self):
        self._contactos = [None] * 10000

    def _hash(self, nombre):
        return hash(nombre) % len(self._contactos)

    def agregar(self, nombre, telefono):
        indice = self._hash(nombre)
        if self._contactos[indice] is None:
            self._contactos[indice] = {}
        self._contactos[indice][nombre] = telefono

    def eliminar(self, nombre):
        indice = self._hash(nombre)
        if self._contactos[indice] is not None and nombre in self._contactos[indice]:
            del self._contactos[indice][nombre]

    def buscar(self, nombre):
        indice = self._hash(nombre)
        if self._contactos[indice] is not None and nombre in self._contactos[indice]:
            return self._contactos[indice][nombre]
        else:
            return None

    def mostrar(self):
        for contacto in self._contactos:
            if contacto is not None:
                for nombre, telefono in contacto.items():
                    print(f"{nombre}: {telefono}")

def main():
    contactos = Contactos()
    while True:
        print("1. Agregar contacto")
        print("2. Actualizar contacto")
        print("3. Eliminar contacto")
        print("4. Buscar contacto")
        print("5. Mostrar contactos")
        print("6. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            nombre = input("Ingrese el nombre del contacto: ")
            telefono = input("Ingrese el número de teléfono del contacto: ")
            contactos.agregar(nombre, telefono)
        elif opcion == "2":
            nombre = input("Ingrese el nombre del contacto a actualizar: ")
            telefono = input("Ingrese el nuevo número de teléfono del contacto: ")
            if contactos.buscar(nombre) is not None:
                contactos.agregar(nombre, telefono)
            else:
                print("El contacto no existe")
        elif opcion == "3":
            nombre = input("Ingrese el nombre del contacto a eliminar: ")
            if contactos.buscar(nombre) is not None:
                contactos.eliminar(nombre)
            else:
                print("El contacto no existe")
        elif opcion == "4":
            nombre = input("Ingrese el nombre del contacto a buscar: ")
            telefono = contactos.buscar(nombre)
            if telefono is not None:
                print(f"{nombre}: {telefono}")
            else:
                print("El contacto no existe")
        elif opcion == "5":
            contactos.mostrar()
        elif opcion == "6":
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()
