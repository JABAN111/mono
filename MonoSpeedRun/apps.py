from django.apps import AppConfig

class MonoConfig(AppConfig):
    name = 'MonoSpeedRun'  # Имя пакета, а не путь к классу

    plugin_app = {
        "url_config": {
            'lms.djangoapp': {
                "namespace": 'mono',
                "regex": '^mono/',
                "relative_path": 'urls'
            }
        }
    }
