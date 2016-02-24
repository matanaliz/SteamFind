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
    games = appcore.get_games(player)

    common = {}
    #{friend.steamid : games in appcore.get_games(friend) for friend in }
    for friend in player.friends:
        com = games in appcore.get_games(friend)
        common[friend.steamid] = com

    return render_template('info.html',
                           user=player.__dict__,
                           friends=player.friends,
                           games=games,
                           commons=common)

