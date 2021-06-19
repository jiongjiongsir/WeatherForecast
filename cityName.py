import requests
from bs4 import BeautifulSoup
import pymysql
import time


class Administrative(object):
    def __init__(self):

        self.main()

    def main(self):
        base_url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2018/'
        trs = self.get_response(base_url, 'provincetr')
        for tr in trs:  # 循环每一行
            datas = []
            for td in tr:  # 循环每个省
                province_name = td.a.get_text()
                province_url = base_url + td.a.get('href')
                print(province_name)
                trs = self.get_response(province_url, None)
                for tr in trs[1:]:  # 循环每个市
                    city_code = tr.find_all('td')[0].string
                    city_name = tr.find_all('td')[1].string
                    city_url = base_url + tr.find_all('td')[1].a.get('href')
                    trs = self.get_response(city_url, None)
                    for tr in trs[1:]:  # 循环每个区
                        county_code = tr.find_all('td')[0].string
                        county_name = tr.find_all('td')[1].string
                        data = [province_name, city_code, city_name, county_code, county_name]
                        print(data)
                        datas.append(data)
                    time.sleep(1)


    def get_response(self, url, attr):
        response = requests.get(url)
        response.encoding = 'gb2312'  # 编码转换
        soup = BeautifulSoup(response.text, 'lxml')
        table = soup.find_all('tbody')[1].tbody.tbody.table
        if attr:
            trs = table.find_all('tr', attrs={'class': attr})
        else:
            trs = table.find_all('tr')
        return trs


if __name__=='__main__':
    Administrative()