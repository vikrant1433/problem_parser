import os
import sys

import requests, json
from bs4 import BeautifulSoup


with requests.Session() as c:
    url = 'https://www.hackerrank.com/login'
    login = 'mailtovikrantpro@gmail.com'
    password = '041291985'
    # c.get(url)
    login_data = dict(login = login, password = password)
    headers = {'Referer': url}
    response = c.post(url, data=login_data, headers=headers)
    # json_string = json.dumps(login_data)
    # print (type (json_string))
    response = json.loads(response.content.decode('ascii'))
    headers = {'Referer': url, 'X-CSRF-Token': response['csrf_token']}
    response = c.post(url, data=login_data, headers = headers)
    # print (response)
    # print(response.content)
    page = c.get('https://www.hackerrank.com/login')
    print(page)
    with open("out.html","w") as out:
        print (page.text, file=out)


    # print (response.content['csrf_token'])
    # post_data = {'email': email, 'answer': answer}

    # response = request.post(URL, data=post_data, headers=headers)






# import urllib3
#
# if len(sys.argv) > 1:
#     problem_code = sys.argv[1]
# else:
#     problem_code = "you-shall-not-pass"
# problem_code = problem_code.upper()
# url = "https://www.hackerrank.com/contests/mtech-cse-2016-practice-test-1/challenges/" + problem_code
# # print(url)
# r = requests.get(url)
#
# soup = BeautifulSoup(r.content, "html.parser")
# print (soup.prettify())
# preTags = soup("pre")
# # print (preTags)
# soup = BeautifulSoup(str(preTags), "html.parser")
# # print (soup.prettify())
# tags = soup.find_all("b");
# # print (tags)
# # print(tags[4].next_sibling)
# # print (len(tags))
# num_test = 1
# # os.chdir()
# input_file = "in"
# output_file = "out"
# for i in range(0, len(tags), 2):
#     f = open(input_file + str(num_test), "w")
#     f.write(tags[i].next_sibling.strip() + "\n")
#     f.close()
#
#     f = open(output_file + str(num_test), "w")
#     f.write(tags[i + 1].next_sibling.strip() + "\n")
#     f.close()
#     num_test += 1

    # while(sibling is not None):
    #     print(sibling)
    #     sibling = sibling.b.next_sibling

    # print(soup)
    # for t in preTags:
    #
    #     print (soup.b.next_sibling)
    # pass
    # [x.extract() for x in t.find_all("b")]
    # print(t)
    # children = t.findChildren()
    # for child in children:
    #     print (child)
    # print (t.findNextSibling(text=None))


    # inp = pre[1].strip('\n') + '\n'
    # out = pre[3].strip('\n') +'\n'

    # print(pre)


    # f = open('in','w')
    # f.write(inp) # python will convert \n to os.linesep
    # f.close() # you can omit in most cases as the destructor will call it

    # f = open('out','w')
    # f.write(out) # python will convert \n to os.linesep
    # f.close() # you can omit in most cases as the destructor will call it


    # print(inp.strip('\n'))
    # print (out.strip('\n'))
    # for elem in pre.contents:
    #     print(elem)
    # print(pre.contents[1])
    # [x.extract() for x in pre.find_all("b")]
    # print (pre)
    # print (soup.prettify())
    # pre = BeautifulSoup(soup.find_all("pre"), "lxml")
    # print (pre.prettify())
    # [x.extract() for x in pre.find_all("b")]
    # print (pre)
    # print soup.html.head.title
    # print(len(links))
    # for link in pre:
    #     print (link)
    # print (r.content)

    # print ('hello')
