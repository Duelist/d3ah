from mongoengine.django.auth import check_password, MongoEngineBackend
from social.models import AppUser

class AppUserAuthBackend(MongoEngineBackend):
    def authenticate(self, username=None, password=None):
        user_username = AppUser.objects(username=username).first()
        user_email = AppUser.objects(email=username).first()
        user = user_username or user_email
        if user:
            if password and user.check_password(password):
                return user
        return None
    
    def get_user(self, user_id):
        return AppUser.objects.with_id(user_id)