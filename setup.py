try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Moon Landing Game',
    'author': 'Anatoliy Poletaev',
    'url': 'https://github.com/Shtepser/MoonLandingGame',
    'download_url': 'https://github.com/Shtepser/MoonLandingGame',
    'author_email': 'Shtepser@yandex.ru',
    'version': 1.0,
    'install_requires': ['nose'],
    'packages': ['moonlanding'],
    'scripts': [],
    'entry_points': {
        "console_scripts": [
            "run_game = moonlanding.main:main"
        ]
    },
    'name': 'MoonLanding'
}

setup(**config)
