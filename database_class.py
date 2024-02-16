import sqlite3


class database:
    def __init__(self, user):
        self.connection = sqlite3.connect('highscores.db')
        self.cursor = self.connection.cursor()
        self.user = user

    def load_user(self):
        self.cursor.execute("SELECT * FROM highscores WHERE username=:username", {'username': self.user})
        result = self.cursor.fetchone()

        if not result:
            self.cursor.execute("INSERT INTO highscores VALUES(:username, :score)",
                                {'username': self.user, 'score': 0})
            self.connection.commit()
            return 0
        else:
            return result[1]

    def update_user(self, score):
        self.cursor.execute("UPDATE highscores SET username=:username, score=:score WHERE username=:username",
                            {'username': self.user, 'score': score})
        self.connection.commit()






