# Este iterador es la base para otros iteradores
class IteradorBidireccional:

    def __init__(self, data, reverse=False):
        """
        Instancia un Iterador Bidireccional.
        :param data: Obtiene los datos los cuales "enlista"
        :param reverse: Booleano para saber si es falso o verdadero
        """
        self.data = data
        self.reverse = reverse
        # Inicializa el índice dependiendo de la dirección, 0 si es normal, o el último si es inverso
        self.index = len(data) - 1 if reverse else 0

    # Métodos de iteración, para hacer la clase iterable
    def __iter__(self):
        return self

    # Método para obtener el siguiente elemento en un iterador
    def __next__(self):
        if not self.reverse:
            if self.index >= len(self.data):
                raise StopIteration
            value = self.data[self.index]
            self.index += 1
        else:
            if self.index < 0:
                raise StopIteration
            value = self.data[self.index]
            self.index -= 1
        return value

class ImplementacionDelIteradorParaVectores(IteradorBidireccional):
    def __init__(self, data: list, reverse: bool =False):
        """
        Instancia un Iterador Bidireccional para vectores.
        :param data: Obtiene los datos los cuales "enlista"
        :param reverse: Booleano para saber si es falso o verdadero
        """
        super().__init__(data, reverse)


# Ejemplo de uso
if __name__ == "__main__":
    vector = [10, 20, 30, 40, 50]

    print("Recorrido ascendente:")
    asc_iter = ImplementacionDelIteradorParaVectores(vector, reverse=False)
    for value in asc_iter:
        print(value, end=" -> ")

    print("\nRecorrido descendente:")
    desc_iter = ImplementacionDelIteradorParaVectores(vector, reverse=True)
    for value in desc_iter:
        print(value, end=" -> ")
