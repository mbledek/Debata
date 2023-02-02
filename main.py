from abc import ABC
import discord
from discord.ext import commands
from logzero import logfile
import os
import pathlib

from bot.verification import Verification, Questions
from bot.config import TOKEN
path = pathlib.Path(__file__).parent.absolute()

if not os.path.isdir(os.path.join(path, "questions")):
    os.mkdir(os.path.join(path, "questions"))


class Debata(commands.Bot, ABC):
    def __init__(self):
        super().__init__(
            command_prefix=commands.when_mentioned_or('?'),
            intents=discord.Intents.all(),
            auto_sync_commands=True
        )

        self.remove_command('help')
        logfile(os.path.join(path, "verification.log"), encoding='UTF-8')
        self.add_cog(Verification(self))
        self.add_cog(Questions(self))
        self.run(TOKEN)

    async def on_ready(self):
        print(f'We have logged in as {self.user}')


Debata()