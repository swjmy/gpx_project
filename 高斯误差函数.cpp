#include <stdio.h>
#include <math.h>
#define PI 3.1415926


float c_K(int k){
	if (k == 0){
		return (float)1;
	}
	else  {
		float num=0.0;
		for(int m=0;m<k;m++){
			num += ((c_K(m)*c_K(k-1-m))/((m+1)*(2*m+1)));}
		return num;
	}
}

double g_D(int n){
	double num=0.0;
	for(int k=0;k<n;k++){
		num += (c_K(k)*(pow(((PI/2)*n),(2*k+1)))/(2*k+1));
		return num;
	} 
}


int main(){
	printf("hello\n"); 
	float e =0.0;
	e=c_K(3);
	printf("c_K(3)=%f\n",e);
	e=(float)127/90;
	printf("127/90=%f\n",e);
	double erf_D=g_D(2);
	printf("erf_D(2)=%f\n",erf_D);
	return 0;
}
