from googleapiclient.discovery import build
from google.oauth2 import service_account

# Configuración de la API de Google Drive
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
SERVICE_ACCOUNT_FILE = 'path/to/service_account.json'

def obtener_servicio_drive():
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    servicio = build('drive', 'v3', credentials=creds)
    return servicio

def listar_archivos_drive(servicio, carpeta_id):
    resultados = servicio.files().list(
        q=f"'{carpeta_id}' in parents",
        pageSize=10, fields="files(id, name)").execute()
    archivos = resultados.get('files', [])
    if not archivos:
        print('No se encontraron archivos.')
    else:
        print('Archivos encontrados:')
        for archivo in archivos:
            print(f"{archivo['name']} ({archivo['id']})")
    return archivos

if __name__ == '__main__':
    servicio_drive = obtener_servicio_drive()
    carpeta_id = 'your_folder_id_here'
    listar_archivos_drive(servicio_drive, carpeta_id)