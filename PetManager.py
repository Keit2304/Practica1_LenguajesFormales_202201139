import os
import datetime
import graphviz
from PIL import Image

print("Bienvenido al sistema")
print("Curso: Lenguajes Formales y de Programación")
print("Sección: B-")
print("Carnet: 202201139")
input("\nPresione enter para continuar...")
lista_imagenes=[]
class Gato():
    def __init__(self, nombre, energia=1):
        self.nombre = nombre
        self.energia = energia
        self.estado = "Vivo" if energia > 0 else "Muerto"

    def dar_de_comer(self, peso_ratón):
        self.energia += 12 + peso_ratón

    def jugar(self, tiempo):
        self.energia -= tiempo * 0.1

    def __str__(self):
        now = datetime.datetime.now()
        return f"[{now}] - Se creo el gato {self.nombre}"

def Generar_Grafo(nombre, energia, estado, lista_imagenes):
    dot = graphviz.Digraph(comment='Gatos')
    
    dot.node(nombre, f'Nombre: {nombre}')

    dot.node(f'Energia_{nombre}', f'Energía: {energia}')
    dot.node(f'Tipo_{nombre}', f'Tipo: GATO')
    dot.node(f'Estado_{nombre}', f'Estado: {estado}')

    dot.edge(nombre, f'Energia_{nombre}')
    dot.edge(nombre, f'Tipo_{nombre}')
    dot.edge(nombre, f'Estado_{nombre}')

    dot.render(filename=f'{nombre}_grafo', format='png', directory='./', cleanup=True)

    lista_imagenes.append(f'{nombre}_grafo.png') 
    

def combinar_imagenes_con_os(nombre_salida="imagenes_combinadas.png"):
    imagenes = [imagen for imagen in os.listdir('.') if imagen.endswith('.png')]
    
    if not imagenes:
        print("No se encontraron imágenes PNG en el directorio.")
        return

    primera_imagen = Image.open(imagenes[0])
    imagenes = imagenes[1:]

    ancho, alto = primera_imagen.size
    imagen_combinada = Image.new("RGB", (ancho, alto * (len(imagenes) + 1)))

    imagen_combinada.paste(primera_imagen, (0, 0))

    for idx, imagen in enumerate(imagenes):
        imagen_actual = Image.open(imagen)
        imagen_combinada.paste(imagen_actual, (0, (idx + 1) * alto))

    imagen_combinada.save(nombre_salida)
    print(f"Se han combinado todas las imágenes en {nombre_salida}")


def LimpiarImagenes():
    directorio = './'
    archivos = os.listdir(directorio)
    for archivo in archivos:
        if archivo != 'imagenes_combinadas.png' and archivo.endswith('.png'):
            os.remove(os.path.join(directorio, archivo))

def Crear_Gatos(archivo):
    gatos = []
    with open(archivo, "r+") as archivo:
        for linea in archivo:
            if linea.startswith("Crear_Gato:"):
                nombre_gato = linea.replace("Crear_Gato:", "").strip()
                gato = Gato(nombre_gato)
                gatos.append(gato)
    return gatos

def Alimentar_Gatos(archivo, gatos):
    output = ""
    with open(archivo, "r+") as archivo:
        for linea in archivo:
            if linea.startswith("Dar_de_Comer:"):
                datos = linea.replace("Dar_de_Comer:", "").strip().split(",")
                nombre_gato = datos[0]
                peso_raton = int(datos[1])
                for gato in gatos:
                    if gato.nombre == nombre_gato:
                        gato.dar_de_comer(peso_raton)
                        output += f"[{datetime.datetime.now()}] - {gato.nombre}, Gracias por alimentarme con un raton de {peso_raton}g, Ahora mi energia es de: {gato.energia}"
                        
    return output

def Jugar_Gatos(archivo, gatos):
    output = ""
    with open(archivo, "r+") as archivo:
        for linea in archivo:
            if linea.startswith("Jugar:"):
                datos = linea.replace("Jugar:", "").strip().split(",")
                nombre_gato = datos[0]
                tiempo = int(datos[1])
                for gato in gatos:
                    if gato.nombre == nombre_gato:
                        gato.jugar(tiempo)
                        output += f"[{datetime.datetime.now()}] - {gato.nombre}, Gracias por jugar conmigo por {tiempo} minutos, Ahora mi energia es de: {round(gato.energia, 1)} \n"
                        
    return output

def Resumen_Mascota(archivo, gatos, nombre):
    resumen = f"__________Resumen de acciones para {nombre} __________\n"

    gatos_creados = [gato for gato in Crear_Gatos(archivo) if gato.nombre == nombre]
    for gato in gatos_creados:
        resumen += f" {gato}\n"

    resumen += Alimentar_Gatos(archivo, gatos_creados) + "\n"
    resumen += Jugar_Gatos(archivo, gatos_creados) + "\n"

    for gato in gatos_creados:
        resumen += f"{gato.nombre}, Energia actual: {gato.energia}, Estado: {gato.estado} \n"

    Generar_Grafo(nombre, gato.energia, gato.estado, [])

    return resumen

def Resumen_Global(archivo, gatos):
    resumen_global = "_________RESUMEN GLOBAL DE GATOS_________\n\n"

    for gato in gatos:
        resumen_global += Resumen_Mascota(archivo, gatos, gato.nombre) + "\n\n"

    return resumen_global

def Imprimiendo(gatos):
    resumen_global = Resumen_Global(archivo, gatos)
    with open("gatos.petworld_result", "w") as archivo_resultado:
        archivo_resultado.write(resumen_global)
    combinar_imagenes_con_os()
Menu = True

while Menu:
    os.system("cls")
    print("\n---------- *Menú Principal* ----------")
    print("1. Módulo PetManager")
    print("2. Salir")

    opcion = input("\nIngrese una opción: ")

    if opcion == "1":
        Submenu = True
        while Submenu:
            os.system("cls")
            print("\n---------- *Módulo PetManager* ----------")
            print("1. Cargar Archivo")
            print("2. Salir")

            opcion_pm = input("\nIngrese una opción: ")

            if opcion_pm == "1":

                archivos = os.listdir()
                archivos_pet = [archivo for archivo in archivos if archivo.endswith(".petmanager")]

                if len(archivos_pet) > 0:
                    for archivo in archivos_pet:
                        print(f"__________Leyendo archivo {archivo}__________")

                        try:
                            f = open(archivo, "r+")

                            contenido = f.read()
                            print(f"****Contenido del Archivo****\n{contenido}\n")
                            print("______________Aquí termina el archivo .petmanager____________________")

                            f.close()

                            gatos_creados = Crear_Gatos(archivo)
                            print("__________Gatos creados: __________")
                            for gato in gatos_creados:
                                print(gato)

                            Imprimiendo(gatos_creados)
                            combinar_imagenes_con_os()
                            LimpiarImagenes()
                        except:
                            print(f"Error leyendo archivo {archivo}")

                else:
                    print("No se encontraron archivos .petmanager")

            elif opcion_pm == "2":
                print("Saliendo...")
                break

    elif opcion == "2":
        print("Gracias por utilizar PetManager... Programa cerrado")
        Menu = False
