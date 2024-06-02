# thread_creation.py
import discord

async def create_thread(bot, message):
    content = message.content.replace(f'@{bot.user.name}', '').strip()
    lines = content.split('\n')
    print(lines)
    thread_name = lines[1].strip()  # スレッド名を取得
    tasks = lines[1:]  # タスクのリストを取得

    # スレッドを作成
    thread = await message.channel.create_thread(name=thread_name, type=discord.ChannelType.public_thread, auto_archive_duration=10080)  # スレッドをオープンにするために auto_archive_duration を設定

    # タスクをスレッドに送信
    for task in tasks:
        if task.startswith('・'):
            message = await thread.send('### ' + task)
