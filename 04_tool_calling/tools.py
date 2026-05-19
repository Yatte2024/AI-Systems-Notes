import ast
import operator


ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}


def search_web(query: str):
    return {
        "query": query,
        "results": [
            "AI systems overview",
            "Agent workflow article",
            "Structured output guide",
        ],
    }


def calculator(expression: str):
    result = _evaluate_math_expression(expression)

    return {
        "expression": expression,
        "result": result,
    }


def verify_claim(claim: str):
    return {
        "claim": claim,
        "verified": True,
        "confidence": 0.91,
    }


def _evaluate_math_expression(expression: str):
    tree = ast.parse(expression, mode="eval")

    return _evaluate_node(tree.body)


def _evaluate_node(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value

    if isinstance(node, ast.BinOp):
        operator_function = ALLOWED_OPERATORS.get(type(node.op))

        if operator_function is None:
            raise ValueError("Unsupported calculator operator.")

        return operator_function(
            _evaluate_node(node.left),
            _evaluate_node(node.right),
        )

    raise ValueError("Unsupported calculator expression.")
