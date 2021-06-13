from ..schemas.schemas import Request, languages
from typing import Literal
from ..compiler.coderunner import CodeRunner


def get_output(language: Literal[languages], request: Request) -> dict:
    code_runner = CodeRunner(
        language=language,
        code=request.code,
        test_input=request.testInput
    )
    is_error, output = code_runner.get_result()
    return {"error": is_error, "output": output}
