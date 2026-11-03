from PyMPDATA import ScalarField, VectorField, Options, Solver, Stepper
from PyMPDATA.boundary_conditions import Periodic
import numpy as np

options = Options()

common = {
    "halo": options.n_halo,
    "boundary_conditions": (Periodic()  ,),
}

advectee = ScalarField(**common, data = np.exp(-(x := np.linspace(-2, 8, 41)) ** 2))
advector = VectorField(**common, data = (np.full(shape=x.size+1, fill_value = 0.25),))

from matplotlib import pyplot as plt
plt.step(x, advectee.get(), where='mid', label='advectee')
plt.axvline(0, color='k', linestyle='--', label='x=0')
plt.show()

solver = Solver(advectee = advectee, advector = advector, stepper = Stepper(n_dims=1, options=options))

solver.advance(n_steps = 100)
plt.step(x, advectee.get(), where='mid', label='advectee')
plt.axvline(0, color='k', linestyle='--', label='x=0')
plt.show()
