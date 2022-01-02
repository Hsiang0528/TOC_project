# TOC Project 2021

這是一個生活小幫手
可以做簡易的心理測驗及星座運勢測驗


                                                      好友介面
						      
![main](https://user-images.githubusercontent.com/92910688/147869373-c4d457d4-9227-4162-862d-002e8ef0a96b.jpg)

                                                       主介面
						       
![主畫面](https://user-images.githubusercontent.com/92910688/147869364-13fb1080-378f-4855-80de-f1698f204309.jpg)

                                                      心理測驗
						      
![心理測驗](https://user-images.githubusercontent.com/92910688/147869386-d94ec599-6eaf-4354-a0ed-a5f6b77c2c28.jpg)

                                                       星座運勢
						       
![星座運勢](https://user-images.githubusercontent.com/92910688/147869391-d47a78c3-93ff-41de-94bb-d14a18513931.jpg)

                                                     顯示FSM graph
						     
![graph](https://user-images.githubusercontent.com/92910688/147869405-388517d7-690c-43fb-802d-ab1bd7361496.jpg)

                                                       FSM狀態圖
						       
![FSM](https://user-images.githubusercontent.com/92910688/147869396-e7d1219c-e9a2-4f11-8f32-19621906d6da.jpg)

user state : 可輸入任意文字到主介面(main state)，或是輸入graph傳送FSM狀態圖

main state : 點選心理測驗button並自動回復"start"，開始心理測驗。或是點選星座運勢buttton並自動回覆"fortune"，開始星座運勢測驗。

心理測驗    : 共四題各2個選項，最終有16種不同的心理人格，共31個state。
             在每個state中皆可輸入restart已重新回到user state。
	   
星座運勢    : 選擇想測試的星座，等待回傳今日的星座運勢。(來源:科技紫微網)

備註        : 在每個state皆有防呆機制，操作簡單好上手。
