// function sigma(num){
// 	var sum=0;
// 	for(var i=1; i<num+1; i++){
// 		sum += i;
// 	}
// 	return sum;
// }

// function factorial(num){
// 	if(num <= 0){
// 		return 0;
// 	}
// 	var fac = 1;
// 	for (var i=1; i<num+1; i++){
// 		fac = fac * i;
// 	}
// 	return fac;
// }

// function fibonacci(num){
// 	var a=1, b=0, temp;
// 	while(num >0){
// 		temp =a;
// 		a = a+b;
// 		b =temp;
// 		num --;
// 	}
// 	return b;
// }




// function secondtolast(arr){
// 	if(arr.length ==1){
// 		return null;
// 	} else {
// 		return arr[arr.length-2];
// 	}
// }

// function nthtolast(arr, num){
// 	if(arr.length < num){
// 		return null;
// 	} else {
// 		return arr[arr.length - num];
// 	}
// }

// function returnSecondLargest(arr){
// 	if(arr.length <2){
// 		return null;
// 	}
// 	for (var i=0; i<arr.length-1; i++){
// 		for ( var j=0; j<arr.length-1-i; j++){
// 			if(arr[j] > arr[j+1]){
// 				temp = arr[j];
// 				arr[j] = arr[j+1];
// 				arr[j+1] = temp;
// 			}
// 		}
// 	}
// 	return arr[arr.length-2];
// }


// function doubletrouble(arr){
// 	for(var i=0; i<arr.length; i+=2){
// 		arr.length ++;
// 		temp = arr[i];
// 		for (j=arr.length-2; j>i; j--){
// 			arr[j+1] = arr[j];
// 		}
// 		arr[i+1] = temp;
// 	}
// 	return arr;
// }

// function fibonaccirec(n){
// 	if(n==0 || n==1){
// 		return n;
// 	}
// 	return fibonaccirec(n-1) + fibonaccirec(n-2);
// }































