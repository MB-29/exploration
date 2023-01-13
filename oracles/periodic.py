import numpy as np

from agents import Agent


class Periodic1D(Agent):

    def __init__(self, model, d, m, gamma, dt):
        super().__init__(model, d, m, gamma, dt=dt)
        self.t_period = model.t_period

    def policy(self, x, t):
        u = self.gamma * np.sign(np.sin(2*np.pi*t/self.t_period))
        return np.array([u])


class Periodic2D(Agent):

    def __init__(self, model, d, m, gamma, dt, batch_size):
        super().__init__(model, d, m, gamma, batch_size, dt)
        self.t_period = model.t_period

    def policy(self, x, t):
        u = np.zeros(2)
        u[0] = self.gamma * np.sign(np.sin(2*np.pi*t/self.t_period))
        # u[1] = self.gamma * np.cos(2*np.pi*t*self.t_period)
        return u
