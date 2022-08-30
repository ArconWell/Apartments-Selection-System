from dataclasses import dataclass
from typing import List

from selectionApartments.models import Question


@dataclass
class QuestionEntity:
    question_name: str
    question_text: str
    answer_first: str
    answer_last: str


class QuestionDAO:

    def _orm_to_entity(self, question_orm: Question):
        return QuestionEntity(
            question_name=question_orm.question_name,
            question_text=question_orm.question_text,
            answer_first=question_orm.answer_first,
            answer_last=question_orm.answer_last,
        )

    def fetch_all(self) -> List[QuestionEntity]:
        return list(map(self._orm_to_entity, Question.objects.all()))
