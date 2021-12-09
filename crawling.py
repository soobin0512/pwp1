# crowling_run.py
import calendar

import bs4
import urllib.request
from tkinter import *
from tkinter import ttk
import numpy as np


# def refresh(site, start=1):
#     if site == 'seoul' or site == 'all':
#         url = 'https://www.seoul.go.kr/coronaV/coronaStatus.do'
#         web_page = urllib.request.urlopen(url)
#         result = bs4.BeautifulSoup(web_page, 'html.parser')
#         return result
#     if site == 'naver' or site == 'all':
#         url = 'https://search.naver.com/search.naver?where=news&query=%EC%BD%94%EB%A1%9C%EB%82%98&start=' + str(start) + '1'
#         web_page = urllib.request.urlopen(url)
#         result = bs4.BeautifulSoup(web_page, 'html.parser')
#         return result


def seoul():
    # result = refresh('seoul')
    url = 'https://www.seoul.go.kr/coronaV/coronaStatus.do'
    web_page = urllib.request.urlopen(url)
    result = bs4.BeautifulSoup(web_page, 'html.parser')

    list_a = []
    list_b = []

    # 발생동향 서울시 크롤링
    list_t = []
    list_n = []
    i_c = 0
    for i in range(0, 4):
        if i == 0 or i == 2:
            i_c = 2
        elif i == 1 or i == 3:
            i_c = 1

        for j in range(0, i_c):
            for k in range(0, 2):
                selector = result.select_one('div.status-seoul > div > div:nth-of-type(' + str(i + 1) +
                                             ') > div:nth-of-type(' + str(j + 1) +
                                             ') > p:nth-of-type(' + str(k + 1) + ')').text
                if k == 0:
                    list_t.append(selector)
                elif k == 1:
                    list_n.append(selector)
    list_a.append([list_t, list_n])

    # 발생동향 대한민국 크롤링
    list_t = []
    list_n = []
    for i in range(0, 5):
        for j in range(0, 2):
            selector = result.select_one('div.status-korea > div > div > div:nth-of-type(' + str(i + 1) +
                                         ') > p:nth-of-type(' + str(j + 1) + ')').text
            if j == 0:
                list_t.append(selector)
            elif j == 1:
                list_n.append(selector)
    list_a.append([list_t, list_n])
    # print('range05 02 list', list_a)

    # 발생동향 자치구별 크롤링
    list_t = []
    list_n = []
    for i in range(0, 6):
        for j in range(0, 13):
            if i == 0 or i == 3:
                selector = result.select_one('tbody > tr:nth-child(' + str(i + 1) +
                                             ') > th:nth-child(' + str(j + 1) + ')').text
                list_t.append(selector)
                # print('list_t : ', list_t)
            elif i == 2 or i == 5:
                selector = result.select_one('tbody > tr:nth-child(' + str(i + 1) +
                                             ') > td:nth-child(' + str(j + 1) + ')').text
                list_n.append(selector)
                # print('list_n ; ', list_n)
    list_a.append([list_t, list_n])
    # print('range06 013 list', list_a)

    # 발생동향 연령대별 크롤링
    list_t = []
    list_n = []
    list_p = []

    for i in range(1, 10):
        selector = result.select_one('div.table-scroll > table > thead > tr > th:nth-child(' +
                                     str(i + 1) + ')').text
        print(selector)
        list_t.append(selector)
        for j in range(1, 3):
            selector = result.select_one('div.table-scroll > table > tbody > tr:nth-child(' +
                                         str(j) + ') > td:nth-child(' +
                                         str(i + 1) + ')').text
            if j == 1:
                list_n.append(selector)
            if j == 2:
                list_p.append(selector + ' %')
    print('연령대별 연령대 list_t : ', list_t)
    print('연령대별 확진자 list_n : ', list_n)
    print('연령대별 비율 list_p : ', list_p)

    list_a.append([list_t, list_n, list_p])

    # 발생동향 검사 및 확진자별 크롤링
    list_t = []
    list_n = []
    list_p = []
    list_q = []

    for i in range(1, 8):
        selector = result.select_one('div.table-scroll > table.tstyle-status-day >\
                                        thead > tr > th:nth-child(' + str(i+1) + ')').text
        list_t.append(selector)
        for j in range(1, 4):
            selector = result.select_one('div.table-scroll > table.tstyle-status-day > tbody > tr:nth-child(' +
                                         str(j) + ') > td:nth-child(' +
                                         str(i + 1) + ')').text
            if j == 1:
                list_n.append(selector)
            if j == 2:
                list_p.append(selector)
            if j == 3:
                list_q.append(selector + ' %')
    print('발생동향 검사 및 확진자별 날짜 list_t : ', list_t)
    print('발생동향 검사 및 확진자별 검사자 list_n : ', list_n)
    print('발생동향 검사 및 확진자별 확진자 list_p : ', list_p)
    print('발생동향 검사 및 확진자별 확진율 list_q : ', list_q)

    list_a.append([list_t, list_n, list_p, list_q])

    # 확진자 추이 달력 크롤링
    date = []  # 일자
    definite = []  # 총확진자
    addition = []  # 추가확진자

    cal_wrap = result.find(class_='clndar_wrap')

    for i in range(0, 5):
        for j in range(0, 7):
            cal_day = cal_wrap.select_one('tr:nth-child(' + str(i+1) + ') > td:nth-child(' + str(j+1) + ') > div > span.date').text
            date.append(cal_day)
            tot_val = cal_wrap.select_one('tr:nth-child(' + str(i + 1) + ') > td:nth-child(' + str(j + 1) + ') > div > span.tot_val').text
            definite.append(tot_val.strip())
            add_val = cal_wrap.select_one('tr:nth-child(' + str(i + 1) + ') > td:nth-child(' + str(j + 1) + ') > div > span.add_val').text
            addition.append(add_val.strip())
    # print(len(date), date)
    # print(len(definite), definite)
    # print(len(addition), addition)

    # 확진자 추이 달력 크롤링 2차원배열

    # date = []  # 일자
    # definite = []  # 총확진자
    # addition = []  # 추가확진자
    # cal = []
    #
    # cal_wrap = result.find(class_='clndar_wrap')
    #
    # for i in range(0, 5):
    #     for j in range(0, 7):
    #         cal_day = cal_wrap.select_one('tr:nth-child(' + str(i+1) + ') > td:nth-child(' + str(j+1) + ') > div > span.date').text
    #         date.append(cal_day)
    #         tot_val = cal_wrap.select_one('tr:nth-child(' + str(i + 1) + ') > td:nth-child(' + str(j + 1) + ') > div > span.tot_val').text
    #         definite.append(tot_val.strip())
    #         add_val = cal_wrap.select_one('tr:nth-child(' + str(i + 1) + ') > td:nth-child(' + str(j + 1) + ') > div > span.add_val').text
    #         addition.append(add_val.strip())
    #         cal.append(cal_day + ' 일 총확진자 ' + tot_val.strip() +'명, 신규확진자 '+ add_val.strip() + '명')
    # cal2 = np.array(cal).reshape(5, 7)
    # print('cal2 : ', cal2)



    selector = result.select_one('div.status-seoul > h4 > span').text
    list_b.append(selector)
    selector = result.select_one('div.status-korea > h4 > span').text
    list_b.append(selector)

    news()

    return list_a, list_b

def news():
    # driver = wd.Chrome(executable_path='./chromedriver.exe')

    url_news = 'https://search.naver.com/search.naver?query=%EC%BD%94%EB%A1%9C%EB%82%98&where=news&ie=utf8&sm=nws_hty'
    news_page = urllib.request.urlopen(url_news)
    res = bs4.BeautifulSoup(news_page, 'html.parser')
    news_list = []

    # 첫 번째 기사 제목
    first_title = res.find(class_='news_tit')
    selector = first_title.text
    print(selector)

    # sp_nws1 > div > div > a
    # sp_nws2 > div.news_wrap.api_ani_send > div > a
    # sp_nws4 > div.news_wrap.api_ani_send > div > a
    # sp_nws18 > div > div > a

    # 기사 제목 리스트
    list_news = res.find(class_='list_news')
    print(list_news)
    li = list_news.find_all(class_='news_tit')
    print('li : ', li)


    return news_list