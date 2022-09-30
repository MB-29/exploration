
from oracles.periodic import Periodic1D


class PeriodicOracle(Periodic1D):

    def __init__(self, x0, m, dynamics, model, gamma, dt):
        super().__init__(x0, m, dynamics, model, gamma, dt, model.period)


oracles = {'periodic': PeriodicOracle}
