from django.apps import AppConfig


class Profiles1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles1'

from django.apps import AppConfig

class ProfilesConfig(AppConfig):
    name = 'profiles'

    def ready(self):
        import profiles.signals
