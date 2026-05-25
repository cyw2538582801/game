"""Classes used by GameGuild."""

class Player:
    def __init__(self, name, games, role):
        self.name = name
        self.games = games
        self.role = role


class Guide:
    def __init__(self, game, title, tip, author, likes=0):
        self.game = game
        self.title = title
        self.tip = tip
        self.author = author
        self.likes = likes


class TeamRequest:
    def __init__(self, game, mode, time, message, author, members=None):
        self.game = game
        self.mode = mode
        self.time = time
        self.message = message
        self.author = author
        if members is None:
            self.members = []
        else:
            self.members = members
