from kivy.app import App #initiates the app
from kivy.uix.button import Button #a button
from kivy.uix.label import Label #label
from kivy.uix.floatlayout import FloatLayout #helps create a floating lay out
from kivy.uix.scatter import Scatter #helps move widgets in any manner with hand when app is running
from kivy.uix.textinput import TextInput #allows user to input text
from kivy.uix.boxlayout import BoxLayout #arranges all child widgets in a box layout
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
class ProfileScreen(Screen):
    pass

class MainApp(App):
    def build(self):
        self.fb = firebase()

    def change_screen(self,screen_name):
        print(self.root)
        screen_changer = self.root
        screen_changer.current = screen_name

if __name__=='__main__':
    MainApp().run()
