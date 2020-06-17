import requests
from lxml import etree
from bs4 import BeautifulSoup

page_f = "https://zhidao.baidu.com/question/{}"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "DNT": "1",
    "Host": "zhidao.baidu.com",
    "Referer": "https://zhidao.baidu.com/usercenter?uid=1b294069236f25705e79fa50&role=ugc",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
}

def get_ans_content(ques_id: str, ans_id: str) -> str:
    # print("uid: {}, qid: {}".format(ques_id), ans_id)

    page_url = page_f.format(ques_id)
    rsp = requests.get(page_url, headers=headers)
    # print(rsp.text)
    rsp.encoding = 'GBK'
    soup = BeautifulSoup(rsp.text, "lxml")

    ans_content2 = soup.select("#answer-content-{}".format(ans_id))
    try:
        if len(ans_content2) > 0:
            return '\n'.join([str(node) for node in ans_content2[0].contents[2:]])

        ans_content = soup.select("#best-content-{}".format(ans_id))
        if len(ans_content) > 0:
            return '\n'.join([str(node) for node in ans_content[0].contents[2:]])

    except TypeError as e:
        print(e)
        print("type err, page_url: {}, ans_id: {}".format(page_url, ans_id))
    except BaseException as e:
        print(e)
        print("base err, page_url: {}, ans_id: {}".format(page_url, ans_id))


    print("empty ans , page_url: {}, ans_id: {}".format(page_url, ans_id))

if __name__ == '__main__':
    print(get_ans_content("750943919372214452", "3116483628"))
    print(get_ans_content("333513610904849165", "3094230594"))