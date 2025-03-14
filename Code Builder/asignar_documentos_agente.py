import os
import requests

# Configuración de la API del agente
API_URL = 'https://api.agente.com/v1/asignar_documento'
API_KEY = 'your_api_key_here'

def asignar_documento_agente(nombre_documento, contenido_documento, agente_id):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }
    data = {
        'agent_id': agente_id,
        'document_name': nombre_documento,
        'document_content': contenido_documento
    }
    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code == 200:
        print(f"Documento '{nombre_documento}' asignado exitosamente al agente {agente_id}.")
    else:
        print(f"Error al asignar el documento '{nombre_documento}': {response.status_code} - {response.text}")

if __name__ == '__main__':
    carpeta_textos = 'ruta/a/carpeta_textos'
    agente_id = 'your_agent_id_here'

    # Asignar todos los archivos de texto al agente
    for nombre_archivo in os.listdir(carpeta_textos):
        if nombre_archivo.endswith('.txt'):
            ruta_archivo = os.path.join(carpeta_textos, nombre_archivo)
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo_texto:
                contenido = archivo_texto.read()
                asignar_documento_agente(nombre_archivo, contenido, agente_id)