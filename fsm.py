from transitions.extensions import GraphMachine

from utils import send_text_message
from utils import send_image_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
        # self.machine.get_graph().draw("FSM.png", prog= 'dot')

    def user_to_graph(self, event):
        text = event.message.text
        return text.lower() == "graph"

    def user_to_start(self, event):
        text = event.message.text
        return text.lower() == "start"
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
        send_image_message(reply_token, "https://upload.cc/i1/2021/12/21/k4qsxn.png")
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
        send_text_message(reply_token, "你是辯論家人格 ENTP\n優點:知識豐富、思想敏銳、善於腦力激盪、精力旺盛、充滿魅力\n缺點:愛唱反調、不能容人、厭惡重複的工作、注意力不集中")
        self.ans_to_user()

    def on_enter_ENTJ(self, event):
        print("I'm entering ENTJ")
        reply_token = event.reply_token
        send_text_message(reply_token, "你是建築師人格 INTJ\n優點:理性、堅定、獨立、好奇心重、易於成功\n缺點:傲慢、忽視他人情感、憤世嫉俗、競爭性強、缺乏浪漫")
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
        send_text_message(reply_token, "你是辯論家人格 ENTP\n優點:知識豐富、思想敏銳、善於腦力激盪、精力旺盛、充滿魅力\n缺點:愛唱反調、不能容人、厭惡重複的工作、注意力不集中")
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
    


    

    