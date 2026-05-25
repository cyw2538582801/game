GameGuild - README

How to run:
Run the program from main.py.

Command:
python main.py

If python does not work in the terminal, try:
python3 main.py

Main file:
main.py

Project description:
GameGuild is a Python command-line prototype for a gaming social platform.
Users can create a player profile, publish strategy guides, search for game
tips, like useful guides, ask a simple Help Bot how to use the program, receive
recommendations, and join team-up requests for games such as Minecraft and
Valorant.

Files:
main.py
- Starts the program.
- Shows the main menu.
- Runs the automatic demo if the user types python main.py --demo.

models.py
- Contains the Player, Guide, and TeamRequest classes.

storage.py
- Stores the program's lists of players, guides, and team-up requests.
- Loads and saves data using a text file.
- Creates sample demo data.

features.py
- Contains the main features of the program, including profile creation,
  guide publishing, guide search, liking guides, the Help Bot, the Team-Up
  Board, joining team-ups, and recommendations.

Python concepts used:
- Variables and strings
- Lists and multi-dimensional lists
- If, elif, and else statements
- For loops and while loops
- Functions
- Classes and objects
- User input
- Try and except for input validation
- Text file input and output
- Searching and sorting
- Simple recommendation logic

Extra libraries:
No external libraries are required.
The program only uses standard Python.

Suggested demo flow:
1. Run python main.py
2. Choose 0 Help bot and ask: How do I use this program?
3. Type menu to return to the main menu.
4. Choose 9 Load demo.
5. Choose 4 Search and search for minecraft.
6. Like the first search result.
7. Choose 7 Team board.
8. Join request 2, the Minecraft team-up.
9. Choose 8 Recommendations.
10. Choose 10 Save and exit.
