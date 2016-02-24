from stc import steamcore
from app import db, models


def get_player(steamid):
    # First try to get player from DB
    player = models.Player.query.get(steamid)
    if not player:
        # Player was not found in DB
        p = steamcore.get_player(steamid)
        player = models.Player(steamid=p.steamid,
                               name=p.name,
                               avatar=p.avatar)

        db.session.add(player)
        db.session.commit()

    # TODO Check all friends in DB and get all
    if not player.friends:
        # Current player has no friends
        friends = steamcore.get_friends(player)
        # Fill up DB with friends
        for friend in friends:
            f = models.Player.query.get(friend.steamid)
            if not f:
                f = models.Player(steamid=friend.steamid,
                                  name=friend.name,
                                  avatar=friend.avatar)
                # Add new player to DB
                db.session.add(f)
                db.session.commit()

            # Add player as friend of current
            player.add_friend(f)

    db.session.commit()
    return player


def resolve_nickname(nickname):
    steamid = steamcore.set_steam_id(nickname)
    return steamid


def get_games(player):
    #if not player.games:

    # Get games appids
    games = steamcore.get_owned_games(player)
    # Fill up DB with games
    for game in games:
        g = models.Game.query.get(game.appid)
        if not g:
            g = models.Game(appid=game.appid,
                            name=game.name,
                            logo=game.logo,
                            icon=game.icon)

            # Add new game to DB
            db.session.add(g)
            db.session.commit()

        # Add game to gamelist of player
        player.add_game(g)

    db.session.commit()

    return models.Player.query.get(player.steamid).games
