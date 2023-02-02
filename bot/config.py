import discord
import asyncio
import time

# Składnia
first_alt_name = ""  # Imię w dopełniaczu
second_alt_name = ""  # Imię w dopełniaczu

# ID Sztabu kandydatów
first_candidates = 0  # Rola Sztab pierwszego kandydata
second_candidates = 0  # Rola Sztab drugiego kandydata

TOKEN = ''
TEACHER_KEY = ''

# General config
VERIFIER_ROLE = 0  # Rola która weryfikuje
AUCTION_GUILD = 0  # ID serwera

# Verification config
VERIFICATION_CHANNEL = 0  # Kanał na którym będą pojawiać się wiadomości o weryfikacji osób
VERIF_QUEST_CHANNEL = 0  # Kanał na którym będą pojawiać się wiadomości o weryfikacji pytań
VERIFIED_QUESTION_CHANNEL = 0  # Kanał na który będą trafiać zweryfikowane pytania

# Role IDs
#  0 - Student
#  1 - Graduate
#  2 - Teacher
UNVERIFIED_ROLES = [0, 0, 0]
VERIFIED_ROLES = [0, 0, 0]


# List of teacher ids
TEACHERS = []


# User class guilds nickname data
# Structure:
#
# {
# USER_ID: [
#   {'guild': 'GUILD_NAME_1', 'nick': 'NICKNAME_1'},
#   {'guild': 'GUILD_NAME_2', 'nick': 'NICKNAME_2'}, ...
#   ]
# }

STUDENT_DATA = {
}
