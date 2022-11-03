import traceback


def sort(ds, data: str, d_id: str) -> list:
    sorted_list = [[] for _ in range(15)]

    try:
        for x in ds:
            if isinstance(x, dict):
                for i, d in enumerate(x.values()):
                    sorted_list[int(d[d_id])].append(d[data])
    except IndexError:
        traceback.format_exc()
    except KeyError:
        traceback.format_exc()

    return sorted_list


class Algorithm:
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

        sorted_answers = sort(Algorithm.answers, "answers", "answers_id")
        sorted_fos = sort(Algorithm.fos, "field_of_study", "field_of_study_id")
        sorted_points = sort(Algorithm.points, "points", "points_id")
        sorted_u_answers = sort(Algorithm.user_answers, "user_answers", "user_answers_id")

        print("answers", sorted_answers)
        print("richting", sorted_fos)
        print("punten", sorted_points)
        print("user answers", sorted_u_answers)

        for i, [*l] in enumerate(zip(sorted_u_answers, sorted_answers, sorted_fos, sorted_points)):
            scores[int(l[0][0])] += int(l[3][int(l[0][0])])

        print(scores)

        return scores
