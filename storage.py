"""Data storage, file input/output, and demo data for GameGuild."""

from models import Player, Guide, TeamRequest

DATA_FILE = "game_guild_data.txt"
players = []
guides = []
teams = []
current = ""


def split_list(text):
    result = []
    for item in text.split(","):
        if item.strip() != "":
            result.append(item.strip())
    return result


def combine_list(items, separator):
    text = ""
    for i in range(len(items)):
        if i > 0:
            text = text + separator
        text = text + items[i]
    return text


def find_player(name):
    for player in players:
        if player.name == name:
            return player
    return None


def save_data():
    file = open(DATA_FILE, "w")
    file.write("CURRENT|" + current + "\n")
    for p in players:
        file.write("PLAYER|" + p.name + "|" + combine_list(p.games, ",") + "|" + p.role + "\n")
    for g in guides:
        file.write("GUIDE|" + g.game + "|" + g.title + "|" + g.tip + "|" + g.author + "|" + str(g.likes) + "\n")
    for t in teams:
        members = combine_list(t.members, ",")
        file.write("TEAM|" + t.game + "|" + t.mode + "|" + t.time + "|" + t.message + "|" + t.author + "|" + members + "\n")
    file.close()
    print("Saved.")


def load_data():
    global current, players, guides, teams
    try:
        lines = open(DATA_FILE).readlines()
    except FileNotFoundError:
        return
    players = []
    guides = []
    teams = []
    for line in lines:
        p = line.strip().split("|")
        if p[0] == "CURRENT" and len(p) >= 2:
            current = p[1]
        elif p[0] == "PLAYER" and len(p) == 4:
            players.append(Player(p[1], split_list(p[2]), p[3]))
        elif p[0] == "GUIDE" and len(p) == 6:
            try:
                guides.append(Guide(p[1], p[2], p[3], p[4], int(p[5])))
            except ValueError:
                pass
        elif p[0] == "TEAM" and len(p) == 6:
            teams.append(TeamRequest(p[1], p[2], p[3], p[4], p[5]))
        elif p[0] == "TEAM" and len(p) == 7:
            teams.append(TeamRequest(p[1], p[2], p[3], p[4], p[5], split_list(p[6])))


def demo_data():
    global current, players, guides, teams
    players = []
    guides = []
    teams = []
    current = "Carl"
    players.append(Player("Carl", ["Minecraft", "Valorant"], "support"))
    players.append(Player("Mia", ["Minecraft", "Stardew Valley"], "builder"))
    players.append(Player("Thor", ["Valorant", "Apex Legends"], "duelist"))
    guides.append(Guide("Minecraft", "Starter Base Guide", "Build a safe base with storage.", "Carl", 5))
    guides.append(Guide("Valorant", "Calm Ranked Routine", "Warm up aim and communicate clearly.", "Thor", 7))
    valorant_time = "Friday 19:30"
    minecraft_time = "Saturday 20:00"
    teams.append(TeamRequest("Valorant", "ranked duo", valorant_time, "Looking for support.", "Thor", ["Thor"]))
    teams.append(TeamRequest("Minecraft", "survival build", minecraft_time, "Looking for builders for a new base.", "Mia", ["Mia"]))
