from django.apps import AppConfig


class FizzBuzzConfig(AppConfig):
    name = 'fizzbuzz'

    def ready(self):
        import fizzbuzz.signals  # noqa: F401
