from linebot.models import QuickReply,QuickReplyButton,MessageAction

def city_quick_reply():
    return QuickReply(
               items=[
                   QuickReplyButton(action=MessageAction(label="宜蘭縣", text="宜蘭縣")),
                   QuickReplyButton(action=MessageAction(label="臺北市", text="臺北市")),
                   QuickReplyButton(action=MessageAction(label="桃園市", text="桃園市")),
                   QuickReplyButton(action=MessageAction(label="新竹市", text="新竹市")),
                   QuickReplyButton(action=MessageAction(label="苗栗縣", text="苗栗縣")),
                   QuickReplyButton(action=MessageAction(label="臺中市", text="臺中市")),
                   QuickReplyButton(action=MessageAction(label="南投縣", text="南投縣")),
                   QuickReplyButton(action=MessageAction(label="彰化縣", text="彰化縣")),
                   QuickReplyButton(action=MessageAction(label="雲林縣", text="雲林縣")),
                   QuickReplyButton(action=MessageAction(label="嘉義市", text="嘉義市")),
                   QuickReplyButton(action=MessageAction(label="臺南市", text="臺南市")),
                   QuickReplyButton(action=MessageAction(label="高雄市", text="高雄市")),
                #    QuickReplyButton(action=MessageAction(label="屏東縣", text="屏東縣")),
                #    QuickReplyButton(action=MessageAction(label="宜蘭縣", text="宜蘭縣")),
                #    QuickReplyButton(action=MessageAction(label="花蓮縣", text="花蓮縣")),
                #    QuickReplyButton(action=MessageAction(label="台東縣", text="台東縣")),
                #    QuickReplyButton(action=MessageAction(label="澎湖縣", text="澎湖縣")),
               ]
           )

def star_quick_reply():
    return QuickReply(
        items=[
            QuickReplyButton(action=MessageAction(label="牡羊座", text="牡羊座")),
            QuickReplyButton(action=MessageAction(label="金牛座", text="金牛座")),
            QuickReplyButton(action=MessageAction(label="雙子座", text="雙子座")),
            QuickReplyButton(action=MessageAction(label="巨蟹座", text="巨蟹座")),
            QuickReplyButton(action=MessageAction(label="獅子座", text="獅子座")),
            QuickReplyButton(action=MessageAction(label="處女座", text="處女座")),
            QuickReplyButton(action=MessageAction(label="天秤座", text="天秤座")),
            QuickReplyButton(action=MessageAction(label="天蠍座", text="天蠍座")),
            QuickReplyButton(action=MessageAction(label="射手座", text="射手座")),
            QuickReplyButton(action=MessageAction(label="摩羯座", text="摩羯座")),
            QuickReplyButton(action=MessageAction(label="水瓶座", text="水瓶座")),
            QuickReplyButton(action=MessageAction(label="雙魚座", text="雙魚座"))
        ]
    )

def blood_quick_reply():
    return QuickReply(
        items=[
            QuickReplyButton(action=MessageAction(label="A型", text="A型")),
            QuickReplyButton(action=MessageAction(label="B型", text="B型")),
            QuickReplyButton(action=MessageAction(label="AB型", text="AB型")),
            QuickReplyButton(action=MessageAction(label="O型", text="O型")),
        ]
    )

def star_img_item(str):
    if( str == "牡羊座"): return 'https://i.imgur.com/cA0sc8N.jpg'
    elif(str == "金牛座"): return 'https://i.imgur.com/OIUPPlY.jpg'
    elif(str == "雙子座"): return 'https://i.imgur.com/owJdeL3.jpg'
    elif(str == "巨蟹座"): return 'https://i.imgur.com/6l5EQ6m.jpg'
    elif(str == "獅子座"): return 'https://i.imgur.com/qxX49jK.jpg'
    elif(str == "處女座"): return 'https://i.imgur.com/qtFOm25.jpg'
    elif(str == "天秤座"): return 'https://i.imgur.com/1KLyIZE.jpg'
    elif(str == "天蠍座"): return 'https://i.imgur.com/GluGfNA.jpg'
    elif(str == "射手座"): return 'https://i.imgur.com/1xxSHcf.jpg'
    elif(str == "魔羯座"): return 'https://i.imgur.com/9cLBqdg.jpg'
    elif(str == "水瓶座"): return 'https://i.imgur.com/xCTHp0h.jpg'
    elif(str == "雙魚座"): return 'https://i.imgur.com/JGK6bYw.jpg'

def star_english(str):
    if( str == "牡羊座"): return "aries"
    elif(str == "金牛座"): return "taurus"
    elif(str == "雙子座"): return "gemini"
    elif(str == "巨蟹座"): return "cancer"
    elif(str == "獅子座"): return "leo"
    elif(str == "處女座"): return "virgo"
    elif(str == "天秤座"): return "libra"
    elif(str == "天蠍座"): return "scorpio"
    elif(str == "射手座"): return "sagittarius"
    elif(str == "魔羯座"): return "capricorn"
    elif(str == "水瓶座"): return "aquarius"
    elif(str == "雙魚座"): return "pisces"

def star_feature(str):
    if( str == "牡羊座"): return "熱情且鋼硬,個性強且男性化 易衝動,富正義感,善良,精力充沛 樂於嘗試冒險性,開創性的事物 有自以為是的個性 是12星座中,除了雙魚座外,其它星座都無法模仿的星座"
    elif(str == "金牛座"): return "頑固,但自己不會查覺 沉著,個性洗鍊,意志堅定,慎重溫和 很少動,很少說,大都靜靜地當聽眾或觀察別人 腦筋計算很快,但下一步卻很慢"
    elif(str == "雙子座"): return "具有雙重個性,如快樂或憂傷,熱情或溫柔 很令人迷惑的個性,聰明,機智也善變 講話速度快,且經常轉換話題 不守時 有偽裝自己動機的想法和慾望 愛自由,不受拘束藝術天分高"
    elif(str == "巨蟹座"): return "愛家,念舊 不容許他人侵入自己的地盤 內向,常把心事放在心底 心情像月亮,常變化 圓臉,五官突出"
    elif(str == "獅子座"): return "討厭黑暗和無聊 果斷力,自尊心強,會隱藏不如意的事,但卻表現的很堅強 喜歡被稱讚 有大男人的傾向 有自傲的氣息"
    elif(str == "處女座"): return "心思細膩,敏感略帶神經質 喜歡保有慣用的東西 具正義感,容易批評別人缺點 完美主義者,要求自己和別人一樣完美"
    elif(str == "天秤座"): return "表面很聰明,但卻時常受騙 有時優雅迷人,但有時固執受爭論 當他作決定時,不要打擾他;等他作好決定後,很難改變他 善於言詞 追求精緻生活"
    elif(str == "天蠍座"): return "有自信,能完全的擁有自我 很少說奉承的話,一旦讚美卻是真心的 是一個熱情的人,也是一個無情的危險份子 是一個真正憂鬱的人 有英雄氣慨,會保護弱者"
    elif(str == "射手座"): return "個性開朗,樂觀 思考路線是直的,常常得罪別人而不知道,不大會說謊 非常愛笑,且音量很大 冒險性大,領悟性高,幽默好動 腦筋常思考,且會有驚人之舉"
    elif(str == "魔羯座"): return "是一個有計畫的人,在一定的時間內能完成預定的目標 較不憑感覺做事,而是實際去力行 喜歡社會地位 脾氣較古怪,對事情執著,少受左右,喜歡一個人做事"
    elif(str == "水瓶座"): return "比較瘋狂的星座,介於瘋子和正常人之間 具理性,言語中帶哲理和邏輯 具領導能力,適合舞台表演 帶神經質,是晚婚的星座 基本上是不受婚姻束縳的,但對愛情的態度忠實 是實在主義者,且有預知的能力"
    elif(str == "雙魚座"): return "愛幻想,他的朋友必須能理解他的想法 生活哲學在精神上,必須像百萬富翁;但現實生活,則不一定 對於生活,認為今日要採溫和態度,但明日卻是以後的事 雙魚座的女性對男性而言,是心目中的理想情人"

def blood_feature(str):
    if(str == "A型"): return "1.在奇怪的地方有原則\n2.不擅長道歉\n3.容易悲觀\n4.好強\n5.不擅長口出惡言\n\
6.深思熟慮後才行動\n7.和平主義者\n8.擅長配合別人\n9.煩躁的時候不愛說話\n10.容易忽視別人\n\
11.不坦率\n12.不擅長說明\n13.責任感強\n14.對喜歡的事物會堅持\n15.獨佔慾強\n\
16.會為了別人勉強自己\n17.常在意很奇怪的點\n18.喜歡努力堅持\n19.直覺很準\n20.初次見面會照顧對方情緒\n\
21.怕麻煩\n22.愛哭\n23.不擅長拒絕\n24.優柔寡斷\n25.不會半途而廢"

    elif(str == "B型"): return "1.比較有常識\n2.不擅長沉默\n3.話題經常轉變\n4.討厭很多人的時候\n5.就算是友人的邀請也會拒絕\n\
6.討厭閒著沒事\n7.和人交往慢熱\n8.三天打魚兩天曬網\n9.不喜歡的人會一直不喜歡\n10.大大咧咧\n\
11.健忘\n12.討厭被麻煩\n13.自由奔放\n14.很難冷靜下來\n15.討厭背後說人壞話\n\
16.不想去察言觀色\n17.距離太近就想逃避\n18.口風很緊\n19.說話聲音很大\n20.不擅長說謊\n\
21.想做就能做到\n22.無法忍受沒有獨處的時光\n23.生氣起來很嚇人\n24.怕寂寞\n25.喜怒形於色"

    elif(str == "O型"): return "1.容易小題大做\n2.拖延症重度患者\n3.容易嫉妒\n4.容易一見鍾情\n5.喜歡跟別人講話\n\
6.無法長時間持續太拼的狀態\n7.討厭競爭\n8.自尊心很強\n9.說話有點浮誇\n10.很會察言觀色\n\
11.擅長照顧別人的心情\n12.常因馬虎犯小錯誤\n13.基本上算樂觀主義者\n14.被誇獎後進步更快\n15.意外的宅\n\
16.不會按照計劃行事\n17.生氣的話就會覺得很麻煩\n18.善於傾聽別人的煩惱\n19.討厭麻煩\n20.口頭禪是「睏」\n\
21.運氣不錯\n22.總是會記住很奇怪的小事\n23.對人忽冷忽熱\n24.常會先道歉\n25.行動先於思考"

    elif(str == "AB型"): return "1.熱血行動派\n2.有點懶散\n3.常後悔\n4.沉迷某事異常熱情\n5.沉著冷靜\n\
6.比起磨磨蹭蹭更喜歡一鼓作氣\n7.不擅長拒絕別人\n8.某些方面很謹慎\n9.容易拘泥不知變通\n10.喜歡被依賴\n\
11.在奇怪的方面非常頑固\n12.黑白分明\n13.沒長性\n14.領悟力好\n15.易招來誤解\n\
16.喜歡逞強\n17.常把麻煩掛在嘴邊\n18.不擅長表現自己\n19.怕生害羞\n20.喜歡收集東西\n\
21.不喜歡人多的地方\n22.喜歡分析別人\n23.擅長社交\n24.表面功夫做的很好\n25.好惡分明"