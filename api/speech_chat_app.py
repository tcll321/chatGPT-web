import asyncio
import os

import api
from Speech_and_Text import speech_to_text_baidu

# os.environ.setdefault('API_KEY', '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')
api_key = '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'


async def chat_process():
    print("通过mic输入：")
    text = speech_to_text_baidu(if_microphone=True)
    print(text)

    messages = [{"role": "user", "content": text}]
    message = {'model': 'gpt-3.5-turbo', 'messages': messages}

    res = await api.completions_turbo_l(message, api_key=api_key)
    print(res['choices'][0]['message']['content'])


if __name__ == '__main__':
    while True:
        str_input = input("按t键开始语音输入:")
        if str_input == 't':
            process = chat_process()
            asyncio.run(process)
        if str_input == 'q':
            break

