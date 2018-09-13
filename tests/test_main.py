
from sxlxs.main import mainTest

def test_sxlxs(tmp):
    with mainTest() as app:
        res = app.run()
        print(res)
        raise Exception

def test_command1(tmp):
    argv = ['command1']
    with mainTest(argv=argv) as app:
        app.run()
