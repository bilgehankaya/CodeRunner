import subprocess
from app.compiler.coderunner import CodeRunner

extensions = {
    "java": ".java",
    "python": ".py",
    "node": ".js"
}


def test(lang):
    with open("./test_data/testinput.txt") as test, open(f"./test_data/test{extensions[lang]}") as code:
        code_runner = CodeRunner(
            language=lang, code=code.read(), test_input=test.read())
    return code_runner.get_result()


if __name__ == "__main__":
    print(test("java"))
