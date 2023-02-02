from ..config import *

from logzero import logger
import os
import pathlib
path = pathlib.Path(__file__).parents[2].absolute()


class ApproveButton(discord.ui.Button):
    def __init__(self, bot, user_id, user_type):
        self.bot = bot
        self.user_id = int(user_id)
        self.guild = bot.get_guild(AUCTION_GUILD)
        self.user_type = user_type

        super().__init__(label="Zatwierdź", style=discord.enums.ButtonStyle.green, custom_id=f'{user_id}_approve')

    async def callback(self, interaction: discord.Interaction):
        if self.guild.get_role(VERIFIER_ROLE) not in interaction.user.roles:
            await interaction.response.send_message(':x: **Nie masz uprawnień by weryfikować użytkowników!**', ephemeral=True)
            logger.warning("Nie masz uprawnień by weryfikować użytkowników (nie mam jak sprawdzić kim jesteś)")
            return

        user = self.guild.get_member(self.user_id)
        await user.add_roles(self.guild.get_role(VERIFIED_ROLES[self.user_type]))
        await user.remove_roles(self.guild.get_role(UNVERIFIED_ROLES[self.user_type]))

        description = f'{interaction.message.embeds[0].description}\n\n:white_check_mark: **Zweryfikowane przez {interaction.user.mention}** <t:{int(time.time())}>'
        logger.info(f"Zatwierdził: {interaction.user.display_name}")

        embed = discord.Embed(description=description, color=discord.Color.green())
        await interaction.message.edit(embed=embed, view=discord.ui.View())

        try:
            await user.send(':white_check_mark: **Twoje konto zostało zweryfikowane pomyślnie!**\n'
                            'Dziękujemy za weryfikację i zapraszamy do zadawania pytań.')
        except discord.Forbidden:
            pass


class DenyButton(discord.ui.Button):
    def __init__(self, bot, user_id, user_type):
        self.bot = bot
        self.user_id = user_id
        self.guild = bot.get_guild(AUCTION_GUILD)
        self.user_type = user_type

        super().__init__(label="Odrzuć", style=discord.enums.ButtonStyle.red, custom_id=f'{user_id}_deny')

    async def callback(self, interaction: discord.Interaction):
        if self.guild.get_role(VERIFIER_ROLE) not in interaction.user.roles:
            await interaction.response.send_message(':x: **Nie masz uprawnień by weryfikować użytkowników!**', ephemeral=True)
            logger.warning("Nie masz uprawnień by weryfikować użytkowników (nie mam jak sprawdzić kim jesteś)")
            return

        user = self.guild.get_member(self.user_id)
        await user.remove_roles(self.guild.get_role(UNVERIFIED_ROLES[self.user_type]))

        description = f'{interaction.message.embeds[0].description}\n\n:x: **Odrzucone przez ' \
                      f'{interaction.user.mention}** <t:{int(time.time())}>'
        logger.info(f"Odrzucił: {interaction.user.display_name}")

        embed = discord.Embed(description=description, color=discord.Color.red())
        await interaction.message.edit(embed=embed, view=discord.ui.View())

        try:
            await user.send(':x: **Twój wniosek o weryfikację został odrzucony!**')
            await user.edit(nick=user.name)
        except discord.Forbidden:
            pass


class ApproveQuestButton(discord.ui.Button):
    def __init__(self, bot, user):
        self.bot = bot
        self.user_id = int(user.id)
        self.user = user
        self.guild = bot.get_guild(AUCTION_GUILD)

        super().__init__(label="Zatwierdź", style=discord.enums.ButtonStyle.green, custom_id=f'{self.user_id}_quest_approve')

    async def callback(self, interaction: discord.Interaction):
        if self.guild.get_role(VERIFIER_ROLE) not in interaction.user.roles:
            await interaction.response.send_message(':x: **Nie masz uprawnień by weryfikować pytania!**', ephemeral=True)
            logger.warning(f"Nie masz uprawnień by weryfikować pytania - {interaction.user.display_name}")
            return

        # Writing the question in a formatted way for OBS/VMIX
        onlyfiles = [f for f in os.listdir("questions") if os.path.isfile(os.path.join("questions", f))]
        with open(os.path.join(path, "questions", f"{len(onlyfiles) + 1}.txt"), "w", encoding="utf-8") as f:
            file_text = interaction.message.embeds[0].description.replace("\n", " ").replace("*", "")
            file_text = file_text.replace("Uczeń - ", "")

            file_text = file_text.replace(f"<@{self.user_id}>", f"{self.user.display_name}:")
            file_text = file_text.replace(":):", "):")
            f.write(file_text)

        description = f'Pytanie nr {len(onlyfiles)+1}\n' \
                      f'{interaction.message.embeds[0].description}\n\n:white_check_mark: **Zweryfikowane przez ' \
                      f'{interaction.user.mention}** <t:{int(time.time())}>'

        logger.info(f"Zatwierdził: {interaction.user.display_name}")
        if "Pytanie od Sztabu" not in description:
            embed = discord.Embed(description=description, color=discord.Color.green())
        else:
            embed = discord.Embed(description=description, color=discord.Color.yellow())
        await interaction.message.edit(embed=embed, view=discord.ui.View())

        await self.bot.get_channel(VERIFIED_QUESTION_CHANNEL).send(embed=embed, view=discord.ui.View())


class DenyQuestButton(discord.ui.Button):
    def __init__(self, bot, user):
        self.bot = bot
        self.user_id = int(user.id)
        self.user = user
        self.guild = bot.get_guild(AUCTION_GUILD)

        super().__init__(label="Odrzuć", style=discord.enums.ButtonStyle.red, custom_id=f'{self.user_id}_quest_deny')

    async def callback(self, interaction: discord.Interaction):
        if self.guild.get_role(VERIFIER_ROLE) not in interaction.user.roles:
            await interaction.response.send_message(':x: **Nie masz uprawnień by weryfikować pytania!**', ephemeral=True)
            logger.warning(f"Nie masz uprawnień by weryfikować pytania - {interaction.user.display_name}")
            return

        description = f'{interaction.message.embeds[0].description}\n\n:x: **Odrzucone przez ' \
                      f'{interaction.user.mention}** <t:{int(time.time())}>'
        logger.info(f"Odrzucił: {interaction.user.display_name}")

        embed = discord.Embed(description=description, color=discord.Color.red())
        await interaction.message.edit(embed=embed, view=discord.ui.View())
