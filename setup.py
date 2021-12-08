from setuptools import setup

setup(
    name = "quiz",
    version = "1.0.0",
    description = "Simple terminal quiz game",
    author = "JeffTheK",
    url = "https://github.com/JeffTheK/quiz",
    packages = ["quiz"],
    entry_points = {
        'console_scripts': [
            'quiz = quiz.__main__:main'
        ]
    },
    package_data = {
        "quiz": [
            "data/**"
        ]
    }

)