import re

import cv2
from bs4 import BeautifulSoup
from bs4.element import NavigableString
import requests
import urllib.request  # 发送网络请求，获取数据
import gzip  # 压缩和解压缩模块
import json  # 解析获得的数据
from PIL import Image
import os
import matplotlib.pylab as pyl


def getWeatherData(city_name):
    url_city = "https://www.tianqi.com/tianqi/ctiy?keyword=" + urllib.parse.quote(city_name)
    url = ""
    headers = {

        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'accept': 'application/json, text/javascript, */*; q=0.01',
    }
    # print(url_city)
    resp_city = requests.get(url_city, headers=headers)
    # print(resp_city.json())

    for i in resp_city.json():
        if (i['name'] == city_name or i['pid_name'] == city_name):
            url = i['url']
            break
    resp = requests.get(url, headers=headers)
    print(resp.encoding)

    html = resp.content.decode('utf8')
    soup = BeautifulSoup(html, 'html.parser')
    body = soup.body
    data = body.find("div", {"class": "wrap1100"})
    data_weather = data.find('dd', {'class': 'weather'})
    data_kongqi = data.find('dd', {'class': 'kongqi'})
    data_shidu = data.find("dd", {"class": "shidu"})
    img_url = data.find('img')['src']

    img_path_endWith = (img_url.split('.'))[-1]
    print((img_url.split('.'))[-1])
    print(img_url)
    path = 'C:/Users/jiongjiong/PycharmProjects/WeatherShow/cityImg/'
    img_path = os.path.join(path, city_name + '.' + img_path_endWith)
    img = requests.get(img_url).content
    with open(img_path, 'wb') as f:
        f.write(img)
    try:
        im = Image.open(img_path)
        im_resize = im.resize((51, 51))
        im_resize.save(img_path)
        print(img_path)
    except:
        print("图片无法加载!")

    week = ''
    shidu_list = []
    now_tempera = ''
    today_tempera = []
    kognqi = []
    for i in data_shidu.strings:
        shidu_list.append(i)

    week = data.find('dd', {'class': 'week'}).string

    now_tempera_data = data.find('p', {'class': 'now'})
    for i in now_tempera_data.strings:
        now_tempera = now_tempera + i

    today_tempera_data = data_weather.find('span')
    for i in today_tempera_data.strings:
        today_tempera.append(i)

    for i in data_kongqi.strings:
        kognqi.append(i)

    weather_img_url = 'https:' + data_weather.find('img')['src']
    weather_headers = {

        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'Accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
        'referer': 'https://www.tianqi.com/'
    }

    weather_img = requests.get(weather_img_url, headers=weather_headers).content
    img_endwith = '.' + weather_img_url.split('.')[-1]
    path = 'C:/Users/jiongjiong/PycharmProjects/WeatherShow/weatherImg/'
    weather_img_path = os.path.join(path, today_tempera[0] + img_endwith)
    print(weather_img_path)
    with open(weather_img_path, 'wb') as f:
        f.write(weather_img)
    weather_im = Image.open(weather_img_path)
    weather_im_resize = weather_im.resize((61, 61))
    weather_im_resize.save(weather_img_path)

    print(week)
    print(now_tempera)
    print(today_tempera)
    print(shidu_list)
    print(kognqi)
    dict = {}
    # 返回日期，当前温度，今日温度，湿度信息，空气信息，天气标志图片
    return week, now_tempera, today_tempera, shidu_list, kognqi, weather_img_path




#获得预测的天气数据，并生成气温变化曲线
def get_weather_data(city_name):  # 获取网站数据
    list_high = []
    list_low = []
    url1 = 'http://wthrcdn.etouch.cn/weather_mini?city=' + urllib.parse.quote(city_name)
    print(url1)
    weather_data = requests.get(url1)
    print((weather_data.json().get('data'))['forecast'])
    forecast_data = (weather_data.json().get('data'))['forecast']
    pattern = re.compile(r'.?\d+')
    for i in forecast_data:
        result_high = re.findall(pattern, i['high'])
        result_low = re.findall(pattern, i['low'])
        list_high.append(int(result_high[0]))
        list_low.append(int(result_low[0]))
    print(list_high, list_low)
    mid_tempare = list(map(lambda x, y: int((x + y) * 5), list_high, list_low))
    x_aix = [10, 20, 30, 40, 50]
    print(mid_tempare)
    pyl.plot(x_aix, mid_tempare)
    pyl.plot(x_aix, mid_tempare, 'o')
    for i in range(5):
        pyl.text(x_aix[i], mid_tempare[i] + 1.5, str(list_high[i]) + '℃')
        pyl.text(x_aix[i], mid_tempare[i] - 3, str(list_low[i]) + '℃')
    pyl.savefig('tempare_change.png')
    tempera = Image.open('C:/Users/jiongjiong/PycharmProjects/WeatherShow//tempare_change.png')
    tempera_resize = tempera.resize((320, 240))
    tempera_resize.save('C:/Users/jiongjiong/PycharmProjects/WeatherShow//tempare_change.png')
    pyl.show()
    return forecast_data


if __name__ == '__main__':
    get_weather_data('南阳')
    # getWeatherData('成都')

# for child in data3.contents:
#     print(child)
#     if(isinstance(child,NavigableString)):
#         print(child.string)


# print(data.contents[1].children)
# for child in data.contents[1].children:
#     print(child)
# for child in data.children:
#     print(type(child))
# ul = data.find("ul")
# li = ul.find_all("li")
# print(li)
