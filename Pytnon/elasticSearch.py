import requests


class ElasticSearch():
    def __init__(self):
        self.BASE_URL = 'http://217.25.89.60:8080/apis/search/'


    def ask_question(self, question: str):
        get_json = requests.get(self.BASE_URL + question).json()
        print(get_json)
        if get_json == []:
            return []
        else:
            questions = []
            for i in range(len(get_json)):
                questions.append(get_json[i]['question'])
            return questions

    def get_answer(self, question: str):
        get_json = requests.get(self.BASE_URL + question).json()
        print(get_json)
        if get_json == []:
            return []
        else:
            answer = get_json[0]['answer']
        return answer

es = ElasticSearch()
print(es.ask_question('Где посмотреть минимальные баллы для поступления'))






