#Função para ouvir e reconhecer a fala
# https://letscode.com.br/blog/speech-recognition-com-python
#https://www.youtube.com/watch?v=XmjY-cFbcqw&ab_channel=RonanVico

import speech_recognition as sr
import os

def ouvir_microfone():
    #Habilita o microfone do usuário
    microfone = sr.Recognizer()
    
    #usando o microfone
    with sr.Microphone() as source:
        
        #Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)
        
        #Frase para o usuario dizer algo
        print("Diga alguma coisa: ")
        
        #Armazena o que foi dito numa variavel
        audio = microfone.listen(source)
        
    try:
        
        #Passa a variável para o algoritmo reconhecedor de padroes
        frase = microfone.recognize_google(audio,language='pt-BR')
        
# caso tenha alguma dessas palavras ele irá executar uma ação
        if 'navegador' in frase:
            os.system('start Chrome.exe')

        if 'Excel' in frase:
            os.system('start Excel.exe')

        #Retorna a frase pronunciada
        print("Você disse: " + frase)
        
    #Se nao reconheceu o padrao de fala, exibe a mensagem
    except sr.UnkownValueError:
        print("Não entendi")
        
    return frase

ouvir_microfone()