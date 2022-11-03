from utils import sort


class Algorithm:
    def __init__(self):
        pass

    answers: tuple
    fos: tuple
    points: tuple
    questions: tuple
    user_answers: tuple

    @staticmethod
    def init(data: list):
        Algorithm.answers = data[0]
        Algorithm.fos = data[1]
        Algorithm.points = data[3]
        Algorithm.questions = data[2]
        Algorithm.user_answers = data[4]

    @staticmethod
    def cs() -> list:
        scores = [0, 0, 0, 0]  #FICT, IICT, SE, DB
        tot_scores = [36, 40, 40, 32]  #FICT, IICT, SE, DB

        sorted_answers = sort(Algorithm.answers, "answers", "answers_id")
        sorted_fos = sort(Algorithm.fos, "field_of_study", "field_of_study_id")
        sorted_points = sort(Algorithm.points, "points", "points_id")
        sorted_u_answers = sort(Algorithm.user_answers, "user_answers", "user_answers_id")

        for i, [*l] in enumerate(zip(sorted_u_answers, sorted_answers, sorted_fos, sorted_points)):
            scores[int(l[0][0])] += int(l[3][int(l[0][0])])

        return [*zip(scores, tot_scores)]
