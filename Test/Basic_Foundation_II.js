
function makeItBig(arr){
	for(var i=0; i<arr.length; i++){
		if(arr[i] >0){
			arr[i] = "big";
		}
	}
	return arr;
}

function printlowreturnhigh(arr){
	var high =arr[0];
	var low =arr[0];
	for(var i=1; i<arr.length; i++){
		if(arr[i]>high){
			high = arr[i];
		} else if (arr[i] < low){
			low = arr[i];
		}
	}
	console.log(low);
	return high;
}



function printonereturnanother(arr){
	var firstodd = arr[0];
	for(var i=1; i<arr.length; i++){
		console.log(arr[i]);
		if(firstodd%2 == 0 && arr[i] %2 != 0){
			firstodd = arr[i];
		}
	}
	if (firstodd%2 == 0){
		return false;
	} else{
		return firstodd;
	}
}

function doublevision(arr) {
	var newarr = [];
	for (var i=0; i<arr.length; i++){
		newarr.push(arr[i]*arr[i]);
	}
	return newarr;
}

function countpositive(arr){
	var poscount =0;
	for (var i=0; i<arr.length; i++){
		if(arr[i]>0){
			poscount++;
		}
	}
	arr[arr.length-1] = poscount;
	return arr;
}

function evensandodds(arr){
	for(var i=0; i<arr.length-2; i++){
		if(arr[i]%2 ==0 & arr[i+1]%2 ==0 & arr[i+2]%2 ==0){
			console.log("Even more so!");
		} else if(arr[i]%2 !=0 & arr[i+1]%2 !=0 & arr[1+2]%2 !=0){
			console.log("That's odd!");
		}
	}
}

add 1 to every other element, specifically those whose index is odd (arr[1], arr[3], arr[5], etc)

function incrementtheseconds(arr){
	if (arr.length== 1){
		arr[0] ++;
	}

	for(var i=1; i< arr.length; i = i+2){
		arr[i] ++;
	}
	for (var i=0; i<arr.length; i++){
		console.log(arr[i]);
	}
	return arr;
}

function previouslength(arr){
	for(i =arr.length-1; i>0; i--){
		arr[i] = arr[i-1].length;
	}
	return arr;
}

function addseven(arr){
	for(var i=0; i<arr.length; i++){
		arr[i] += 7;
	}
	return arr;
}

function reversearray(arr){
	for(var i=0; i < arr.length/2; i++){
		temp =arr[i];
		arr[i] = arr[arr.length-1-i];
		arr[arr.length-1-i] = temp;
	}
	return arr;
}


function returnneg(arr){
	var newarr = [];
	for (var i=0; i<arr.length; i++){
		if(arr[i] >0){
			newarr.push(-1 * arr[i]);
		} else {
			newarr.push(arr[i]);
		}
	}
	return newarr;
}

function printhungry(arr){
	var huncount =0;
	for(var i=0; i<arr.length; i++){
		if (arr[i] == "food"){
			console.log("yummy");
			huncount ++;
		}
	}
	if (huncount < 1){
		console.log("I'm hungry");
	}
}


function swapTowardCenter(arr){
	for(var i=0; i<arr.length/2; i+=2){
		temp = arr[i];
		arr[i] = arr[arr.length-1-i];
		arr[arr.length-1-i] = temp;
	}
	return arr;
}


function scaleArray(arr,num){
	for (var i=0; i<arr.length; i++){
		arr[i] = arr[i]*num
	}
	return arr;
}






















