# Verificación de la entrega

Pruebas realizadas en Microsoft Edge, abriendo index.html directamente con file://:

- Flujo completo de solicitud, con validación de datos y consentimiento.
- Suma de BHC + Qs6 + EGO: $1,040 MXN; bloqueo de productos duplicados.
- Persistencia al recargar, historial, comprobante, impresión PDF y generación QR local.
- Lectura, creación de TXT, archivo inexistente, fecha inválida y fecha bisiesta.
- Búsqueda sin resultados y panel móvil del carrito.
- Ausencia de desbordamiento horizontal en las ocho vistas principales, a 390, 768 y 1440 px.
- Acceso del encargado: admin/admin correcto, contraseña incorrecta rechazada, sesión conservada al recargar y cierre de sesión.
- Cola vacía, búsqueda por paciente, ficha de solicitud y estados persistentes En espera → En proceso → Finalizado.
- QR real generado por la aplicación y decodificado desde una imagen para abrir la ficha correcta.
- Folios inválidos y folios inexistentes: mensajes controlados.
- Acceso y panel del doctor revisados a 390, 639, 768 y 1440 px.
- Sin errores JavaScript no controlados durante estas pruebas.

La cámara física no se probó: su disponibilidad depende del navegador, permisos y contexto seguro. Se verificó la lectura QR mediante carga de imagen. La integración opcional WebMCP no se validó mediante invocación. Las pruebas responsive se realizaron con ventanas de navegador, no con dispositivos físicos.
