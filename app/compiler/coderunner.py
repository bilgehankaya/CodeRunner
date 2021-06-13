import subprocess


class CodeRunner:
    _file_name = "solution"
    _file_direc = "/tmp/"

    def __init__(self, language: str, code: str, test_input: str):
        self._language = language
        self._code = code
        self._test_input = test_input
        self._file_path = f"{self._file_direc}{self._file_name}{self._get_file_extension()}"

    def _get_file_extension(self) -> str:
        extensions = {
            "java": ".java",
            "python": ".py"
        }
        return extensions[self._language]

    def _get_command(self) -> str:
        if self._language == "java":
            command = (
                f"javac -cp {self._file_direc} {self._file_path} &&"
                f"java -cp {self._file_direc} {self._file_name}"
            )
        else:  # for python
            command = f"{self._language } {self._file_path}"
        return command

    def _create_file(self):
        with open(self._file_path, "w") as f:
            f.write(self._code)

    def get_result(self) -> tuple[str]:
        self._create_file()
        result = subprocess.run(
            self._get_command(),
            capture_output=True,
            shell=True,
            input=self._test_input,
            text=True
        )
        print(result)

        if result.stdout:
            return False, result.stdout.removesuffix("\n")
        return True, result.stderr.replace(self._file_direc, "").removesuffix("\n")
