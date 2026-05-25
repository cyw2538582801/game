"""Run this file with: python main.py or python main.py --demo."""

import sys
import storage as st
import features as ft


def menu():
    st.load_data()
    while True:
        ft.heading("GameGuild")
        print("0 Help bot")
        print("1 Dashboard  2 Create profile  3 Publish guide  4 Search")
        print("5 Like guide  6 Create team-up  7 Team board")
        print("8 Recommendations  9 Load demo  10 Save and exit")
        c = input("Choose: ").strip()
        if c == "0":
            ft.help_bot()
            continue
        elif c == "1":
            ft.dashboard()
        elif c == "2":
            ft.make_profile()
        elif c == "3":
            ft.add_guide()
        elif c == "4":
            ft.search_guides()
        elif c == "5":
            ft.like_guide()
        elif c == "6":
            ft.add_team()
        elif c == "7":
            ft.show_teams()
        elif c == "8":
            ft.recommend()
        elif c == "9":
            st.demo_data()
            print("Demo loaded.")
        elif c == "10":
            st.save_data()
            break
        else:
            print("Invalid option.")
        input("\nPress Enter...")


def run_demo():
    ft.heading("Demo Step 1: Load Sample Data")
    st.demo_data()
    print("Loaded sample players, guides, and team-up requests.")

    ft.heading("Demo Step 2: View Dashboard")
    ft.dashboard()

    ft.heading("Demo Step 3: Ask Help Bot")
    question = "How do I use this program?"
    print("You:", question)
    print("Bot:")
    print(ft.answer_help(question))

    ft.heading("Demo Step 4: Search for Minecraft Guides")
    ft.search_guides("minecraft", False)

    ft.heading("Demo Step 5: Like a Guide")
    st.guides[0].likes += 1
    print("Liked:", st.guides[0].title)
    print("New likes:", st.guides[0].likes)

    ft.heading("Demo Step 6: Get Recommendations")
    ft.recommend()

    ft.heading("Demo Step 7: View Team-Up Board")
    for t in st.teams:
        print("\nGame:", t.game)
        print("Mode:", t.mode)
        print("Time:", t.time)
        print("Message:", t.message)
        print("Posted by:", t.author)
        print("Members:", st.combine_list(t.members, ", "))

    ft.heading("Demo Step 8: Join a Team-Up")
    team = st.teams[1]
    if st.current not in team.members:
        team.members.append(st.current)
    print(st.current, "joined", team.game, team.mode)
    print("Members:", st.combine_list(team.members, ", "))

    ft.heading("Demo Step 9: Save and Reload Data")
    st.save_data()
    st.players = []
    st.guides = []
    st.teams = []
    st.current = ""
    st.load_data()
    print("Data reloaded from game_guild_data.txt.")
    ft.dashboard()


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        run_demo()
    else:
        menu()
