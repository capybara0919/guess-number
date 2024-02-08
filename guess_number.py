# 產生一個隨機整數1-100 
# 讓使用者重複輸入數字去猜
# 猜對就 印出 "終於猜對了"
# 猜錯就告訴他 比答案大或小

import random

r = random.randint(1, 100)
while True:
	num = input('請輸入數字:')
	num = int(num)
	if num == r:
		print('你猜對了')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')

