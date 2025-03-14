import fitz  # PyMuPDF
import os

def convertir_pdf_a_texto(ruta_pdf, ruta_salida):
    # Abrir el archivo PDF
    documento = fitz.open(ruta_pdf)
    texto_completo = ""

    # Iterar sobre cada página del PDF
    for pagina in documento:
        texto_completo += pagina.get_text()

    # Guardar el texto extraído en un archivo de texto
    with open(ruta_salida, 'w', encoding='utf-8') as archivo_texto:
        archivo_texto.write(texto_completo)

    print(f"Texto extraído y guardado en {ruta_salida}")

if __name__ == '__main__':
    carpeta_pdfs = 'ruta/a/carpeta_pdfs'
    carpeta_textos = 'ruta/a/carpeta_textos'

    # Asegurarse de que la carpeta de salida exista
    if not os.path.exists(carpeta_textos):
        os.makedirs(carpeta_textos)

    # Convertir todos los archivos PDF en la carpeta especificada
    for nombre_archivo in os.listdir(carpeta_pdfs):
        if nombre_archivo.endswith('.pdf'):
            ruta_pdf = os.path.join(carpeta_pdfs, nombre_archivo)
            nombre_salida = os.path.splitext(nombre_archivo)[0] + '.txt'
            ruta_salida = os.path.join(carpeta_textos, nombre_salida)
            convertir_pdf_a_texto(ruta_pdf, ruta_salida)