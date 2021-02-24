#pragma once

#include <iostream>
#include <fstream>

using namespace std;

#define NBR_POINTS 3000 // number of points in file

#define OMEGA   0    // pulse frequency of the leg [rad/s]
#define RADIUS 	0	 // radius of the leg
#define MASS  	0	 // mass of the system [kg]
#define GRAVITY 9.81 // gravity acceleration [m/s²]
#define HEIGHT	0	 // penetration depth of the leg [m]
#define KPHI 	0	 // penetration resistance constant

double v_normalized [NBR_POINTS]; // array containing velocity