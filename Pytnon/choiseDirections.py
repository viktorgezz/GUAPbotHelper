from db import *



class ChoiseDirections():
    def __init__(self, directions: dict, passing_points: int):
        self.directions = directions
        self.passing_points = passing_points

    def get_directions(self):
        result = []
        focusDb = Focus()
        directions = focusDb.get_all_info(passing_points=self.passing_points)
        for direction in directions:
            subjects = eval(direction[4])
            subject_list = []
            for i in range(1, 4):
                subj = subjects[f'{i}']
                subj = subj.split('/')
                for s in subj:
                    subject_list.append(s)

            if set(self.directions).issubset(subject_list):
                directionDb = Directions()
                info = directionDb.get_name_description_price_by_id(direction[1])
                result.append({"name": info[0], "focus": direction[0], 'description' : info[1], 'price' : info[2], 'passing_points' : direction[-2]})

        return result


a = ChoiseDirections(["Математика", "Русский язык", "Информатика"], 210)
print(a.get_directions())







