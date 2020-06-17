import time
from typing import List

import requests
import ques

p_page_f = "https://zhidao.baidu.com/ihome/api/myanswer?pn={}" \
         "&rn=20&t={}&uid={}" \
         "&type=default"

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "DNT": "1",
    "Host": "zhidao.baidu.com",
    "Referer": "https://zhidao.baidu.com/usercenter?uid=1b294069236f25705e79fa50&role=ugc",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
    "X-ik-ssl": "1",
    "X-Requested-With": "XMLHttpRequest",
}

class ques_item():
    def __int__(self):
        self.qid = ""
        self.ques_title = ""
        self.ques_create_time = ""
        self.ques_tag = []

        self.ans_id = ""
        self.ans_create_time = ""
        pass

def get_ans_list(uid: str) -> List[ques_item]:
    res = []
    pn = 0
    while True:
        p_page = p_page_f.format(pn, round(time.time() * 1000), uid)
        rsp = requests.get(p_page, headers=headers)
        if rsp.status_code != 200:
            print("err get ans list, status code: ", rsp.status_code)
            return res
        else:
            rsp.encoding = "GBK"
            ans_list = rsp.json().get("data", {}).get("question", {}).get("list", [])
            if len(ans_list) == 0:
                return res
            for v in ans_list:
                pn += 1

                item = ques_item()

                item.qid = v.get("qid", "")
                item.ques_title = v.get("title", "")
                item.ques_create_time = v.get("createTime", "")
                item.ques_tag = v.get("qTags", [])

                item.ans_id = v.get("replyId")
                item.ans_create_time = v.get("replyCreateTime")
                res.append(item)



if __name__ == '__main__':
    res = get_asn_list("1b294069236f25705e79fa50")
    print(res)
