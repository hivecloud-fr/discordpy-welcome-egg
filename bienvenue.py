import sys

ascii_art = """
  _  _ _          ___ _             _ 
 | || (_)_ _____ / __| |___ _  _ __| |
 | __ | \\ V / -_) (__| / _ \\ || / _` |
 |_||_|_|\\_/\\___|\\___|_\\___/\\_,_\\__,_|
"""

colored_ascii_art = ''.join([
    f'\033[31m{char}\033[0m' if index % 6 == 0 else
    f'\033[32m{char}\033[0m' if index % 6 == 1 else
    f'\033[33m{char}\033[0m' if index % 6 == 2 else
    f'\033[34m{char}\033[0m' if index % 6 == 3 else
    f'\033[35m{char}\033[0m' if index % 6 == 4 else
    f'\033[36m{char}\033[0m' if index % 6 == 5 else char
    for index, char in enumerate(ascii_art)
])

print(colored_ascii_art)
print("""
Bienvenue sur votre hébergement Discord.JS propulsé par \033[34mHiveCloud.FR\033[0m
Pour mettre en place votre instance, connectez-vous via le serveur SFTP en cliquant sur la catégorie "Paramètres".
\033[32mMerci de votre confiance\033[0m !\n\n\033[31m# Liens utiles\033[0m
Site internet: \033[36mhttps://hivecloud.fr/\033[0m
Discord: \033[36mhttps://discord.hivecloud.fr/\033[0m
""")

print("                                            ")
sys.stdin.read(1)