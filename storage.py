"""Storage, demo data, and shared lists for GameGuild."""

import hashlib
import json
from models import Player, Guide, HelpRequest, TeamRequest, TeamInvite, FriendRequest, FriendMessage

DATA_FILE = "game_guild_v6.json"
players = []
guides = []
help_requests = []
teams = []
invites = []
friend_requests = []
messages = []
current = ""


def split_list(text):
    result = []
    for item in text.split(","):
        item = item.strip()
        if item != "":
            result.append(item)
    return result


def combine_list(items, separator):
    text = ""
    for i in range(len(items)):
        if i > 0:
            text = text + separator
        text = text + str(items[i])
    return text


def ask_yes_no(text):
    answer = input(text).strip().lower()
    return answer in ["y", "yes", "true"]


def hash_password(password):
    salted = "gameguild:" + password
    return hashlib.sha256(salted.encode()).hexdigest()


def find_player(name):
    for player in players:
        if player.name.lower() == name.lower():
            return player
    return None


def player_to_dict(player):
    return {
        "name": player.name,
        "games": player.games,
        "playstyle": player.playstyle,
        "skill_level": player.skill_level,
        "availability": player.availability,
        "language": player.language,
        "region": player.region,
        "looking_for_team": player.looking_for_team,
        "bio": player.bio,
        "credits": player.credits,
        "earnings": player.earnings,
        "password_hash": player.password_hash,
        "friends": player.friends,
    }


def guide_to_dict(guide):
    return {
        "game": guide.game,
        "title": guide.title,
        "category": guide.category,
        "difficulty": guide.difficulty,
        "tags": guide.tags,
        "content": guide.content,
        "author": guide.author,
        "likes": guide.likes,
        "comments": guide.comments,
        "created": guide.created,
        "tips": guide.tips,
    }


def help_request_to_dict(request):
    return {
        "game": request.game,
        "title": request.title,
        "description": request.description,
        "tags": request.tags,
        "author": request.author,
        "reward": request.reward,
        "status": request.status,
        "replies": request.replies,
        "best_reply": request.best_reply,
        "created": request.created,
    }


def team_to_dict(team):
    return {
        "team_id": team.team_id,
        "game": team.game,
        "mode": team.mode,
        "time": team.time,
        "message": team.message,
        "author": team.author,
        "skill_level": team.skill_level,
        "language": team.language,
        "region": team.region,
        "max_members": team.max_members,
        "members": team.members,
        "status": team.status,
    }


def invite_to_dict(invite):
    return {
        "from_player": invite.from_player,
        "to_player": invite.to_player,
        "game": invite.game,
        "message": invite.message,
        "status": invite.status,
        "created": invite.created,
        "team_id": invite.team_id,
    }


def friend_request_to_dict(request):
    return {
        "from_player": request.from_player,
        "to_player": request.to_player,
        "message": request.message,
        "status": request.status,
        "created": request.created,
    }


def message_to_dict(message):
    return {
        "from_player": message.from_player,
        "to_player": message.to_player,
        "text": message.text,
        "created": message.created,
        "read": message.read,
        "reply_to": getattr(message, "reply_to", ""),
    }


def dict_to_player(data):
    return Player(
        data.get("name", ""),
        data.get("games", []),
        data.get("playstyle", "casual"),
        data.get("skill_level", "beginner"),
        data.get("availability", "flexible"),
        data.get("language", "English"),
        data.get("region", "Global"),
        data.get("looking_for_team", True),
        data.get("bio", ""),
        data.get("credits", 100),
        data.get("earnings", 0),
        data.get("password_hash", ""),
        data.get("friends", []),
    )


def dict_to_guide(data):
    return Guide(
        data.get("game", ""),
        data.get("title", ""),
        data.get("category", "General"),
        data.get("difficulty", "Any"),
        data.get("tags", []),
        data.get("content", data.get("tip", "")),
        data.get("author", ""),
        data.get("likes", 0),
        data.get("comments", []),
        data.get("created", "Unknown"),
        data.get("tips", []),
    )


def dict_to_help_request(data):
    return HelpRequest(
        data.get("game", ""),
        data.get("title", ""),
        data.get("description", ""),
        data.get("tags", []),
        data.get("author", ""),
        data.get("reward", 0),
        data.get("status", "open"),
        data.get("replies", []),
        data.get("best_reply", -1),
        data.get("created", "Unknown"),
    )


def dict_to_team(data):
    return TeamRequest(
        data.get("game", ""),
        data.get("mode", ""),
        data.get("time", ""),
        data.get("message", ""),
        data.get("author", ""),
        data.get("skill_level", "any"),
        data.get("language", "any"),
        data.get("region", "any"),
        data.get("max_members", 4),
        data.get("members", []),
        data.get("status", "open"),
        data.get("team_id", ""),
    )


def dict_to_invite(data):
    return TeamInvite(
        data.get("from_player", ""),
        data.get("to_player", ""),
        data.get("game", ""),
        data.get("message", ""),
        data.get("status", "pending"),
        data.get("created", "Unknown"),
        data.get("team_id", ""),
    )


def dict_to_friend_request(data):
    return FriendRequest(
        data.get("from_player", ""),
        data.get("to_player", ""),
        data.get("message", ""),
        data.get("status", "pending"),
        data.get("created", "Unknown"),
    )


def dict_to_message(data):
    return FriendMessage(
        data.get("from_player", ""),
        data.get("to_player", ""),
        data.get("text", ""),
        data.get("created", "Unknown"),
        data.get("read", False),
        data.get("reply_to", ""),
    )


def save_data():
    data = {
        "current": current,
        "players": [],
        "guides": [],
        "help_requests": [],
        "teams": [],
        "invites": [],
        "friend_requests": [],
        "messages": [],
    }
    for player in players:
        data["players"].append(player_to_dict(player))
    for guide in guides:
        data["guides"].append(guide_to_dict(guide))
    for request in help_requests:
        data["help_requests"].append(help_request_to_dict(request))
    for team in teams:
        data["teams"].append(team_to_dict(team))
    for invite in invites:
        data["invites"].append(invite_to_dict(invite))
    for request in friend_requests:
        data["friend_requests"].append(friend_request_to_dict(request))
    for message in messages:
        data["messages"].append(message_to_dict(message))

    file = open(DATA_FILE, "w")
    json.dump(data, file, indent=2)
    file.close()
    print("Saved to", DATA_FILE)


def load_data():
    global current, players, guides, help_requests, teams, invites, friend_requests, messages
    try:
        file = open(DATA_FILE)
        data = json.load(file)
        file.close()
    except FileNotFoundError:
        return
    except json.JSONDecodeError:
        print("Saved data could not be read. Loading an empty workspace.")
        return

    current = data.get("current", "")
    players = []
    guides = []
    help_requests = []
    teams = []
    invites = []
    friend_requests = []
    messages = []
    for item in data.get("players", []):
        players.append(dict_to_player(item))
    for item in data.get("guides", []):
        guides.append(dict_to_guide(item))
    for item in data.get("help_requests", []):
        help_requests.append(dict_to_help_request(item))
    for item in data.get("teams", []):
        teams.append(dict_to_team(item))
    for item in data.get("invites", []):
        invites.append(dict_to_invite(item))
    for item in data.get("friend_requests", []):
        friend_requests.append(dict_to_friend_request(item))
    for item in data.get("messages", []):
        messages.append(dict_to_message(item))


def demo_comments(*items):
    comments = []
    for item in items:
        comments.append({"author": item[0], "text": item[1]})
    return comments


def demo_tips(*items):
    tips = []
    for item in items:
        tips.append({"from": item[0], "amount": item[1], "message": item[2]})
    return tips


def demo_data():
    global current, players, guides, help_requests, teams, invites, friend_requests, messages
    current = "Carl"
    players = [
        Player("Carl", ["Minecraft", "Valorant"], "support", "intermediate", "weekends", "English", "Australia", True, "Enjoys calm teamwork, safe base design, and guide writing.", 120, 5, hash_password("1234"), ["Mia", "Thor"]),
        Player("Mia", ["Minecraft", "Stardew Valley"], "builder", "intermediate", "weekends", "English", "Australia", True, "Creative builder who publishes beginner-friendly building guides.", 95, 26, hash_password("1234"), ["Carl"]),
        Player("Thor", ["Valorant", "Apex Legends"], "duelist", "advanced", "weeknights", "English", "Australia", True, "Competitive FPS player who likes clear comms and review notes.", 110, 12, hash_password("1234"), ["Ari", "Carl"]),
        Player("Luna", ["Minecraft", "Terraria"], "explorer", "beginner", "weekends", "English", "New Zealand", True, "New player looking for friendly survival groups and readable guides.", 80, 0, hash_password("1234")),
        Player("Ari", ["League of Legends", "Valorant"], "strategist", "advanced", "evenings", "English", "Singapore", False, "Writes macro strategy notes and prefers ranked analysis.", 100, 0, hash_password("1234"), ["Thor"]),
    ]
    guides = [
        Guide(
            "Minecraft",
            "Ultimate Starter Base Design",
            "Building",
            "Beginner",
            ["survival", "base", "storage", "farms"],
            "Start with a small square base, add torches outside every few blocks, keep storage near the entrance, and protect farms with fences. This makes the first nights safer and gives the team a clear shared home.",
            "Mia",
            28,
            demo_comments(("Carl", "Great for new survival teams."), ("Luna", "The lighting tip helped a lot.")),
            "2026-05-20",
            demo_tips(("Carl", 10, "This saved our first night."), ("Luna", 8, "Beginner friendly and clear.")),
        ),
        Guide(
            "Minecraft",
            "Team Mining Route Plan",
            "Co-op",
            "Intermediate",
            ["mining", "resources", "teamwork"],
            "Split the team into a torch carrier, miner, and chest runner. Mark every branch with signs so nobody gets lost. Bring extra food before going below deep caves.",
            "Carl",
            14,
            demo_comments(("Mia", "Good role split for small squads.")),
            "2026-05-21",
            demo_tips(("Mia", 5, "Useful for planning a group run.")),
        ),
        Guide(
            "Valorant",
            "Calm Ranked Routine",
            "Competitive",
            "Intermediate",
            ["ranked", "warmup", "communication"],
            "Warm up aim for ten minutes, call simple information, and reset mentally after each round. Do not argue during buy phase; save review comments for after the match.",
            "Thor",
            31,
            demo_comments(("Ari", "Useful mindset advice.")),
            "2026-05-21",
            demo_tips(("Ari", 12, "Good ranked reminder.")),
        ),
        Guide(
            "Valorant",
            "Support Role Checklist",
            "Roles",
            "Advanced",
            ["support", "utility", "teamplay"],
            "Track teammate positions before using utility. A support player should help entries, trade safely, and keep voice calls short. Good support makes ranked duos more stable.",
            "Carl",
            17,
            [],
            "2026-05-22",
            [],
        ),
        Guide(
            "Stardew Valley",
            "Cozy Farm Layout for Two Players",
            "Planning",
            "Beginner",
            ["farm", "co-op", "layout"],
            "Put crops near the house, animals near the south path, and shared chests beside the shipping bin. This keeps co-op chores easy to divide.",
            "Mia",
            12,
            [],
            "2026-05-22",
            demo_tips(("Carl", 8, "Nice layout idea.")),
        ),
    ]
    help_requests = [
        HelpRequest(
            "Minecraft",
            "How can I stop mobs entering my starter base?",
            "I followed a basic base guide, but zombies still get near the door at night. I need simple beginner advice for lighting and entrance safety.",
            ["survival", "base", "mobs", "beginner"],
            "Luna",
            12,
            "open",
            [
                {"author": "Mia", "text": "Place torches outside the door and use a fence gate or two-door entrance so mobs cannot walk straight in.", "created": "2026-05-23"},
            ],
            -1,
            "2026-05-23",
        ),
        HelpRequest(
            "Valorant",
            "How do I stay calm after losing pistol round?",
            "Our ranked duo tilts quickly after the first round. I want a simple reset routine that works during the match.",
            ["ranked", "mindset", "communication"],
            "Carl",
            8,
            "solved",
            [
                {"author": "Thor", "text": "Use the next buy phase only for information: economy, plan, and one short call. Save blame for review after the match.", "created": "2026-05-23"},
            ],
            0,
            "2026-05-23",
        ),
    ]
    teams = [
        TeamRequest("Valorant", "ranked duo", "Friday 19:30", "Looking for a support player with calm comms.", "Thor", "advanced", "English", "Australia", 2, ["Thor"], "open", "team-1"),
        TeamRequest("Minecraft", "survival build", "Saturday 20:00", "Building a shared starter village from Mia's base guide. Builders and explorers welcome.", "Mia", "intermediate", "English", "Australia", 0, ["Mia"], "open", "team-2"),
        TeamRequest("Minecraft", "mining squad", "Sunday 15:00", "Testing Carl's team mining route with a small group.", "Carl", "beginner", "English", "Australia", 0, ["Carl"], "open", "team-3"),
    ]
    invites = [
        TeamInvite("Mia", "Carl", "Minecraft", "Want to build a starter village together?", "pending", "2026-05-23", "team-2"),
    ]
    friend_requests = [
        FriendRequest("Luna", "Carl", "Thanks for the beginner guide. Want to be friends?", "pending", "2026-05-23"),
    ]
    messages = [
        FriendMessage("Mia", "Carl", "I can build tonight if you are online.", "2026-05-23", False),
    ]
