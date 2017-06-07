<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>JAM OSC MONITOR</title>
<link href="styles/style.css" rel="stylesheet" type="text/css" />

<?php 
	$etiqueta = $_GET['etiqueta']; 
	$json = $etiqueta.'.json';
?>

<script type="text/javascript" src="https://www.google.com/jsapi"></script>
<script type="text/javascript" src="http://code.jquery.com/jquery-1.8.2.min.js"></script>

<script type="text/javascript">
	function update() {
		$.ajax({
			type: "GET",
			url:"labellist.json",
			success: function (e) {
				//TODO: don't reload if result has HTML code 304 (not modified)
				document.getElementById("#summary").innerHTML = "";
				for(label in e) {
					var qs=e[label][1];
					var n_params= e[label][0];
					// var a = $("<a>");
					// a.text(label + " (" + n_params + ")");
					// a.attr("href", "graph.php?etiqueta=" + qs);
					var a = "<a href=\"graph.php?etiqueta=" + qs + "\">" + label + " (" + n_params + ")</a>";
					document.getElementById("#summary").innerHTML += a + "<hr/>"; 	
				}
			},
			error: function (e) {
                    //alert('Error Received: ' + e);
            }
		}, "json") 
	}	
	setInterval("update()", 600);	
</script>
</head>

<body>
	<div id="#chart_div" style="margin-left:100px;margin-top:30px">
	</div>

	OSC addresses<hr/>

	<div id="#summary">
		OSC Party
	</div>
</body>

</html>


