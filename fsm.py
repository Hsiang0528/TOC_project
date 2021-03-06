from transitions.extensions import GraphMachine

from utils import send_text_message
from utils import send_image_message
from utils import send_button_message
from linebot.models import MessageTemplateAction

import requests

# pip install requests


keyword = ["牡羊座", "金牛座", "雙子座", "巨蟹座", "獅子座", "處女座", "天秤座", "天蠍座", "射手座", "摩羯座", "水瓶座", "雙魚座", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
        # self.machine.get_graph().draw("FSM.png", prog= 'dot')

    def user_to_main(self, event):
        text = event.message.text
        return text.lower() != "graph"
    
    def on_enter_main(self, event):
        title = "請選擇功能"
        text = "請選擇功能"
        btn = [
            MessageTemplateAction(
                label = "心理測驗",
                text = "start"
            ),
            MessageTemplateAction(
                label = "星座運勢",
                text = "fortune"
            )
        ]
        url = 'https://upload.cc/i1/2021/12/23/YWmdDu.png'
        send_button_message(event.reply_token, title, text, btn, url)
    # 貓狗辨識
    # def user_to_pet(self, event):
    #     text = event.message.text
    #     return text.lower() == "pet"

    # def on_enter_pet(self, event):
    #     print("I'm entering pet")
    #     reply_token = event.reply_token
    #     send_text_message(reply_token, "Please send pet's image!")

    # def pet_to_pet2(self, event):
    #     return event.message.type == 'image'


    # def on_enter_pet2(self, event):
    #         net = load_model('model.h5')
    #         cls_list = ['cat', 'dog']
        
    #         path = './petImages/test/' +cls_list[random.randint(0,1)] + '/' + text + '.jpg'

    #         showimg = cv2.imread(path)
    #         img = image.load_img(path, target_size=(224, 224))
    #         # 圖像欲處理
    #         x = image.img_to_array(img)
    #         x = np.expand_dims(x, axis=0)

    #         # 對圖像進行分類
    #         preds = net.predict(x)
    #         cv2.imshow(cls_list[int(np.argmax(preds, axis=1))],showimg)
    #         self.pet_to_user()
    
    # 心理測驗
    def main_to_fortune(self, event):
        text = event.message.text
        return text.lower() == "fortune"
    
    def on_enter_fortune(self, event):
        print("I'm entering fortune")
        reply_token = event.reply_token
        send_text_message(reply_token, "請輸入你的星座:\n牡羊座 請輸入0\n金牛座 請輸入1\n雙子座 請輸入2\n巨蟹座 請輸入3\n獅子座 請輸入4\n處女座 請輸入5\n天秤座 請輸入6\n天蠍座 請輸入7\n射手座 請輸入8\n摩羯座 請輸入9\n水瓶座 請輸入10\n雙魚座 請輸入11")
    
    def fortune_to_fortune2(self, event):
        print("fortune")
        text = event.message.text
        return text.lower() in keyword
    
    def on_enter_fortune2(self, event):
        print(event.message.text)
        i=0
        if(len(event.message.text)==3):
            i=0
            for key in keyword:
                if(key == event.message.text):
                    break
                i=i+1
        else :
            i=int(event.message.text)

        reply_token = event.reply_token
        if (i==12):
            send_message(reply_token, canmessage)
            self.go_back()
            return
        reply_arr = []

        str_arr = keyword[i]+"\n\n"

        res = requests.get("https://astro.click108.com.tw/daily_"+str(i)+".php?iAstro="+str(i))
        
        pos = res.text[res.text.find('love.png'):res.text.find('love.png')+200]
        pos = pos[pos.find('LIGHT">'):pos.find('LIGHT">')+100]

        star =""
        for i in range (0, int(pos[pos.find('icon')+5:pos.find('.png')])):
            star =star+"★"
        for i in range (0, 5-int(pos[pos.find('icon')+5:pos.find('.png')])):
            star =star+"☆"
        str_arr = str_arr + "愛情運勢: "+star+"\n\n"

        pos = res.text[res.text.find('work.png'):res.text.find('work.png')+200]
        pos = pos[pos.find('LIGHT">'):pos.find('LIGHT">')+100]

        star =""
        for i in range (0, int(pos[pos.find('icon')+5:pos.find('.png')])):
            star =star+"★"
        for i in range (0, 5-int(pos[pos.find('icon')+5:pos.find('.png')])):
            star =star+"☆"
        str_arr = str_arr +"工作運勢: "+star+"\n\n"

        pos = res.text[res.text.find('all.png'):res.text.find('all.png')+200]
        pos = pos[pos.find('LIGHT">'):pos.find('LIGHT">')+100]

        star =""
        for i in range (0, int(pos[pos.find('icon')+5:pos.find('.png')])):
            star =star+"★"
        for i in range (0, 5-int(pos[pos.find('icon')+5:pos.find('.png')])):
            star =star+"☆"
        str_arr = str_arr + "整體運勢: "+star+"\n\n"

        str_arr = str_arr + "幸運數字: "+res.text[res.text.find('"NUMERAL">')+10:res.text.find('"NUMERAL">')+11]+"\n\n"

        pos = res.text[res.text.find('title02.png')+52:res.text.find('title02.png')+90]

        str_arr = str_arr + "幸運顏色: "+pos[pos.find("<h4>")+4:pos.find("</h4>")]+"\n\n資料來源:科技紫微網" 

        send_text_message(reply_token, str_arr)
        self.fortune2_to_user()
    # 畫圖
    def user_to_graph(self, event):
        text = event.message.text
        return text.lower() == "graph"

    def main_to_start(self, event):
        text = event.message.text
        return text.lower() == "start"

    # 心理測驗
    # 第一題
    def start_to_I(self, event):
        text = event.message.text
        return text.lower() == "i"

    def start_to_E(self, event):
        text = event.message.text
        return text.lower() == "e"
    # 第二題
    def I_to_IN(self, event):
        text = event.message.text
        return text.lower() == "n"

    def I_to_IS(self, event):
        text = event.message.text
        return text.lower() == "s"
    
    def E_to_EN(self, event):
        text = event.message.text
        return text.lower() == "n"

    def E_to_ES(self, event):
        text = event.message.text
        return text.lower() == "s"

    # 第三題
    def IN_to_INT(self, event):
        text = event.message.text
        return text.lower() == "t"

    def IS_to_IST(self, event):
        text = event.message.text
        return text.lower() == "t"
    
    def EN_to_ENT(self, event):
        text = event.message.text
        return text.lower() == "t"

    def ES_to_EST(self, event):
        text = event.message.text
        return text.lower() == "t"
    
    def IN_to_INF(self, event):
        text = event.message.text
        return text.lower() == "f"

    def IS_to_ISF(self, event):
        text = event.message.text
        return text.lower() == "f"
    
    def EN_to_ENF(self, event):
        text = event.message.text
        return text.lower() == "f"

    def ES_to_ESF(self, event):
        text = event.message.text
        return text.lower() == "f"

     # 第四題
    def INT_to_INTJ(self, event):
        text = event.message.text
        return text.lower() == "j"

    def IST_to_ISTJ(self, event):
        text = event.message.text
        return text.lower() == "j"
    
    def ENT_to_ENTJ(self, event):
        text = event.message.text
        return text.lower() == "j"

    def EST_to_ESTJ(self, event):
        text = event.message.text
        return text.lower() == "j"
    
    def INF_to_INFJ(self, event):
        text = event.message.text
        return text.lower() == "j"

    def ISF_to_ISFJ(self, event):
        text = event.message.text
        return text.lower() == "j"
    
    def ENF_to_ENFJ(self, event):
        text = event.message.text
        return text.lower() == "j"

    def ESF_to_ESFJ(self, event):
        text = event.message.text
        return text.lower() == "j"

    def INT_to_INTP(self, event):
        text = event.message.text
        return text.lower() == "p"

    def IST_to_ISTP(self, event):
        text = event.message.text
        return text.lower() == "p"
    
    def ENT_to_ENTP(self, event):
        text = event.message.text
        return text.lower() == "p"

    def EST_to_ESTP(self, event):
        text = event.message.text
        return text.lower() == "p"
    
    def INF_to_INFP(self, event):
        text = event.message.text
        return text.lower() == "p"

    def ISF_to_ISFP(self, event):
        text = event.message.text
        return text.lower() == "p"
    
    def ENF_to_ENFP(self, event):
        text = event.message.text
        return text.lower() == "p"

    def ESF_to_ESFP(self, event):
        text = event.message.text
        return text.lower() == "p"
    
    def go_to_user_1(self, event):
        text = event.message.text
        return text.lower() == "restart"
    # 
    #
    def on_enter_graph(self, event):
        print("I'm entering graph")

        reply_token = event.reply_token
        send_image_message(reply_token, "https://upload.cc/i1/2021/12/23/7YH2aw.png")
        # https://upload.cc/i1/2021/12/21/k4qsxn.png
        self.back()
    #
    def on_enter_user_1(self, event):
        print("I'm entering start")
        reply_token = event.reply_token
        send_text_message(reply_token, "Current position: Menu")
        self.uu()

    def on_enter_start(self, event):
        print("I'm entering start")
        reply_token = event.reply_token
        send_text_message(reply_token, "你更喜歡哪一個? \n(i)獨處 \n(e)與他人相處\nPlease \"I\" or \"E\"")

    def on_enter_I(self, event):
        print("I'm entering I")
        reply_token = event.reply_token
        send_text_message(reply_token, "學習新鮮事物時，你更喜歡?\n(n)瞭解概念與理論 \n(s)註重實際用途？\nPlease \"N\" or \"S\"")

    def on_enter_E(self, event):
        print("I'm entering E")
        reply_token = event.reply_token
        send_text_message(reply_token, "學習新鮮事物時，你更喜歡?\n(n)瞭解概念與理論 \n(s)註重實際用途？\nPlease \"N\" or \"S\"")

    def on_enter_IN(self, event):
        print("I'm entering IN")
        reply_token = event.reply_token
        send_text_message(reply_token, "當你在做決策時，你比較在乎? \n(t)重視邏輯與公平 \n(f)重視感情與和睦\nPlease \"T\" or \"F\"")

    def on_enter_EN(self, event):
        print("I'm entering EN")
        reply_token = event.reply_token
        send_text_message(reply_token, "當你在做決策時，你比較在乎? \n(t)重視邏輯與公平 \n(f)重視感情與和睦\nPlease \"T\" or \"F\"")

    def on_enter_IS(self, event):
        print("I'm entering IS")
        reply_token = event.reply_token
        send_text_message(reply_token, "當你在做決策時，你比較在乎? \n(t)重視邏輯與公平 \n(f)重視感情與和睦\nPlease \"T\" or \"F\"")

    def on_enter_ES(self, event):
        print("I'm entering ES")
        reply_token = event.reply_token
        send_text_message(reply_token, "當你在做決策時，你比較在乎? \n(t)重視邏輯與公平 \n(f)重視感情與和睦\nPlease \"T\" or \"F\"")
    def on_enter_INT(self, event):
        print("I'm entering INT")
        reply_token = event.reply_token
        send_text_message(reply_token, "你的生活方式更傾向於? \n(j)先工作，再玩耍。做事著重結果 \n(p)先玩耍，再工作。做事享受過程\nPlease \"J\" or \"P\"")

    def on_enter_ENT(self, event):
        print("I'm entering ENT")
        reply_token = event.reply_token
        send_text_message(reply_token, "你的生活方式更傾向於? \n(j)先工作，再玩耍。做事著重結果 \n(p)先玩耍，再工作。做事享受過程\nPlease \"J\" or \"P\"")

    def on_enter_IST(self, event):
        print("I'm entering IST")
        reply_token = event.reply_token
        send_text_message(reply_token, "你的生活方式更傾向於? \n(j)先工作，再玩耍。做事著重結果 \n(p)先玩耍，再工作。做事享受過程\nPlease \"J\" or \"P\"")
    def on_enter_EST(self, event):
        print("I'm entering EST")
        reply_token = event.reply_token
        send_text_message(reply_token, "你的生活方式更傾向於? \n(j)先工作，再玩耍。做事著重結果 \n(p)先玩耍，再工作。做事享受過程\nPlease \"J\" or \"P\"")

    def on_enter_INF(self, event):
        print("I'm entering INF")
        reply_token = event.reply_token
        send_text_message(reply_token, "你的生活方式更傾向於? \n(j)先工作，再玩耍。做事著重結果 \n(p)先玩耍，再工作。做事享受過程\nPlease \"J\" or \"P\"")

    def on_enter_ENF(self, event):
        print("I'm entering ENF")
        reply_token = event.reply_token
        send_text_message(reply_token, "你的生活方式更傾向於? \n(j)先工作，再玩耍。做事著重結果 \n(p)先玩耍，再工作。做事享受過程\nPlease \"J\" or \"P\"")

    def on_enter_ISF(self, event):
        print("I'm entering ISF")
        reply_token = event.reply_token
        send_text_message(reply_token, "你的生活方式更傾向於? \n(j)先工作，再玩耍。做事著重結果 \n(p)先玩耍，再工作。做事享受過程\nPlease \"J\" or \"P\"")

    def on_enter_ESF(self, event):
        print("I'm entering ESF")
        reply_token = event.reply_token
        send_text_message(reply_token, "你的生活方式更傾向於? \n(j)先工作，再玩耍。做事著重結果 \n(p)先玩耍，再工作。做事享受過程\nPlease \"J\" or \"P\"")
    #
    def on_enter_INTJ(self, event):
        print("I'm entering INTJ")
        reply_token = event.reply_token
        send_text_message(reply_token, "你是建築師人格 INTJ\n優點:理性、堅定、獨立、好奇心重、易於成功\n缺點:傲慢、忽視他人情感、憤世嫉俗、競爭性強、缺乏浪漫")
        self.ans_to_user()

    def on_enter_ENTJ(self, event):
        print("I'm entering ENTJ")
        reply_token = event.reply_token
        send_text_message(reply_token, "你是指揮官人格 ENTJ\n優點:有效率、充滿活力、自信、意志堅定、充滿魅力\n缺點:固執、不能容人、傲慢、沒有耐心、冷酷無情")
        self.ans_to_user()

    def on_enter_ISTJ(self, event):
        print("I'm entering ISTJ")
        reply_token = event.reply_token
        send_text_message(reply_token, "你是物流師人格 ISTJ\n優點:誠實正直、有責任感、冷靜自律、服從紀律\n缺點:固執、情感不敏感、過於教條、不尊重多樣化")
        self.ans_to_user()

    def on_enter_ESTJ(self, event):
        print("I'm entering ESTJ")
        reply_token = event.reply_token
        send_text_message(reply_token, "你是總經理人格 ESTJ\n優點:勇於奉獻、意志堅定、誠實直率、享受秩序\n缺點:固執、難以變通、不喜歡非傳統、喜歡評價他人、過於在意社會地位")
        self.ans_to_user()

    def on_enter_INFJ(self, event):
        print("I'm entering INFJ")
        reply_token = event.reply_token
        send_text_message(reply_token, "你是提倡者人格 INFJ\n優點:富有創意、思想敏銳、原則性強、熱情、利他主義者\n缺點:對批評敏感、很難敞開心扉、過於完美主義、忽略自己的感受")
        self.ans_to_user()

    def on_enter_ENFJ(self, event):
        print("I'm entering ENFJ")
        reply_token = event.reply_token
        send_text_message(reply_token, "你是主人公人格 ENFJ\n優點:體諒他人、可被依賴、利他主義、天生的領導者、為人善良\n缺點:太無私易吃虧、過於敏感、搖擺不定、不安全感重")
        self.ans_to_user()

    def on_enter_ISFJ(self, event):
        print("I'm entering ISFJ")
        reply_token = event.reply_token
        send_text_message(reply_token, "你是守衛者人格 ISFJ\n優點:樂於助人、可靠有耐心、善於觀察、努力又忠誠\n缺點:有時過於害羞、情感敏感，壓抑自己的情感、害怕改變")
        self.ans_to_user()

    def on_enter_ESFJ(self, event):
        print("I'm entering ESFJ")
        reply_token = event.reply_token
        send_text_message(reply_token, "你是執政官人格 ESFJ\n優點:責任感強、對朋友忠誠、暖心又感性、善於交朋友\n缺點:不善於臨場發揮、對批評很脆弱、太過黏人、在意社會地位")
        self.ans_to_user()

    def on_enter_INTP(self, event):
        print("I'm entering INTP")
        reply_token = event.reply_token
        send_text_message(reply_token, "你是邏輯學家人格 INTP\n優點:善於分析總結、有大局觀、創造性強、思想開放、客觀、誠實\n缺點:難以敞開心扉、居高臨下、總是懷疑自己、情感上不敏感、厭惡規則束縛")
        self.ans_to_user()

    def on_enter_ENTP(self, event):
        print("I'm entering ENTP")
        reply_token = event.reply_token
        send_text_message(reply_token, "你是辯論家人格 ENTP\n優點:知識豐富、思想敏銳、善於腦力激盪、精力旺盛、充滿魅力\n缺點:愛唱反調、不能容人、厭惡重複的工作、注意力不集中")
        self.ans_to_user()

    def on_enter_ISTP(self, event):
        print("I'm entering ISTP")
        reply_token = event.reply_token
        send_text_message(reply_token, "你是鑒賞家人格 ISTP\n優點:樂觀有活力、富有創造性、隨性又理想、臨危不亂\n缺點:注重個人領域、很容易感到無聊、不喜歡承諾、非常喜歡冒險")
        self.ans_to_user()

    def on_enter_ESTP(self, event):
        print("I'm entering ESTP")
        reply_token = event.reply_token
        send_text_message(reply_token, "你是企業家人格 ESTP\n優點:大膽、理性、動手能力強、洞察力強、社交能力好\n缺點:感情不敏感、不耐心、喜歡冒險、沒有大局觀、叛逆")
        self.ans_to_user()

    def on_enter_INFP(self, event):
        print("I'm entering INFP")
        reply_token = event.reply_token
        send_text_message(reply_token, "你是調停者人格 INFP\n優點:關愛他人、慷慨大方、思想開明、有創意、熱情似火\n缺點:太理想主義、常自我批評、不切實際、意氣用事")
        self.ans_to_user()

    def on_enter_ENFP(self, event):
        print("I'm entering ENFP")
        reply_token = event.reply_token
        send_text_message(reply_token, "你是競選者人格 ENFP\n優點:充滿好奇、觀察力強、充滿激情、善於溝通、非常受歡迎\n缺點:實作能力不強、難以集中注意力、思慮過度、非常情緒化")
        self.ans_to_user()

    def on_enter_ISFP(self, event):
        print("I'm entering ISFP")
        reply_token = event.reply_token
        send_text_message(reply_token, "你是探險家人格 ISFP\n優點:有魅力、想象力豐富、充滿好奇、藝術氣質濃厚\n缺點:過於獨立、行事難以預測、非常容易有壓力、過於有競爭性")
        self.ans_to_user()

    def on_enter_ESFP(self, event):
        print("I'm entering ESFP")
        reply_token = event.reply_token
        send_text_message(reply_token, "你是表演者人格 ESFP\n優點:大膽、有原創性、表演者性格、實踐能力強、善於觀察\n缺點:非常容易感到無聊、感情敏感、無法制定長期計劃、難以集中注意力")
        self.ans_to_user()
    


    

    