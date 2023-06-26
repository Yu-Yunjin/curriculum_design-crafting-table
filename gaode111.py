# encoding:utf-8
import requests
import base64
import xlrd

'''
天气查询
'''


def checkWeather(adcode):
    request_url = "https://restapi.amap.com/v3/weather/weatherInfo?city=" + adcode + \
                  "&key=2150dfb6e7d3dbbaf89c9df87998c829"
    response = requests.get(request_url)
    response.raise_for_status()  # 检查响应是否正常
    weather_data = response.json()
    if weather_data is None:
        return "Error: failed to parse the response as JSON."
    return weather_data


def sfe(ans, flag=0):
    book = xlrd.open_workbook('citycode1.xls')
    sh = book.sheet_by_index(0)
    nrow = sh.nrows
    adcode = '110000'
    for i in range(1, nrow):
        data = sh.row(i)
        cellcheck = sh.cell_value(i, flag)
        if ans in cellcheck:
            adcode = sh.cell_value(i, 1)
            break
    return adcode


def gaode_getweather(city):
    str_city = city
    adcode = sfe(str_city)
    weather = checkWeather(adcode)
    if weather == "Error: no response.":
        weather_text = weather
    elif weather['status'] == 0:
        weather_text = "Error: check status."
    else:
        weather_text = str_city + "今天" + weather['lives'][0]['weather'] + "，" + weather['lives'][0]['winddirection'] \
                       + "风" + weather['lives'][0]['windpower'] + "级，气温" + weather['lives'][0]['temperature'] + \
                       "度，空气湿度" + weather['lives'][0]['humidity'] + "%。"
        # print(weather)
    return weather_text


def checkForeWeather(adcode):
    request_url = "https://restapi.amap.com/v3/weather/weatherInfo?city=" + adcode + \
                  "&key=2150dfb6e7d3dbbaf89c9df87998c829&extensions=all"
    response = requests.get(request_url)
    response.raise_for_status()  # 检查响应是否正常
    weather_data = response.json()
    if weather_data is None:
        return "Error: failed to parse the response as JSON."
    return weather_data


def gaode_getforeweather(city):
    str_city = city
    adcode = sfe(str_city)
    weather = checkForeWeather(adcode)
    if weather == "Error: no response.":
        weather_text = weather
    elif weather['status'] == 0:
        weather_text = "Error: check status."
    else:
        # print(weather)
        weather_text = str_city + "明天白天" + weather['forecasts'][0]['casts'][2]['dayweather'] + "，" + \
                       weather['forecasts'][0]['casts'][2]['daywind'] \
                       + "风" + weather['forecasts'][0]['casts'][2]['daypower'] + "级，气温" + \
                       weather['forecasts'][0]['casts'][2]['daytemp'] + \
                       "度。"

    return weather_text


'''
经纬度查询
'''


def checkGeocode(geocity):
    request_url = "https://restapi.amap.com/v3/geocode/geo?address=" + geocity + \
                  "&key=2150dfb6e7d3dbbaf89c9df87998c829"
    response = requests.get(request_url)
    response.raise_for_status()  # 检查响应是否正常
    Geo_data = response.json()
    # print(Geo_data)
    if Geo_data is None:
        return "Error: failed to parse the response as JSON."
    res = Geo_data['geocodes'][0]['formatted_address'] + "的经纬度为" + Geo_data['geocodes'][0]['location'] + "\n区号为：" + Geo_data['geocodes'][0]['citycode']
    # print(res)
    return res
