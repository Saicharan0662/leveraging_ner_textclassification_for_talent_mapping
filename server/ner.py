import spacy
import random

nlp = spacy.load('en_core_web_sm')


class NER():
    def __init__(self, text):
        self.text = text
        self.sentence_range_list = []

    def get_formated_text(self):
        doc = nlp(self.text)
        sentence = list(doc.sents)

        # print(sentence)

        for i in range(len(sentence)):
            if i == 0:
                self.sentence_range_list = [(0, len(str(sentence[0])))]
            else:
                self.sentence_range_list.append(
                    (self.sentence_range_list[i-1][1], self.sentence_range_list[i-1][1]+1 + len(str(sentence[i]))))

        ents = [(e.text, e.start_char, e.end_char, e.label_)
                for e in doc.ents]
        questions = []
        answers = []

        for i in range(len(ents)):
            ents_elm = ents[i]
            sent_no = self.get_sentence_no(ents_elm[1], ents_elm[2])

            if sent_no == -1:
                continue

            ques = str(sentence[sent_no])
            questions.append([ques, ents_elm])

        return {"res": questions}

    def get_sentence_no(self, l, r):
        for i in range(len(self.sentence_range_list)):
            l1, r1 = self.sentence_range_list[i]
            if l >= l1 and r < r1:
                return i

        return -1

    # def get_mcq_questions(self):
    #     doc = nlp(self.text)
    #     sentence = list(doc.sents)

    #     for i in range(len(sentence)):
    #         if i == 0:
    #             self.sentence_range_list = [(0, len(str(sentence[0])))]
    #         else:
    #             self.sentence_range_list.append(
    #                 (self.sentence_range_list[i-1][1], self.sentence_range_list[i-1][1]+1 + len(str(sentence[i]))))

    #     ents = [(e.text, e.start_char, e.end_char, e.label_) for e in doc.ents]
    #     questions = []
    #     answers = []

    #     for i in range(len(ents)):
    #         ents_elm = ents[i]
    #         sent_no = self.get_sentence_no(ents_elm[1], ents_elm[2])

    #         if sent_no == -1:
    #             continue

    #         if ents_elm[3] == 'NORP' or ents_elm[3] == 'GPE' or ents_elm[3] == 'CARDINAL' or ents_elm[3] == 'LOC' or ents_elm[3] == 'PERCENT' or ents_elm[3] == 'MONEY' or ents_elm[3] == 'WORK_OF_ART':
    #             continue

    #         ques = str(sentence[sent_no])
    #         if ques.count('(') > 0 or ques.count(')') < 0:
    #             continue
    #         if ents_elm[3] == 'DATE':
    #             ques = ques.replace(ents_elm[0], 'which year/date')
    #         else:
    #             ques = ques.replace(ents_elm[0], "_______")
    #         if (ents_elm[3] == 'DATE' or '_____' in ques) and len(ques) > 60:
    #             questions.append((sent_no, ents_elm[3], ques))
    #             answers.append(ents_elm[0])

    #     for ent in ents:
    #         if ent[3] == 'QUANTITY':
    #             quantity.append(ent[0])

    #     return questions

    # def getQuestionIndex(self, questions, ques):
    #     for i in range(len(questions)):
    #         if questions[i]['question'] == ques:
    #             return i
    #     return -1
