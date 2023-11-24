from app.db.interaction.iteraction import DbIteraction


class Transformation:
    @staticmethod
    def dict_gallery(db, list_photo):
        data = list()

        for photo in list_photo:
            phot = db.get_gallery(photo)
            arr = {'url': phot.url}
            data.append(arr)

        return data

    @staticmethod
    def dict_schedule(db, schedule):
        first_team_logo = db.get_team_info_name(schedule.first_team).logo
        second_team_logo = db.get_team_info_name(schedule.second_team).logo

        data = {'first_team': schedule.first_team,
                'second_team': schedule.second_team,
                'first_logo': first_team_logo,
                'second_logo': second_team_logo,
                'match_date': schedule.match_date,
                'goal_first': schedule.goal_first,
                'goal_second': schedule.goal_second,
                'tour_number': schedule.tour_number}

        return data

    @staticmethod
    def dict_player(db, player):
        photo = Transformation.dict_gallery(db, [player.photo])

        data = {'name': player.name,
                'surname': player.surname,
                'lastname': player.lastname,
                'team': player.team,
                'photo': photo,
                'number_of_matches': player.number_of_matches,
                'number_of_goals': player.number_of_goals,
                'number_of_assists': player.number_of_assists,
                'yellow_cards': player.yellow_cards,
                'red_cards': player.red_cards,
                'date_of_birth': str(player.date_of_birth),
                'city': player.city,
                'role': player.role
                }

        return data

    @staticmethod
    def dict_team(db, team):
        players = db.get_players_team(team.team_name)
        player_in_team = list()
        goals = 0
        for player in players:
            photo = Transformation.dict_gallery(db, [player.photo])

            arr = {'name': player.name,
                   'surname': player.surname,
                   'lastname': player.lastname,
                   'team': player.team,
                   'photo': photo,
                   'number_of_matches': player.number_of_matches,
                   'number_of_goals': player.number_of_goals,
                   'number_of_assists': player.number_of_assists,
                   'yellow_cards': player.yellow_cards,
                   'red_cards': player.red_cards,
                   'date_of_birth': str(player.date_of_birth),
                   'city': player.city,
                   'role': player.role
                   }
            goals += player.number_of_goals
            player_in_team.append(arr)

        captain = db.get_player_info_id(team.captain)

        schedule = list()
        schedule_all = db.get_all_schedule()
        if schedule_all:
            for item in schedule_all:
                if item.first_team == team.team_name or item.second_team == team.team_name:
                    schedule.append(Transformation.dict_schedule(db, item))

        logo = Transformation.dict_gallery(db, [team.logo])
        gallery = Transformation.dict_gallery(db, list(map(int, team.gallery.split(','))))

        data = {'team_name': team.team_name,
                'logo': logo,
                'gallery': gallery,
                'captain': f'{captain.surname} {captain.name} {captain.lastname}',
                'players': player_in_team,
                'place_in_the_tournament': team.place_in_the_tournament,
                'games_played': team.victory + team.defeat + team.draw,
                'vk': team.vk,
                'schedule': schedule,
                'victory': team.victory,
                'defeat': team.defeat,
                'draw': team.draw,
                'goals_scored': goals,
                'missed_goals': team.missed_goals,
                'score': team.victory * 3 + team.draw,
                }

        return data

    @staticmethod
    def dict_admins(admin):
        data = {
            'name': admin.name,
            'photo': admin.photo,
            'tg': admin.tg,
        }

        return data


if __name__ == '__main__':
    db = DbIteraction(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='pass',
        db_name='MephiLeague',
        rebuild_db=False
    )

    print(Transformation.dict_team(db, 'bara'))
