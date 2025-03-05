# Conversor de Texto a Voz

Un script simple en Python que convierte texto a voz utilizando la biblioteca pyttsx3.

## Descripción

Este script utiliza la biblioteca pyttsx3 para convertir texto en un archivo de audio MP3. Está configurado para usar una voz en español para la conversión de texto a voz.

## Requisitos

- Python 3.x
- Biblioteca pyttsx3

## Instalación

Instala la biblioteca requerida usando pip:

```bash
pip install pyttsx3
```

## Uso

1. Establece tu texto en la variable `texto`.
2. Modifica la ruta de salida en `save_to_file()` a la ubicación deseada.
3. Ejecuta el script:

```bash
python texto_a_voz.py
```

## Explicación del Código

```python
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('voice', 'es')

texto = """
fabio con ese ojo asi tiene es una teta bionica
"""
engine.save_to_file(texto, r'D:\Escritorio\audio_sora.mp3')
engine.runAndWait()
```

- `import pyttsx3`: Importa la biblioteca de texto a voz.
- `engine = pyttsx3.init()`: Inicializa el motor TTS.
- `engine.setProperty('voice', 'es')`: Establece la voz en español.
- `texto = """..."""`: Define el texto que se convertirá.
- `engine.save_to_file(texto, r'D:\Escritorio\audio_sora.mp3')`: Guarda la voz como un archivo MP3 en la ruta especificada.
- `engine.runAndWait()`: Espera a que la voz se complete antes de salir.

## Personalización

- Para cambiar la voz, modifica el valor `'es'` a otro código de idioma.
- Las voces disponibles se pueden listar con:

```python
voices = engine.getProperty('voices')
for voice in voices:
    print(voice.id)
```

- También puedes ajustar la velocidad y el volumen:

```python
engine.setProperty('rate', 150)    # Velocidad (por defecto es 200)
engine.setProperty('volume', 0.9)  # Volumen (0.0 a 1.0)
```

## Nota

Asegúrate de que el directorio de salida exista antes de ejecutar el script.
