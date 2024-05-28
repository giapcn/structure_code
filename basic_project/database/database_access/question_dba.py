# database/database_access/question_dba.py
from database.database_access.dba import DBA
import os
import sys

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
sys.path.append(project_root)

from configs import db_config
from utils.json_encoder import convert_objectid_to_str

class QuestionDBA(DBA):
    def __init__(self):
        super().__init__(db_config.CONNECT['QUESTION_COLLECTION'])

    def get_100_questions(self):
        questions = self.find_many(100, {})
        if questions is None:
            return []
        questions_serializable = [convert_objectid_to_str(question) for question in questions]
        return questions_serializable
