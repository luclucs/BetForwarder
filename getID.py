from telethon.sync import TelegramClient

# Configurações da sua conta do Telegram
api_id = 'ID HERE'
api_hash = 'HASH HERE'

async def list_groups_and_channels():
    async with TelegramClient('my_account', api_id, api_hash) as client:
        async for dialog in client.iter_dialogs():
            if dialog.is_group or dialog.is_channel:
                print(f'Nome: {dialog.name}')
                print(f'ID: {dialog.id}')
                print('---')

if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(list_groups_and_channels())
