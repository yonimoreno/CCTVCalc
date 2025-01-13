# Camera Parameter Calculator

## Overview
The Camera Parameter Calculator is a Python program designed to compute essential camera parameters, including focal distance, vertical and horizontal aperture angles, and the necessary tilt of the camera with respect to the vertical. This tool is particularly useful for photographers, videographers, and anyone involved in camera setup for various scenes.

## Author
- **Name:** Yonathan Moreno
- **Email:** yonimgut@gmail.com

## License
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

## Features
- Calculates focal distance based on user inputs.
- Computes vertical and horizontal aperture angles.
- Determines the necessary tilt of the camera.
- Handles decimal inputs with both comma and point formats.

## Requirements
- Python 2.x (the program uses `raw_input()` which is specific to Python 2)
- Basic mathematical libraries (included in Python standard library)

## Usage
1. **Run the Program:** Execute the script in a Python environment.
2. **Input Parameters:**
   - **Ceiling Height:** Enter the height of the ceiling in the scene.
   - **Scene Width:** Enter the width of the scene.
   - **Distance to Scene Center:** Enter the distance from the camera axis to the center of the scene.
   - **Lens Type:** Specify the type of lens to use (options: 1/2, 1/3, 1/4).
3. **View Results:** The program will output the calculated focal distance, aperture angles, and camera tilt.

## Example
Ceiling height: 3.0
Scene width: 5.0
Distance to scene center: 2.0
Type of lens to use: (1/2, 1/3, 1/4): 1/2
## Notes
- Ensure that the inputs are provided in the correct format. If using a decimal comma, the program will automatically convert it to a point.
- The program is designed for educational and practical use in photography and videography.

## Contact
For any questions or feedback, please reach out to the author at yonimgut@gmail.com. 

## Acknowledgments
This program is inspired by the need for precise camera setup in various photographic and videographic applications. Thank you for using the Camera Parameter Calculator!
