from django.apps import AppConfig


class MonoConfig(AppConfig):

    name = 'mono'
    print('ne mongo db, just mono' * 200)
    plugin_app = {
        "url_config": {
            # ProjectType.LMS p.s. const LMS equal to "lms.djangoapp"
            'lms.djangoapp': {
                "namespace": 'mono',
                "regex": '^mono/',
                "relative_path": 'urls'
            }
        }
    }