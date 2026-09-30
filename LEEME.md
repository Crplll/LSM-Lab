# LSM SmartLab — aplicación web local

Descomprime la carpeta y abre **index.html** con Chrome, Edge, Firefox o Safari. No necesita instalación, conexión a internet ni servidor. Mantén las carpetas assets, css y js junto al HTML.

## Uso

1. Explora los 12 estudios y 5 perfiles, busca por nombre o filtra por categoría.
2. Abre Mi solicitud, revisa la selección y completa los datos.
3. Elige una fecha, consulta la preparación y confirma.
4. Descarga TXT o utiliza **Imprimir / Guardar PDF** y selecciona “Guardar como PDF” en el diálogo del navegador. El comprobante incluye un QR real generado localmente.
5. Vuelve a descargar solicitudes desde Mis solicitudes.

En móvil, Mi solicitud aparece en la barra inferior. En escritorio se muestra al costado del catálogo. Los precios están en pesos mexicanos.

## Alcance

Esta entrega es una aplicación local funcional: no realiza cobros, no envía datos al laboratorio y no reserva citas. Los comprobantes muestran PAGO PENDIENTE y la fecha solicitada. El QR codifica folio, fecha y total; no contiene datos personales ni abre un portal de verificación.

Las solicitudes y archivos se guardan en el almacenamiento del navegador de este dispositivo. No se sincronizan entre teléfonos y computadoras ni entre navegadores. En navegación privada, al limpiar datos o cambiar de ubicación la carpeta pueden dejar de estar disponibles. Descarga los comprobantes que quieras conservar. Cambiar usuario limpia el borrador, pero el historial sigue siendo compartido en el dispositivo: el nickname no es una cuenta ni una barrera de seguridad.

Los logos son los originales recuperados de la conversación. Los 17 precios, componentes e indicaciones se transcribieron de Proyecto final.py. La indicación original sobre suspender biotina se presenta con una confirmación médica explícita antes de modificar su uso. Donde el código no contenía preparación, se indica que debe consultarse al laboratorio. Los perfiles pueden solaparse con estudios individuales; el resumen muestra un aviso y permite editar la selección. No se permite agregar dos veces el mismo producto.

## Herramientas del proyecto

El enlace del pie de página permite leer, editar, crear, importar y descargar archivos TXT; cambiar nickname; validar fechas y ejecutar demostraciones de control de flujo y errores. El navegador edita copias locales: por seguridad no sobrescribe archivos del disco sin una descarga explícita.

JavaScript no tiene tuplas nativas ni la sintaxis try/except de Python. La web demuestra un arreglo inmutable equivalente y try/catch. Para demostrar esos requisitos literalmente se incluye **academico.py**, que se ejecuta con Python 3 y contiene tuplas, while, for, menú tabular, nickname, bienvenida de 0.5 segundos, temporizador de 10 minutos, lectura/escritura/creación, cuatro TXT y manejo de errores. Más del 50 % de sus líneas son comentarios explicativos. El módulo Python y la web utilizan almacenes separados. No se afirma cumplimiento de una rúbrica adicional no disponible.

## Organización

- index.html: estructura y accesibilidad.
- css/styles.css: estilos, adaptación móvil/tablet/escritorio e impresión.
- js/catalog.js: catálogo y recomendaciones originales.
- js/app.js: navegación, validaciones, carrito, archivos y comprobantes.
- js/qrcode.js: QR Code Generator de Kazuhiko Arase (licencia MIT incluida en el archivo).
- assets/: logos originales.
- archivos/: cuatro archivos TXT para el módulo académico.
- academico.py: demostración complementaria de los requisitos de Python.

WebMCP se registra solo si el navegador expone la API experimental; no es necesario para usar la aplicación.

## Doctor / Encargado

El botón del encabezado abre el acceso del personal. Usuario: **admin**. Contraseña: **admin**. Es un acceso demostrativo visible en el código, no una autenticación apta para datos clínicos reales.

El panel muestra todas las solicitudes de este navegador, con filtros En espera, En proceso y Finalizado. Una nueva solicitud aparece automáticamente En espera. Busca por paciente o folio, abre la ficha y guarda el estado de atención. El estado de atención es independiente del pago, que sigue pendiente.

**Escanear código QR** permite activar la cámara o cargar una imagen del QR del comprobante. También puedes escribir el folio. La lectura de imágenes funciona sin internet; la cámara depende de permisos y de un contexto seguro compatible (HTTPS o localhost). El QR solo localiza un registro existente: escanearlo desde otro dispositivo no transfiere los pacientes ni sincroniza datos. Los códigos no incluyen admin/admin ni funcionan como contraseñas.

La sesión del encargado se mantiene en la pestaña hasta cerrar sesión. Se agregó jsQR 1.4.0 para decodificación local de QR, bajo licencia Apache-2.0. La opción Cámara se detiene al cerrar el lector, encontrar un QR o salir de la vista.
