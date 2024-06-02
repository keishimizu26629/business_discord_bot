import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

from thread_creation import create_thread
from reaction_handling import task_check_handling

# .envファイルからTOKENを読み込む
load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
CHANNEL_ID = int(os.getenv('KEISUKE_TASK_CHANNEL_ID'))

# Intentsの設定
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.guilds = True
intents.reactions = True  # リアクションのIntentを追加

# Botの初期設定
bot = commands.Bot(command_prefix='!', intents=intents)

# Botが起動したときに実行されるイベント
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# メッセージを受信したときに実行されるイベント
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    print('test1')
    # メッセージがボットをメンションしているかどうかを確認
    if any(mention.id == bot.user.id for mention in message.mentions):
        if message.channel.id == CHANNEL_ID:
            print('test2')
            await create_thread(bot, message)

    await bot.process_commands(message)

@bot.event
async def on_reaction_add(reaction, user):
    if user == bot.user:
        return

    if isinstance(reaction.message.channel, discord.Thread) and str(reaction.emoji) == '✅':
        await task_check_handling(reaction, user)

# Botを実行
bot.run(TOKEN)
