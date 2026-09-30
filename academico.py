# Módulo complementario: ejecuta Python 3 academico.py desde esta carpeta.
# No es necesario ejecutarlo para abrir la aplicación web.
from pathlib import Path
# datetime verifica fechas reales, incluidos años bisiestos.
from datetime import datetime
# time permite demostrar una espera de bienvenida menor de cinco segundos.
import time
# select no es portable en consola Windows; el menú usa una lectura en un hilo.
from concurrent.futures import ThreadPoolExecutor, TimeoutError
# Solo se trabaja con archivos TXT dentro de la carpeta archivos.
BASE = Path(__file__).resolve().parent / 'archivos'
# Se crea la carpeta si aún no existe.
BASE.mkdir(exist_ok=True)
# El diccionario conserva las cuatro opciones y sus descripciones.
OPCIONES = {'1': 'Leer archivo', '2': 'Escribir archivo', '3': 'Crear archivo', '4': 'Cambiar usuario', '5': 'Validar fecha', '0': 'Salir'}
# Se conserva una lista para mostrar los archivos disponibles.
INICIALES = ['bienvenida.txt', 'estudios.txt', 'preparacion.txt', 'notas.txt']
# for recorre los archivos iniciales sin sobrescribir contenido existente.
for nombre in INICIALES:
    # Los archivos entregados con el proyecto se conservan intactos.
    if not (BASE / nombre).exists():
        # write_text crea un archivo UTF-8 cuando falta.
        (BASE / nombre).write_text('Archivo del proyecto LSM SmartLab.\n', encoding='utf-8')
# Esta función devuelve una tupla nativa (día, mes, año).
def pedir_fecha():
    # while repite hasta que se introduzca una fecha válida.
    while True:
        # try/except muestra el error sin terminar el programa.
        try:
            # La fecha se solicita en el formato académico.
            texto = input('Fecha dd/mm/aaaa: ')
            # strptime valida tanto el formato como el calendario.
            fecha = datetime.strptime(texto, '%d/%m/%Y')
            # return conserva el tipo tuple de Python.
            return (fecha.day, fecha.month, fecha.year)
        # Una fecha imposible produce ValueError.
        except ValueError:
            # Se ofrece una indicación concreta para corregirla.
            print('Fecha inválida. Usa dd/mm/aaaa y una fecha que exista.')
# Limita las operaciones de archivos a la carpeta del proyecto.
def ruta_segura(nombre):
    # No se aceptan rutas, extensiones diferentes ni nombres vacíos.
    if Path(nombre).name != nombre or not nombre.endswith('.txt'):
        # El menú captura este error y continúa.
        raise ValueError('Escribe solo un nombre terminado en .txt.')
    # Devuelve una ruta absoluta dentro de archivos.
    return BASE / nombre
# La bienvenida solicita un usuario no vacío.
def cambiar_usuario():
    # Se repite la pregunta cuando no hay nombre.
    while True:
        # strip elimina espacios accidentales.
        nombre = input('Nombre o nickname: ').strip()
        # Solo se acepta un nombre con contenido.
        if nombre:
            # La espera de bienvenida es de medio segundo.
            time.sleep(0.5)
            # La interpolación muestra el usuario elegido.
            print(f'Bienvenido, {nombre}.')
            # Devuelve el nuevo usuario al menú.
            return nombre
# Lee una selección con un for que mide hasta diez minutos.
def leer_opcion():
    # El único hilo recoge la entrada; el principal mide la espera.
    with ThreadPoolExecutor(max_workers=1) as pool:
        # Se inicia una única lectura, evitando entradas simultáneas.
        pendiente = pool.submit(input, 'Opción: ')
        # for espera 600 intervalos de un segundo.
        for segundo in range(600):
            # Cada intento devuelve la selección o un timeout normal.
            try:
                # Se devuelve inmediatamente cuando hay entrada.
                return pendiente.result(timeout=1).strip()
            # Un segundo sin entrada no es un error fatal.
            except TimeoutError:
                # Continúa el siguiente intervalo.
                continue
        # No se inicia otra lectura mientras la anterior está pendiente.
        print('\n10 minutos sin selección. Pulsa Enter para decidir si continúas.')
        # Espera terminar la lectura pendiente antes de la confirmación.
        pendiente.result()
        # La respuesta decide continuar o cambiar usuario.
        return '4' if input('¿Continuar? s/n: ').strip().lower() == 'n' else ''
# main permite importar este módulo para pruebas sin abrir el menú.
def main():
    # Se obtiene el nickname inicial.
    usuario = cambiar_usuario()
    # El menú permanece activo hasta seleccionar salir.
    while True:
        # El encabezado identifica usuario y proyecto.
        print(f'\nLSM SmartLab | Usuario: {usuario}')
        # La salida tabular tiene dos columnas.
        print(f'{"NÚM.":<8} OPCIÓN')
        # El diccionario alimenta el menú con un for.
        for clave, descripcion in OPCIONES.items():
            # Alinea la columna numérica.
            print(f'{clave:<8} {descripcion}')
        # Muestra los archivos disponibles con una lista.
        print('Archivos:', [p.name for p in BASE.glob('*.txt')])
        # Se controlan errores de entradas y sistema de archivos.
        try:
            # La selección utiliza la función con temporizador.
            opcion = leer_opcion()
            # Cero finaliza el while.
            if opcion == '0':
                # Salida normal sin borrar los archivos.
                break
            # Cuatro cambia de usuario sin reiniciar el programa.
            if opcion == '4':
                # Sustituye el nickname actual.
                usuario = cambiar_usuario()
            # Cinco demuestra una tupla nativa.
            elif opcion == '5':
                # Imprime el valor y su representación de tupla.
                print('Tupla:', pedir_fecha())
            # Las tres operaciones requieren un nombre de archivo.
            elif opcion in ('1', '2', '3'):
                # La ruta se valida antes de abrirla.
                ruta = ruta_segura(input('Nombre del archivo: ').strip())
                # Lectura: read_text puede lanzar FileNotFoundError.
                if opcion == '1':
                    # Se muestra el contenido completo.
                    print(ruta.read_text(encoding='utf-8'))
                # Escritura solo actualiza un archivo existente.
                elif opcion == '2':
                    # Se comprueba su existencia antes de modificarlo.
                    if not ruta.exists():
                        # Se eleva el error capturado por el menú.
                        raise FileNotFoundError('Archivo inexistente.')
                    # La confirmación evita un reemplazo accidental.
                    if input('¿Reemplazar contenido? s/n: ').lower() == 's':
                        # Guarda el nuevo contenido como UTF-8.
                        ruta.write_text(input('Nuevo contenido: ') + '\n', encoding='utf-8')
                # Creación exclusiva: x no sobrescribe un archivo existente.
                else:
                    # El contexto cierra el archivo incluso ante un error.
                    with ruta.open('x', encoding='utf-8') as archivo:
                        # Se escribe el primer contenido.
                        archivo.write(input('Contenido inicial: ') + '\n')
            # Una selección no reconocida devuelve al menú.
            elif opcion:
                # Se presenta un mensaje comprensible.
                print('Opción inválida. Selecciona un número del menú.')
        # Incluye archivo inexistente, permisos y archivo ya existente.
        except (OSError, ValueError) as error:
            # El programa informa y permite intentarlo otra vez.
            print('Error controlado:', error)
# Solo abre el menú al ejecutar directamente este archivo.
if __name__ == '__main__':
    # Entrada principal del programa académico.
    main()
