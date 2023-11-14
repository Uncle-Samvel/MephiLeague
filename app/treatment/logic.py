from app.treatment.transformation import Transformation


class Logic:

    # вернуть 1 команду по названию
    @staticmethod
    def team_by_name(db, team_name):
        team = db.get_team_info_name(team_name)
        data = Transformation.dict_team(db, team)
        return data

    # вернуть все команды
    @staticmethod
    def teams(db):
        teams = db.get_teams()
        data = list()

        for team in teams:
            data.append(Transformation.dict_team(db, team))

        data.sort(key=lambda x: x['score'], reverse=True)

        return data

    # вернуть всех бомбардиров
    @staticmethod
    def top_goals(db):
        players = db.get_players()
        data = list()

        for player in players:
            if player.number_of_goals > 0:
                data.append(Transformation.dict_player(db, player))

        data.sort(key=lambda x: x['number_of_goals'], reverse=True)

        return data

    # вернуть всех ассистентов
    @staticmethod
    def top_assists(db):
        players = db.get_players()
        data = list()

        for player in players:
            if player.number_of_assists > 0:
                data.append(Transformation.dict_player(db, player))

        data.sort(key=lambda x: x['number_of_assists'], reverse=True)

        return data

    # вернуть расписание по турам
    @staticmethod
    def get_schedule(db):
        data = list()

        for i in range(1,4):
            pre_data = list()
            db.get_schedule(i)

            for item in db.get_schedule(i):
                pre_data.append(Transformation.dict_schedule(db, item))

            data.append(pre_data)

        return data

    # вернуть все фотографии
    @staticmethod
    def get_gallery(db):
        data = list()
        gallery = db.get_all_gallery()

        for photo in gallery:
            data.append(photo.url)

        return data




