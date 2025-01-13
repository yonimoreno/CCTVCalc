#***********************************
#
#
# Program that calculates the focal distance, vertical/horizontal aperture angle, and
# the necessary tilt of the camera with respect to the vertical.
#
# Author: Yonathan Moreno
# email: yonathan.morenog at gmail.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# Function that checks if a number has a decimal comma, and if it does, converts it to
# a point.
def escomacheck(numero):
    escoma = numero.find(",")
    if escoma != -1:
        numero = numero[:escoma] + '' + numero[escoma + 1:]
        return numero

# Define program variables.
rad2deg = 180 / 3.1416
# Variable to convert from radians to degrees.

# Start of the program.
print(" ")
print("-")
print("Program that calculates the focal distance, vertical/horizontal aperture angle, and")
print("the necessary tilt of the camera with respect to the vertical.")
print("-")
print(" ")

# Input parameters from the user, converting from text to integer with decimals. If the user
# writes with a comma, it converts it to a point.
print("Ceiling height: ")
h = input()
h = escomacheck(h)
h = int(float(h))

print("Scene width: ")
H = input()
H = escomacheck(H)
H = int(float(H))

print("Distance from the camera axis to the center of the scene:")
d = input()
d = escomacheck(d)
d = int(float(d))

print("Type of lens to use: (1/2, 1/3, 1/4)")
lentepul = raw_input()
if lentepul == '1/2':
    lente = 3.6
elif lentepul == '1/3':
    lente = 4.8
elif lentepul == '1/4':
    lente = 6.4
else:
    print("Error, you must enter the type of lens in inches (1/2, 1/3, 1/4)")

# Calculations of D rounding to two decimal places and converting to text.
from math import sqrt
D = sqrt((h * h) + (d * d))
D = round(D, 2)
D2 = str(D)

# Calculations of f and standardized f rounding to two decimal places and converting to text.
f = lente * (D / H)
f = round(f, 2)
fr = round(f)
f = str(f)
fr = str(fr)

# Calculations of AH and AV rounding to two decimal places.
from math import atan
AH = atan((lente / 2) / 3)
AH = 2 * (AH * rad2deg)
AV = AH * 3 / 4
AH = round(AH, 2)
AH = str(AH)
AV = round(AV, 2)
AV2 = str(AV)

# Calculations of x, AF, and IV, rounding IV to two decimal places.
x = sqrt((h - 2) * (h - 2) + d * d)
calc = ((h - 2) / x)
from math import acos
AF = (acos(calc) * rad2deg)
IV = AF - (AV / 2)
