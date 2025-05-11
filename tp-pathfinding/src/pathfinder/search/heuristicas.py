def distancia_manhattan(estado, estado_objetivo):
    """
    Calcula la distancia de Manhattan entre el estado actual y el estado objetivo.
    """
    return (abs(estado_objetivo[1] - estado[1]) + abs(estado_objetivo[0] - estado[0]))

def distancia_euclidiana(estado, estado_objetivo):
    """
    Calcula la distancia euclidiana entre el estado actual y el estado objetivo.
    """
    return ((estado_objetivo[1] - estado[1]) ** 2 + (estado_objetivo[0] - estado[0]) ** 2) ** 0.5
