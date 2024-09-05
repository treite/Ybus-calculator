"""
This script implements the classes that are used for modelling a power system in order to calculate an Y-bus matrix.
"""

import numpy as np

class Bus:
    def __init__(self, busID, connectedLines = [], connectedGenerators = [], connectedLoads = []):
        self.busID = busID
        self.connectedLines = connectedLines
        self.connectedGenerators = connectedGenerators
        self.connectedLoads = connectedLoads


class Line:
    def __init__(self, impedance = 0, fullLineChargingAdmittance = 0, connectedToBusID = []):
        self.impedance = impedance
        self.lineAdmittance = 1/impedance
        self.fullLineChargingAdmittance = fullLineChargingAdmittance
        self.connectedTo = connectedToBusID

    def getAdmittance(self):
        return self.lineAdmittance + self.fullLineChargingAdmittance/2
    

class YbusMatrix:
    def __init__(self, buses):
        self.buses = buses
        self.numberOfBuses = len(buses)
        self.matrix = self.createMatrix()
        self.zBus = np.linalg.inv(self.matrix)

    def createMatrix(self):
        finishedMatrix = np.array([], dtype=np.complex128).reshape(0, self.numberOfBuses)

        for row in range(self.numberOfBuses):
            matrixRow = np.zeros(self.numberOfBuses, dtype=np.complex128)
            totalImpedance = 0
            for connectedLine in self.buses[row].connectedLines:
                totalImpedance += connectedLine.getAdmittance()

                for BusID in connectedLine.connectedTo:
                    if BusID != row + 1:
                        matrixRow[BusID-1] = -connectedLine.lineAdmittance
            matrixRow[row] = totalImpedance

            finishedMatrix = np.append(finishedMatrix, [matrixRow], axis=0)

        return finishedMatrix
    
    def printMatrix(self):
        for row in self.matrix:
            formatted_row = ["{:.2f}{:+.2f}j".format(c.real, c.imag) for c in row]
            print(" | ".join(formatted_row))

    def printZbus(self):
        for row in self.zBus:
            formatted_row = ["{:.2f}{:+.2f}j".format(c.real, c.imag) for c in row]
            print(" | ".join(formatted_row))

