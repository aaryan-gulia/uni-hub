from kivy.app import App #initiates the app
from kivy.uix.button import Button #a button
from kivy.uix.label import Label #label
from kivy.uix.floatlayout import FloatLayout #helps create a floating lay out
from kivy.uix.scatter import Scatter #helps move widgets in any manner with hand when app is running
from kivy.uix.textinput import TextInput #allows user to input text
from kivy.uix.boxlayout import BoxLayout #arranges all child widgets in a box layout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.checkbox import CheckBox
from kivy.uix.behaviors import ButtonBehavior
from kivy.lang import Builder #to include Kv file without issues with name.
from kivy.properties import ListProperty, ObjectProperty, NumericProperty #to declare non-kivy entities as kivy properties
from kivy.graphics.vertex_instructions import (Rectangle, Ellipse, Line) #canvas graphics
from kivy.graphics.context_instructions import Color #canvas graphics

from functools import partial
from os import walk
import time

from firebase import firebase

class LoginScreen(Screen):
    pass
class HomeScreen(Screen):
    pass
class CreateActivityScreen(Screen):
    pass
class JoinActivityScreen(Screen):
    pass
class ActivitySubmittedScreen(Screen):
    pass
class SearchResultScreen(Screen):
    def CreateButtons(self):
        activities=MainApp.fb.get_activities()
        for i in range(len(activities)-1):
            button = Button(text = (activities[i][0]['name'])+'\n'+'Location: '+(activities[i][0]['location'])+'\n'+'remote/in person: '+str(activities[i][0]['remote/in_person'][0])+'/'+str(activities[i][0]['remote/in_person'][1])+'\n'+'Date: '+(activities[i][0]['date'])+'\n'+'Time: '+(activities[i][0]['time'])+'\n'+'Discription: '+(activities[i][0]['discription'])+'\n'+'Contact Creator: '+(activities[i][0]['email']))
            button.id = str(i)
            button.background_normal="pictures/bgtexture2.jpg"
            button.background_down="pictures/bgtexture2.jpg"
            button.color=(1,1,1)
            button.font_size=30
            button.size_hint=(1.0,0.15)
            button.pos_hint={'top':0.75-2*i/10,'right':1.0}
            button.halign='center'
            self.ids['scroll_gridlayout'].size_hint_y = 10*i/10
            self.ids['scroll_gridlayout'].add_widget(button)

class ProfileScreen(Screen):
    pass
class ActivityScreen(GridLayout):
    activity_dict = ObjectProperty(None)
    pass

class MainApp(App):
    fb = firebase()

    def change_screen(self,screen_name):
        print(self.root)
        screen_changer = self.root
        screen_changer.current = screen_name

    def new_activity_screen(self,i):
        activity = MainApp.fb.get_activities()[i][1]
        name = activity['name']+str(time.time())
        id = name
        s = ActivityScreen(name=name,id=id,activity_dict=activity)
        self.root.add_widget(s)
        self.root.current = s

if __name__=='__main__':
    MainApp().run()
