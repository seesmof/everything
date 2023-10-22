from twitchio.ext import commands
from archive.vars import *
from archive.mfs import *
import asyncio


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(token=GPT_TOKEN,
                         prefix='!', initial_channels=['seesmof', 'PixelFedya', 'k3ned1', 'unjustfridgesmod'])
        self.lock = asyncio.Lock()

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        async with self.lock:
            letters = ["@piprly", "@wuyodo"]
            if check_for_letters(message.content.lower(), letters) and message.author.name != "piprly":
                if message.channel.name == "k3ned1":
                    if message.author.name == "k3ned1":
                        output_text = generate_ai_message(message.content)
                    else:
                        return
                else:
                    output_text = generate_ai_message(message.content)
                output_text = split_long_gpt(output_text)
                for substr in output_text:
                    await message.channel.send(f"{substr} @{message.author.name}")
                    await asyncio.sleep(20)
            write_to_log(message.content, message.author.name,
                         message.channel.name)


bot = Bot()
bot.run()
