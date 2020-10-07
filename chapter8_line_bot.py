'''
line-bot
1. 去 line 的 Messaging API 去啟動一個機器人 (然後去設定名字和provider那些，不過不是很重要)。

2. 建立新資料夾,建立GitHub專案 (打那六行指令)。

3. 開始coding出一個line server並可放在雲端上執行(利用LINE的SDK，所以要import進來SDK，然後用SDK已寫好的某些function去達成目的)，記得要先去pip install。把SDK的usage給copy下來。
*SDK(software development kit)概念: 車子(某種軟體或硬體的商品)需要有方向盤(已寫好的產品的軟體，而這個軟體就是SDK)，才能讓使用者去操控車子(知道這個軟體或硬體的產品的資料結構是啥，才有辦法去開發某些功能)。

4. 將程式命名為app.py(寫網站/server時，而我們會將主要程式檔案(叫做web app，網路應用程式)通常命名為app.py，另外寫網站就是在寫server，因為網站本身就是server)。
*python架設server或寫網站有兩種:flask(較小型，無畫面或無圖的應用程式),django(較大型，有畫面或圖的應用程式)。

5. 去 line 的 Messaging API，把channel secret和channel access token給複製下來到程式碼內對應的地方，另外把webhooks給啟用(沒有的話就不用啟用，他已經自動啟用了)。
*secret和token就是雙重密碼的意思，以免其他人能侵入你建的line server。webhooks可想像成server和機器人之間的連線，這樣一但機器人收到訊息才能轉載到server，所以下方有個網址輸入就是要輸入到時候我們建的server網址。
*程式碼中有個@app.route("/callback")，其中/callback是某種觸發鍵，觸發執行下面那個def callback()，也就是說當你機器人的webhooks網址(來連結line server的網址)的結尾是"/callback"時，server才會去執行那個function，所以當你結尾網址是/123，那你@的""那邊也要改成123。
*執行callback()時，會再去執行handler.handle()，接著會再去執行def handle_message()。而我們主要修改的是def handle_message()的地方(這是回復接受訊息的function)，其他地方都不用改。

6. 上傳程式碼到GitHub(三步驟)

7. 註冊heroku並安裝heroku。要安裝，先點python,點set up,然後載根據你的作業系統去下載CLI(下載時，可以把安裝Git那個勾勾取消，因為我們已經有裝了，其他就一直按下一步就行)。
*世界三大雲端平台:amazon的aws,microsoft的azure,google的GCE。但這些都要錢，所以用heroku。 

8. CMD重開。 然後打heroku login來登錄heroku。

9. 在heroku首頁去create new app。app name隨意你取，國家也隨意。

10. 去資料夾建立兩個檔案: Procfile 和 requirements.txt。檔案名必須打對，然後第一個檔案不用副檔名。在第一個檔案內打 web gunicorn app:app ，其中app:app當中第二個app是你的主要程式名字，即app.py只是.py不用打。第一個app是告知這是一個app的意思。第二個檔案內容為三行: line-bot-sdk, gunicorn, flask.
*Procfile目的是為了讓heroku去知道怎麼運行你的程式，還有要執行哪個主要程式檔案。requirements.txt目的是為了讓運行者(像是cmd)知道我們用到哪些套件，然後它會去找並安裝。

11. 把剛剛那個程式給放在heroku。去最下面Existing Git repository(因為我們已經有先在GitHub建立專案了)，先執行那行程式(用意是來把GitHub和heroku做連結)，再執行git push heroku master(開始上傳的動作)。
*heroku和github最大的差別就是heroku會幫你執行程式，但github不會，只是單純幫你放程式而已。相同點就是你都可以上傳程式上去。
*cmd打pip list可知目前有裝哪些套件，打pip freeze可知目前那些套件是哪個版本。 >符號可以把印出的東西給存到某個檔案。

12. 把資料夾內的檔案再新增到github(三步驟)。另外第一步驟可打 git add . 意思是把目前所在資料夾的東西全都新增進去。就不用git add 然後後面打一堆想加的檔名。 

13. 把資料夾內的檔案再新增到heroku。只需打 git push heroku master 。

14. 去heroku的setting找到Domain有個app的網址，去把它複製，並到 line 的 Messaging API 的 webhooks的網址欄貼上去。最後記得網址最後結尾要是/callback，所以記得加上去。
*這個heroku的那個app網址就是剛剛那個主要程式，架構好的server。 
*可以在cmd打 heroku logs ，把遇到的程式問題都顯示出來。

15. 去LINE Messaging API那邊去掃QRcode加好友，即可開始測試。

Q: 如何更改LINE回復訊息:
Ans: 去def handle_message()內改。TextSendMessage(text='你想回的訊息')。其他你想做啥你再去LINE的SDK去查，然後複製貼上在TextSendMessage()的位置，把它取代掉就好(其實就是line_bot_api.reply_message()這函式的第二個參數是放你可以改的，這就是主要回復訊息用的函式，你也可以打很多這個函式，回復很多東西)。不過記得要先在import linebot.models import()內import需要的模組。
*注意:程式做修改後，都要重新上傳到github和heroku(github三步驟，heroku一個步驟)。

補充: 你可以寫一堆rule-based(也就是一堆if和elif)來裝成像是人工智慧機器人一樣可以對話，但真正的人工智慧應該是non-rule-based的，也就是非用if和elif去寫的。而且現在很多公司說他們在做人工智慧，其實都是假的，那種rule-based去寫的。
'''
