# ✅ README – Entrega Completa RA1 – Ciberseguridad, Bash, Git & Solidity

Este repositorio contiene todos los apartados correspondientes al **Resultado de Aprendizaje RA1**, incluyendo Python, Bash, Git Branching y Solidity. La estructura y el contenido cumplen exactamente los requisitos de la práctica evaluable.

## Contenido

- Apartado 1: Aplicación de criptografía en Python + tests (pytest)
- Apartado 2: Script Bash de información del sistema
- Apartado 3: Ejercicios de Git Branching (capturas incluidas)
- Apartado 4: Smart contract en Solidity (Merkle Tree) y captura

---

## 🟦 1. Aplicación de Criptografía en Python + Tests Unitarios

En este apartado se desarrolla una aplicación de criptografía en Python con funciones centradas en hashing y codificación.

### 🔐 Funcionalidades implementadas

- Hasheo SHA-256 de un texto.
- Verificación de contraseñas mediante hash.
- Codificación y decodificación Base64.
- Menú interactivo con opciones:
  - Encriptar (SHA-256 o Base64)
  - Desencriptar (Base64)
  - Fuerza bruta SHA-256 (palabras de hasta 4 caracteres en minúsculas)
- 6 tests unitarios implementados con pytest (cobertura de funciones principales).

### ▶️ Cómo ejecutar

Ejecutar la aplicación interactiva:

```bash
python EJ1/app.py
```

Ejecutar los tests con pytest:

```bash
pytest -v
```

### 🧠 Tecnologías y conceptos utilizados

- Criptografía de hash (SHA-256)
- Codificación Base64
- Fuerza bruta (attenuada: palabras hasta 4 letras, minúsculas)
- Testing automático con pytest
- Diseño modular de funciones para facilitar testeo y comprensión

---

## 🟧 2. Script Bash de Información del Sistema

Script que muestra en un único mensaje:

- Dirección MAC (si está disponible)
- Sistema operativo
- Hostname
- Usuario actual

### ▶️ Cómo ejecutar

Dar permisos y ejecutar:

```bash
chmod +x EJ2/script.sh
./EJ2/script.sh
```

### 🧩 Compatibilidad

| Sistema | Estado | Notas |
|--------:|:-----:|:-----|
| Linux | ✔️ Funciona | Obtiene MAC correctamente |
| macOS | ✔️ Funciona | Igual que en Linux |
| Windows (Git Bash) | ✔️ Parcial | Puede no obtener la MAC; si no está disponible, el script devuelve: "MAC no disponible" |

### 🧠 Conceptos aplicados

- Comandos del sistema (`ifconfig`, `ip`, `getmac`)
- Manejo de errores y detección de entorno
- Compatibilidad multiplataforma básica

---

## 🟩 3. Git Branching – LearnGitBranching

Se han completado los ejercicios requeridos en: https://learngitbranching.js.org/

### 📸 Capturas incluidas

- `Apartado3/pantallazo_main.jpg` (vista Main)
- `Apartado3/pantallazo_remote.jpg` (vista Remote)

Cada captura incluye identificadores propios que prueban la autoría.

### 🧠 Conceptos aplicados

- Creación y manejo de ramas
- Merge y rebase
- Remote tracking, push/pull
- Resolución de conflictos

---

## 🟪 4. Solidity – Merkle Tree

Tras completar el tutorial solicitado, este apartado contiene:

- Captura del tutorial con identificador personal: `Apartado4/pantallazo_solidity.jpg`
- Smart contract en Solidity que implementa la base de un árbol de Merkle:
  - Inserción de hojas (hashes)
  - Almacenamiento seguro
  - Preparación para la generación de raíz y la verificación de pruebas (Merkle Proofs)

### 🧠 Conceptos aplicados

- Hashing en Solidity
- Estructuras criptográficas y árboles de Merkle
- Buenas prácticas en contratos inteligentes

---

## 🟦 5. Estructura del proyecto

La estructura requerida del entregable es (reemplazar NOMBRE_APELLIDO1_APELLIDO2 por el nombre real según se indique en la entrega):

```
NOMBRE_APELLIDO1_APELLIDO2/
├── Apartado1/
│   ├── crypto_app.py
│   ├── test_crypto_app.py
│   └── README.md
├── Apartado2/
│   ├── script.sh
│   └── README.md
├── Apartado3/
│   ├── pantallazo_main.jpg
│   ├── pantallazo_remote.jpg
│   └── README.md
├── Apartado4/
│   ├── merkle_contract.sol
│   ├── pantallazo_solidity.jpg
│   └── README.md
└── README.md
```
