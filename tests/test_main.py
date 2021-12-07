import quiz.main

def test_load_questions():
    out = quiz.main.load_questions()
    assert(len(out) == 2)
    assert(out[0]["answer"] == "Amsterdam")