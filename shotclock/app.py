from django.apps import AppConfig


class ShotClockConfig(AppConfig):
    name = 'shotclock'

    def ready(self):
        import shotclock.signals  # noqa: F401
