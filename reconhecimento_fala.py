#pip install SpeechRecognition
#pyaudio, digite no google "install pyaudio seu_sistema_operacional" - 
# pip install pipwin
# pipwin install pyaudio - pip install pyaudio
from cgitb import text
import speech_recognition as sr
#essa biblioteca reconhece frases precisando do silencio no início e no fim do código para que ela reconheça o inicio e o fim da frase

rec = sr.Recognizer()

#print(sr.Microphone().list_microphone_names()) # printa a lista de microfones existentes no computador
# sr.Microphone() - recebe como parametro o indice do microfone que será utilizado
with sr.Microphone(1) as mic:
    #ajusta o microfone para não captar som ambiente
    rec.adjust_for_ambient_noise(mic)
    print('Pode falar que eu vou gravar')
    #grava o audio
    audio = rec.listen(mic)
    # faz o reconhecimento do audio e passa para texto
    #           biblioteca do google
    texto = rec.recognize_google(audio, language="pt-BR")
    print(texto)
