
# Prueba Técnica - Software Engineer MID  
**Empresa:** Jikkosoft S.A.S  
**Postulante:** Jose Rafael Peña Mena  

## 📋 Descripción  
Este repositorio contiene el desarrollo de la prueba técnica para el cargo **Software Engineer MID**.  
El objetivo fue implementar soluciones a tres ejercicios:  
1. **Diseño de esquema de base de datos** para una plataforma de blogs sencilla.  
2. **Función de programación** para encontrar índices de dos números en una lista que sumen un valor objetivo.  
3. **Sistema de gestión de bibliotecas** con clases para libros, bibliotecas y miembros.  

El proyecto está desarrollado con **Python 3** y **Django REST Framework**, utilizando buenas prácticas y un entorno virtual aislado.

---






## Instalación

1. Instalar docker en el equipo que se va a realizar la revisión. https://www.docker.com/
2. Clonar el repositorio

```bash
  git clone https://github.com/joserafaelpm/jikkosoft-mid-test.git
```
3. Abrir una terminal y en la raiz del proyecto ejecutar el comando
```bash
  docker compose up --build
```
4. Cuando se construya el docker correctamente, abrir http://localhost:8000/swagger/
--- 
## API Reference

#### POST login

```http
  POST /api/token/
```

| Parameter | Type     | Description                |  Return   |
| :-------- | :------- | :------------------------- | :---------|
| `username, password` | `string` | { "username": "admin", "password": "Adminpass123" } |{"refresh": "xxxx","access": "xxxx"} |

#### POST refresh

```http
   POST /api/token/refresh/
```

| Parameter | Type     | Description                       | Return   |
| :-------- | :------- | :-------------------------------- |:---------|
| `refresh`      | `string` | **Required**. { "refresh": "xxxx" } |{"refresh": "xxxx","access": "xxxx"} |

---

### Libraries

#### GET libraries
```http
   GET /api/libraries/
```
| Parameter | Description                       | Return   |
| :-------- | :-------------------------------- |:---------|
| `No Parameters` | Lista de bibliotecas |{"status": 200, "data": []} |

#### GET library id
```http
   GET /api/libraries/{id}/detail/
```
| Parameter | Description                       | Return   |
| :-------- | :-------------------------------- |:---------|
| `id` | Biblioteca |{"msg": "", "status": 200, "data": {}} |

#### POST library
```http
   POST /api/libraries/new/
```
| Parameter | Description                       | Return   |
| :-------- | :-------------------------------- |:---------|
| `{"name": "string", "location": "string", "telephone": "stringstri", "email": "user@example.com"}` | Biblioteca |{"msg": "", "status": 201, "data": {}} |

#### PUT library
```http
   PUT /api/libraries/{id}/edit/
```
| Parameter | Description                       | Return   |
| :-------- | :-------------------------------- |:---------|
| `id & {"name": "string", "location": "string", "telephone": "stringstri", "email": "user@example.com"}` | Biblioteca |{"msg": "", "status": 200, "data": {}} |

#### DELETE library id
```http
   DELETE /api/libraries/{id}/delete/
```
| Parameter | Description                       | Return   |
| :-------- | :-------------------------------- |:---------|
| `id` | Biblioteca |{"msg": "", "status": 200, "data": {}} |

---

### Books

#### GET books
```http
   GET /api/books/
```
| Parameter | Description                       | Return   |
| :-------- | :-------------------------------- |:---------|
| `No Parameters` | Lista de libros |{"status": 200, "data": []} |

#### GET book id
```http
   GET /api/books/{id}/detail/
```
| Parameter | Description                       | Return   |
| :-------- | :-------------------------------- |:---------|
| `id` | Libro |{"msg": "", "status": 200, "data": {}} |

#### POST book
```http
   POST /api/books/new/
```
| Parameter | Description                       | Return   |
| :-------- | :-------------------------------- |:---------|
| `{"library": int, "name": "string","author": "string", "published_date": "YYYY-MM-DD", "isbn": "string", "language": "string", "items_available": int}` | Libro |{"msg": "", "status": 201, "data": {}} |

#### PUT book
```http
   PUT /api/books/{id}/edit/
```
| Parameter | Description                       | Return   |
| :-------- | :-------------------------------- |:---------|
| `id & {"library": int, "name": "string","author": "string", "published_date": "YYYY-MM-DD", "isbn": "string", "language": "string", "items_available": int}` | Libro |{"msg": "", "status": 200, "data": {}} |

#### DELETE book id
```http
   DELETE /api/books/{id}/delete/
```
| Parameter | Description                       | Return   |
| :-------- | :-------------------------------- |:---------|
| `id` | Libro |{"msg": "", "status": 200, "data": {}} |

---

### Memebers

#### GET members
```http
   GET /api/members/
```
| Parameter | Description                       | Return   |
| :-------- | :-------------------------------- |:---------|
| `No Parameters` | Lista de miembros |{"status": 200, "data": []} |

#### GET member id
```http
   GET /api/members/{id}/detail/
```
| Parameter | Description                       | Return   |
| :-------- | :-------------------------------- |:---------|
| `id` | Miembro |{"msg": "", "status": 200, "data": {}} |

#### POST member
```http
   POST /api/members/new/
```
| Parameter | Description                       | Return   |
| :-------- | :-------------------------------- |:---------|
| `{ "library": int, "password": "string", "username": "string", "email": "user@example.com", "first_name": "string" "last_name": "string"}` | Miembro |{"msg": "", "status": 201, "data": {}} |

#### PUT member
```http
   PUT /api/members/{id}/edit/
```
| Parameter | Description                       | Return   |
| :-------- | :-------------------------------- |:---------|
| `id & { "library": int, "password": "string", "username": "string", "email": "user@example.com", "first_name": "string" "last_name": "string"}` | Miembro |{"msg": "", "status": 200, "data": {}} |

#### DELETE member id
```http
   DELETE /api/members/{id}/delete/
```
| Parameter | Description                       | Return   |
| :-------- | :-------------------------------- |:---------|
| `id` | Miembro |{"msg": "", "status": 200, "data": {}} |

---

### Managements

#### GET managements
```http
   GET /api/managements/
```
| Parameter | Description                       | Return   |
| :-------- | :-------------------------------- |:---------|
| `No Parameters` | Lista de gestiones |{"status": 200, "data": []} |

#### GET member id
```http
   GET /api/managements/{id}/detail/
```
| Parameter | Description                       | Return   |
| :-------- | :-------------------------------- |:---------|
| `id` | Gestión |{"msg": "", "status": 200, "data": {}} |

#### POST member
```http
   POST /api/managements/new/
```
| Parameter | Description                       | Return   |
| :-------- | :-------------------------------- |:---------|
| `{"member": int,"book": int}` | Miembro |{"msg": "", "status": 201, "data": {}} |

#### PUT member
```http
   PUT /api/managements/{id}/edit/
```
| Parameter | Description                       | Return   |
| :-------- | :-------------------------------- |:---------|
| `id & {"member": int,"book": int}` | Gestión |{"msg": "", "status": 200, "data": {}} |

#### DELETE member id
```http
   DELETE /api/managements/{id}/delete/
```
| Parameter | Description                       | Return   |
| :-------- | :-------------------------------- |:---------|
| `id` | Gestión |{"msg": "", "status": 200, "data": {}} |


## Usuarios para pruebas

con el siguiente usuario podra realizar el login y realizar las pruebas pertinentes

```bash
{
    "username": "admin",
	"password": "Adminpass123"
}
```
depues de realizado obtendra el token, cada vez que lo use debe ir antes la palabra Bearer

```bash
Bearer token 
```

## Documentation

[Documentation swagger](http://localhost:8000/swagger/)

