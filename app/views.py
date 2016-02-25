from flask import render_template, request, redirect, url_for
from app import app
from app import appcore


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return redirect(url_for('info', username=request.form['username']))
    return render_template('index.html')


@app.route('/info/<username>', methods=['GET', 'POST'])
def info(username):
    # static_steamID = '76561198044310785'
    steamid = appcore.resolve_nickname(username)
    if not steamid:
        return redirect('/')

    player = appcore.get_player(steamid)

    # Remove all games without icon
    player_games = [g for g in appcore.get_games() if g.icon]

    # This is horrible!
    common = {}
    for friend in player.friends:
        friend_games = appcore.get_games(friend)
        common[friend.steamid] = []
        for game in friend_games:
            if any(g.appid == game.appid for g in player_games):
                if game.icon:
                    common[friend.steamid].append(game)

    return render_template('info.html',
                           user=player.__dict__,
                           friends=player.friends,
                           games=player_games,
                           commons=common)

