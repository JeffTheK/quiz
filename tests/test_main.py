import quiz.main

def test_main(capsys):
    quiz.main.run()
    out, err = capsys.readouterr()
    assert(out == "hello world\n")