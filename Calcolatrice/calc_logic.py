# calc_logic.py

def evaluate_expression(expression):
    try:
        # Usa eval per calcolare l'espressione
        result = eval(expression)
        return result
    except Exception:
        return "Error"
