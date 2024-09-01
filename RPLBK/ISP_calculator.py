import math
from abc import ABC, abstractmethod

#Implementasi ISP pada program ini, pada pemisahan interface perhitungan operasi dasar  
#dan interface operasi advance

class BasicOP(ABC):
    @abstractmethod
    def add(self, a:float, b:float)->float:
        pass
    @abstractmethod
    def subtract(self, a:float, b:float)->float:
        pass
    @abstractmethod
    def multiply(self, a:float, b:float)->float:
        pass
    @abstractmethod
    def divide(self, a:float, b:float)->float:
        pass

class AdvancedOP(ABC):
    @abstractmethod
    def square_root(self, a: float) -> float:
        pass

    @abstractmethod
    def power(self, a: float, b: float) -> float:
        pass

    @abstractmethod
    def limit(self, func, a: float, delta: float = 1e-6) -> float:
        pass

    @abstractmethod
    def factorial(self, a: int) -> int:
        pass
   
class BasicCalculator(BasicOP):
    def add(self, a:float, b:float)->float:
        return a+b
    def subtract(self, a:float, b:float)->float:
        return a-b
    def multiply(self, a:float, b:float)->float:
        return a*b
    def divide(self, a:float, b:float)->float:
        if b == 0:
            raise ValueError("Tidak Bisa Dibagi Nol")
        return a/b
    
class AdvancedCalculator(AdvancedOP):
    def square_root(self, a: float) -> float:
        if a < 0:
            raise ValueError("Tidak bisa menghitung angka negatif")
        return math.sqrt(a)

    def power(self, a: float, b: float) -> float:
        return math.pow(a, b)

    def limit(self, func, a: float, delta: float = 1e-6) -> float:
        return (func(a + delta) - func(a)) / delta

    def factorial(self, a: int) -> int:
        if a < 0:
            raise ValueError("Tidak bisa menghitung angka negatif")
        return math.factorial(a)
    
def main():
    while True:
        print("\nPilih Tipe Kalkulator: ")
        print("1. Mudah")
        print("2. Susah")
        print("3. Exit Program")

        choice = input("\nPilih: ")
        if choice == "1":
            basic_calculator = BasicCalculator()
            print("\nOperasi Kalkulasi Dasar/Mudah:")
            print("1. Pertambahan")
            print("2. Pengurangan")
            print("3. Perkalian")
            print("4. Pembagian")
            
            operation = input("Pilih Operasi: ")
            a = float(input("Angka Pertama: "))
            b = float(input("Angka Kedua: "))

            if operation == "1":
                print(f"Hasil: {basic_calculator.add(a, b)}")
            elif operation == "2":
                print(f"Hasil: {basic_calculator.subtract(a, b)}")
            elif operation == "3":
                print(f"Hasil: {basic_calculator.multiply(a, b)}")
            elif operation == "4":
                try:
                    print(f"Hasil: {basic_calculator.divide(a, b)}")
                except ValueError as e:
                    print(e)
            else:
                print("Invalid operation...")
        
        elif choice == "2":
            advanced_calculator = AdvancedCalculator()
            print("\nOperasi Kalkulasi Advanced/Susah:")
            print("1. Akar Pangkat")
            print("2. Eksponen")
            print("3. Limit (approximation)")
            print("4. Faktorial")
            
            operation = input("Pilih Operasi: ")
            
            if operation == "1":
                a = float(input("Masukkan Angka: "))
                try:
                    print(f"Hasil: {advanced_calculator.square_root(a)}")
                except ValueError as e:
                    print(e)
            elif operation == "2":
                a = float(input("Masukkan Angka Basis: "))
                b = float(input("Masukkan Angka Eksponen: "))
                print(f"Hasil: {advanced_calculator.power(a, b)}")
            elif operation == "3":
                print("Contoh Fungsi: f(x) = x^2")
                a = float(input("Masukkan Angka dari x: "))
                print(f"Hasil: {advanced_calculator.limit(lambda x: x**2, a)}")
            elif operation == "4":
                a = int(input("Masukkan Bilangan Bulat Positif: "))
                try:
                    print(f"Hasil: {advanced_calculator.factorial(a)}")
                except ValueError as e:
                    print(e)
            else:
                print("Invalid operation.....")
        
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
