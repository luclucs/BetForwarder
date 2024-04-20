from telethon.sync import TelegramClient, events, Message
from telethon import events
import asyncio
import re

# Configurações da sua conta do Telegram
api_id = 'ID HERE'
api_hash = 'HASH HERE'

# Inicialize um conjunto vazio para armazenar os IDs de mensagens copiadas
mensagens_copiadas = set()

ascii_art = """
 ___       ___  ___  ________  ___       ___  ___  ________  ________      
|\  \     |\  \|\  \|\   ____\|\  \     |\  \|\  \|\   ____\|\   ____\     
\ \  \    \ \  \\\  \ \  \___|\ \  \    \ \  \\\  \ \  \___|\ \  \___|_    
 \ \  \    \ \  \\\  \ \  \    \ \  \    \ \  \\\  \ \  \    \ \_____  \   
  \ \  \____\ \  \\\  \ \  \____\ \  \____\ \  \\\  \ \  \____\|____|\  \  
   \ \_______\ \_______\ \_______\ \_______\ \_______\ \_______\____\_\  \ 
    \|_______|\|_______|\|_______|\|_______|\|_______|\|_______|\_________\
                                                               \|_________|
"""

print(ascii_art)

msgInicial = """
#########################################################################################
Inicializando o bot...
#########################################################################################
As apostas serão enviadas ao canal: @ambasmarcam365 e aparecerão no terminal.
#########################################################################################
https://github.com/luclucs
#########################################################################################
Aguardando novas apostas...
"""
print(msgInicial)

# Função para manipular o texto da mensagem
def manipular_texto(texto_original):
    return re.sub(r'Padrão - Tropa Milionária', '💥 MEGABOT AMBAS MARCAM 💥', texto_original)

async def copiar_mensagens():
    async with TelegramClient('conta', api_id, api_hash) as client:
        origem = await client.get_entity("Grupo ou canal de origem, ex: -1001832972582 <- pegue esse id no getID.py")
        destino = await client.get_entity("Grupo ou canal de destino, ex: -1001628172903 <- pegue esse id no getID.py")

        @client.on(events.NewMessage(chats=origem))
        async def handle_new_message(event):
            mensagem = event.message
            if mensagem and isinstance(mensagem, Message):
                texto_original = mensagem.text
                texto_modificado = re.sub(r'Padrão - Tropa Milionária', '💥 MEGABOT AMBAS MARCAM 💥', texto_original)

        # Envie a mensagem com o texto modificado (ou original) para o canal de destino
            mensagem_enviada = await client.send_message(destino, texto_modificado)
            mensagens_copiadas.add(mensagem_enviada.id)  # Adicionar a ID da mensagem enviada


        # Imprima a mensagem enviada no terminal
            print("Bet enviada ao canal:")
            print(texto_modificado)
            print("#########################################################################################\nAguardando novas apostas...")

        @client.on(events.MessageEdited(chats=origem))
        async def handle_message_edit(event):
            mensagem_editada = event.message

            if mensagem_editada.id in mensagens_copiadas:
                mensagem_copiada_id = mensagens_copiadas[mensagem_editada.id]

                texto_original = mensagem_editada.text
                texto_modificado = manipular_texto(texto_original)

                if texto_modificado != texto_original:
                    await mensagem_copiada_id.edit(texto_modificado)
                    print("A bet recebeu uma edição:")
                    print(texto_modificado)
                    print("#########################################################################################\nAguardando novas apostas...")

        await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(copiar_mensagens())
