import os
import re

def replace_imports_in_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    updated_lines = []
    typing_extensions_added = False

    for line in lines:
        # Reemplazar la línea de importación si contiene TypedDict, Required o NotRequired
        if re.search(r'from typing import.*(TypedDict|Required|NotRequired)', line):
            # Filtrar los elementos que no son TypedDict, Required o NotRequired
            imports = re.findall(r'\b\w+\b', line.split('import')[-1])
            filtered_imports = [imp for imp in imports if imp not in {'TypedDict', 'Required', 'NotRequired'}]

            # Agregar la nueva línea de typing_extensions si no se ha añadido
            if not typing_extensions_added:
                updated_lines.append("from typing_extensions import TypedDict, Required, NotRequired\n")
                typing_extensions_added = True

            # Si quedan otros imports de typing, añadirlos
            if filtered_imports:
                updated_lines.append(f"from typing import {', '.join(filtered_imports)}\n")
            continue

        # Agregar la línea de typing_extensions si no existe y se detecta su uso
        if not typing_extensions_added and re.search(r'\b(TypedDict|Required|NotRequired)\b', line):
            updated_lines.append("from typing_extensions import TypedDict, Required, NotRequired\n")
            typing_extensions_added = True

        updated_lines.append(line)

    # Escribir los cambios en el archivo
    with open(file_path, 'w') as file:
        file.writelines(updated_lines)

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                replace_imports_in_file(os.path.join(root, file))

# Ruta del directorio del proyecto
project_directory = './chargebee'
process_directory(project_directory)