"""This script calculates the Y-bus matrix, using classes imported from bus.py"""

import numpy as np
from bus import Bus, Line, YbusMatrix

bus1 = Bus(1)
bus2 = Bus(2)
bus3 = Bus(3)
#bus4 = Bus(4)

line12 = Line(impedance=(1/(1j*0.7)), fullLineChargingAdmittance=1j*0.2, connectedToBusID=(1,2))
line13 = Line(impedance=(1/(1j*0.3)), fullLineChargingAdmittance=1j*0.2, connectedToBusID=(1,3))
line23 = Line(impedance=(1/(1j*0.5)), fullLineChargingAdmittance=1j*0.2, connectedToBusID=(2,3))
#line34 = Line(impedance=0.01272 + 1j*0.06360, fullLineChargingAdmittance=1j*0.1275, connectedToBusID=(3,4))

bus1.connectedLines = [line12, line13]
bus2.connectedLines = [line12, line23]
bus3.connectedLines = [line13, line23]
#bus4.connectedLines = [line24, line34]

yBus = YbusMatrix([bus1, bus2, bus3])
yBus.printMatrix()
print("---------------------------------------------------------------")
yBus.printZbus()