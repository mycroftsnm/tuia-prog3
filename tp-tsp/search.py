"""Este modulo define la clase LocalSearch.

LocalSearch representa un algoritmo de busqueda local general.

Las subclases que se encuentran en este modulo son:

* HillClimbing: algoritmo de ascension de colinas. Se mueve al sucesor con
mejor valor objetivo. Ya viene implementado.

* HillClimbingReset: algoritmo de ascension de colinas de reinicio aleatorio.
No viene implementado, se debe completar.

* Tabu: algoritmo de busqueda tabu.
No viene implementado, se debe completar.
"""


from __future__ import annotations
from time import time
from problem import OptProblem


class LocalSearch:
    """Clase que representa un algoritmo de busqueda local general."""

    def __init__(self) -> None:
        """Construye una instancia de la clase."""
        self.niters = 0  # Numero de iteraciones totales
        self.time = 0  # Tiempo de ejecucion
        self.tour = []  # Solucion, inicialmente vacia
        self.value = None  # Valor objetivo de la solucion

    def solve(self, problem: OptProblem):
        """Resuelve un problema de optimizacion."""
        self.tour = problem.init
        self.value = problem.obj_val(problem.init)


class HillClimbing(LocalSearch):
    """Clase que representa un algoritmo de ascension de colinas.

    En cada iteracion se mueve al estado sucesor con mejor valor objetivo.
    El criterio de parada es alcanzar un optimo local.
    """

    def solve(self, problem: OptProblem):
        """Resuelve un problema de optimizacion con ascension de colinas.

        Argumentos:
        ==========
        problem: OptProblem
            un problema de optimizacion
        """
        # Inicio del reloj
        start = time()

        # Arrancamos del estado inicial
        actual = problem.init
        value = problem.obj_val(problem.init)

        while True:

            # Buscamos la acción que genera el sucesor con mayor valor objetivo
            act, succ_val = problem.max_action(actual)

            # Retornar si estamos en un maximo local:
            # el valor objetivo del sucesor es menor o igual al del estado actual
            if succ_val <= value:

                self.tour = actual
                self.value = value
                end = time()
                self.time = end-start
                return

            # Sino, nos movemos al sucesor
            actual = problem.result(actual, act)
            value = succ_val
            self.niters += 1


class HillClimbingReset(LocalSearch):
    """Algoritmo de ascension de colinas con reinicio aleatorio."""

    REINICIOS = 5  # Cantidad de reinicios aleatorios
    
    def solve(self, problem: OptProblem):
        """Resuelve un problema de optimizacion con ascension de colinas con reinicio aleatorio.

        Argumentos:
        ==========
        problem: OptProblem
            un problema de optimizacion
        """
        # Inicio del reloj
        start = time()

        for _ in range(self.REINICIOS):
            actual = problem.random_reset()
            value = problem.obj_val(actual)
            self.value = value

            while True:
                act, succ_val = problem.max_action(actual)

                if succ_val <= value: #Maximo local -> nos quedamos con el mayor valor y reiniciamos
                    if value > self.value:
                        self.tour = actual
                        self.value = value
                    break

                actual = problem.result(actual, act)
                value = succ_val
                self.niters += 1

        end = time()
        self.time = end - start



class Tabu(LocalSearch):
    """Algoritmo de busqueda tabu."""

    ITERACIONES = 20  # Cantidad de iteraciones sin mejoras permitidas // pasos laterales
    TABU_SIZE = 15  # Cantidad máxima de acciones en la lista tabú


    def solve(self, problem: OptProblem):
        """Resuelve un problema de optimizacion con busqueda tabú.

        Argumentos:
        ==========
        problem: OptProblem
            un problema de optimizacion
        """
        # Inicio del reloj
        start = time()
        tabu = []
        # Arrancamos del estado inicial
        actual = problem.init
        self.value = problem.obj_val(problem.init)
        iteraciones = self.ITERACIONES
       
        while iteraciones > 0:
            act, succ_val = problem.max_action(actual, tabu)
            actual = problem.result(actual, act)
            self.niters += 1
            iteraciones -= 1

            if succ_val > self.value:
                iteraciones = self.ITERACIONES
                self.value = succ_val
                self.tour = actual

            tabu.append(act)

            while len(tabu) > self.TABU_SIZE:
                tabu.pop(0)

        end = time()
        self.time = end - start
        