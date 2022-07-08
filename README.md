# ec_getlayawaylist

## Descripción

microservicio por el cual el usuario pueda consultar los cómics que actualmente
tiene en su sistema de apartado, se deberá de cumplir con los siguientes criterios:

- CA1: Solo a los usuarios previamente registrados se les permitirá consultar el registro personal de cómics apartados.
- CA2: Se les permitirá acceder a todos los registros personales, pero a su vez los usuarios podrán agregar filtros de
  ordenamiento a la búsqueda (por fecha, personaje u orden alfabético del cómic).

## Requerimientos

- [python 3.9 o mayor](https://www.python.org/)
- [ms_users](https://github.com/RicardoPizano/ec_users)

## Instalación

### Local

#### virtualenv (Opcional)

instalar virtualenv

``` bash 
$ pip3 install virtualenv 
``` 

crear virtualenv

``` bash 
$ virtualenv venv 
``` 

activar virtualenv

- linux

``` bash 
$ ./venv/bin/activate
``` 

- windows

``` bash 
$ ./venv/Scripts/activate
``` 

#### Dependencias

instalacion de dependencias

``` bash 
$ pip3 install -r requirements.tx
``` 

#### Ejecutar

``` bash 
$ python3 main.py
``` 

### Docker

#### Descargar imagen

``` bash
$ docker pull ec_getlayawaylist:latest
```

#### Crear contenedor

``` bash
$ docker run -d -p ${puerto}:80 --name container_ec_getlayawaylist ec_getlayawaylist 
```

## Edpoints

## /addToLayaway

#### GET

``` json
auth:
 En el header de la peticion mandar el token del usuario en formato Bearer
  Authorization : Bearer {user_token}
 
body response:
[
    {
        "id": int,
        "title": "string",
        "image": "string",
        "onsaleDate": "string"
    }
]
```

##### Para mayor información una vez ejecutando el proyecto entrar a la url: `{base_url}/docs`
