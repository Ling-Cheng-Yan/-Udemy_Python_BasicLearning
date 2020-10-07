'''
圖片處理(例如: 將圖片變成黑白)
'''
'''
from PIL import Image #PIL全名叫做Pillow
image_file = Image.open("nayeon.jpg") # open colour image ，補充:這個function一定有return才有辦法存到image_file。
image_file = image_file.convert('L') # convert image to black
image_file.save('nayeon1.jpg')
'''


'''
將多個圖片都轉成黑白
'''
from PIL import Image
import os
for file in os.listdir('orig'): #若打'.'則是現在檔案位置的層級，而這行for loop會把檔案名字一個一個取出來。
	if file.endswith('.jpg'): #endswith()是字串功能，功能是: 檢查結尾是.jpg的字串。
		image_file = Image.open('orig/' + file) #不能只打file，因為這py檔路徑的問題，會出錯讀不到此檔案，因為不會讀到orig的。
		image_file = image_file.convert('L') 
		image_file.save(os.path.join('result', file[:-4] + '_grey.png')) #注意，fille[:-4]的結束值不包含，所以倒數第四個不會包含到。另外，此是實用的檔案結尾替換的寫法。

#補充: 上述19行在做手動合併檔案路徑，但也可以靠模組，打 os.path.join('orig', file) 去合併。 就像是第21行一樣。

