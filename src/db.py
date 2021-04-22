from typing import Dict, List
import sqlite3
from src.schema import SCHEMA


class DataBase:
    def __init__(self, db_name: str) -> None:
        """
        creates an instance of the DataBase class

        Args:
            `db_name: (str)` -> db name to be created 

        Example:
            `db = DataBase('test.db')`

        Returns:
            `None`
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute(SCHEMA)

    def create(self, data: Dict) -> Dict:
        """
        creates an entry in the database

        Args:
            `param1: (obj)` -> with specific keys and data types for the db

        Returns:
            `obj` if successful else returns `None`
        """
        try:
            self.cursor.execute(
                """
                INSERT INTO sportsbetting 
                (league, home_team, away_team, home_team_win_odds, away_team_win_odds, draw_odds, game_date)
                 VALUES (?, ?, ?, ?, ?, ?, ?)
                 """,
                (data['league'], data['home_team'], data['away_team'], data['home_team_win_odds'], data['away_team_win_odds'], data['draw_odds'], data['game_date']))
            self.conn.commit()
            return data
        except Exception as e:
            print(e)
            return None

    def read(self) -> List:
        """
        Gets all entries in the DataBase

        Returns:
            `list` if successfull else `None`
        """
        try:
            data = self.conn.execute("""SELECT * FROM sportsbetting""")
            self.conn.commit()
            return list(data)
        except Exception as e:
            print(e)
            return None

    def update(self, old_data: Dict, new_data: Dict) -> Dict:
        """
        updates data from the database if data in the database

        Args:
            `param1: (obj)` -> with specific keys and values with the right data type

        Returns:
            `obj` if successfully updated else `None`
        """
        try:
            self.cursor.execute(
                """
                UPDATE sportsbetting 
                SET league = ?, home_team = ?, away_team = ?, home_team_win_odds = ?, away_team_win_odds = ?, draw_odds = ?, game_date = ?
                WHERE 
                """
            )
            self.conn.commit()
            return new_data
        except Exception as e:
            print(e)
            return None

    def delete(self, data: Dict) -> Dict:
        """
        deletes data from the database if data in the database

        Args:
            `data: (obj)` -> with specified keys

        Returns:
            `obj` if successfully deleted else `None`
        """
        try:
            self.cursor.execute(
                """DELETE FROM sportsbetting WHERE league = ?, home_team = ?, away_team = ?, game_date = ?""",
                (data["league"], data["home_team"], data["away_team"], data["game_date"],))
            self.conn.commit()
            return data
        except Exception as e:
            print(e)
            return None

    def __del__(self) -> None:
        """
        closes the database instance
        """
        self.conn.close()