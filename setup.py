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
            'quiz = quiz.main:run'
        ]
    },
    package_data = {
        "quiz": [
            "data/**"
        ]
    }

)