class Operaciones:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.resultado = 0
        
    def leerNumeros(self):
        while True:
            try:
                self.num1 = int(input("Número 1: "))
                break
            except ValueError:
                print("Número inválido. Intenta de nuevo.")
        while True:
            try:
                self.num2 = int(input("Número 2: "))
                break
            except ValueError:
                print("Número inválido. Intenta de nuevo.")
                continue    
    
    def sumar(self):
        self.resultado = "La suma de " + str(self.num1) + " + " + str(self.num2) + " es igula a " + str(self.num1 + self.num2)
    
    def restar(self):
        self.resultado = f"La resta de {self.num1} - {self.num2} es igual a {self.num1 - self.num2}"
    
    def multiplicar(self):
        self.resultado = f"La multiplicación de {self.num1} * {self.num2} es igual a {self.num1 * self.num2}"
    
    def mostrarResultado(self):
        print(self.resultado)

    def elegirOperacion(self):
        print("Elige la operación que deseas realizar:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        while True:
            opcion = input("Opcion (1/2/3): ")
            if opcion in ["1", "2", "3"]:
                self.leerNumeros()
                if opcion == "1":
                    self.sumar()
                elif opcion == "2":
                    self.restar()
                else:
                    self.multiplicar()
                self.mostrarResultado()
                break
            else:
                print("Opción invalida, intenta de nuevo.")
    def mostrarResultado(self):
        print(self.resultado)
        
        