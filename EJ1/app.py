import hashlib
import base64
import itertools
import string

#Encrypt y Decrypt

def hash_sha256(texto: str) -> str:
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()


def verificar_password(password: str, hash_guardado: str) -> bool:
    return hash_sha256(password) == hash_guardado


def base64_encode(texto: str) -> str:
    return base64.b64encode(texto.encode("utf-8")).decode("utf-8")


def base64_decode(cadena: str) -> str:
    return base64.b64decode(cadena.encode("utf-8")).decode("utf-8")


# Brute force SHA256
def brute_force_sha256(target_hash, max_len=5):
    letras = string.ascii_lowercase
    
    for length in range(1, max_len + 1):
        for combo in itertools.product(letras, repeat=length):
            posible = "".join(combo)
            if hash_sha256(posible) == target_hash:
                return posible

    return None


#Menu

def menu():
    print("\n=== CRYPTO APP ===")
    print("1. Encriptar")
    print("2. Desencriptar")
    print("0. Salir")

    opcion = input("Selecciona una opción: ")
    return opcion


def menu_tipo1():
    print("\n=== TIPO DE CIFRADO ===")
    print("1. Base64")
    print("2. SHA256")
    
    opcion = input("Selecciona tipo: ")
    return opcion

def menu_tipo2():
    print("\n=== TIPO DE DESCIFRADO ===")
    print("1. Base64")
    print("2. SHA256 (Max 4 car)")
    
    opcion = input("Selecciona tipo: ")
    return opcion

#Main
if __name__ == "__main__":
    while True:
        opcion = menu()
        #Salida elegante
        if opcion == "0":
            print("Saliendo…")
            break
        #Ejecucion menu Encrypt
        if opcion == "1":
            tipo = menu_tipo1()
            texto = input("Introduce el texto: ")

            if tipo == "1":  
                print("Base64:", base64_encode(texto))

            elif tipo == "2":  
                print("SHA-256:", hash_sha256(texto))

            else:
                print("Opción inválida.")
        #Ejecucion menu Decrypt
        elif opcion == "2":
            tipo = menu_tipo2()
            texto = input("Introduce el texto: ")

            if tipo == "1":  # Base64
                try:
                    print("Base64 decoded:", base64_decode(texto))
                except:
                    print("Error: cadena Base64 inválida.")
        #Bruteforce para sacar el sha256 que solo admite 4 caracteres porque no quiero quemar el pc
            elif tipo == "2":  
                print("Desencriptando HASH a fuerza bruta")
                resultado = brute_force_sha256(texto, max_len=5)

                if resultado:
                    print("Texto encontrado:", resultado)
                else:
                    print("El mensaje contiene caracteres raros o mide mas de 4 caracteres")

            else:
                print("Opción inválida.")
