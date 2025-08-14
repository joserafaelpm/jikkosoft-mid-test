# Usamos Python como base
FROM python:3.11-slim

# Variables de entorno para no crear archivos pyc y mostrar logs en consola
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Crear directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    python3-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements y instalar dependencias de Python
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiar todo el proyecto
COPY . .

# Exponer puerto de Django
EXPOSE 8000

# Comando por defecto
CMD ["gunicorn", "api.wsgi:application", "--bind", "0.0.0.0:8000"]