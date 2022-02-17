import re


class LatexParser:
    """
    LatexParser
    this can parse latex style mathmatics to tree architecture
    """

    def __init__(self) -> None:
        pass


def parse_inline(inputs: str):
    inputs = re.sub(r"(^\n*\$+\n*)|(\n*\$+\n*$)", "", inputs)
    function, *equations = inputs.split("=")
    equation = "".join(equations)
    # parse args
    f_name = re.sub(r"{|}", "", re.sub(r"\(.*\)", "", function)).strip()
    args = re.split(r"\s*,\s*", re.sub(r"(.*\(|\).*)", "", function))
    args = [re.sub(r"{|}", "", arg) for arg in args]
    tree = {}
    tree["equation"] = ""

    return f_name, args, equation.strip()


if __name__ == "__main__":
    latex = "$$f(x_{1}, x_{2}) = x_{1}^2 + x_{2}^2 + 3$$"
    print(latex)
    print(parse_inline(latex))
