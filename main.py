#File and local files stuff 
import sys
import os

#All custom modules
from start import starting
from recommendedFollow import randomFollow
from choosenFollow import choosen_Following
from cleanUnfollowers import cleaner

#Importing kivy configurations for front-end development
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.config import Config

kv = Builder.load_file("main.kv")

class CleanAlwaysPopup(Screen):
    Config.set('graphics','resizable','0')
    def always(self):
        limitation = int(self.ids.limitation.text)
        new_cleaner = cleaner(driver,limitation)
        new_cleaner.findUnfollowers()
        sm.current = "_main_screen_"
        
    def cancel(self):
        sm.current = "_main_screen_"

class HashtagPopupScreen(Screen):
    def get_hashtag(self):
        self.hashtag = self.ids.hashtag.text
        # Customized Following
        new_customFollow = choosen_Following(driver,self.hashtag)
        user_follower = new_customFollow.set()
        user_follower = int(user_follower)
        new_customFollow.followAlways(user_follower)
        sm.current = "_main_screen_"
        
    def cancel(self):
        sm.current = "_main_screen_"
        

class LoginScreen(Screen):
    def login(self):
        self.username = self.ids.ussername.text
        self.password = self.ids.passsword.text
        #Change page first
        sm.current = "_main_screen_"
        # Starting and setting everything to sign in an go home page of instagram
        new_starting = starting(self.username,self.password)
        global driver
        driver = new_starting.driver
        new_starting.open_Ig()
        new_starting.sign_In()
        new_starting.goToMainPage()
    def quit(self):
        sys.exit()

class MainScreen(Screen):
    def recommended_follow(self):
        print("recommended working!")
        # Recommended following 
        new_recommendedFollow = randomFollow(driver,43)
        new_recommendedFollow.goToRecommended()
        new_recommendedFollow.followAll()
    
    def clean_unfollowers(self):
        sm.current = "_clean_always_popup_"

    def hashtag_popup_start(self):
        sm.current = "_hashtag_popup_screen_"
        
    def quit(self):
        sys.exit()

sm = ScreenManager()
sm.add_widget(LoginScreen())
sm.add_widget(MainScreen())
sm.add_widget(HashtagPopupScreen())
sm.add_widget(CleanAlwaysPopup())

class MyApp(App):
    def build(self):
        return sm


if __name__ == '__main__':
    MyApp().run()
    

