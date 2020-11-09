import re
import ast


# data = 'QiaoLulu20200914'
# result = re.match('Q',data)
# print(result)
# print(result.group())
import requests
from bs4 import BeautifulSoup
url = 'https://ieeexplore.ieee.org/document/6509229/keywords#keywords'
#url = 'https://ieeexplore.ieee.org/search/searchresult.jsp?queryText=IEEE%20Transactions%20on%20Smart%20Grid&highlight=true&returnFacets=ALL&returnType=SEARCH&matchPubs=true&ranges=2010_2014_Year&pageNumber=2'
headers = {
    'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
}

response = requests.get(url=url,headers=headers)
# print(response)
#response.json().get('doi')#
html = response.text
#print(html)
pattern = 'global.document.metadata'
# # res = re.match(pattern,html)
# # print(res.group())
#html = response.content.decode('utf-8')
#print(html)
res = re.search('global.document.metadata.*',html)
title = None
authors = [0] * 100
first_author = None
institution = None
doi = None
date = None
year = None
month = None
if res:
    #data = res[0]
    data = res.group()
    print(data)
    #doi = re.search(r'doi":"\d+.\d+/[\w]+.[\d]+.[\d]+',data)
    #print(doi.group())
    doi2 = re.search(r'"doi":".{1,40}[\d]',data)
    #print('doi2+'+doi2.group())
    #print(doi[0])
    doi_str = doi2.group()
    # num2 = re.search(r'[\d].{1,30}[\d]',doi2.group())
    # print(num2.group())
    doi = re.sub(r'doi":"','',doi_str)
    print('doi: '+ doi)
    title_str = re.search(r'title":".*',data)
    #print(title.group())
    title_result = title_str.group()
    title1 = title_result.split(',')
    print(title1[0])
    title = re.sub(r'title":','',title1[0])
    print('title: '+ title)
    authors_list = re.findall(r'"name":.{0,40}",',data)
    print(authors_list)
    i = 0
    for name in authors_list:
        author = re.search(r'[A-Z].{0,40}[\w]',name).group()
        authors[i] = author
        i += 1
        print('author: '+ author)
    first_author = authors[0]
    print('first_author: '+ first_author)
    institution_str = re.search(r'"affiliation":."[\w][^"]+',data).group()
    institution = re.search(r'[A-Z][^"]+',institution_str)
    print('institution: '+ institution.group())
    online_date = re.search(r'"onlineDate":".{0,20}\d',data).group()
    print(online_date)
    date = re.sub(r'"onlineDate":"','',online_date)
    print('date' + date)
    publication_year = re.search(r'"publicationYear":"\d{4}',data).group()
    year = re.sub(r'"publicationYear":"','',publication_year)
    print('year: ' + year)
    keywords_str = re.search(r'"kwd":."[\w]+[^]]+', data)
    if keywords_str:
        # keywords = keywords_str.group()
        print(keywords_str.group())
        # keywords1 = re.search(r'[A-Z][^]]+', keywords_str.group())
        # print(keywords1.group())
        keywords = re.sub(r'"kwd":."', '', keywords_str.group())
        keywords = re.sub(r'"','',keywords)
        print('keywords: ' + keywords)
   # print(institution_str.group())
else:
    print('no')
#soup = BeautifulSoup(html,'lxml')
#print(soup)

# title = None
# if soup.find('title'):
#     title = soup.find('title').text.strip()
#     print(title)
# scriptText = None
# if soup.find('script'):
#     scriptText = soup.find('script')
#     print(scriptText)
# # if soup.find('abstract'):
# #     abstract = soup.find('abstract').text.strip()
# #     abstract = re.sub(r'\n|\r|\t', '', abstract)
# #     abstract = re.sub('Abstract:', '', abstract)
#     print(abstract)
# dianData = 'Qll'
# dianResult = re.match('.',dianData)
# print(dianResult.group())

# groupData = 'luluQiao'
# pattern = '[Ql]'
# result = re.match(pattern,groupData)
# if result:
#     print(result.group())
# else:
#     print('None')
# data = 'Qiaolulu'
# pattern = '[A-Z][a-z]*'
# pattern2 = '[a-z]*[A-Z]'
# result = re.match(pattern,data)
# result2 = re.match(pattern2,data)
# print(result.group())
# print(result2.group())
# data1 = 'qiaoL66_'
# pattern = '[a-zA-Z]{1,5}'
# result1 = re.match(pattern,data1)
# print(result1.group())
# email = re.match('[a-zA-Z0-9]{6,11}@163.com','qll766@163.com')
# if email:
#     print('匹配成功{}'.format(email.group()))
#     pass
# filePath1 = 'D:\software\pycharm'
# filePath2 = 'D:\\software\\pycharm'
# print(filePath1)
# print(filePath2)
#email = re.match('[\w]{5,15}@[\w]{2,3}.com$','qll766@qq.com')
# data = 'beijingyoudian2020'
# result = re.match('(beijingyou|beijingyoudian2020)', data)
# print(result.group())
# res = re.match('([0-9]*)-(\d*)','1000-234567')
# print(res.group())
# print(res.group(1))
# print(res.group(2))
# htmlTag = '<html><h1>测试数据</h1></html>'
# res = re.match(r'<(.+)><(.+)>(.+)</\2></\1>',htmlTag)
# print(res.group())
# data = '今天三节课，block chain 好困'
# res = re.search('b[\w]*[\W]*[a-z]*',data)
# print(res.group())
