✅ README – Entrega Completa RA1 – Ciberseguridad, Bash, Git & Solidity

Este repositorio contiene todos los apartados correspondientes al Resultado de Aprendizaje RA1, incluyendo Python, Bash, Git Branching y Solidity.
La estructura y el contenido cumplen exactamente los requisitos de la práctica evaluable.

🟦 1. Aplicación de Criptografía en Python + Tests Unitarios

En este apartado se desarrolla una aplicación de criptografía en Python con diversas funciones centradas en hashing y codificación.

🔐 Funcionalidades Implementadas

Hasheo SHA-256 de un texto.

Verificación de contraseñas mediante hash.

Codificación y decodificación Base64.

Menú interactivo con opciones:

Encriptar (SHA-256 o Base64)

Desencriptar (Base64)

Fuerza bruta SHA-256 (palabras de hasta 4 caracteres en minúsculas)

6 tests unitarios implementados con pytest.

▶️ Ejecución de la aplicación
python crypto_app.py

▶️ Ejecución de los tests unitarios
pytest -v

🧠 Tecnologías y conceptos utilizados

Criptografía de hash (SHA-256)

Codificación Base64

Fuerza bruta

Testing automático (pytest)

Diseño modular de funciones

🟧 2. Script Bash de Información del Sistema

Este apartado incluye un script Bash que muestra en un único mensaje:

Dirección MAC

Sistema operativo

Hostname

Usuario actual

▶️ Ejecución

Dar permisos:

chmod +x script.sh


Ejecutar:

./script.sh

🧩 Compatibilidad
Sistema	Estado	Notas
Linux	✔ Funciona	Obtiene MAC correctamente
macOS	✔ Funciona	Igual que en Linux
Windows (Git Bash)	✔ Parcial	Puede no obtener la MAC

En caso de no poder extraer la MAC, el script devuelve:

MAC no disponible

🧠 Conceptos aplicados

Comandos del sistema (ifconfig, ip, getmac)

Manejo de errores

Compatibilidad multiplataforma

🟩 3. Git Branching – LearnGitBranching

Se han completado los ejercicios requeridos en:

https://learngitbranching.js.org/

📸 Capturas incluidas

pantallazo_main.jpg (vista Main)

pantallazo_remote.jpg (vista Remote)

Cada captura incluye identificadores propios que prueban la autoría.

🧠 Conceptos aplicados

Creación y manejo de ramas

Merge

Rebase

Remote Tracking

Push/Pull

Resolución de conflictos

🟪 4. Solidity – Merkle Tree

Tras completar el tutorial solicitado en Aules, este apartado contiene:

📸 Captura del tutorial

Incluye nombre o identificador personal.

🔐 Smart Contract desarrollado

Un contrato en Solidity que implementa la base de un árbol de Merkle, permitiendo:

Inserción de hojas (hashes)

Almacenamiento seguro

Preparación para generación de raíz y pruebas (Merkle Proofs)

🧠 Conceptos aplicados

Hashing en Solidity

Estructuras criptográficas

Árboles de decisión

Buenas prácticas en contratos inteligentes

🟦 5. Estructura del proyecto
NOMBRE_APELLIDO1_APELLIDO2/
│
├── Apartado1/
│   ├── crypto_app.py
│   ├── test_crypto_app.py
│   └── README.md
│
├── Apartado2/
│   ├── script.sh
│   └── README.md
│
├── Apartado3/
│   ├── pantallazo_main.jpg
│   ├── pantallazo_remote.jpg
│   └── README.md
│
├── Apartado4/
│   ├── merkle_contract.sol
│   ├── pantallazo_solidity.jpg
│   └── README.md
│
└── README.md   ← Este documento
