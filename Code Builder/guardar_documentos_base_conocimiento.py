import os
import json
import requests

# Configuración de la API de CodeGPT
API_URL = 'https://api.codegpt.com/v1/documents'
API_KEY = 'your_api_key_here'

def guardar_documento_base_conocimiento(nombre_documento, contenido_documento):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }
    data = {
        'name': nombre_documento,
        'content': contenido_documento
    }
    response = requests.post(API_URL, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        print(f"Documento '{nombre_documento}' guardado exitosamente en la base de conocimiento.")
    else:
        print(f"Error al guardar el documento '{nombre_documento}': {response.status_code} - {response.text}")

if __name__ == '__main__':
    carpeta_textos = 'ruta/a/carpeta_textos'

    # Guardar todos los archivos de texto en la base de conocimiento
    for nombre_archivo in os.listdir(carpeta_textos):
        if nombre_archivo.endswith('.txt'):
            ruta_archivo = os.path.join(carpeta_textos, nombre_archivo)
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo_texto:
                contenido = archivo_texto.read()
                guardar_documento_base_conocimiento(nombre_archivo, contenido)