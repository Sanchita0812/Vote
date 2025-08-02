def multiply(a, b):
    """
    Multiplies two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The product of a and b.  Returns an error message if input is not a number.
    """
    if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
        return "Error: Inputs must be numbers."
    return a * b
