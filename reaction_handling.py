async def task_check_handling(reaction, user):
    message = reaction.message
    content = message.content
    print(f'Original message: {content}')  # 元のメッセージ内容を表示

    strikethrough_content = content.replace('### ', '### ~~') + '~~'
    print(f'Strikethrough message: {strikethrough_content}')  # 打ち消し線が適用されたメッセージ内容を表示

    await message.edit(content=strikethrough_content)
    print('Message edited')  # メッセージが編集されたことを示すメッセージを表示
