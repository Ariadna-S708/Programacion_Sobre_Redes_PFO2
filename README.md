# Programacion_Sobre_Redes_PFO2

---

## Instalar y ejecutar

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual desde PowerShell (Windows)
.\venv\Scripts\Activate.ps1

# Activar entorno virtual desde CMD (Windows)
venv\Scripts\activate.bat

# Instalar dependencias
pip install flask bcrypt

# Guardar dependencias en requirements.txt
pip freeze > requirements.txt

# Instalar desde requirements.txt
pip install -r requirements.txt

# Ejecutar servidor
python servidor.py
```

---

## Pruebas desde PowerShell

```bash
# Registro
Invoke-RestMethod -Uri http://127.0.0.1:5000/registro -Method POST -ContentType "application/json" -Body '{"username":"juan","password":"1234"}'
```

Posibles respuestas:
- `200` → Registro exitoso
- `400` → Usuario ya existe
- `400` → Faltan campos
- `500` → Error del servidor


```bash
# Login
Invoke-RestMethod -Uri http://127.0.0.1:5000/login -Method POST -ContentType "application/json" -Body '{"username":"juan","password":"1234"}'
```

Posibles respuestas:
- `200` → Login exitoso
- `404` → Usuario no encontrado
- `401` → Contraseña incorrecta
- `400` → Faltan campos


```bash
# Tareas
Invoke-RestMethod -Uri http://127.0.0.1:5000/tareas -Method GET
```

Posbles respuestas:
- Link a la pagina

---

## Notas importantes

- El archivo de base de datos se llama usuarios.db y se crea automáticamente si no existe.
- Las contraseñas se almacenan hasheadas con bcrypt para mayor seguridad.
- Recuerda activar el entorno virtual antes de instalar dependencias y ejecutar el servidor.
- Dependiendo de la consola, activa el entorno virtual con el comando adecuado.