from app.db.client.client import MySQLConnection
from app.db.models.models import Base, Player, Team, Gallery, Schedule


class DbIteraction:

    def __init__(self, host, port, user, password, db_name, rebuild_db=False):
        self.mysql_connection = MySQLConnection(
            host=host,
            port=port,
            user=user,
            password=password,
            db_name=db_name,
            rebuild_db=rebuild_db
        )

        #self.mysql_connection.add_players()

        self.engine = self.mysql_connection.connection.engine

        if rebuild_db:
            self.create_tables()

    def create_tables(self):
        Base.metadata.create_all(self.engine)

    def get_players(self):
        players = self.mysql_connection.session.query(Player).all()

        if players:
            self.mysql_connection.session.expire_all()
            return players

    def get_player_info_id(self, id):
        player = self.mysql_connection.session.query(Player).filter_by(id=id).first()

        if player:
            self.mysql_connection.session.expire_all()
            return player

    def get_team_info_name(self, name):
        team = self.mysql_connection.session.query(Team).filter_by(team_name=name).first()

        if team:
            self.mysql_connection.session.expire_all()
            return team

    def get_teams(self):
        teams = self.mysql_connection.session.query(Team).all()

        if teams:
            self.mysql_connection.session.expire_all()
            return teams

    def get_gallery(self, photo_id):
        photo = self.mysql_connection.session.query(Gallery).filter_by(id=photo_id).first()

        if photo:
            self.mysql_connection.session.expire_all()
            return photo

    def get_all_gallery(self):
        gallery = self.mysql_connection.session.query(Gallery).all()

        if gallery:
            self.mysql_connection.session.expire_all()
            return gallery

    def get_players_team(self, team):
        players = self.mysql_connection.session.query(Player).filter_by(team=team).all()

        if players:
            self.mysql_connection.session.expire_all()
            return players

    def get_schedule(self, tour_numbers):
        schedule = self.mysql_connection.session.query(Schedule).filter_by(tour_number=tour_numbers).all()
        if schedule:
            self.mysql_connection.session.expire_all()
            return schedule

    def get_all_schedule(self):
        schedule = self.mysql_connection.session.query(Schedule).all()

        if schedule:
            self.mysql_connection.session.expire_all()
            return schedule


if __name__ == '__main__':
    db = DbIteraction(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='pass',
        db_name='MephiLeague',
        rebuild_db=False
    )
