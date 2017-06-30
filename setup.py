from distutils.core import setup

setup(
    name = 'mygreeter',
    packages = ['mygreeter'],
    version = 'v0.0.2',  # Ideally should be same as your GitHub release tag varsion
    description = 'Package to greet me, you or the world',
    author = 'Timon Schmelzer',
    author_email = 'timon.schmelzer@tu-dortmund.de',
    url = 'https://github.com/Kecksdose/mygreeter',
    download_url = 'https://github.com/Kecksdose/mygreeter/archive/v0.0.2.tar.gz',
    keywords = ['hello world', 'greeter', 'greetings'],
    classifiers = [],
)
