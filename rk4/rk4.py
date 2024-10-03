#!/usr/bin/env python3
def rk4(func, oper, state, h):

    """Aquí se realizan las ecuaciónes del metodo rk4 y se obtiene el valor siguiente del sistema.

    Examples:
        >>> rk4(x,y,z,w)
        2.0

    Args:
        func (función): First argument
        oper (numpy.ndarray): Second argument
        state (numpy.ndarray): Third argument
        h (numpy.float64): Fourth argument

    Returns:
        result (numpy.ndarray): Retorna el resultado siguiente del metodo

    """

    k1 = h * func(oper, state)
    k2 = h * func(oper, (state + (0.5 * k1)))
    k3 = h * func(oper, (state + (0.5 * k2)))
    k4 = h * func(oper, state + k3)
    return state + (1/6) * (k1 + k2 + k3 + k4)

