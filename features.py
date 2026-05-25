"""Interactive features for GameGuild."""

import storage as st
from models import Player, Guide, TeamRequest


HELP_TOPICS = [
    [
        ["how do i use", "how to use", "use this program", "use the program", "operate", "workflow", "what can i do"],
        "A good first-time flow is:\n"
        "1. Choose 2 Create profile and enter your name, favourite games, and playstyle.\n"
        "2. Choose 4 Search to find strategy guides for a game such as Minecraft.\n"
        "3. Choose 5 Like guide if a post is useful.\n"
        "4. Choose 7 Team board to view open squads, then type y and choose a request number to join.\n"
        "5. Choose 8 Recommendations to find guides, players, and team-ups that match your games.\n"
        "6. Choose 10 Save and exit when you are finished.",
    ],
    [
        ["join", "enter team", "team-up board", "minecraft team", "group up", "play together"],
        "To join a team-up:\n"
        "1. Choose 7 Team board.\n"
        "2. Read the open requests, such as Valorant or Minecraft.\n"
        "3. Type y when the program asks if you want to join.\n"
        "4. Enter the request number, for example 2 for the Minecraft team.\n"
        "5. The program will add your player name to that squad.",
    ],
    [
        ["profile", "account", "start"],
        "Choose 2 Create profile, then enter your name, favourite games, and playstyle.",
    ],
    [
        ["guide", "publish", "tip"],
        "Choose 3 Publish guide to share a tip. You need a profile before posting.",
    ],
    [
        ["search", "find", "minecraft", "valorant"],
        "Choose 4 Search, then type a game or keyword such as Minecraft.",
    ],
    [
        ["like", "vote"],
        "Choose 5 Like guide, then enter the number of the guide you found useful.",
    ],
    [
        ["team", "party", "squad"],
        "Choose 6 Create team-up to post a new squad request for a game session.",
    ],
    [
        ["recommend", "match", "suggest"],
        "Choose 8 Recommendations to see guides, team-ups, and players matching your games.",
    ],
    [
        ["demo", "sample"],
        "Choose 9 Load demo to add sample players, guides, and team-up requests.",
    ],
    [
        ["save", "exit", "quit"],
        "Choose 10 Save and exit when you want to store your data in a text file.",
    ],
]


def heading(text):
    print("\n" + "=" * 40)
    print(text)
    print("=" * 40)


def make_profile():
    heading("Create Profile")
    name = input("Name: ").strip()
    games = st.split_list(input("Favourite games: "))
    role = input("Role/playstyle: ").strip()
    if name and games and role:
        st.players.append(Player(name, games, role))
        st.current = name
        print("Profile created.")
    else:
        print("Please fill in all fields.")


def add_guide():
    if st.current == "":
        print("Create a profile first.")
        return
    heading("Publish Guide")
    game = input("Game: ").strip()
    title = input("Title: ").strip()
    tip = input("Tip: ").strip()
    if game and title and tip:
        st.guides.append(Guide(game, title, tip, st.current))
        print("Guide published.")
    else:
        print("Please fill in all fields.")


def show_guide(g):
    print("\nGame:", g.game)
    print("Title:", g.title)
    print("Tip:", g.tip)
    print("Author:", g.author, "| Likes:", g.likes)


def guide_score(item):
    return item[0]


def answer_help(question):
    text = question.lower()
    for topic in HELP_TOPICS:
        keywords = topic[0]
        answer = topic[1]
        for word in keywords:
            if word in text:
                return answer
    return "Try asking about profile, guides, search, likes, teams, recommendations, demo, or saving."


def help_bot():
    heading("Help Bot")
    print("Ask how to use GameGuild.")
    print("Example: How do I use this program?")
    print("Type back, menu, or main to return to the menu.")
    while True:
        question = input("You: ").strip()
        if question.lower() in ["back", "menu", "main", "return", "exit", "quit"]:
            print("Returning to main menu.")
            return
        print("Bot:")
        print(answer_help(question))


def search_guides(keyword=None, offer_like=True):
    heading("Search Guides")
    if keyword is None:
        keyword = input("Keyword: ")
    keyword = keyword.lower().strip()
    results = []
    for g in st.guides:
        mark = g.likes
        if keyword in g.game.lower():
            mark += 3
        if keyword in g.title.lower():
            mark += 2
        if keyword in g.tip.lower():
            mark += 1
        if keyword == "" or mark > g.likes:
            results.append([mark, g])
    results.sort(reverse=True, key=guide_score)
    if not results:
        print("No guides found.")
        return
    number = 1
    for item in results:
        print("\nResult", number)
        show_guide(item[1])
        number += 1
    if offer_like:
        like_search_result(results)


def like_search_result(results):
    answer = input("\nLike one of these guides? (y/n): ").strip().lower()
    if answer != "y":
        return
    try:
        choice = int(input("Result number: "))
        if choice >= 1 and choice <= len(results):
            guide = results[choice - 1][1]
            guide.likes += 1
            print("Liked:", guide.title)
            print("New likes:", guide.likes)
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid choice.")


def like_guide():
    heading("Like Guide")
    if not st.guides:
        print("No guides available.")
        return
    for i in range(len(st.guides)):
        print(i + 1, st.guides[i].title)
    try:
        choice = int(input("Guide number: "))
        if choice >= 1 and choice <= len(st.guides):
            st.guides[choice - 1].likes += 1
            print("Liked.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid choice.")


def add_team():
    if st.current == "":
        print("Create a profile first.")
        return
    heading("Create Team-Up")
    game = input("Game: ").strip()
    mode = input("Mode: ").strip()
    time = input("Time: ").strip()
    msg = input("Message: ").strip()
    if game and mode and time and msg:
        st.teams.append(TeamRequest(game, mode, time, msg, st.current))
        print("Team-up created.")
    else:
        print("Please fill in all fields.")


def show_teams():
    heading("Team-Up Board")
    if not st.teams:
        print("No team-up requests.")
        return
    number = 1
    for t in st.teams:
        print("\nRequest", number)
        print("Game:", t.game)
        print("Mode:", t.mode)
        print("Time:", t.time)
        print("Message:", t.message)
        print("Posted by:", t.author)
        print("Members:", st.combine_list(t.members, ", "))
        number += 1
    join = input("\nJoin a team-up? (y/n): ").strip().lower()
    if join == "y":
        join_team()


def join_team():
    player = st.find_player(st.current)
    if not player:
        print("Create or load a profile first.")
        return
    try:
        choice = int(input("Request number: "))
        if choice >= 1 and choice <= len(st.teams):
            team = st.teams[choice - 1]
            if player.name not in team.members:
                team.members.append(player.name)
                print(player.name, "joined", team.game, team.mode)
            else:
                print("You are already in this team-up.")
        else:
            print("Invalid request number.")
    except ValueError:
        print("Invalid request number.")


def dashboard():
    heading("Dashboard")
    player = st.find_player(st.current)
    if player:
        print("Current player:", player.name)
        print("Games:", st.combine_list(player.games, ", "))
        print("Role:", player.role)
    else:
        print("Current player: none")
    print("Players:", len(st.players), "| Guides:", len(st.guides), "| Teams:", len(st.teams))


def recommend():
    heading("Recommendations")
    player = st.find_player(st.current)
    if not player:
        print("Create a profile first.")
        return
    print("Guides:")
    for g in st.guides:
        if g.game in player.games:
            print("-", g.title, "for", g.game)
    print("Team-ups:")
    for t in st.teams:
        if t.game in player.games:
            print("-", t.game, t.mode, "at", t.time)
    print("Player matches:")
    found = False
    for other in st.players:
        if other.name != player.name:
            shared_games = []
            for game in player.games:
                if game in other.games:
                    shared_games.append(game)
            if shared_games:
                print("-", other.name, "also plays", st.combine_list(shared_games, ", "))
                found = True
    if not found:
        print("No player matches yet.")
