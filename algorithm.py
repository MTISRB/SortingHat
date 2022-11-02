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
    def cs():
        scores = []

        sorted_answers = [[] for _ in range(15)]
        sorted_fos = [[] for _ in range(15)]
        sorted_points = [[] for _ in range(15)]

        print(sorted_answers)

