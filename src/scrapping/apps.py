from django.apps import AppConfig


class ScrappingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'scrapping'
    verbose_name='Приложение по сбору вакансии'
