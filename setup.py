from setuptools import setup, find_packages

setup(
    name='mono',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        #парсить сюда requerements.txt?
    ],
    entry_points={
        "lms.djangoapp": [
            "mono = MonoSpeedRun.apps:MonoConfig",
        ],
        "cms.djangoapp": [
        ],
    }
)
