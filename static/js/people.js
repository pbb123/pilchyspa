
var flag=true

function adw()
{
	if (flag)
	{
		var div=$("#adw")
		div.css("display","block")
		var div2=$("#base")
		div2.css("display","none")
		$("button").html("Ustawienia podstawowe")
		flag=false
	}
	else
	{
		var div=$("#base")
		div.css("display","block")
		var div2=$("#adw")
		div2.css("display","none")
		$("button").html("Ustawienia zaawansowane")
		flag=true
		
	}
}