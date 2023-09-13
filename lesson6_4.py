#猜數字遊戲
import random

def play_game():
    min = 1
    max = 100
    count = 0
    target  = random.randint(min,max)
    print("===========猜數字遊戲===========\n") #顯示出來的
    #\n 空行
    print(target)


    while(True):
        try: 
            keyin = int(input(f"猜數字範圍:{min}~{max}:")) #執行時跑出來要輸入的
        except: #解決輸入格式錯誤問題,例如:A
            print("輸入格式錯誤")
            count += 1 #也同樣計算次數
            print(f"您已經猜了{count}次")
        else: #格式正確才會執行
            count += 1
            if(keyin >= min and keyin <= max): #猜的數值範圍要>=最小值,<=最大值
                if keyin == target: # ==兩邊相等
                    print(f"賓果!猜對了,答案是:",target)
                    print(f"您總共猜了{count}次")
                    break #迴圈終止
                elif keyin > target: #給提示 else if
                    print("再小一點喔")
                    max = keyin - 1 #多複習!
                elif keyin < target:
                    print(("再大一點喔"))
                    min = keyin + 1

                print(f"您已經猜了{count}次")

            else: #若超出範圍,即傳出
                print("輸入錯誤,超出範圍")
                print(f"您已經猜了{count}次")

while(True):
    play_game()
    play_again = input("請問還要繼續嗎?y,n:")
    if play_again == 'n':
        break
print("遊戲結束")
