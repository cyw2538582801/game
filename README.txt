GameGuild Guide-First Prototype - README

How to run:
python main.py

How to run the first Flask web version:
python -m pip install -r requirements.txt
python app.py
Then open:
http://127.0.0.1:5000

Optional automatic demo:
python main.py --demo

Product direction:
GameGuild is now designed as a guide-first gaming social platform. The main
idea is that useful community guides attract players and creators first. After
players find useful knowledge, the platform can recommend related team-ups,
compatible teammates, and eventually AI answers based on the community's posts.
Users now login before using personal features, so each player sees their own
profile, credits, recommendations, team actions, and creator earnings.
Friend and invitation features have also been added so players can keep useful
teammates, send messages, reply from the inbox, and invite several friends into
the same temporary friend squad.
Help Requests have been added so players can ask the community when no guide
solves their problem. Good answers can be marked as the best answer and rewarded
with virtual credits.
Help Requests are not only a separate board: they are also shown after failed
guide searches, under related guide pages, in recommendations, and in the
dashboard so capable players are guided toward questions they can answer.

Core product loop:
1. Creators publish guides.
2. Players search, read, like, and comment on guides.
3. Players can tip helpful creators with virtual credits.
4. Players ask for help when no existing guide answers their problem.
5. Other players answer help requests and can earn reward credits.
6. Strong creators and helpers gain visibility through platform activity.
7. Related team-ups appear under guides.
8. Players find compatible teammates and send direct team-up invitations.
9. Players accept public team invitations or private temporary friend squad
   invitations.
10. The growing guide and help request database becomes a future knowledge
   source for built-in AI.

Main features:
- Register, login, logout, and account-specific player profiles
- Guide Hub with featured guides
- Rich guide posts with game, category, difficulty, tags, content, author,
  likes, comments, and created date
- Guide search by game, title, tag, category, or content
- Guide detail pages with like, comment, and creator tip actions
- Help Requests board for asking community questions when no guide exists
- Help request search by game, title, tag, or problem description
- Help answers, solved status, best answer selection, and reward credits
- Failed guide searches can route the user to existing help requests or Ask for Help
- Guide detail pages show related help requests for the same game
- Dashboard and Recommendations show questions the current player may answer
- Helper leaderboard rewards visible answering activity
- Virtual credit tipping system for rewarding helpful guide creators
- Related team-up discovery under each guide
- Creator leaderboard that uses guide count, likes, comments, and tips
- Rich player profiles
- Team-up requests and joining teams
- Teammate matching with direct invitations
- Invitation inbox with accept/decline actions
- Friend requests and friend lists
- Friend messages with inbox reply action and replies shown under the original message
- Temporary friend squads that stay separate from the public Team-Up Board
- Temporary squad invitations show the full invited roster plus accepted/pending members
- Multi-friend squad invitations using numbers like 1,2 or all
- Many input flows support cancel/back/return/menu before submitting
- JSON save/load storage

Files:
app.py
- Starts the first Flask web version of GameGuild.
- Reuses the existing models.py and storage.py data layer.
- Provides web pages for the dashboard, Guide Hub, Help Requests, Team-Ups,
  Friends, Messages, creator tipping, answers, and temporary squad invitations.

main.py
- Starts the app, shows the guide-first menu, and runs the automatic demo.

models.py
- Defines Player, Guide, HelpRequest, TeamRequest, TeamInvite, FriendRequest,
  and FriendMessage classes.

storage.py
- Stores shared data, JSON save/load logic, helper functions, and demo data.
- Saves account/profile, guide, team, invitation, friend, and message data to
  game_guild_v6.json.
- Also saves help requests, answers, solved status, best answer, and rewards.

features.py
- Contains Guide Hub, guide publishing/search/detail actions, comments,
  Help Requests, virtual creator tips, creator leaderboard, account/profile
  management, team-up joining, teammate matching, direct invitations, friends,
  messages, recommendations, and Help Bot logic.

templates/
- Contains the Flask HTML pages for the web interface.

static/style.css
- Contains the first web version's visual design and responsive layout.

Suggested manual test:
1. Run python main.py
2. Choose 11 Load demo
3. Choose 5 Account / profile manager
4. Login as Carl with password 1234
5. Choose 10 Dashboard to see Carl's own profile
6. Choose 5 again, logout, then login as Mia with password 1234
7. Choose 10 Dashboard to see Mia's own profile
8. Choose 2 Search guides
9. Search for minecraft
10. Open guide 1
11. Like, comment, or tip the guide creator with virtual credits
12. Choose 13 Help Requests
13. Browse or search open player questions
14. Ask for help or answer an existing request
15. Mark the best answer if you are the request author
16. Search for a guide that does not exist and choose Ask for Help
17. Open a guide detail page and view related help requests for that game
18. Join related team-up 1
19. Choose 8 Find teammates / invite
20. Send an invite to a matched player
21. Login as that player through Account / profile manager
22. Choose My invitations and accept or decline the invite
23. Choose Friends / messages to accept friend requests or send messages
24. Open the message inbox and reply to a received message
25. Invite several friends to one temporary squad with 1,2 or all
26. Choose 4 Creator leaderboard to see creator and helper leaderboards
27. Choose 12 Save and exit

Demo accounts:
Carl, Mia, Thor, Luna, and Ari all use password 1234 after Load demo.

Prototype economy note:
The tip feature uses virtual credits only. It is designed to show the future
creator reward flow without connecting to real payment services.

Future AI plan:
The built-in AI should not answer from nowhere. It should search GameGuild's
guide posts and solved help requests first, retrieve the most relevant posts,
summarize the answer, and show which guides or help threads were used as
sources.
