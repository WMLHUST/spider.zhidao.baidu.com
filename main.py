import openpyxl

import person
import ques

uids = ["1b294069236f25705e79fa50"]

class ques_item():
    def __int__(self):
        self.qid = ""
        self.ques_title = ""
        self.ques_create_time = ""
        self.ques_tag = []

        self.ans_id = ""
        self.ans_create_time = ""
        pass

if __name__ == '__main__':
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["qid", "ques_title", "ques_create_time", "ques_tag",
               "ans_id", "ans_create_time", "ans_content"])

    for uid in uids:
         ans_list = person.get_ans_list(uid)
         for v in ans_list:
             ans_content = ques.get_ans_content(v.qid, v.ans_id)
             ws.append([v.qid, v.ques_title, v.ques_create_time, ';'.join(v.ques_tag),
                       v.ans_id, v.ans_create_time, ans_content])

    wb.save("res.xlsx")
