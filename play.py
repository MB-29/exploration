import importlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc, rcParams

from agents import Random, Passive
from active_agents import GradientDesign, Spacing, Variation, D_optimal

from environments import get_environment

ENVIRONMENT_NAME = 'aircraft'
ENVIRONMENT_NAME = 'arm'
ENVIRONMENT_NAME = 'pendulum'
ENVIRONMENT_NAME = 'damped_cartpole'
ENVIRONMENT_NAME = 'gym_cartpole'
ENVIRONMENT_NAME = 'damped_pendulum'
ENVIRONMENT_NAME = 'linearized_pendulum'
ENVIRONMENT_NAME = 'gym_pendulum'
# ENVIRONMENT_NAME = 'quadrotor'

ENVIRONMENT_PATH = f'environments.{ENVIRONMENT_NAME}'
# TODO : get_model
MODEL_PATH = f"models.{ENVIRONMENT_NAME.split('_')[-1]}"
ORACLE_PATH = f'oracles.{ENVIRONMENT_NAME}'
Environment = get_environment(ENVIRONMENT_NAME)
# Environment = importlib.import_module(ENVIRONMENT_PATH).GymPendulum
models = importlib.import_module(MODEL_PATH)

plot = False    
plot = True

T = 100
T_random = 0
dt = 2e-2
dt = 80e-3
environment = Environment(dt)

model = models.NeuralModel(environment)
# model = models.LinearModel(environment)
model = models.GymNeural(environment)
# model = models.Partial(environment)

gamma = environment.gamma
sigma = environment.sigma

# x0 = np.array([np.pi/2, 0.0])
x0 = environment.x0.copy()

# from oracles.cartpole import PeriodicOracle
Agent = Passive
Agent = Random
Agent = D_optimal
# Agent = PeriodicOracle
# Agent = Spacing
# Agent = oracles.LinearOracle

# model = models.Model()

# model = models.LinearModel()

agent = Agent(
    x0.copy(),
    environment.m,
    environment.dynamics,
    model,
    gamma,
    environment.dt
    )

test_values = agent.identify(
    T,
    test_function=environment.test_error,
    plot=plot,
    T_random=T_random
    )

plt.plot(test_values, alpha=0.7)
plt.title(r'Test loss')
plt.show()
