from turtle import position
from webbrowser import open_new_tab
import pyautogui as pt
import pyperclip as pc
from pynput.mouse import Controller, Button
from time import sleep
#from whatsapp_responses import response

#instruction for instagram bot

class instagram:

    #defines starting values
    

    def __init__(self, speed=.5, click_speed=.3):
        self.speed = speed
        self.click_speed = click_speed
        self.message = ''
        self.last_message = ''

    #navigate to likes
    def nav_likes_one(self):
        try: 
            position = pt.locateOnScreen('x_first.PNG', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(-330, 75, duration=self.speed)
            sleep(1)
        except Exception as e:
            print('Exception (nav_likes_one): ', e)
    
    def nav_likes_two(self):
        try: 
            position = pt.locateOnScreen('x_first.PNG', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(-330, 150, duration=self.speed)
            sleep(1)
        except Exception as e:
            print('Exception (nav_likes_two): ', e)

    def nav_likes_three(self):
        try: 
            position = pt.locateOnScreen('x_first.PNG', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(-330, 225, duration=self.speed)
            sleep(1)
        except Exception as e:
            print('Exception (nav_likes_three): ', e)

    def nav_likes_four(self):
        try: 
            position = pt.locateOnScreen('x_first.PNG', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(-330, 300, duration=self.speed)
            sleep(1)
        except Exception as e:
            print('Exception (nav_likes_four): ', e)
    
    def nav_likes_five(self):
        try: 
            position = pt.locateOnScreen('x_first.PNG', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(-330, 375, duration=self.speed)
            sleep(1)
        except Exception as e:
            print('Exception (nav_likes_five): ', e)

    def nav_likes_six(self):
        try: 
            position = pt.locateOnScreen('x_first.PNG', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(-330, 450, duration=self.speed)
            sleep(1)
        except Exception as e:
            print('Exception (nav_likes_six): ', e)

    #open new tab on the like
    def open_new_tab(self):
        # try: 
        pt.click(button='right', interval=self.click_speed)
        sleep(self.speed)
        position = pt.locateOnScreen('open_tab.PNG', confidence=.7)
        i = 0
        while i < 1:
            if position == None:
                print('lokasi tidak ditemukan')
                break
            else:
                pt.moveTo(position[0:2], duration=self.speed)
                pt.moveRel(5, 5, duration=self.speed)
                sleep(self.speed)
                pt.click(interval=self.click_speed)
        sleep(2)
        # except Exception as e:
        #     print('Exception (open_new_tab): ', e)
    
    #navigate to new tab
    def nav_new_tab(self):
        try: 
            position = pt.locateOnScreen('new_tab.PNG', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            sleep(self.speed)
            pt.moveRel(-200, 10, duration=self.speed)
            sleep(self.speed)
            pt.click(interval=self.click_speed)
        except Exception as e:
            print('Exception (nav_new_tab): ', e)

    #navigate to first post
    def nav_first_post(self):
        try: 
            pt.moveRel(0, 300, duration=self.speed)
            pt.scroll(-300)
            position = pt.locateOnScreen('post.PNG', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(-100, 100, duration=self.speed)
            sleep(self.speed)
            pt.click(interval=self.click_speed)
            sleep(3)
        except Exception as e:
            print('Exception (nav_first_post): ', e)
    
    #navigate to like
    def nav_like(self):
        try: 
            position = pt.locateOnScreen('arrow.PNG', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(-80, 15, duration=self.speed)
            sleep(self.speed)
            pt.click(interval=self.click_speed)
            sleep(1)
        except Exception as e:
            print('Exception (nav_like): ', e)
    
    #navigate to comment box and comment
    def nav_comment_one(self):
        try: 
            position = pt.locateOnScreen('arrow_comment.PNG', confidence=.9)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(20, 170, duration=self.speed)
            sleep(self.speed)
            pt.click(interval=self.click_speed)
            pt.typewrite('Keren Kak, ke Jepang murah hanya dengan follow IG Kami.', interval=.1)
            position = pt.locateOnScreen('ribbon.PNG', confidence=.9)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(10, 160, duration=self.speed)
            pt.click(interval=self.click_speed) 
            sleep(1)   
        except Exception as e:
            print('Exception (nav_comment_one): ', e)
    
    def nav_comment_two(self):
        try: 
            position = pt.locateOnScreen('arrow_comment.PNG', confidence=.9)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(20, 170, duration=self.speed)
            sleep(self.speed)
            pt.click(interval=self.click_speed)
            pt.typewrite('Keren! Follow kami untuk mendapatkan penawaran terbaik ke Jepang.', interval=.1)
            position = pt.locateOnScreen('ribbon.PNG', confidence=.9)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(10, 160, duration=self.speed)
            pt.click(interval=self.click_speed)
            sleep(1)     
        except Exception as e:
            print('Exception (nav_comment_two): ', e)
    
    def nav_comment_three(self):
        try: 
            position = pt.locateOnScreen('arrow_comment.PNG', confidence=.9)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(20, 170, duration=self.speed)
            sleep(self.speed)
            pt.click(interval=self.click_speed)
            pt.typewrite('Keren Kak, dapatkan info terbaru ke Jepang murah hanya dengan follow IG kami.', interval=.1)
            position = pt.locateOnScreen('ribbon.PNG', confidence=.9)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(10, 160, duration=self.speed)
            pt.click(interval=self.click_speed)
            sleep(1)     
        except Exception as e:
            print('Exception (nav_comment_three): ', e)
    
    #close new tab
    def close_new_tab(self):
        try: 
            position = pt.locateOnScreen('new_tab.PNG', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            sleep(self.speed)
            pt.moveRel(-30, 10, duration=self.speed)
            sleep(self.speed)
            pt.click(interval=self.click_speed)
            sleep(1)
        except Exception as e:
            print('Exception (close_new_tab): ', e)
    
    #scrolling the next six likes
    def scroll_next_likes(self):
        try: 
            position = pt.locateOnScreen('x_first.PNG', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(-330, 75, duration=self.speed)
            pt.scroll(-433)
            sleep(1)
        except Exception as e:
            print('Exception (scroll_next_like): ', e)
    
    #close chrome
    def close_chrome(self):
        try: 
            position = pt.locateOnScreen('chrome.PNG', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(60, -30, duration=self.speed)
            pt.click(interval=self.click_speed)
            sleep(1)
        except Exception as e:
            print('Exception (close_chrome): ', e)
   
    #copy the message
#    def get_message(self):
#        pt.tripleClick(interval=self.click_speed)
#        sleep(self.speed)
#        pt.click(button='right', interval=self.click_speed)
#        sleep(self.speed)
#        pt.moveRel(10, -150, duration=self.speed)
#        pt.click(interval=self.click_speed)
#        sleep(1)

#        self.message = pc.paste()
#        print('user says: ', self.message)

    #send message
#    def send_message(self):
#        try:
            #check if the last message is the same
#            if self.message != self.last_message:
#                bot_response = response(self.message)
#                print('you say: ', bot_response)
#                pt.typewrite(bot_response, interval=.1)
#                pt.typewrite('\n') #simulate enterkey

                #assign them the same message
#                self.last_message = self.message
            
#            else:
#                print('No new messages..')
        
#        except Exception as e:
#            print('Exception (send_message): ', e)
        


instagram_bot = instagram(speed=.5, click_speed=.4)
sleep(3)
n=1
x=0
y=0
#run program in a loop
while y < 12:
    i = 0
    #first itteration
    instagram_bot.nav_likes_one()
    pt.click(button='right', interval=0.1)
    sleep(1)
    position_x = pt.locateOnScreen('open_tab.PNG', confidence=.7)
    while i < 1:
            if position_x == None:
                pt.click(interval=0.1)
                print('lokasi tidak ditemukan')
                break
            else:
                pt.moveTo(position_x[0:2], duration=0.1)
                pt.moveRel(5, 5, duration=0.1)
                sleep(1)
                pt.click(interval=0.1)
                sleep(3)
                instagram_bot.nav_new_tab()
                instagram_bot.nav_first_post()
                instagram_bot.nav_like()
                if n == 1:
                    instagram_bot.nav_comment_one()
                    n=2
                elif n == 2:
                    instagram_bot.nav_comment_two()
                    n=3
                else:
                    instagram_bot.nav_comment_three()
                    n = 1
                break
    # instagram_bot.open_new_tab()
    # instagram_bot.nav_new_tab()
    # instagram_bot.nav_first_post()
    # instagram_bot.nav_like()
    # if n == 1:
    #     instagram_bot.nav_comment_one()
    #     n=2
    # elif n == 2:
    #     instagram_bot.nav_comment_two()
    #     n=3
    # else:
    #     instagram_bot.nav_comment_three()
    #     n = 1
    if position_x != None:
        instagram_bot.close_new_tab()
    x = x + 1
    print('IG Profile processed: ', x)

    #second itteration
    instagram_bot.nav_likes_two()
    pt.click(button='right', interval=0.1)
    sleep(1)
    position_x = pt.locateOnScreen('open_tab.PNG', confidence=.7)
    while i < 1:
            if position_x == None:
                pt.click(interval=0.1)
                print('lokasi tidak ditemukan')
                break
            else:
                pt.moveTo(position_x[0:2], duration=0.1)
                pt.moveRel(5, 5, duration=0.1)
                sleep(1)
                pt.click(interval=0.1)
                sleep(3)
                instagram_bot.nav_new_tab()
                instagram_bot.nav_first_post()
                instagram_bot.nav_like()
                if n == 1:
                    instagram_bot.nav_comment_one()
                    n=2
                elif n == 2:
                    instagram_bot.nav_comment_two()
                    n=3
                else:
                    instagram_bot.nav_comment_three()
                    n = 1
                break
    # instagram_bot.open_new_tab()
    # instagram_bot.nav_new_tab()
    # instagram_bot.nav_first_post()
    # instagram_bot.nav_like()
    # if n == 1:
    #     instagram_bot.nav_comment_one()
    #     n=2
    # elif n == 2:
    #     instagram_bot.nav_comment_two()
    #     n=3
    # else:
    #     instagram_bot.nav_comment_three()
    #     n = 1
    # instagram_bot.close_new_tab()
    if position_x != None:
        instagram_bot.close_new_tab()
    x = x + 1
    print('IG Profile likes: ', x)

    #third itteration
    instagram_bot.nav_likes_three()
    pt.click(button='right', interval=0.1)
    sleep(1)
    position_x = pt.locateOnScreen('open_tab.PNG', confidence=.7)
    while i < 1:
            if position_x == None:
                pt.click(interval=0.1)
                print('lokasi tidak ditemukan')
                break
            else:
                pt.moveTo(position_x[0:2], duration=0.1)
                pt.moveRel(5, 5, duration=0.1)
                sleep(1)
                pt.click(interval=0.1)
                sleep(3)
                instagram_bot.nav_new_tab()
                instagram_bot.nav_first_post()
                instagram_bot.nav_like()
                if n == 1:
                    instagram_bot.nav_comment_one()
                    n=2
                elif n == 2:
                    instagram_bot.nav_comment_two()
                    n=3
                else:
                    instagram_bot.nav_comment_three()
                    n = 1
                break
    # instagram_bot.open_new_tab()
    # instagram_bot.nav_new_tab()
    # instagram_bot.nav_first_post()
    # instagram_bot.nav_like()
    # if n == 1:
    #     instagram_bot.nav_comment_one()
    #     n=2
    # elif n == 2:
    #     instagram_bot.nav_comment_two()
    #     n=3
    # else:
    #     instagram_bot.nav_comment_three()
    #     n = 1
    # instagram_bot.close_new_tab()
    if position_x != None:
        instagram_bot.close_new_tab()
    x = x + 1
    print('IG Profile likes: ', x)

    #fourth itteration
    instagram_bot.nav_likes_four()
    pt.click(button='right', interval=0.1)
    sleep(1)
    position_x = pt.locateOnScreen('open_tab.PNG', confidence=.7)
    while i < 1:
            if position_x == None:
                pt.click(interval=0.1)
                print('lokasi tidak ditemukan')
                break
            else:
                pt.moveTo(position_x[0:2], duration=0.1)
                pt.moveRel(5, 5, duration=0.1)
                sleep(1)
                pt.click(interval=0.1)
                sleep(3)
                instagram_bot.nav_new_tab()
                instagram_bot.nav_first_post()
                instagram_bot.nav_like()
                if n == 1:
                    instagram_bot.nav_comment_one()
                    n=2
                elif n == 2:
                    instagram_bot.nav_comment_two()
                    n=3
                else:
                    instagram_bot.nav_comment_three()
                    n = 1
                break
    # instagram_bot.open_new_tab()
    # instagram_bot.nav_new_tab()
    # instagram_bot.nav_first_post()
    # instagram_bot.nav_like()
    # if n == 1:
    #     instagram_bot.nav_comment_one()
    #     n=2
    # elif n == 2:
    #     instagram_bot.nav_comment_two()
    #     n=3
    # else:
    #     instagram_bot.nav_comment_three()
    #     n = 1
    # instagram_bot.close_new_tab()
    if position_x != None:
        instagram_bot.close_new_tab()
    x = x + 1
    print('IG Profile likes: ', x)

    #fifth itteration
    instagram_bot.nav_likes_five()
    pt.click(button='right', interval=0.1)
    sleep(1)
    position_x = pt.locateOnScreen('open_tab.PNG', confidence=.7)
    while i < 1:
            if position_x == None:
                pt.click(interval=0.1)
                print('lokasi tidak ditemukan')
                break
            else:
                pt.moveTo(position_x[0:2], duration=0.1)
                pt.moveRel(5, 5, duration=0.1)
                sleep(1)
                pt.click(interval=0.1)
                sleep(3)
                instagram_bot.nav_new_tab()
                instagram_bot.nav_first_post()
                instagram_bot.nav_like()
                if n == 1:
                    instagram_bot.nav_comment_one()
                    n=2
                elif n == 2:
                    instagram_bot.nav_comment_two()
                    n=3
                else:
                    instagram_bot.nav_comment_three()
                    n = 1
                break
    # instagram_bot.open_new_tab()
    # instagram_bot.nav_new_tab()
    # instagram_bot.nav_first_post()
    # instagram_bot.nav_like()
    # if n == 1:
    #     instagram_bot.nav_comment_one()
    #     n=2
    # elif n == 2:
    #     instagram_bot.nav_comment_two()
    #     n=3
    # else:
    #     instagram_bot.nav_comment_three()
    #     n = 1
    # instagram_bot.close_new_tab()
    if position_x != None:
        instagram_bot.close_new_tab()
    x = x + 1
    print('IG Profile likes: ', x)

    #sixth itteration
    instagram_bot.nav_likes_six()
    pt.click(button='right', interval=0.1)
    sleep(1)
    position_x = pt.locateOnScreen('open_tab.PNG', confidence=.7)
    while i < 1:
            if position_x == None:
                pt.click(interval=0.1)
                print('lokasi tidak ditemukan')
                break
            else:
                pt.moveTo(position_x[0:2], duration=0.1)
                pt.moveRel(5, 5, duration=0.1)
                sleep(1)
                pt.click(interval=0.1)
                sleep(3)
                instagram_bot.nav_new_tab()
                instagram_bot.nav_first_post()
                instagram_bot.nav_like()
                if n == 1:
                    instagram_bot.nav_comment_one()
                    n=2
                elif n == 2:
                    instagram_bot.nav_comment_two()
                    n=3
                else:
                    instagram_bot.nav_comment_three()
                    n = 1
                break
    # instagram_bot.open_new_tab()
    # instagram_bot.nav_new_tab()
    # instagram_bot.nav_first_post()
    # instagram_bot.nav_like()
    # if n == 1:
    #     instagram_bot.nav_comment_one()
    #     n=2
    # elif n == 2:
    #     instagram_bot.nav_comment_two()
    #     n=3
    # else:
    #     instagram_bot.nav_comment_three()
    #     n = 1
    # instagram_bot.close_new_tab()
    if position_x != None:
        instagram_bot.close_new_tab()
    x = x + 1
    print('IG Profile likes: ', x)

    y = y + 1
    #scrolling to next six likes
    instagram_bot.scroll_next_likes()
    sleep(3) #delay between checking message
#finish
#instagram_bot.close_chrome()
