import quiz.main

def test_main(capsys):
    quiz.main.run()
    out, err = capsys.readouterr()
    assert(out == "hello world\n")

def test_load_questions():
    out = quiz.main.load_questions()
    assert(len(out) == 2)
    assert(out[0]["answer"] == "Amsterdam")