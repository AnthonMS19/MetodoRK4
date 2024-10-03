#!/usr/bin/env python 3
def dyngenerator(oper, state):

    """Esta funcion define la funcion a la cual se le aplica el metodo

    Examples:
        >>> dyn_generator(x,y)
        [[0.-0.j 0.+1.j][0.-1.j 0.-0.j]]

    Args:
        oper (numpy.ndarray): First argument
        state (numpy.ndarray): Second argument

    Returns:
        result (numpy.ndarray): Retorna una matriz que es la función a la que aplicar el metodo
    """

    return -1.0j * (np.dot(oper,state) - np.dot(state,oper)) 
