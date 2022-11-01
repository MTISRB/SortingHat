def algorithm(data: dict):
     # SE, FICT, IICT, DB
     scores = {
         "SE": 0,
         "FICT": 0,
         "IICT": 0,
         "DB": 0
     }
     vragen = {
         "vraag1": "In welke richting heb je al interesse?",
         "antwoorden1": "A: Forensiche ICT B: Interactie-Technologie C: Software Engineering D: Data Engineer E: Geen idee"

     }
     vraag_1 = vragen["vraag1"], vragen["antwoorden1"]

     input_vraag1 = input(vraag_1)
     print(input_vraag1)
     if input_vraag1 == "a":
         scores["SE"] += 6
     print(scores)
     input_vraag2 = input(vraag_1)
     if input_vraag2 == "a":
         scores["FICT"] += 8
     print(scores)


#Berekend hoogste waarde in dict
     hoogste_waarde = max(scores, key=scores.get)
     print("jij behoort tot afdeling:", hoogste_waarde)