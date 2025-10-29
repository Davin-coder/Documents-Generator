<div align="center">

# Generador de Documentos - Python

<img src="./public/word_logo.png" width="88">
<img src="./public/python_logo.png" width="88" style="margin: 0 0.5rem">
<img src="./public/excel_logo.png" width="88">


### Social Medias 📲

<p align="center" style="margin: 0.7rem 0 0.7rem 0">
    <a href="https://www.linkedin.com/in/davin-coder/" target="_blank">
        <img src="https://img.shields.io/static/v1?message=LinkedIn&logo=linkedin&label=&color=0077B5&logoColor=white&labelColor=&style=for-the-badge" height="25" alt="linkedin logo"  /></a>&nbsp;&nbsp;
    <a href="https://www.instagram.com/davin_coder/" target="_blank">
        <img src="https://img.shields.io/static/v1?message=Instagram&logo=instagram&label=&color=E4405F&logoColor=white&labelColor=&style=for-the-badge" height="25" alt="instagram logo"  /></a>&nbsp;&nbsp;
    <a href="https://github.com/Davin-coder" target="_blank">
        <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" height="25" alt="instagram logo"  /></a>&nbsp;&nbsp;
</p>

</div>

## Introducción

Bienvenido a "**Generador de Documentos - Python**", aquí encontrarás un sistema que se encarga de obtener los datos de un archivo excel, separarlos y generar una carpeta individual con la información de cada registro, a su vez que mediante una plantilla simple con word, se migran todos esos datos a los campos esperados, esta solución busca reducir considerablemente el tiempo gastado en el analisis de estos archivos, a su vez de su correcta separación y evitar errores humanos de por medio.

## Proceso de Ejecución

### 1) Clonar este repositorio
```bash
git clone https://github.com/Davin-coder/Documents-Generator.git
```

### 2) Dirigete al directorio del proyecto
```bash
cd Documents-Generator
```

### 3) Inicia un entorno virtual con Python
```bash
# Puede variar según tu configuración y OS
py -m venv venv
```

### 4) Instalar las dependencias
```bash
# dentro del venv ingresa:
pip install -r requirements.txt
```

### 5) Iniciar el sistema

- **En Windows**
    ```bash
    # dentro del venv ingresa:
    py .\src\cli.py --excel .\data\listado_ejemplo.xlsx --template .\data\plantilla_easy.docx --out .\data\output
    ```

- **En Linux**
    ```bash
    # dentro del venv ingresa:
    python src/cli.py --excel .\data\listado_ejemplo.xlsx --template .\data\plantilla_easy.docx --out .\data\output
    ```

### 6) Respuesta esperada dentro de output (salida)

```bash
output/
├───Ana Martinez/ # Carpeta de la persona con sus archivos generados
├───Andres Ruiz/
├───Camila Torres/
├───Carlos Rodriguez/
├───Daniela Rojas/
├───Diego Lopez/
├───Esteban Gil/
├───Felipe Navarro/
├───Gabriela Ortiz/
├───Jorge Ramirez/
├───Laura Morales/
├───Luis Perez/
├───Maria Gomez/
├───Monica Suarez/
├───Natalia Silva/
├───Paula Medina/
├───Ricardo Pena/
├───Santiago Vargas/
├───Sofia Hernandez/
└───Valentina Castro/
```