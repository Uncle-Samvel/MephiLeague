from sqlalchemy import Column, Integer, ForeignKey, VARCHAR, UniqueConstraint, Date, PickleType
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Gallery(Base):
    __tablename__ = 'gallery'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    url = Column(VARCHAR(200), nullable=False)

    UniqueConstraint(url)


class Team(Base):
    __tablename__ = 'team'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    team_name = Column(VARCHAR(30), nullable=False)
    logo = Column(Integer, ForeignKey(f'{Gallery.__tablename__}.{Gallery.id.name}'), nullable=False)
    gallery = Column(VARCHAR(200))

    captain = Column(Integer, nullable=False)

    place_in_the_tournament = Column(Integer, nullable=False)

    vk = Column(VARCHAR(200), nullable=False)

    games_played = Column(Integer, nullable=False)
    victory = Column(Integer, nullable=False)
    defeat = Column(Integer, nullable=False)
    draw = Column(Integer, nullable=False)

    goals_scored = Column(Integer, nullable=False)
    missed_goals = Column(Integer, nullable=False)
    score = Column(Integer, nullable=False)

    UniqueConstraint(team_name)


class Player(Base):
    __tablename__ = 'player'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    name = Column(VARCHAR(30))
    surname = Column(VARCHAR(30))
    lastname = Column(VARCHAR(30))

    team = Column(VARCHAR(30), nullable=False)

    photo = Column(Integer, ForeignKey(f'{Gallery.__tablename__}.{Gallery.id.name}'), nullable=False)

    number_of_matches = Column(Integer, nullable=False)
    number_of_goals = Column(Integer, nullable=False)
    number_of_assists = Column(Integer, nullable=False)

    yellow_cards = Column(Integer, nullable=False)
    red_cards = Column(Integer, nullable=False)

    date_of_birth = Column(VARCHAR(30), nullable=False)
    city = Column(VARCHAR(40))
    role = Column(VARCHAR(20))


class Schedule(Base):
    __tablename__ = 'schedule'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    first_team = Column(VARCHAR(30), nullable=False)
    second_team = Column(VARCHAR(30), nullable=False)

    match_date = Column(Date, nullable=False)

    goal_first = Column(Integer, nullable=True)
    goal_second = Column(Integer, nullable=True)

    tour_number = Column(Integer, nullable=False)
