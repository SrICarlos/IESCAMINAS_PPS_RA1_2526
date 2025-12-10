📄 README – Entrega Completa RA1 – Ciberseguridad, Bash, Git & Solidity

Este documento recoge toda la información necesaria para comprender y ejecutar los distintos apartados del Resultado de Aprendizaje RA1, incluyendo Python, Bash, GIT y Solidity, siguiendo exactamente los requisitos descritos en la práctica.

🟦 📌 Apartado 1 – Aplicación de Criptografía en Python + Tests Unitarios

En este apartado se desarrolla una aplicación de criptografía en Python que permite:

🔐 Funcionalidades implementadas

Hasheo SHA-256 de un texto.

Verificación de contraseñas mediante hash.

Codificación y decodificación Base64.

Sistema de menú interactivo con:

Encriptar (SHA256 o Base64)

Desencriptar (Base64)

Intento de fuerza bruta SHA256 (para palabras de hasta 4 caracteres en minúsculas).

Implementación de pruebas unitarias (un total de 6) con pytest.

▶️ Ejecución de la aplicación

Dentro del directorio del apartado 1:

python crypto_app.py

▶️ Ejecución de los tests unitarios

Los tests están diseñados para validar las funciones sin depender del menú interactivo.

Ejecutarlos con:

pytest -v

🧠 Tecnologías y conceptos aplicados

Criptografía de hash (SHA-256)

Codificación Base64

Fuerza bruta para búsqueda de pre-imagen

Testing automático con pytest

Diseño modular de funciones

🟧 📌 Apartado 2 – Script Bash de Obtención de Información del Sistema

Se incluye un script Bash que obtiene y muestra en un único mensaje:

La MAC del equipo

El sistema operativo

El hostname

El usuario que ejecuta el script

▶️ Ejecución del script

Dar permisos:

chmod +x script.sh


Ejecutar:

./script.sh

🧩 Compatibilidad

El script funciona correctamente en:

Sistema	Compatibilidad general	MAC
Linux	✔ Funciona	✔ Sí
macOS	✔ Funciona	✔ Sí
Windows (Git Bash)	✔ Funciona	⚠ Puede no obtener MAC

En caso de no encontrar la dirección MAC, el script devolverá:

MAC no disponible


Esto no rompe el script y cumple el requisito de mostrar un único mensaje con la información.

🧠 Tecnologías aplicadas

Uso de comandos del sistema (ifconfig, ip, getmac)

Control de errores

Compatibilidad multiplataforma

🟩 📌 Apartado 3 – Git Branching (LearnGitBranching)

Se han realizado los ejercicios del tutorial de:

https://learngitbranching.js.org/

📸 Se incluyen dos capturas obligatorias:

Pestaña Main (Principal)

Pestaña Remote (Remota)

Las capturas incluyen elementos identificativos propios para demostrar que han sido obtenidas por mí (por ejemplo, nombre visible junto a la pantalla o terminal abierta).

🧠 Conceptos aplicados

Branching

Merge

Rebase

Remote tracking

Push y Pull

Resolución de conflictos

🟪 📌 Apartado 4 – Solidity + Merkle Tree

Tras realizar el tutorial solicitado en Aules, se incluye:

📸 Captura de resultados del tutorial de Solidity

Incluye un identificador propio para demostrar autoría.

🔐 Smart Contract desarrollado

Se implementa un contrato en Solidity que representa el inicio de un árbol de Merkle (Merkle Tree):

Inserción de hojas (hashes)

Almacenamiento privado

Preparado para generar raíz y pruebas (Merkle Proofs)

Este contrato demuestra comprensión de:

Hashing en Solidity

Árboles de decisión criptográficos

Estructuras de datos

Buenas prácticas de diseño en contratos inteligentes

🟦 📁 Estructura del proyecto
NOMBRE_APELLIDO1_APELLIDO2/
├── Apartado1/
│   ├── crypto_app.py
│   ├── test_crypto_app.py
│   └── README.md (opcional si deseas separar)
├── Apartado2/
│   ├── script.sh
│   └── README.md (opcional)
├── Apartado3/
│   ├── pantallazo_main.jpg
│   ├── pantallazo_remote.jpg
│   └── README.md (opcional)
├── Apartado4/
│   ├── merkle_contract.sol
│   ├── pantallazo_solidity.jpg
│   └── README.md (opcional)
└── README.md   ← ESTE DOCUMENTO

🟫 📌 Subida al repositorio y Pull Request

Clonar el repositorio original proporcionado por el profesor.

Crear una nueva rama de trabajo.

Añadir la carpeta con mi nombre y apellidos:
NOMBRE_APELLIDO1_APELLIDO2/

Subir toda la solución:

git add .
git commit -m "Entrega completa RA1"
git push origin mi-rama


Crear un Pull Request hacia la rama principal del repositorio.

Con esto, la entrega queda completamente realizada.