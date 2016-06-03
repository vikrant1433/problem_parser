import sys
import time

from selenium import webdriver


class HackerRank(object):
    base_url = "http://hackerrank.com"

    def __init__(self, username, password):
        self.username = username
        self.password = password
        chrome_options = webdriver.ChromeOptions()
        prefs = {"download.default_directory": "/tmp"}
        chrome_options.add_experimental_option("prefs", prefs)
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        # self.browser = webdriver.Chrome()  # PhantomJS('phantomjs')

    def login(self):
        self.browser.get(self.base_url + "/login")
        self.browser.maximize_window()
        self.browser.find_element_by_css_selector('input[id="login"]').send_keys(self.username)
        self.browser.find_element_by_css_selector('input[id="password"][data-attr2="Login"]').send_keys(self.password)
        self.browser.find_element_by_css_selector("button.login-button").click()
        time.sleep(1)
        self.browser.find_element_by_css_selector('button#no-button').click()

    def teardown(self):
        self.browser.quit()

    def get_contest_problems(self, url):
        self.browser.get(url)
        time.sleep(2)
        problem_links = self.browser.find_elements_by_css_selector("h4 > a")
        return [link.get_attribute("href") for link in problem_links]

    def get_download_testcase_link(self, url):
        time.sleep(5)
        self.browser.get(url)
        time.sleep(5)
        more_btn = self.browser.find_element_by_id("sidebar-more-button")
        # print(more_btn.get_attribute("outerHTML"))
        time.sleep(1)
        more_btn.click()
        time.sleep(1)
        link = self.browser.find_element_by_id("test-cases-link")
        # print(link.get_attribute("outerHTML"))
        link.click()
        return link.get_attribute("href")


h = HackerRank("mailtovikrantpro@gmail.com", "041291985")

h.login()
time.sleep(2)
contest_link = sys.argv[1]
problem_links = h.get_contest_problems(contest_link)
# print(problem_links)
# f = open("testcase_links", "w")
# https://www.hackerrank.com/contests/mtech-cse-2016-practice-test-2/challenges/coin-change
# https://www.hackerrank.com/rest/contests/mtech-cse-2016-practice-test-2/challenges/coin-change/download_testcases
for link in problem_links:
    # print(link)
    download_url = "https://www.hackerrank.com/rest" + link[len("https://www.hackerrank.com"):] + '/download_testcases'
    h.browser.get(download_url)
    # testcase_link = h.get_download_testcase_link(link)
    # print(testcase_link)
    print(link)
time.sleep(60)
# f.close()

# class MyClass(object):
#     base_url = "hello"
#
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password


#
#
# tri = MyClass("1", "2")

# login_btn = browser.find_element_by_css_selector('a[href="/login"]')
# login_btn.click()
# browser.execute_script(open("jquery.js", "r").read())
# print(browser.execute_script('return $("input")')[0].get_attribute("outerHTML"))
# exit(0)

# print(user_name.get_attribute("outerHTML"))

# # print(user_name.get_attribute("outerHTML")) #source_code = elem.get_attribute("outerHTML")
# user_name.click()
# # //*[@id="password"]
# # print(password.get_attribute("outerHTML"))
# # password.submit()
# print(login_btn.get_attribute("outerHTML"))

# elem_present = EC.presence_of_element_located((By.ID, 'no-button'))
# try:
#     # WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'no-button')))
#     # print ("Page is ready!")
#     browser.find_element_by_css_selector('button#no-button').click()
#     # browser.execute_script('$("#no-button").click()')
# except TimeoutException:
#     print ("Loading took too much time!")
# time.sleep(2)
# browser.execute_script(open("jquery.js", "r").read())
# elem = browser.execute_script('$("no-button").click()')
# print(elem.text)
# no_login_btn = browser.execute_script('document.getElementById("no-button").click()')
# print(no_login_btn.get_attribute("outerHTML"))
# no_login_btn.click()

# no_login_btn = browser.find_element_by_css_selector('button#no-button')
# no_login_btn.click()
# print(no_login_btn.get_attribute("outerHTML"))
# no_login_btn.submit()

# login_btn.click()
# with open("out.html", "w") as f:
#     print(browser.page_source, file=f)
# elems = browser.find_elements_by_css_selector('button#no-button');
# print(elems)
# no_login_btn = browser.execute_script('return document.getElementById("no-button")')
#
# print(no_login_btn.get_attribute("outerHTML"))
# no_login_btn.click()
# no_login_btn = browser.find_element_by_css_selector('button#no-button')
# print(no_login_btn.get_attribute("outerHTML"))
# no_login_btn.submit()
# time.sleep(10);
# print(login_btn.text)


# from robobrowser import RoboBrowser



# Browse to a page with checkbox inputs
# https://www.codechef.com/submit/KOL1509
# def submit(b, problem_code, file_path):
#     b.open('https://www.codechef.com/submit/' + problem_code)
#     # with open("submit.html","w") as f:
#     #     print(b.parsed,file=f)
#     form = b.get_form('problem-submission')
#     form['language'].value = "44"
#     form['form_build_id'].value = form['form_build_id'].value
#     form['form_token'].value = form['form_token'].value
#     form['form_id'].value = form['form_id'].value
#     form['files[sourcefile]'].value = open(file_path, "r")
#     b.submit_form(form=form)
#     b.open("https://www.codechef.com/status/LADDU/")
#     with open("submit.html", "w") as f:
#         print(b.parsed, file=f)
#         # print(b.parsed)
#
#
# def login(b):
#     b.open('https://www.codechef.com/')
#     form = b.get_form(id='new-login-form')
#     # print(form)                            # <RoboForm vehicle=[]>
#     form['name'].value = 'vikrant1433'
#     form['pass'].value = '041291985'
#     form['form_build_id'].value = form['form_build_id'].value
#     form['form_id'].value = form['form_id'].value
#     b.submit_form(form)
#
#     # with open("login.html", "w") as f:
#     #     print(b.parsed, file=f)
#
#
# def logout(b):
#     b.open('https://www.codechef.com/')
#     # with open("logout.html", "w") as f:
#     #     print(b.parsed, file=f)
#     logout_link = b.select('.logout-link')[0]
#     # print(logout_link)
#     b.follow_link(logout_link)
#     # with open("logout.html", "w") as f:
#     #     print(b.parsed, file=f)


# browser = RoboBrowser(
#     user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102
# Safari/537.36')

# browser.session.headers['Cookie'] = 'enableIntellisenseUserPref=true;
# hackerrank_mixpanel_token=c0ab8247-a2e0-4fbb-98df-f2e6fa66bf2b;
# _hackerrank_session
# =BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJTI4MmFkMzQwZjBhZTM5OTg3OWE5ZGRmZDJhNWUyYmU2BjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMXgyRHkvYnJiQW9Tc1BEV0hoQ0pDKzFkdzdvWjhPbWM1ZVQzVWxneUtwSVU9BjsARg%3D%3D--c8a0ad625ce09a2c147ace20027e14ea08ddc067; session_id=jzjvy3bq-1464100677373; cdn_url=d3keuzeb2crhkn.cloudfront.net; hacker_editor_theme=light'
#
# browser.session.headers['Content-Type'] = 'text/html; charset=utf-8'
# browser.session.headers['ETag'] = 'aa9ea69c65906fcc6152901746d402ea'
# browser.session.headers['referer'] = 'https://www.hackerrank.com/domains/algorithms/graph-theory/difficulty/all
# /page/1'
# browser.session.headers['Upgrade-Insecure-Requests'] = '1'
# browser.session.headers['Host'] = 'www.hackerrank.com'
# browser.session.headers['Pragma'] = 'no-cache'
# browser.session.headers['Connection'] = 'keep-alive'
# browser.session.headers['Cache-Control'] = 'no-cache'
# browser.session.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
# browser.session.headers['Accept-Encoding'] = 'gzip, deflate, sdch'
# browser.session.headers['Accept-Language'] = 'en-US,en;q=0.8,ms;q=0.6,hi;q=0.4'

# browser.open('https://www.codechef.com/')
# browser.open('https://www.hackerrank.com/domains/algorithms/graph-theory/difficulty/all/page/1')
#
# with open("out.html", "w") as f:
#     print(browser.parsed, file=f)
# file_path = "/home/vikrant/coding/codechef/laddu/laddu.cpp"
# login(browser)
# submit(browser, "LADDU", file_path)
# logout(browser)


# import re
# import sys
#
# import requests, json
# from bs4 import BeautifulSoup


# with requests.Session() as c:
#     url = 'https://www.hackerrank.com/'
# login = 'mailtovikrantpro@gmail.com'
# password = '041291985'
# # c.get(url)
# login_data = dict(login = login, password = password)
# headers = {'Referer': url}
# response = c.post(url, data=login_data, headers=headers)
# # json_string = json.dumps(login_data)
# # print (type (json_string))
# response = json.loads(response.content.decode('ascii'))
# headers = {'Referer': url, 'X-CSRF-Token': response['csrf_token']}
# response = c.post(url, data=login_data, headers = headers)
# print (response)
# print(response.content)
# page = c.get(url)
# # page = c.get('https://www.hackerrank.com/domains/algorithms/graph-theory', headers=headers)
# print(page)
# with open("out.html","w") as out:
#     print (page.text, file=out)

# import urllib3

# if len(sys.argv) > 1:
#     problem_code = sys.argv[1]
# else:
#     problem_code = "LADDU"
# problem_code = problem_code.upper()
# url = sys.argv[1]
# url = "https://www.hackerrank.com/domains/algorithms/graph-theory"
# # print(url)
# r = requests.get(url)
#
# soup = BeautifulSoup(r.content, "html.parser")
# with open("tmp.html","w") as f:
#     print(soup.prettify(), file=f)
# inputs = soup.find_all('pre')
# print(inputs)
# num_tests=1
# for inp in inputs:
#     with open("input"+str(num_tests)+ ".txt", "w") as f:
#         print(inp.next_sibling.strip(), file=f)
#     num_tests += 1
#
# outputs = soup.find_all('b', text = re.compile('output:', re.IGNORECASE))
# num_tests=1
# for out in outputs:
#     with open("output"+str(num_tests)+ ".txt", "w") as f:
#         print(out.next_sibling.strip(), file=f)
#     num_tests += 1
#
# with open("num_tests", "w") as f:
#     print(num_tests-1, file=f)
# print(inputs)
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
# input_file = "input"
# output_file = "output"
# for i in range(0, len(tags), 2):
#     f = open(input_file + str(num_test)+".txt", "w")
#     f.write(tags[i].next_sibling.strip() + "\n")
#     f.close()
#
#     f = open(output_file + str(num_test)+".txt", "w")
#     f.write(tags[i + 1].next_sibling.strip() + "\n")
#     f.close()
#     num_test += 1
# with open("num_tests", "w") as f:
#     print(num_test-1, file=f)

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

# import os
# import sys
#


# with requests.Session() as c:
#     url = 'https://www.hackerrank.com/login'
#     login = 'mailtovikrantpro@gmail.com'
#     password = '041291985'
#     # c.get(url)
#     login_data = dict(login = login, password = password)
#     headers = {'Referer': url}
#     response = c.post(url, data=login_data, headers=headers)
#     # json_string = json.dumps(login_data)
#     # print (type (json_string))
#     response = json.loads(response.content.decode('ascii'))
#     headers = {'Referer': url, 'X-CSRF-Token': response['csrf_token']}
#     response = c.post(url, data=login_data, headers = headers)
#     # print (response)
#     # print(response.content)
#     page = c.get('https://www.hackerrank.com/login')
#     print(page)
#     with open("out.html","w") as out:
#         print (page.text, file=out)
#
#
#     # print (response.content['csrf_token'])
#     # post_data = {'email': email, 'answer': answer}
#
#     # response = request.post(URL, data=post_data, headers=headers)
#
#
#
#
#
#
# # import urllib3
# #
# # if len(sys.argv) > 1:
# #     problem_code = sys.argv[1]
# # else:
# #     problem_code = "you-shall-not-pass"
# # problem_code = problem_code.upper()
# # url = "https://www.hackerrank.com/contests/mtech-cse-2016-practice-test-1/challenges/" + problem_code
# # # print(url)
# # r = requests.get(url)
# #
# # soup = BeautifulSoup(r.content, "html.parser")
# # print (soup.prettify())
# # preTags = soup("pre")
# # # print (preTags)
# # soup = BeautifulSoup(str(preTags), "html.parser")
# # # print (soup.prettify())
# # tags = soup.find_all("b");
# # # print (tags)
# # # print(tags[4].next_sibling)
# # # print (len(tags))
# # num_test = 1
# # # os.chdir()
# # input_file = "in"
# # output_file = "out"
# # for i in range(0, len(tags), 2):
# #     f = open(input_file + str(num_test), "w")
# #     f.write(tags[i].next_sibling.strip() + "\n")
# #     f.close()
# #
# #     f = open(output_file + str(num_test), "w")
# #     f.write(tags[i + 1].next_sibling.strip() + "\n")
# #     f.close()
# #     num_test += 1
#
#     # while(sibling is not None):
#     #     print(sibling)
#     #     sibling = sibling.b.next_sibling
#
#     # print(soup)
#     # for t in preTags:
#     #
#     #     print (soup.b.next_sibling)
#     # pass
#     # [x.extract() for x in t.find_all("b")]
#     # print(t)
#     # children = t.findChildren()
#     # for child in children:
#     #     print (child)
#     # print (t.findNextSibling(text=None))
#
#
#     # inp = pre[1].strip('\n') + '\n'
#     # out = pre[3].strip('\n') +'\n'
#
#     # print(pre)
#
#
#     # f = open('in','w')
#     # f.write(inp) # python will convert \n to os.linesep
#     # f.close() # you can omit in most cases as the destructor will call it
#
#     # f = open('out','w')
#     # f.write(out) # python will convert \n to os.linesep
#     # f.close() # you can omit in most cases as the destructor will call it
#
#
#     # print(inp.strip('\n'))
#     # print (out.strip('\n'))
#     # for elem in pre.contents:
#     #     print(elem)
#     # print(pre.contents[1])
#     # [x.extract() for x in pre.find_all("b")]
#     # print (pre)
#     # print (soup.prettify())
#     # pre = BeautifulSoup(soup.find_all("pre"), "lxml")
#     # print (pre.prettify())
#     # [x.extract() for x in pre.find_all("b")]
#     # print (pre)
#     # print soup.html.head.title
#     # print(len(links))
#     # for link in pre:
#     #     print (link)
#     # print (r.content)
#
#     # print ('hello')
