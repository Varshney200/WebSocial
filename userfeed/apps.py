from django.apps import AppConfig


class UserfeedConfig(AppConfig):
    name = 'userfeed'

    def ready(self):
        import userfeed.signals