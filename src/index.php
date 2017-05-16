<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>MARDER OSC MONITOR</title>
<link href="styles/style.css" rel="stylesheet" type="text/css" />


<?php $etiqueta = $_GET['etiqueta']; 
	$json = $etiqueta.'.json';
?>

<script type="text/javascript" src="https://www.google.com/jsapi"></script>
	<script type="text/javascript" src="http://code.jquery.com/jquery-1.8.2.min.js"></script>
	<script type="text/javascript">

	function update() {
		$.ajax({url:"labellist.json",
			success: function (e) {
				$("#chart_div div").remove(); 
				
				for(label in e) {
					
					var qs=e[label][1];
					var n_params= e[label][0];
					var div= $("<div>")
					var a = $("<a>");
					a.appendTo(div);
					a.text(label + " (" + n_params + ")");
					a.attr("href", "graph.php?etiqueta=" + qs);
					div.appendTo("#chart_div")
				}
			}
		}, "json") 
	}	
	
	setInterval("update()", 300);	
</script>
	

</head>

<body>

   <div id="slidingDiv">
       	<div id="chart_div" style="margin-left:100px;margin-top:30px">
	</div>
    </div>

</div>

</body>
</html>


