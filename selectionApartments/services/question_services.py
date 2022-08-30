from typing import List

from selectionApartments.services.dao.question_dao import QuestionDAO


class GetQuestionsInfoService:

    def execute(self) -> List[QuestionDAO]:
        return QuestionDAO().fetch_all()
