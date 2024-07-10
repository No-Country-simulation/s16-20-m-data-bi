#!/bin/bash

# Crear directorios principales
mkdir -p data/{raw,processed,external,webapp}
mkdir -p notebooks
mkdir -p src/{data,features,models,visualization}
mkdir -p tests
mkdir -p reports/figures

# Crear archivos iniciales
touch environment.yml
touch .gitignore
touch README.md
touch estructura.txt

# Mensaje de finalización
echo "Estructura del proyecto creada con éxito."

# Opcional: Inicializar un repositorio Git
git add .
git commit -m "Repositorio estructurado"
git push origin github-config
echo "Repositorio Git actualizado."