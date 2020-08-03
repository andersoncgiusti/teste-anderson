window.onload = function(){
	var count = 0;
		document.getElementById("btn").onclick = function(){
		count ++;
		document.getElementById("show").innerHTML = count;
		}
}