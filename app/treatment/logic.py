from app.treatment.transformation import Transformation
import datetime

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

    # вернуть всех гол + ассист
    @staticmethod
    def top_assists_goals(db):
        players = db.get_players()
        data = list()

        for player in players:
            if player.number_of_assists > 0 or player.number_of_goals > 0:
                data.append(Transformation.dict_player(db, player))

        data.sort(key=lambda x: x['number_of_assists'] + x['number_of_goals'], reverse=True)

        return data

    # вернуть расписание по турам
    @staticmethod
    def get_schedule(db):
        data = list()

        for i in range(1, 4):
            pre_data = list()
            db.get_schedule(i)

            for item in db.get_schedule(i):
                pre_data.append(Transformation.dict_schedule(db, item))

            data.append({'id': i, 'res': pre_data})

        return data

    # вернуть все фотографии
    @staticmethod
    def get_gallery(db):
        data = list()
        gallery = db.get_all_gallery()

        for photo in gallery:
            if photo.PIN == 'G':
                data.append(photo.url)

        return data

    # вернуть администраторов
    @staticmethod
    def get_admins(db):
        data = list()
        dat = list()
        admins = db.get_admins()
        func = ['тех','медиа', 'cудьи', 'руководство']
        for i in func:
            for admin in admins:
                if admin.function == i:
                    dat.append(Transformation.dict_admins(admin))
            data.append({func: dat})
            dat = list()

        return data

    # главная страница
    @staticmethod
    def get_main(db):
        schedule = db.get_all_schedule()
        data_schedule = list()
        for item in schedule:
            data_schedule.append(Transformation.dict_schedule(db,item))

        data_schedule = sorted(data_schedule, key=lambda date: datetime.datetime.strptime(date['match_date'], '%d.%m.%Y'), reverse=True)
        match = 0

        today_date = datetime.date.today()
        current_date_object = datetime.datetime.strptime(str(today_date), '%Y-%m-%d')


        for item in data_schedule:
            date_object = datetime.datetime.strptime(item['match_date'] + ' 00:00:00', '%d.%m.%Y %H:%M:%S')
            if date_object > current_date_object:
                match = item

        data = {
            'best_goal': Logic.top_goals(db)[0],
            'best_assists': Logic.top_assists(db)[0],
            'match': match,
        }

        return data
