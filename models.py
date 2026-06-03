"""Core classes for the guide-first GameGuild prototype."""


class Player:
    def __init__(
        self,
        name,
        games,
        playstyle,
        skill_level,
        availability,
        language,
        region,
        looking_for_team=True,
        bio="",
        credits=100,
        earnings=0,
        password_hash="",
        friends=None,
    ):
        self.name = name
        self.games = games
        self.playstyle = playstyle
        self.skill_level = skill_level
        self.availability = availability
        self.language = language
        self.region = region
        self.looking_for_team = looking_for_team
        self.bio = bio
        self.credits = credits
        self.earnings = earnings
        self.password_hash = password_hash
        if friends is None:
            self.friends = []
        else:
            self.friends = friends


class Guide:
    def __init__(
        self,
        game,
        title,
        category,
        difficulty,
        tags,
        content,
        author,
        likes=0,
        comments=None,
        created="Today",
        tips=None,
    ):
        self.game = game
        self.title = title
        self.category = category
        self.difficulty = difficulty
        self.tags = tags
        self.content = content
        self.author = author
        self.likes = likes
        self.created = created
        if comments is None:
            self.comments = []
        else:
            self.comments = comments
        if tips is None:
            self.tips = []
        else:
            self.tips = tips


class HelpRequest:
    def __init__(
        self,
        game,
        title,
        description,
        tags,
        author,
        reward=0,
        status="open",
        replies=None,
        best_reply=-1,
        created="Today",
    ):
        self.game = game
        self.title = title
        self.description = description
        self.tags = tags
        self.author = author
        self.reward = reward
        self.status = status
        self.best_reply = best_reply
        self.created = created
        if replies is None:
            self.replies = []
        else:
            self.replies = replies


class TeamRequest:
    def __init__(
        self,
        game,
        mode,
        time,
        message,
        author,
        skill_level,
        language,
        region,
        max_members,
        members=None,
        status="open",
        team_id="",
    ):
        self.team_id = team_id
        self.game = game
        self.mode = mode
        self.time = time
        self.message = message
        self.author = author
        self.skill_level = skill_level
        self.language = language
        self.region = region
        self.max_members = max_members
        self.status = status
        if members is None:
            self.members = []
        else:
            self.members = members


class TeamInvite:
    def __init__(
        self,
        from_player,
        to_player,
        game,
        message,
        status="pending",
        created="Today",
        team_id="",
    ):
        self.from_player = from_player
        self.to_player = to_player
        self.game = game
        self.message = message
        self.status = status
        self.created = created
        self.team_id = team_id


class FriendRequest:
    def __init__(
        self,
        from_player,
        to_player,
        message,
        status="pending",
        created="Today",
    ):
        self.from_player = from_player
        self.to_player = to_player
        self.message = message
        self.status = status
        self.created = created


class FriendMessage:
    def __init__(
        self,
        from_player,
        to_player,
        text,
        created="Today",
        read=False,
        reply_to="",
    ):
        self.from_player = from_player
        self.to_player = to_player
        self.text = text
        self.created = created
        self.read = read
        self.reply_to = reply_to
