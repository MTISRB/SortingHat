dataset = {
    "ID" : ['0'],
    "Vraag" : ["In welke richting heb je al interesse?"],
    "Antwoord" : ["forenische ict", "interachtie-technologie", "software engineer", "data engineer", "geen idee"],
    "Richting" : ["FICT", "IICT", "SE", "DB"],
    "Punten" : ["4","4","4","0"]
}

user_input = "data engineer"

def algorithm(data: dict,user_input):
    __list__ = []
    composed = []
    composed_2 = []
    for each in data.values():
        __list__.append(each)
    data_id = __list__[0]
    vraag = __list__[1]
    antwoord = __list__[2]
    richting = __list__[3]
    punten = __list__[4]
    # print(data_id)
    # print(vraag)
    # print(antwoord)
    # print(richting)
    # print(punten)
    composed.append(richting)
    composed.append(punten)
    composed_2.append(composed)
    for each2 in antwoord:
        list(each2)
        composed_dict = dict(zip(each2, composed_2))
        print(composed_dict)



algorithm(dataset,user_input)
