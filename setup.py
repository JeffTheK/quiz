from setuptools import setup

setup(
    name = "quiz",
    version = "0.1.0",
    description = "TODO",
    author = "JeffTheK",
    url = "https://github.com/JeffTheK/quiz",
    packages = ["quiz"],
    entry_points = {
        'console_scripts': [
            'quiz = quiz.main:run'
        ]
    }
)