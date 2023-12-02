import json
from app.treatment.logic import Logic

class Acrhiving():

    @staticmethod
    def archive_the_tournament(video_url, photo_url, db, name):
        with open('../archive/data/1.json', 'r', encoding="utf-8") as file:
            data = json.load(file)

        data.append({
            'video': video_url,
            'photo': photo_url,
            'top_goals': Logic.top_goals(db)[:10],
            'top_assists': Logic.top_assists(db)[:10],
            'top_goals_assists': Logic.top_assists_goals(db)[:10],
            'table': Logic.teams(db),
            'name_of_tournament': name,
        })

        with open("../archive/data/1.json", "w", encoding="utf-8") as file:
            json.dump(data, file)


