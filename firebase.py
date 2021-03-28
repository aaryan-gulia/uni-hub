import firebase_admin
from firebase_admin import credentials, firestore
import string
from operator import itemgetter

cred = credentials.Certificate("uni-hub-c04bd-firebase-adminsdk-5sbqj-ba8cc08404.json")
firebase_admin.initialize_app(cred)
db = firebase_admin.firestore.client()

class firebase():

    def signup(self, email, password):
        new_user = db.collection("users").document().set({'email':email.lower(), 'password':password})

    def signin(self, email, password):
        self.email = email
        get_user = db.collection('users').where('email','==',email.lower()).stream()
        for user in get_user:
            user_dict = user.to_dict()
            user_id = user.id
            if user_dict["password"] == password:
                self.user_id = user_id
                return user_id
            else: print("not a user")


    def create_activity(self,info):
        if len(info["name"])==0:
            return False
        info["email"] = self.email
        info["user_id"] = self.user_id
        new_activity = db.collection("Activities").document().set(info)
        return True

    def search_activity(self,info):
        self.activities = list()
        activities = db.collection('Activities').stream()
        for activity in activities:
            match_score = 0
            activity_dict = activity.to_dict()
            if (activity_dict['name'].lower() == info['name'].lower()) and len(info['name']) != 0:
                match_score += 1
            if (activity_dict['location'].lower() == info['location'].lower()) and len(info['location']) != 0:
                match_score += 2
            if (activity_dict['remote/in_person']==info['remote/in_person']):
                match_score += 1
            self.activities.append([activity_dict,match_score])
        print(self.activities)
        return self.activities

    def get_activities(self):
        return self.activities
