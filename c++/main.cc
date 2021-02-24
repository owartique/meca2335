/*
*	LMECA2335 - Biorobotics
*	RHex - Gr4
*/

#include "param.h"


int main(){

	// Open file and save it into an array
	ifstream myReadFile;
	myReadFile.open("../log/output.txt");	
	double output;
	int i = 0;
	if(myReadFile.is_open()){
		while(!myReadFile.eof()){
			myReadFile >> output;
			v_normalized[i] = output;
			i++;
		}
	}

	myReadFile.close();

	return 0;

}