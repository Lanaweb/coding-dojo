// function a(x){
//    z = [];
//    z.push(x);
//    z.pop();
//    z.push(x);
//    z.push(x);
//    return z;
// }

// y = a(2);
// y.push(5);
// console.log(y);



// function a(x){
//    if(x[0] < x[1]) {
//       return true;
//    }
//    else {
//       return false;
//    }
// }
// b = a([2,3,4,5])
// console.log(b);


// function a(x){
//    if(x[0] > x[1]) {
//     return x[1];
//    }
//    return 20;
// }
// b = a([9,7])
// console.log(b);




// function printAverage(x){
// 	sum =0;
// 	for (var i =0; i< x.length; i++){
// 		sum = sum + x[i];
// 	}
// 	return sum/x.length
// }


// function returnOddArray(){
// 	z = [];
// 	for (var i=1; i< 256; i +=2 ){
// 		z.push(i)
// 	}
// 	return z;
// }

// function squareValue(x){
//    for (var i=0; i< x.length; i++){
//    	x[i] = x[i] * x[i];
//    }
//    return x;resetNegatives
// }

// function resetNegatives(arr){
// 	for (var i=0; i<arr.length; i++){
// 		if (arr[i] < 0){
// 			arr[i] = 0;
// 		}
// 	}
// 	return arr;
// }


// function moveForward(arr){
// 	for (var i=0; i< arr.length-1; i++){
// 		arr[i] = arr[i+1];
// 	}
// 	arr[arr.length-1] = 0;
// 	return arr;
// }

// function returnReversed(arr){
// 	len = arr.length
// 	for (var i=0; i<len/2; i++){
// 		temp = arr[i];
// 		arr[i] = arr[len-1-i];
// 		arr[len-1-i] = temp;
// 	}
// 	return arr;
// }


// Can you do it by not creating a new array?

// function repeatTwice(arr){
// 	z = [];
// 	len = arr.length;
// 	for (var i=0; i< len; i++){
// 		z.push(arr[i])
// 		z.push(arr[i])
// 	}
// 	return z;
// }

// function PrintNumberofArraryGreater(arr,Y){
// 	great_num = 0;
// 	for (var i=0; i<arr.length; i++){
// 		if(arr[i] >Y){
// 			great_num ++;
// 		}
// 	}
// 	return great_num;
// }


// function PrintMaxMinAverage(arr){
// 	max=arr[0];
// 	min=arr[0];
// 	ave = arr[0];
// 	for (var i =1; i<arr.length; i++){
// 		if (max < arr[i]){
// 			max = arr[i];
// 		}
// 		if (min > arr[i]){
// 			min = arr[i];
// 		}

// 		ave += arr[i];
// 	}
// 	console.log(max);
// 	console.log(min);
// 	console.log(ave/arr.length);
// }

// function replaceNegatives(arr){
// 	for (var i=0; i<arr.length; i++){
// 		if(arr[i] < 0){
// 			arr[i] = 'Dojo';
// 		}
// 	}
// 	return arr;
// }

function removeVals(arr, s, e){
	a = e - s;
	count = 0;
	while(count<a+1){
		arr.splice(s,1);
		count ++;
	}
	return arr

}































