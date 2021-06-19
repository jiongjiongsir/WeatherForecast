import os
import urllib
import re
import matplotlib.pylab as pyl
import requests


# url = 'https://static.tianqistatic.com/static/wap2018/ico1/b1.png'
# headers = {
#
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
#     'Accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
#     'referer': 'https://www.tianqi.com/'
# }
#
# data = requests.get(url, headers=headers)
# img=data.content
# img_endwith=url.split('.')[-1]
# print(img_endwith)
# path = 'C:/Users/jiongjiong/PycharmProjects/WeatherShow/weatherImg/'
# img_path = os.path.join(path,img_endwith)
# with open(img_path, 'wb') as f:
#     f.write(img)
# url='https://static.tianqistatic.com/static/js/canvas.js'
# headers={
# 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
# 'accept': '*/*',
# 'referer': 'https://www.tianqi.com/'
#
# }
# data=requests.get(url,headers=headers)
# print(data.text)

# 生成温度曲线
def get_weather_data(city_name):  # 获取网站数据
    list_high = []
    list_low = []
    url1 = 'http://wthrcdn.etouch.cn/weather_mini?city=' + urllib.parse.quote(city_name)
    url2 = 'http://wthrcdn.etouch.cn/weather_mini?citykey=101010100'
    # 网址1只需要输入城市名，网址2需要输入城市代码
    print(url1)
    weather_data = requests.get(url1)
    # print((weather_data.json().get('data'))['forecast'])
    forecast_data = (weather_data.json().get('data'))['forecast']
    pattern = re.compile(r'.?\d+')
    for i in forecast_data:
        result_high = re.findall(pattern, i['high'])
        result_low = re.findall(pattern, i['low'])
        list_high.append(int(result_high[0]))
        list_low.append(int(result_low[0]))
    print(list_high, list_low)
    mid_tempare=list(map(lambda x,y:int((x+y)/2),list_high,list_low))
    x_aix=[10,20,30,40,50]
    print(mid_tempare)
    pyl.plot(x_aix,mid_tempare)
    pyl.plot(x_aix,mid_tempare,'o')
    pyl.text(x_aix[0], mid_tempare[0]+0.5, '7')
    pyl.text(x_aix[0]+2,mid_tempare[0],'7')
    pyl.show()
    pyl.savefig('tempare_change.png')
    return forecast_data


if __name__ == '__main__':
    get_weather_data('沈阳')
