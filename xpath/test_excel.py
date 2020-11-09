import requests
import re
import xlrd
from xlutils.copy import copy
from xlutils.copy import copy
import requests
import re

import xlrd as xlrd
import xlwt as xlwt
headers = {
    'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
}


def search(row,url):
    # try:
    #     browser.get(url)
    #     #WebDriverWait.until(browser,30)
    #     html = browser.page_source
    #     #print(html)
    #     soup = BeautifulSoup(html,'lxml')
    #     title = None
    #     abstract = None
    #     authors = None
    #     first_author = None
    #     PublishIn = None
    #     volume_list = None
    #     volume = None
    #     issue = None
    #     Date = None
    #     year = None
    #     month = None
    #     publisher = None
    #     keywords = None
    #     doi = None
    #     author_card = None
    #     institution = None
    #     if soup.find('h1', class_='document-title'):
    #         title = soup.find('h1', class_='document-title').text.strip()
    #         print(title)
    #     if soup.find('div', class_='abstract-text row'):
    #         abstract = soup.find('div', class_='abstract-text row').text.strip()
    #         abstract = re.sub(r'\n|\r|\t', '', abstract)
    #         abstract = re.sub('Abstract:', '', abstract)
    #         print(abstract)
    #     if soup.find('div', class_='authors-info-container overflow-ellipsis'):
    #         authors = soup.find('div', class_='authors-info-container overflow-ellipsis').text.strip()
    #         authors = re.sub(r'\n|\r|\t', '', authors)
    #         print(authors)
    #         list_author = authors.split(';')
    #         first_author = list_author[0]
    #         print(first_author)
    #         #u-pb-1 stats-document-abstract-publishedIn
    #     if soup.find('a', class_='u-pb-1 stats-document-abstract-publishedIn'):
    #         PublishIn = soup.find('div', class_='u-pb-1 stats-document-abstract-publishedIn').text.strip()
    #         PublishIn = re.sub(r'\n|\r|\t', '', PublishIn)
    #         PublishIn = re.sub('Published in: ', '', PublishIn)
    #         volume_list = re.findall(r"\b\d+\b", PublishIn)
    #         print(volume_list)
    #         volume = volume_list[0]
    #         issue = volume_list[1]
    #         print(''+PublishIn)
    #     if soup.find('div', class_='u-pb-1 doc-abstract-pubdate'):
    #         Date = soup.find('div', class_='u-pb-1 doc-abstract-pubdate').text.strip()
    #         Date = re.sub(r'\n|\r|\t', '', Date)
    #         Date = re.sub('Date of Publication:', '', Date)
    #         print(''+Date)
    #         month = ''.join(re.findall(r'[A-Za-z]', Date))
    #         print(month)
    #         Data_list = Date.split(' ')
    #         year = Data_list[len(Data_list)-1]
    #         print(year)
    #     if soup.find('div', class_='u-pb-1 doc-abstract-publisher publisher-info-container black-tooltip'):
    #         publisher = soup.find('div', class_='u-pb-1 doc-abstract-publisher publisher-info-container black-tooltip').text.strip()
    #         publisher = re.sub(r'\n|\r|\t', '', publisher)
    #         publisher = re.sub('Publisher:', '', publisher)
    #         print(publisher)
    #         #doc-keywords-list-item
    #     if soup.find('li', class_='doc-keywords-list-item'):
    #         keywords = soup.find('li', class_='doc-keywords-list-item').text
    #         keywords = re.sub(r'\n|\r|\t', '', keywords)
    #         keywords = keywords.replace('Keywords', 'Keywords:')
    #         keywords = re.sub('IEEE Keywords:', '', keywords)
    #         print(keywords)
    #     if soup.find('div', class_='u-pb-1 stats-document-abstract-doi'):
    #         doi = soup.find('div', class_='u-pb-1 stats-document-abstract-doi').text.strip()
    #         doi = re.sub(r'\n|\r|\t', '', doi)
    #         doi = re.sub('DOI:', '', doi)
    #         print(doi)
    #     if title != None:
    #         work_book = xlrd.open_workbook("IEEE.xls")
    #         sheet = work_book.sheet_by_name('TransactionsCommunications')
    #         rows = sheet.nrows
    #         new_workbook = copy(work_book)
    #         new_worksheet = new_workbook.get_sheet('TransactionsCommunications')
    #         new_worksheet.write(rows, 0, title)
    #         new_worksheet.write(rows, 1, authors)
    #         #Institutions_1
    #         new_worksheet.write(rows, 2, first_author)
    #         new_worksheet.write(rows, 3, PublishIn)
    #         new_worksheet.write(rows, 4, volume)
    #         new_worksheet.write(rows, 5, issue)
    #         new_worksheet.write(rows, 6, Date)
    #         new_worksheet.write(rows, 7, year)
    #         new_worksheet.write(rows, 8, month)
    #         new_worksheet.write(rows, 9, publisher)
    #         new_worksheet.write(rows, 10, keywords)
    #         new_worksheet.write(rows, 11, abstract)
    #         new_worksheet.write(rows, 12, doi)
    #         new_workbook.save("IEEE.xls")
    # except TimeoutException:
    #     return search(row,url)
    response = requests.get(url=url, headers=headers)
    # print(response)
    # response.json().get('doi')#
    html = response.text
    # print(html)
    pattern = 'global.document.metadata'
    # # res = re.match(pattern,html)
    # # print(res.group())
    # html = response.content.decode('utf-8')
    # print(html)
    res = re.search('global.document.metadata.*', html)
    title = None
    authors = ''
    first_author = None
    institution = None
    doi = None
    date = None
    year = None
    month = None
    published_in = None
    volume = None
    issue = None
    publisher = None
    keywords = None
    abstract = None
    if res:
        # data = res[0]
        data = res.group()
        print(data)
        print('-' * 100)
        # doi = re.search(r'doi":"\d+.\d+/[\w]+.[\d]+.[\d]+',data)
        # print(doi.group())
        doi_str = re.search(r'"doi":"[\w\s./]+[^"]', data)
        # print('doi2+'+doi2.group())
        # print(doi[0])
        if doi_str:
        # num2 = re.search(r'[\d].{1,30}[\d]',doi2.group())
        # print(num2.group())displayDoctitle
            doi = re.sub(r'doi":"', '', doi_str.group())
            print('doi: ' + doi)
        title_str = re.search(r'displayDocTitle":"[\w][^"]+', data)
        # print(title.group())
        if title_str:
            print(title_str.group())
        # title_result = title_str.group()
        # title1 = title_result.split(',')
        # print(title1[0])
            title = re.sub(r'displayDocTitle":"', '', title_str.group())
            print('title: ' + title)
        authors_list = re.findall(r'"name":".+,"affiliation"', data)
        if len(authors_list) > 0:
            #authors_str = authors_list[0]
            authors_str = re.findall(r'"name":"[\w\s.-]+[^"]',authors_list[0])
        print(authors_str)
        if len(authors_str) > 0:
            #i = 0
            for name in authors_str:
                #print(len(authors_str))
                name1 = re.sub(r'"name":"', '', name)
                #print(name1)
                authors = authors + name1 + ';'
            print(authors)
            first_author = re.sub(r'"name":"','',authors_str[0])
            print(first_author)
                # author = re.search(r'[\w].{0,40}[\w]', name1)
                # if author:
                #     authors_list[i] = author.group()
                    #print('author: ' + authors_list[i])
                    #first_author = authors_list[0]
                    # print('first_author: ' + first_author)
                    #i += 1
                # else:
                #     print('no author')
            #author_last = authors_list[len(authors_list)-1]
            # if "IEEE" in author_last:
            #     authors_list.pop(len(authors_list)-1)
            # for i in authors_list:
            #     if "IEEE" in str(i):
            #         authors_list.remove(i)
            # authors = ';'.join(str(i) for i in authors_list)
            # au = re.sub(r';','',authors)
            #print('authors: ' + au)
            #print('authors: ' + authors)
            # if len(authors_list) > 0:
            #     first_author = authors_list[0]
            #     print('first_author:', first_author)
        institution_str = re.search(r'"affiliation":."[\w][^"]+',data)
        if institution_str:
            institution_str1 = re.search(r'[A-Z][^"]+', institution_str.group())
            if institution_str1:
                institution = institution_str1.group()
                print('institution: ' + institution)
        online_date = re.search(
            r'"onlineDate":"\d.{0,30}\d|"conferenceDate":"\d.{0,30}\d|"dateOfInsertion":"\d[\w\s]{0,30}', data)
        if online_date:
            #print(online_date)
            date = re.sub(r'"onlineDate":"|"conferenceDate":"|"dateOfInsertion":"', '', online_date.group())
            print('date: ' + date)
            publication_year = re.search(r'"publicationYear":"\d{4}', data)
            # if publication_year:
            #     year = re.sub(r'"publicationYear":"', '', publication_year.group())
            #     print('year: ' + year)
            year = re.search('20\d{2}',date).group()
            print('year:'+ year)
            month_str = re.search(r'[A-Z][\w]+',date)
            if month_str:
                month = month_str.group()
                print('month: ' + month)
        publication_title = re.search(r'"publicationTitle":"[A-Z][\w\s]+[a-z]', data)
        if publication_title:
            published_in = re.sub(r'"publicationTitle":"', '', publication_title.group())
            print('published_in: ' + published_in)
        volume_str = re.search(r'"volume":"\d{0,3}', data)
        if volume_str:
            volume = re.sub(r'"volume":"', '', volume_str.group())
            print('volume: ' + volume)
        issue_str = re.search(r'"issue":"\d{0,3}', data)
        if issue_str:
            issue = re.sub(r'"issue":"', '', issue_str.group())
            print('issue: ' + issue)
        publisher_str = re.search(r'"publisher":"[A-Z][\w\s]+', data)
        if publisher_str:
            publisher = re.sub(r'"publisher":"', '', publisher_str.group())
            print('publisher: ' + publisher)
        keywords_str = re.search(r'"kwd":."[\w]+[^]]+', data)
        if keywords_str:
            # keywords = keywords_str.group()
            print(keywords_str.group())
            #keywords1 = re.search(r'[A-Z][^]]+', keywords_str.group())
            # print(keywords1.group())
            keywords = re.sub(r'"kwd":."', '', keywords_str.group())
            keywords = re.sub(r'"','',keywords)
            print('keywords: ' + keywords)
        abstract_str = re.search(r'"abstract":"[A-Z][^"]*', data)
        if abstract_str:
            abstract = re.sub(r'"abstract":"', '', abstract_str.group())
            print('abstract: ' + abstract)
        print('*' * 100)
        work_book = xlrd.open_workbook("IEEE.xls")
        sheet = work_book.sheet_by_name('TransactionsCommunications')
        rows = sheet.nrows
        new_workbook = copy(work_book)
        new_worksheet = new_workbook.get_sheet('TransactionsCommunications')
        new_worksheet.write(rows, 0, title)
        new_worksheet.write(rows, 1, authors)
        new_worksheet.write(rows, 2, first_author)
        new_worksheet.write(rows, 3, institution)
        new_worksheet.write(rows, 4, published_in)
        new_worksheet.write(rows, 5, volume)
        new_worksheet.write(rows, 6, issue)
        new_worksheet.write(rows, 7, date)
        new_worksheet.write(rows, 8, year)
        new_worksheet.write(rows, 9, month)
        new_worksheet.write(rows, 10, publisher)
        new_worksheet.write(rows, 11, keywords)
        new_worksheet.write(rows, 12, abstract)
        new_worksheet.write(rows, 13, doi)
        new_workbook.save("IEEE.xls")
    else:
        print('no')
def save_to_excel():
    urls = []
    row = 0
    for url in open('IEEE Transactions on Communications.txt'):
        if url.strip('\n') != '':
            urls.append(url.strip('\n') + 'keywords')
            search(row,urls[row])
            row += 1


def main():
    # save_to_excel()
    url = 'https://ieeexplore.ieee.org/document/5611612/keywords#keywords'
    search(0,url)


if __name__ == '__main__':
    main()
