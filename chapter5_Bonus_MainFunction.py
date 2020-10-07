'''
影片中我們提到，最好有一個main function來作為程式的進入點。

我們在最下面寫上main()來呼叫(執行)這個  main function 

但，許多程式碼你會看到​ 

if __name__ == '__main__':​

    main()



他們多寫了一個if 。

這個if因為不好解釋＋比較進階，我放到這邊來講，（這是可有可無的，最理想是有）

最簡單的解釋就是，

如果你沒有寫這個if，這個python檔被import的時候，會直接執行了main function。但通常這不是我們要的，

我們如果import別的模組（也就是python檔），我們不希望有東西立刻執行，而是我們叫它執行再執行。

所以加了這個if的意思就是要確認　這個python檔是被主要運行的python檔，而不是被import，也就是說我們是打python 這個檔案的名字 　　來執行這個檔案，那這樣我們就希望main function執行。如果這個檔案是被import的話，就不要執行main function了。

舉一個例子好了：

所謂的被import就是說我們寫了另一個檔案來import這個檔案

例如現在寫的是 a.py

後來又寫一個b.py　裡面寫到import a

如果a 裡面有main()　然後沒有寫那個if來檢查是不是被import，那b.py執行的時候一遇到import a，竟然會直接執行了a 的main function。



如果還想深入了解
可以閱讀這篇文章：
http://technology-sea.blogspot.tw/2012/03/python-name-import.html​

還有問題可以去討論區發問​喔！
'''