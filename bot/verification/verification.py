from discord.ext import commands
from .application_buttons import *
from ..config import *


class Questions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        view = discord.ui.View(timeout=None)
        view.add_item(ToFirstCandidate(self.bot))
        view.add_item(ToSecondCandidate(self.bot))
        view.add_item(ToAllCandidates(self.bot))
        self.bot.add_view(view)

        guild = self.bot.get_guild(AUCTION_GUILD)

        for user in guild.members:
            view = discord.ui.View(timeout=None)
            view.add_item(ApproveQuestButton(self.bot, user))
            view.add_item(DenyQuestButton(self.bot, user))
            self.bot.add_view(view)

    @commands.command()
    async def question(self, ctx):
        await ctx.message.delete()
        view = discord.ui.View(timeout=None)
        view.add_item(ToFirstCandidate(self.bot))
        view.add_item(ToSecondCandidate(self.bot))
        view.add_item(ToAllCandidates(self.bot))
        self.bot.add_view(view)

        text = '**Wybierz, do kogo chcesz zadać swoje pytanie:**'
        embed = discord.Embed(description=text, colour=0x001437)

        await ctx.send(embed=embed, view=view)
        logger.info("Wiadomość Question wysłana")


class Verification(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        view = discord.ui.View(timeout=None)
        view.add_item(VerifyStudentButton(self.bot))
        view.add_item(VerifyGraduateButton(self.bot))
        view.add_item(VerifyTeacherButton(self.bot))
        self.bot.add_view(view)

        guild = self.bot.get_guild(AUCTION_GUILD)
        unverified = {
            0: guild.get_role(UNVERIFIED_ROLES[0]).members,
            1: guild.get_role(UNVERIFIED_ROLES[1]).members
        }

        for user_type in unverified:
            for user in unverified[user_type]:
                view = discord.ui.View(timeout=None)
                view.add_item(ApproveButton(self.bot, user.id, user_type))
                view.add_item(DenyButton(self.bot, user.id, user_type))
                self.bot.add_view(view)

    @commands.command()
    async def post(self, ctx):
        await ctx.message.delete()
        view = discord.ui.View(timeout=None)
        view.add_item(VerifyStudentButton(self.bot))
        view.add_item(VerifyGraduateButton(self.bot))
        view.add_item(VerifyTeacherButton(self.bot))

        text = '**Witaj w systemie weryfikacji uczestników debaty 2023/2024!\n\n' \
               'Aby się zweryfikować, wybierz swoją kategorię wciskając odpowiedni przycisk:**'
        embed = discord.Embed(description=text, colour=0x001437)

        await ctx.send(embed=embed, view=view)
        logger.info("Wiadomość Post wysłana")
