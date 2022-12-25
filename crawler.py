import json
import requests

def get_data(city, type):

    url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001"
    params = {
        "Authorization": "CWB-59610462-3156-4540-81D5-1C17FB99EDAA",
        "locationName": city,
    }

    response = requests.get(url, params=params)
    print(response.status_code)

    if response.status_code == 200:
        # print(response.text)
        data = json.loads(response.text)

        location = data["records"]["location"][0]["locationName"]

        weather_elements = data["records"]["location"][0]["weatherElement"]
        start_time = weather_elements[0]["time"][0]["startTime"]
        end_time = weather_elements[0]["time"][0]["endTime"]
        weather_state = weather_elements[0]["time"][0]["parameter"]["parameterName"]
        rain_prob = weather_elements[1]["time"][0]["parameter"]["parameterName"]
        min_tem = weather_elements[2]["time"][0]["parameter"]["parameterName"]
        comfort = weather_elements[3]["time"][0]["parameter"]["parameterName"]
        max_tem = weather_elements[4]["time"][0]["parameter"]["parameterName"]

    else:
        print("Can't get data!")

    if(type == 1): # weather
        message = "預測時間:\n"+ start_time+ " ~ " + end_time + "\n" + city + "的天氣為:\n" + weather_state + "\n降雨的機率是:" + rain_prob + "%"
        return message

    if(type == 2):
        message = "預測時間:\n"+ start_time+ " ~ " + end_time + "\n" + city + "的氣溫為:\n" + min_tem + "°C ~ " +max_tem + "°C\n" + "體感溫度:\n" + comfort
        return message

def get_data_of_star(star):
    url = "https://apis.tianapi.com/star/index"
    params = {
        "key": "5e7708fb9c3c3f8dd8983f0a42a7d2ae",
        "astro": star 
    }

    response = requests.get(url, params=params)
    print(response.status_code)

    if response.status_code == 200:
        # print(response.text)
        data = json.loads(response.text)
        # print(data)

        composite = data["result"]["list"][0]["content"]
        love = data["result"]["list"][1]["content"]
        work = data["result"]["list"][2]["content"]
        money = data["result"]["list"][3]["content"]
        health = data["result"]["list"][4]["content"]
        color = data["result"]["list"][5]["content"]
        number = data["result"]["list"][6]["content"]
        people = data["result"]["list"][7]["content"]
        comment = data["result"]["list"][8]["content"]
    else:
        print("Can't get data!")

    message = "綜合指數: " + composite + "\n愛情指數: " + love + "\n工作指數: " + work + "\n財運指數: " + money + "\n健康指數: " + health + "\n幸運色: " + color + "\n幸運數字: " + number + "\n貴人星座: " + people + "\n今日概述:\n" + comment
    return message

# if __name__ == '__main__':
#     m = get_data_of_star("金牛座")
#     print(m)