from transitions.extensions import GraphMachine

from linebot import LineBotApi, WebhookParser 

from linebot.models import MessageEvent, TextMessage, TextSendMessage,FlexSendMessage, BubbleContainer, ImageComponent,ImageSendMessage,QuickReply,QuickReplyButton,MessageAction, AudioSendMessage, StickerSendMessage

from utils import send_text_message
from templane import handle_main_menu, handle_weather_menu, handle_song_menu, handle_sunny_menu, handle_cloudy_menu, handle_rainy_menu, handle_pray_menu, handle_predict_menu, handle_star_menu, handle_blood_menu, handle_divination_menu, handle_tarot_menu
from reply import city_quick_reply, star_quick_reply, blood_quick_reply, star_img_item, star_english, star_feature, blood_feature
from crawler import get_data, get_data_of_star
import os

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)

global loc,star, blood

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_main_menu(self, event):
        text = event.message.text
        return text.lower() == "主選單" 

    def on_enter_main_menu(self, event):
        reply_token = event.reply_token
        message=[
                FlexSendMessage(alt_text='你想知道什麼',contents=handle_main_menu()),
                TextSendMessage(text=f"你可以選擇分類"),
                ]
        line_bot_api = LineBotApi(channel_access_token)
        line_bot_api.reply_message(reply_token, message)

    def is_going_to_weather_menu(self, event):
        text = event.message.text
        return text.lower() == "天氣預報"

    def on_enter_weather_menu(self, event):
        reply_token = event.reply_token
        message=[
                TextSendMessage(text=f"請選擇城市", quick_reply=city_quick_reply())
                ]
        line_bot_api = LineBotApi(channel_access_token) 
        line_bot_api.reply_message(reply_token,message)
        
    def is_going_to_weather_location(self, event):
        global loc
        text = event.message.text
        loc = text   
        return True

    def on_enter_weather_location(self, event):
        reply_token = event.reply_token
        message=[
                FlexSendMessage(alt_text='爬氣象局',contents=handle_weather_menu())
                ]
        #爬的東西
        line_bot_api = LineBotApi(channel_access_token)
        line_bot_api.reply_message(reply_token, message)

    def is_going_to_weather_final(self, event):
        text = event.message.text
        return text.lower() == "天氣如何"

    def on_enter_weather_final(self, event):
        global loc
        reply_token = event.reply_token
        message=[
                    TextSendMessage(text=get_data(loc, 1)),
                    TextSendMessage(text=f'如果還想知道氣溫，請輸入[氣溫如何]，否則輸入[返回]'),
                ]
        line_bot_api = LineBotApi(channel_access_token)
        line_bot_api.reply_message(reply_token, message)

    def is_going_to_temp(self, event):
        text = event.message.text
        return text.lower() == "氣溫如何"

    def on_enter_temp(self, event):
        global loc
        reply_token = event.reply_token
        message=[
                    TextSendMessage(text=get_data(loc,2)),
                    TextSendMessage(text=f'如果還想知道天氣，請輸入[天氣如何]，否則輸入[返回]') 
                ]
        line_bot_api = LineBotApi(channel_access_token)
        line_bot_api.reply_message(reply_token, message)

    def is_going_to_w_song(self, event):
        text = event.message.text
        return text.lower() == "要聽什麼歌呢?"

    def on_enter_w_song(self, event):
        reply_token = event.reply_token
        message=[
                    FlexSendMessage(alt_text='3種天氣',contents=handle_song_menu())
                ]
        line_bot_api = LineBotApi(channel_access_token)
        line_bot_api.reply_message(reply_token, message)

    def is_going_to_sunny(self, event):
        text = event.message.text
        return text.lower() == "晴天"

    def on_enter_sunny(self, event):
        reply_token = event.reply_token
        message=[
                   FlexSendMessage(alt_text='晴天',contents=handle_sunny_menu())
                ]
        line_bot_api = LineBotApi(channel_access_token)
        line_bot_api.reply_message(reply_token, message)

    def is_going_to_cloudy(self, event):
        text = event.message.text
        return text.lower() == "陰天"

    def on_enter_cloudy(self, event):
        reply_token = event.reply_token
        message=[
                    FlexSendMessage(alt_text='陰天',contents=handle_cloudy_menu())
                ]
        line_bot_api = LineBotApi(channel_access_token)
        line_bot_api.reply_message(reply_token, message)

    def is_going_to_rainy(self, event):
        text = event.message.text
        return text.lower() == "雨天"

    def on_enter_rainy(self, event):
        reply_token = event.reply_token
        message=[
                   FlexSendMessage(alt_text='雨天',contents=handle_rainy_menu())
                ]
        line_bot_api = LineBotApi(channel_access_token)
        line_bot_api.reply_message(reply_token, message)

    def is_going_to_pray_rain(self, event):
        text = event.message.text
        return text.lower() == "求雨儀式"

    def on_enter_pray_rain(self, event):
        reply_token = event.reply_token
        message=[
                   FlexSendMessage(alt_text='祈雨',contents=handle_pray_menu()),
                   AudioSendMessage(original_content_url='https://od.lk/s/ODFfNjQxMDY4MDJf/yisell_sound_20200317244579336_88012.mp3', duration = 11000)
                ]
        line_bot_api = LineBotApi(channel_access_token)
        line_bot_api.reply_message(reply_token, message)

    def is_going_to_predict_menu(self, event):
        text = event.message.text
        return text.lower() == "運勢占卜"

    def on_enter_predict_menu(self, event):
        reply_token = event.reply_token
        message=[
                   FlexSendMessage(alt_text='預測menu',contents=handle_predict_menu())
                ]
        line_bot_api = LineBotApi(channel_access_token)
        line_bot_api.reply_message(reply_token, message)

    def is_going_to_star_menu(self, event):
        text = event.message.text
        return text.lower() == "星座"

    def on_enter_star_menu(self, event):
        reply_token = event.reply_token
        message=[
                   TextSendMessage(text=f"請選擇星座", quick_reply=star_quick_reply())
                ]
        line_bot_api = LineBotApi(channel_access_token)
        line_bot_api.reply_message(reply_token, message)

    def is_going_to_star(self, event):
        global star
        text = event.message.text
        star = text
        return True

    def on_enter_star(self, event):
        reply_token = event.reply_token
        message=[
                   FlexSendMessage(alt_text='星座表單',contents=handle_star_menu())
                ]
        line_bot_api = LineBotApi(channel_access_token)
        line_bot_api.reply_message(reply_token, message)

    def is_going_to_star_property(self, event):
        text = event.message.text
        return text.lower() == "特性"

    def on_enter_star_property(self, event):
        global star
        reply_token = event.reply_token
        message=[
                   TextSendMessage(text=star_feature(star)),
                   TextSendMessage(text=f'如果還想知道其他，請輸入[圖示]或[今日運勢]，否則輸入[返回]')
                ]
        line_bot_api = LineBotApi(channel_access_token)
        line_bot_api.reply_message(reply_token, message)

    def is_going_to_star_img(self, event):
        text = event.message.text
        return text.lower() == "圖示"

    def on_enter_star_img(self, event):
        global star
        reply_token = event.reply_token
        message=[
                    ImageSendMessage(original_content_url=star_img_item(star), preview_image_url=star_img_item(star)),
                    TextSendMessage(text=f'如果還想知道其他，請輸入[特性]或[今日運勢]，否則輸入[返回]')
                ]
        line_bot_api = LineBotApi(channel_access_token)
        line_bot_api.reply_message(reply_token, message)

    def is_going_to_star_predict(self, event):
        text = event.message.text
        return text.lower() == "今日運勢"

    def on_enter_star_predict(self, event):
        global star
        e = star_english(star)
        reply_token = event.reply_token
        message=[
                    TextSendMessage(text=get_data_of_star(e)),
                    TextSendMessage(text=f'如果還想知道其他，請輸入[圖示]或[特性]，否則輸入[返回]')
                ]
        line_bot_api = LineBotApi(channel_access_token)
        line_bot_api.reply_message(reply_token, message)

    def is_going_to_blood_menu(self, event):
        text = event.message.text
        return text.lower() == "血型"

    def on_enter_blood_menu(self, event):
        reply_token = event.reply_token
        message=[
                   TextSendMessage(text=f"請選擇血型", quick_reply=blood_quick_reply())
                ]
        line_bot_api = LineBotApi(channel_access_token)
        line_bot_api.reply_message(reply_token, message)

    def is_going_to_blood(self, event):
        global blood
        text = event.message.text
        blood = text
        return  True

    def on_enter_blood(self, event):
        reply_token = event.reply_token
        message=[
                   FlexSendMessage(alt_text='血型表單',contents=handle_blood_menu())
                ]
        line_bot_api = LineBotApi(channel_access_token)
        line_bot_api.reply_message(reply_token, message)

    def is_going_to_blood_property(self, event):
        text = event.message.text
        return text.lower() == "特性"

    def on_enter_blood_property(self, event):
        global blood
        reply_token = event.reply_token
        message=[
                   TextSendMessage(text=blood_feature(blood)),
                   TextSendMessage(text=f'請輸入[返回]')
                ]
        line_bot_api = LineBotApi(channel_access_token)
        line_bot_api.reply_message(reply_token, message)

    def is_going_to_divination_menu(self, event):
        text = event.message.text
        return text.lower() == "占卜"

    def on_enter_divination_menu(self, event):
        reply_token = event.reply_token
        message=[
                   FlexSendMessage(alt_text='占卜表單',contents=handle_divination_menu())
                ]
        line_bot_api = LineBotApi(channel_access_token)
        line_bot_api.reply_message(reply_token, message)

    def is_going_to_tarot(self, event):
        text = event.message.text
        return text.lower() == "塔羅牌"

    def on_enter_tarot(self, event):
        reply_token = event.reply_token
        message=[
                   FlexSendMessage(alt_text='塔羅表單',contents=handle_tarot_menu())
                    
                ]
        line_bot_api = LineBotApi(channel_access_token)
        line_bot_api.reply_message(reply_token, message)


    def is_going_to_leave(self, event):
        text = event.message.text
        return True
    
    def on_enter_leave(self, event):
        reply_token = event.reply_token
        message=[
                    StickerSendMessage(package_id = '8522', sticker_id = '16581276'),
                    TextSendMessage(text=f"掰掰~"),
                ]
        line_bot_api = LineBotApi(channel_access_token)
        line_bot_api.reply_message(reply_token, message)
        self.go_back()
