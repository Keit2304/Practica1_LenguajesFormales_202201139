# Lenguajes Formales y de Programación (Sección B-)
## Práctica 1 PetManager
### Primer Semestre 2024
```js
Universidad San Carlos de Guatemala
Programador: Keitlyn Valentina Tunchez Castañeda
Carne: 202201139
Correo: 2986847560101@ingenieria.usac.edu.gt
```
---
## Descripción del Proyecto
El Consejo Nacional de Áreas Protegidas ha lanzado el programa educativo "PetWorld Manager", destinado a niños de 6 a 12 años, con el objetivo de inculcar valores de cuidado y responsabilidad en la tenencia de mascotas. En colaboración con la Universidad de San Carlos de Guatemala, el curso de Lenguajes Formales y de Programación se ha comprometido a ofrecer su apoyo a este proyecto socialmente responsable.
"PetWorld Manager" no solo es un programa de entretenimiento y educación, sino también una herramienta pedagógica diseñada para concientizar a los niños sobre el compromiso y cuidado necesario al tener una mascota. Este proyecto se alinea estrechamente con la misión del Consejo Nacional de Áreas Protegidas de fomentar la responsabilidad social y ambiental desde una edad temprana.

## Objetivos
* Objetivo General
    * Desarrollar un sistema de gestión integral de mascotas virtuales (gatos), incorporando módulos de almacenamiento de palabras, utilizando principios de programación en Python y aplicando paradigmas de programación orientada a objetos y funcional.
* Objetivos Específicos
    * Desarrollar las clases y funciones necesarias para la creación, interacción y gestión de mascotas virtuales.
    * Asegurar que la aplicación pueda interpretar y ejecutar los comandos contenidos en estos archivos.

---
## Métodos y funciones de la práctica 
El sistema permite cargar archivos de texto con instrucciones específicas para gestionar gatos, tales como crearlos, alimentarlos, jugar con ellos y generar un resumen de sus acciones. Además, proporciona funcionalidades para visualizar gráficamente el estado de los gatos y generar un resumen global de todas las acciones realizadas.
A continuación, se describen los métodos y funciones utilizados en el código:

Importaciones de módulos:

- import os: Proporciona funciones para interactuar con el sistema operativo.
- import datetime: Permite trabajar con fechas y horas.
- import graphviz: Se utiliza para generar y visualizar gráficos.
- from PIL import Image: Importa la clase Image del módulo PIL (Python Imaging Library) para manipular imágenes.
![Interpretaciones](https://i.ibb.co/r4wcC49/interpretaciones-de-m-dulo.png)


Métodos de la clase Gato:

- __init__(self, nombre, energia=1): Constructor de la clase Gato que inicializa las propiedades del gato (nombre, energía y estado).

![init](https://i.ibb.co/fMxxThP/init.png)
- dar_de_comer(self, peso_ratón): Método que aumenta la energía del gato según el peso del ratón que come.

![comer](https://i.ibb.co/DL6g4Dm/comer.png)
- jugar(self, tiempo): Método que disminuye la energía del gato según el tiempo que juega.

![jugar](https://i.ibb.co/5hk9MPZ/jugar.png)
- __str__(self): Método especial que devuelve una representación en cadena del objeto Gato.

![str](https://i.ibb.co/f90S6my/str.png)


Funciones auxiliares:

- Generar_Grafo(nombre, energia, estado, lista_imagenes): Genera un grafo representando el estado del gato y lo guarda como una imagen PNG.

![generargrafo](https://i.ibb.co/ZLCdSnw/generar-grafo.png)
- combinar_imagenes_con_os(nombre_salida="imagenes_combinadas.png"): Combina las imágenes PNG en el directorio actual en una sola imagen.

![combinar](https://i.ibb.co/6YtMPXz/combinar.png)
- LimpiarImagenes(): Elimina las imágenes PNG generadas en el directorio actual, excepto la imagen combinada.

![limpiar](https://i.ibb.co/9cJChXM/limpiar.png)
- Crear_Gatos(archivo): Lee un archivo de texto y crea instancias de gatos según las instrucciones en el archivo.

![creargatos](https://i.ibb.co/JyL0HFv/crear-gatos.png)
- Alimentar_Gatos(archivo, gatos): Lee un archivo de texto y alimenta a los gatos según las instrucciones en el archivo.

![alimentar](https://i.ibb.co/SXhd52K/alimentar-gatos.png)
- Jugar_Gatos(archivo, gatos): Lee un archivo de texto y hace que los gatos jueguen según las instrucciones en el archivo.

![jugar](https://i.ibb.co/VB8KpvW/jugar-gatos.png)
- Resumen_Mascota(archivo, gatos, nombre): Genera un resumen de las acciones realizadas en un gato específico y su estado.

![resumen](https://i.ibb.co/NZzPqkm/Resumen.png)
- Resumen_Global(archivo, gatos): Genera un resumen global de todas las acciones realizadas en todos los gatos.

![global](https://i.ibb.co/s5WZW1S/Resumen-Global.png)
- Imprimiendo(gatos): Genera un archivo de resumen y combina las imágenes de los gatos.

![imprimiendo](https://i.ibb.co/YNN0cpw/Imprimiendo.png)
 

Menús y bucles:

while Menu: Bucle principal del programa.
- Menú Principal:
__Opción 1__: Acceso al módulo PetManager.
__Opción 2__: Salir del programa.
- Menú PetManager:
__Opción 1__: Cargar archivo.
__Opción 2__: Salir del módulo PetManager.

# En conclusión
El manual técnico proporcionado detalla el funcionamiento y la implementación del código de PetManager, un sistema diseñado para gestionar las acciones y el estado de gatos virtuales. A lo largo de este manual, hemos explorado los diferentes componentes del programa, desde la creación y alimentación de gatos hasta la generación de resúmenes globales y la visualización de datos mediante gráficos. Con la comprensión de este manual, los usuarios estarán equipados para utilizar eficazmente el sistema PetManager, aprovechando su funcionalidad para gestionar y monitorear a sus felinos virtuales.