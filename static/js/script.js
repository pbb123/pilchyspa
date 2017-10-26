//login style opacity
function onfocus2()
{
	//alert("FOCUS")
	$('#login').css('opacity','1')
}
function lost(){
	$('#login').css('opacity','0.5')
}




//slider
var numer=Math.round(Math.random()*10);
function zmień()
{
	var plik=url+"/image"+numer+".jpg";
	//console.log(url);
	$('body').css('background-image','url('+plik+')');
	numer++;if (numer>10){numer=0};
	setTimeout(zmień,5000);
	
	
}
//sound
var sounds= new Array(2)
sounds[0]=url2+"/Sound1.m4a"
sounds[1]=url2+"/Sound2.mp3"
sounds[2]=url2+"/Sound3.mp3"
var snd=null
var soundnr=0
var play=true;
function offon()
{
	if (play==true){
		var content="<i class=\"icon-volume-off\"></i>";
		play=false;
		snd.pause();
	}
	else{
		var content="<i class=\"icon-volume-low\"></i>";
		play=true;
		snd.play();
	}
	//alert("offon")
	$("#sound").html(content);
	
}
function playsound()
{
	snd =new Audio(sounds[soundnr]);
	snd.autoplay=true;
	snd.onended=function()
	{
		soundnr++;if (soundnr>sounds.length){soundnr=0} ;
		playsound();
	}
	
}



$(document).ready(function(){playsound();zmień()})
