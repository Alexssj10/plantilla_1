import os
import shutil

def remove_file(file_path):
    """Elimina un archivo si existe."""
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"El archivo {file_path} ha sido eliminado.")
    else:
        print(f"El archivo {file_path} no existe.")

def create_gitignore():
    """Crea un archivo .gitignore básico."""
    gitignore_content = """
    # Python
    __pycache__/
    *.pyc
    *.pyo
    *.pyd
    .env/
    .venv/
    """
    with open(".gitignore", "w") as f:
        f.write(gitignore_content)
        print(".gitignore ha sido creado.")

def post_gen():
    """Este es el script que se ejecutará después de generar el proyecto."""
    
    # Ejemplo: Eliminar archivos innecesarios después de la generación
    remove_file("README.md")
    
    # Ejemplo: Crear un archivo .gitignore
    create_gitignore()
    
    # Otros scripts personalizados pueden ir aquí

# Ejecutar la función
