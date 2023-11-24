import threading
import requests
import argparse

from utils import config_parser
from flask import Flask, request
from flask_cors import cross_origin


from app.archive.archiving import Acrhiving
from app.archive.unzipping import Unzipping

from app.db.interaction.iteraction import DbIteraction
from app.treatment.logic import Logic

import json


class Server():

    def __init__(self, host, port, db_host, db_port, db_user, db_password, db_name):
        self.db = DbIteraction(
            host=db_host,
            port=db_port,
            user=db_user,
            password=db_password,
            db_name=db_name,
            rebuild_db=False
        )

        self.host = host
        self.port = port

        self.app = Flask(__name__)

        self.app.add_url_rule('/GetTeam/<team_name>', view_func=self.get_team_by_name)
        self.app.add_url_rule('/GetTeams', view_func=self.get_teams)
        self.app.add_url_rule('/GetSchedule', view_func=self.get_schedule)
        self.app.add_url_rule('/GetGoals', view_func=self.get_top_goals)
        self.app.add_url_rule('/GetAssists', view_func=self.get_top_assists)
        self.app.add_url_rule('/GetGallery', view_func=self.get_gallery)
        self.app.add_url_rule('/GetHistory', view_func=self.archive)
        self.app.add_url_rule('/GetAdmins', view_func=self.get_gallery)


    def run_server(self):
        self.server = threading.Thread(target=self.app.run, kwargs={'host': self.host, 'port': self.port})
        self.server.start()
        return self.server

    @cross_origin()
    def get_team_by_name(self, team_name):
        return Logic.team_by_name(self.db, team_name)

    @cross_origin()
    def get_teams(self):
        return Logic.teams(self.db)

    @cross_origin()
    def get_schedule(self):
        return json.dumps(Logic.get_schedule(self.db))

    @cross_origin()
    def get_top_goals(self):
        return Logic.top_goals(self.db)

    @cross_origin()
    def get_top_assists(self):
        return Logic.top_assists(self.db)

    @cross_origin()
    def get_gallery(self):
        return Logic.get_gallery(self.db)

    @cross_origin()
    def get_admins(self):
        return Logic.get_admins(self.db)

    @cross_origin()
    def archive(self):
        return Unzipping.unzipp_the_tournaments()




if __name__ == '__main__':
    config = config_parser('config.txt')

    server_host = config['SERVER_HOST']
    server_port = int(config['SERVER_PORT'])
    db_host = config['DB_HOST']
    db_port = int(config['DB_PORT'])
    db_user = config['DB_USER']
    db_password = config['DB_PASSWORD']
    db_name = config['DB_NAME']



    server = Server(host=server_host,
                    port=server_port,
                    db_host=db_host,
                    db_port=db_port,
                    db_user=db_user,
                    db_password=db_password,
                    db_name=db_name)

    server.run_server()

