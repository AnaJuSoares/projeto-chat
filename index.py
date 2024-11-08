import os
from groq import Groq

# Defina a chave da APT diretamente no código
os.environ["GROQ_API_KEY"] = "Digite aqui a sua chave de API"

client = Groq(
    api_key=os.environ.get("GROT_API_KEY"),
)

#Inicializa a lista de mensagens para manter o contexto da conversa
message = []

while True:
    usuario = input("Digite uma mensagem ou 'sair' para emcerrar: ")

    if usuario.lower() == 'sair':
        print("Conversa encerrada.")
        break

    #Adiciona a mensagem do usuário a'lista de mensagens
    messages.append({"role": "user", "content"})
