import pyttsx3
engine = pyttsx3.init()
engine.setProperty('voice', 'es')

texto = """
fabio con ese ojo asi tiene es una teta bionica
"""
engine.save_to_file(texto, r'D:\Escritorio\audio_sora.mp3')
engine.runAndWait()