/*
*	LMECA2335 - Biorobotics
*	RHex - Gr4
*/

//#include "param.h"
#include <iostream>
#include <fstream>

using namespace std;



int main(){

	ifstream myReadFile;
	myReadFile.open("../log/output.txt");	
	char output[100];
	if(myReadFile.is_open()){
		while(!myReadFile.eof()){
			myReadFile >> output;
			cout << output << endl;
		}
	}

	myReadFile.close();

	return 0;

}