#include 
#include 
#define PI 3.1415926

int count = 0; //calculate times of funC
double funCMemo[128]; //memo for funC, funCMemo[k] is funC[k] if funCMemoFlag is set
int funCMemoFlag[128]; //memoFlag, 1 is set, 0 is unset

/**
*@brief calculate Ck
*/
double funC(int k){
	//printf("funC(%d)\n", k);
	if(k != 0){
		double sum = 0.0;
		int i;
		//at first, look up, success
		if(funCMemoFlag[k] == 1){
			return funCMemo[k];
		}
		//else
		++count;
		for(i = 0; i < k; ++i){
			sum += ((funC(i) * funC(k - 1 - i)) / ((i + 1) * (2 * i + 1)));
		}
		//record to memo
		funCMemoFlag[k] = 1;
		funCMemo[k]=sum;
		return sum;
	}
	else{
	return 1.0;
	}
}

/**
*@brief calculate eK
*/
double funE(int n, int k){
	double sum = 0.0;
	int i;
	for(i = 0; i < k; ++i){
		sum += (funC(i) * (pow((pow(PI, 0.5) * n / 2), (2 * i + 1)))/ (2 * i + 1));
	}
	return sum;
}

int main(){

double erf = 0;
int i;
int n,k;
//init funCMemo and funCMemoFlag
for(i = 0; i < 128; ++i){
    funCMemo[i]=0.0;
    funCMemoFlag[i]=0;
}

printf("input n:\n");
scanf("%d", &n);
printf("input k(<128):\n");
scanf("%d", &k);

//erf = funC(k);
erf = funE(n, k);
printf("erf=%f\n", erf);
printf("count=%d\n", count);
return 0;
}
