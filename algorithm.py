# __list__ = []
# composed = []
# composed_2 = []
# for each in data.values():
#     __list__.append(each)
# data_id = __list__[0]
# vraag = __list__[1]
# antwoord = __list__[2]
# richting = __list__[3]
# punten = __list__[4]
# # print(data_id)
# # print(vraag)
# # print(antwoord)
# # print(punten)
# composed.append(richting)
# composed.append(punten)
# composed_2.append(composed)
# for each2 in antwoord:
#     list(each2)
#     composed_dict = dict(zip(each2, composed_2))
#     print(composed_dict)

class Algorithm:
    d_id: tuple
    a: tuple
    fos: tuple
    p: tuple
    q: tuple
    ua: tuple

    @staticmethod
    def init(data: list):
        Algorithm.d_id = data[0]
        Algorithm.a = data[1]
        Algorithm.fos = data[2]
        Algorithm.p = data[3]
        Algorithm.q = data[4]
        Algorithm.ua = data[5]

    @staticmethod
    def cs():
        pass
