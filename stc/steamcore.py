from stc import steamApp
from stc import steamKey

DEBUG = True


class SteamUser:
    def __init__(self):
        pass


class LogInOut(object):
    def __init__(self, f):
        self.f = f

    def __call__(self, *args):
        if DEBUG:
            print("Call {} with args: ".format(self.f.__name__))

            for arg in enumerate(args):
                print("{}".format(arg))

            results = self.f(*args)
            print('Result: ')

            if results:
                for res in enumerate(results):
                    print("{}".format(res))
            else:
                    print("None")
        else:
            results = self.f(*args)
        return results


class Player:
    def __init__(self):
        self._steamid = ''
        self._name = ''
        self._avatar = ''
        self._games = {}

    def __repr__(self):
        attrs = vars(self)
        return ', '.join("%s: %s" % item for item in attrs.items())

    def __str__(self):
        attrs = vars(self)
        return ', '.join("%s: %s" % item for item in attrs.items())

    @property
    def steamid(self):
        return self._steamid

    @steamid.setter
    def steamid(self, value):
        self._steamid = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def avatar(self):
        return self._avatar

    @avatar.setter
    def avatar(self, value):
        self._avatar = value

    @property
    def games(self):
        return self._games

    @games.setter
    def games(self, value):
        self._games = value

    def get_common_with(self, player):
        pass


class Game:
    def __init__(self):
        pass


def get_player(steamid):
    summary = get_player_summary(steamid)
    # Get first player from list
    return summary[0]


@LogInOut
def set_steam_id(steamid):
    request = steamApp.ISteamUser.ResolveVanityURL(key=steamKey, vanityurl=steamid)
    if 'steamid' in request['response']:
        return request['response']['steamid']
    return None


@LogInOut
def get_friends(player):
    request = steamApp.ISteamUser.GetFriendList(key=steamKey, steamid=player.steamid)
    return [get_player(f['steamid']) for f in request['friendslist']['friends']]


@LogInOut
def get_owned_games(player):
    request = steamApp.IPlayerService.GetOwnedGames(
            appids_filter=None,
            include_appinfo=True,
            include_played_free_games=True,
            key=steamKey,
            steamid=player.steamid)
    if 'games' in request['response'].keys():
        games = sorted(request['response']['games'], key=lambda g: g['playtime_forever'], reverse=True)
        player.games = [g['appid'] for g in games]
        return player.games
    else:
        return []


@LogInOut
def get_common_games(steamid, games):
    common = []
    for game in games:
        if game in get_owned_games(steamid):
            request = steamApp.ISteamUserStats.GetSchemaForGame_v2(appid=game, key=steamKey)
            common.append(request['game']['gameName'])

    return common


@LogInOut
def get_player_summary(steamids):
    if not isinstance(steamids, list):
        steamids = [steamids]

    id_string = ",".join(steamids)
    request = steamApp.ISteamUser.GetPlayerSummaries_v2(key=steamKey, steamids=id_string)
    response_player_list = request['response']['players']

    players = []
    for player in response_player_list:
        players.append(Player(
            steamid=player['steamid'],
            name=player['personaname'],
            avatar=player['avatar']
        ))

    return players


@LogInOut
def get_game_summary(appid):
    request = steamApp.ISteamUserStats.GetSchemaForGame_v2(appid=appid, key=steamKey)
    game_name = request['game']['gameName']

    return game_name
