from app import db

game_table = db.Table('game_table',
                      db.Column('player_id',
                                db.String(64),
                                db.ForeignKey('player.steamid'),
                                primary_key=True),
                      db.Column('game_id',
                                db.String(32),
                                db.ForeignKey('game.appid'),
                                primary_key=True)
                      )

friend_table = db.Table('friend_table',
                        db.Column('player_id',
                                  db.String(64),
                                  db.ForeignKey('player.steamid'),
                                  primary_key=True),
                        db.Column('friend_id',
                                  db.String(64),
                                  db.ForeignKey('player.steamid'),
                                  primary_key=True)
                        )


class Player(db.Model):
    __tablename__ = 'player'
    steamid = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(64), index=True)
    avatar = db.Column(db.String(255))
    games = db.relationship('Game',
                            secondary=game_table,
                            primaryjoin=steamid == game_table.c.player_id,
                            backref='owner',
                            lazy='dynamic'
                            )
    friends = db.relationship('Player',
                              secondary=friend_table,
                              primaryjoin=steamid == friend_table.c.player_id,
                              secondaryjoin=steamid == friend_table.c.friend_id
                              )

    def __repr__(self):
        return "<Player {}>".format(self.name)

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)

    def add_game(self, game):
        if game not in self.games:
            self.games.append(game)


class Game(db.Model):
    __tablename__ = 'game'
    appid = db.Column(db.String(32), primary_key=True)
    name = db.Column(db.String(64), index=True)
    logo = db.Column(db.String(255))
    icon = db.Column(db.String(255))

    def __repr__(self):
        return '<Game {} {}>'.format(self.appid, self.name)
