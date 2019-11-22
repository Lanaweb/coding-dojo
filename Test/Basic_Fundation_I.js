
function printto1to255(){
	var arr = [];
	for (var i=1; i< 256; i++){
		arr.push(i);
	}
	return arr;
}


function sumeven1to1000() {
	var evensum = 0;
	for (var i=2; i<1001; i=i+2){
		evensum += i;
	}
	return evensum;
}

function sumodds1to5000(){
	var oddsum = 0;
	for (var i=1; i<5001; i=i+2){
		oddsum += i;
	}
	return oddsum;
}

function returnsumofarray(arr){
	var arrsum =0;
	for(var i=0; i<arr.length; i++){
		arrsum += arr[i];
	}
	return arrsum;
}


function findmax(arr){
	if (arr.length <1){
		return false;
	}
	var max = arr[0];
	for (var i=1; i<arr.length; i++){
		if(max < arr[i]){
			max = arr[i];
		}
	}
	return max;
}

function findaverage(arr){
	var arraverage = 0;
	for (var i =0; i<arr.length; i++){
		arraverage += arr[i];
	}
	return arraverage/arr.length;
}

function returnooddarray1to50(){
	var arr=[];
	for(var i=1; i<51; i =i+2){
		arr.push(i);
	}
	return arr;
}

function returngreaterthanY(arr, Y){
	var num = 0;
	for (var i=0; i<arr.length;i++){
		if(arr[i] > Y){
			num +=1;
		}
	}
	return num;
}


function squarearry(arr){
	for (var i=0; i<arr.length; i++){
		arr[i] = arr[i] * arr[i];
	}
	return arr;
}

function negativesreplace(arr){
	for(var i=0; i<arr.length; i++){
		if(arr[i] < 0){
			arr[i] = 0;
		}
	}
	return arr;
}

function returnmaxminavg(arr){
	var min =0;
	var max =0;
	var ave = 0;
	var newarr = [];
	for(var i=0; i<arr.length; i++){
		if (min > arr[i]){
			min = arr[i];
		}
		if (max < arr[i]){
			max = arr[i];
		}
		ave += arr[i];
	}
	newarr = [max, min, ave/arr.length];

	return newarr;
}


function swapfistlast(arr){
	var temp = 0;
	temp = arr[0];
	arr[0] = arr[arr.length-1] ;
	arr[arr.length-1] = temp;
	return arr;
}

function numbertostring(arr){
	for (var i=0; i<arr.length; i++){
		if(arr[i] <0){
			arr[i] = "Dojo";
		}
	}
	return arr;
}
































