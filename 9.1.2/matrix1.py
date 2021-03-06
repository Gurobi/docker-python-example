#!/usr/bin/env python3.7

# Copyright 2021, Gurobi Optimization, LLC

# This example formulates and solves the following simple MIP model
# using the matrix API:
#  maximize
#        x +   y + 2 z
#  subject to
#        x + 2 y + 3 z <= 4
#        x +   y       >= 1
#        x, y, z binary

import numpy as np
import scipy.sparse as sp
import gurobipy as gp
from gurobipy import GRB
import os


try:

    # Setup the Gurobi environment with the WLS license
    e = gp.Env(empty=True)

    wlsaccessID = os.getenv('GRB_WLSACCESSID','undefined')
    e.setParam('WLSACCESSID', wlsaccessID)

    licenseID = os.getenv('GRB_LICENSEID', '0')
    e.setParam('LICENSEID', int(licenseID))

    wlsSecrets = os.getenv('GRB_WLSSECRET','undefined')
    e.setParam('WLSSECRET', wlsSecrets)

    e.setParam('CSCLIENTLOG', int(3))

    e.start()


    # Create the model within the Gurobi environment
    m = gp.Model(env=e, name="matrix1")

    # Create variables
    x = m.addMVar(shape=3, vtype=GRB.BINARY, name="x")

    # Set objective
    obj = np.array([1.0, 1.0, 2.0])
    m.setObjective(obj @ x, GRB.MAXIMIZE)

    # Build (sparse) constraint matrix
    data = np.array([1.0, 2.0, 3.0, -1.0, -1.0])
    row = np.array([0, 0, 0, 1, 1])
    col = np.array([0, 1, 2, 0, 1])

    A = sp.csr_matrix((data, (row, col)), shape=(2, 3))

    # Build rhs vector
    rhs = np.array([4.0, -1.0])

    # Add constraints
    m.addConstr(A @ x <= rhs, name="c")

    # Optimize model
    m.optimize()

    print(x.X)
    print('Obj: %g' % m.objVal)

except gp.GurobiError as e:
    print('Error code ' + str(e.errno) + ": " + str(e))

except AttributeError:
    print('Encountered an attribute error')
