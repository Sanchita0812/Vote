def add_numbers(x, y):
    """Adds two numbers together.

    Args:
        x: The first number.
        y: The second number.

    Returns:
        The sum of x and y.  Returns an error message if inputs are not numbers.
    """
    if not isinstance(x,(int,float)) or not isinstance(y,(int,float)):
        return "Error: Inputs must be numbers."
    return x + y
