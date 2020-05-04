# Prueba Backend

El objetivo de la prueba es implementar el backend (API + bases de datos), que permita al consumidor del API obtener la información del formulario, para realizar la correspondiente
implementación en el UI, acorde al archivo de excel de ejemplo.

Algunos criterios a tener en cuenta:

* Implementación del API acorde al archivo de excel “Negocio propio Specs” que seencuentra en esta misma carpeta.

* Implementar la tabla o tablas en la base de datos para la consulta de las preguntas y almacenamiento de las respuestas que ingresaría el usuario final.

* Uso de Python/Django (preferiblemente django-rest-framework)


## Instalación

Usar el manejador de paquetes [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install -r requirements.txt
```

## Endpoints
```bash
company/
Lista el registro de todos los campos (Ingresos, costos, gatos) para todas las compañias
```
```bash
company/<int>
Lista el registro de todos los campos (Ingresos, costos, gatos) para una compañia especifica
```
```bash
company_ss/<int>
Lista el registro de todos los campos (Aporte a seguridad social) para una compañia especifica
```


