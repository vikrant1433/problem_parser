import sys

import requests
from bs4 import BeautifulSoup

# import urllib3

# if len(sys.argv) > 1:
#     problem_code = sys.argv[1]
# else:
#     problem_code = "LADDU"
# problem_code = problem_code.upper()
url = sys.argv[1]
# print(url)
r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")
preTags = soup("pre")
# print (preTags)
soup = BeautifulSoup(str(preTags), "html.parser")
# print (soup.prettify())
tags = soup.find_all("b");
# print (tags)
# print(tags[4].next_sibling)
# print (len(tags))
num_test = 1
# os.chdir()
input_file = "input"
output_file = "output"
for i in range(0, len(tags), 2):
    f = open(input_file + str(num_test)+".txt", "w")
    f.write(tags[i].next_sibling.strip() + "\n")
    f.close()

    f = open(output_file + str(num_test)+".txt", "w")
    f.write(tags[i + 1].next_sibling.strip() + "\n")
    f.close()
    num_test += 1
with open("num_tests", "w") as f:
    print(num_test-1, file=f)

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
