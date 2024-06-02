import os
from dotenv import load_dotenv

load_dotenv()

TASK_CHANNEL_IDS = [
    os.getenv('KEISUKE_TASK_CHANNEL_ID'),
    os.getenv('INOWORL_TASK_CHANNEL_ID'),
]
