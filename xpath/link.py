import math

import requests
import re
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
wait = WebDriverWait(browser,30)
headers = {
    'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
}
url = 'https://ieeexplore.ieee.org/search/searchresult.jsp?queryText=IEEE%20Journal%20on%20Selected%20Areas%20in%20Communications&highlight=true&returnType=SEARCH&matchPubs=true&ranges={}_{}_Year&returnFacets=ALL&pageNumber={}'
#https://ieeexplore.ieee.org/search/searchresult.jsp?queryText=IEEE%20Transactions%20on%20Systems,%20Man%20and%20Cybernetics,%20Part%20C:%20Applications%20and%20Reviews&highlight=true&returnType=SEARCH&matchPubs=true&pageNumber=1&ranges=2010_2013_Year&returnFacets=ALL
#https://ieeexplore.ieee.org/search/searchresult.jsp?queryText=IEEE%20Transactions%20on%20Systems,%20Man%20and%20Cybernetics,%20Part%20C:%20Applications%20and%20Reviews&highlight=true&returnType=SEARCH&matchPubs=true&pageNumber=4&ranges=2010_2013_Year&returnFacets=ALL
#https://ieeexplore.ieee.org/search/searchresult.jsp?queryText=IEEE%20Transactions%20on%20Systems,%20Man%20and%20Cybernetics,%20Part%20C:%20Applications%20and%20Reviews&highlight=true&returnType=SEARCH&matchPubs=true&pageNumber=3&ranges=2010_2013_Year&returnFacets=ALL
#https://ieeexplore.ieee.org/search/searchresult.jsp?queryText=IEEE%20Transactions%20on%20Systems,%20Man%20and%20Cybernetics,%20Part%20C:%20Applications%20and%20Reviews&highlight=true&returnType=SEARCH&matchPubs=true&ranges=2010_2013_Year&returnFacets=ALL&pageNumber=2
#https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText=IEEE%20Transactions%20on%20Systems,%20Man%20and%20Cybernetics,%20Part%20C:%20Applications%20and%20Reviews&highlight=true&returnFacets=ALL&returnType=SEARCH&matchPubs=true&pageNumber=2
# def get_list(url):
#     # response = requests.get(url=url, headers=headers)
#     # html = response.content.decode('utf-8')
#     # print(html)
#     html = browser.get(url)

def get_list(url):
    y = 'https://ieeexplore.ieee.org/search/searchresult.jsp?queryText=IEEE%20Journal%20on%20Selected%20Areas%20in%20Communications&highlight=true&returnFacets=ALL&returnType=SEARCH&matchPubs=true&ranges={}_{}_Year'
    for year in range(2020,2021):
        every_year = y.format(year,year)
        print(every_year)
        #total = 'https://ieeexplore.ieee.org/search/searchresult.jsp?queryText=IEEE%20Solid-State%20Circuits%20Magazine&highlight=true&returnFacets=ALL&returnType=SEARCH&matchPubs=true&ranges=2015_2016_Year'
        pages = get_page_count(every_year)
        #url_list = url + '_Year&pageNumber={}'
        print(pages)
        page = 1
        try:
            while page <= pages:
                print(url.format(year,year,page))
                browser.get(url.format(year,year,page))
                locator_link_list = (By.XPATH, '//*[@id="xplMainContent"]/div[2]/div[2]/xpl-results-list/div/xpl-results-item/div[1]/div[1]/div[2]/h2/a')
                WebDriverWait(browser, 60, 0.5).until(expected_conditions.presence_of_element_located(locator_link_list))
                link_list = browser.find_elements_by_xpath(
                    '//*[@id="xplMainContent"]/div[2]/div[2]/xpl-results-list/div/xpl-results-item/div[1]/div[1]/div[2]/h2/a')
                for link in link_list:
                    ele_num = link.get_attribute('href')
                    print(ele_num)
                    herf_txt = open('2.txt','a',encoding='utf-8')
                    herf_txt.write(ele_num+'\n')
                    herf_txt.close()
                    #search(ele_num)
                page += 1
        except TimeoutException:
            browser.close()
        return get_list()


def get_page_count(url):
    try:
        browser.get(url)
        n = 0
        locator = (By.XPATH, '//*[@id="xplMainContent"]/div[1]/div[2]/xpl-search-dashboard/section/div/div[1]/span')
        WebDriverWait(browser, 30, 0.5).until(expected_conditions.presence_of_element_located(locator))
        if browser.find_element_by_xpath(
                '//*[@id="xplMainContent"]/div[1]/div[2]/xpl-search-dashboard/section/div/div[1]/span'):
            if browser.find_element_by_xpath(
                    '//*[@id="xplMainContent"]/div[1]/div[2]/xpl-search-dashboard/section/div/div[1]/span').text != 'No results found':
                number = browser.find_element_by_xpath(
                    '//*[@id="xplMainContent"]/div[1]/div[2]/xpl-search-dashboard/section/div/div[1]/span[1]/span[2]').text
                number = number.replace(",", '')
                n = int(number) / 25
                n = math.ceil(n)
                print(n)
                return n
    except TimeoutException:
        return get_page_count()


def main():
    get_list(url)
    #get_page_count(url)


if __name__ == '__main__':
    main()