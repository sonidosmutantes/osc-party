<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>OSC MONITOR</title>
<link href="styles/style.css" rel="stylesheet" type="text/css" />

<?php $etiqueta = $_GET['etiqueta'];
	$json = $etiqueta.'.json';
?>

<script type="text/javascript" src="https://www.google.com/jsapi"></script>
	<script type="text/javascript" src="http://code.jquery.com/jquery-1.8.2.min.js"></script>
	<script type="text/javascript">

		google.load("visualization", "1", {packages:["corechart"]});
		google.setOnLoadCallback(drawChart);

		function drawChart() {
			document.getElementById("#summary").innerHTML = "";
			var jsonData = $.ajax({
				type: "GET",
				url: "<?php echo $json?>",
				// url: "inharmonicity.json",
				dataType: "json",
				async: false
				}).responseText;
			// Create our data table out of JSON data loaded from server.

			// document.getElementById("#summary").innerHTML = jsonData;

//			var jsonDataOld = $.extend(jsonDataOld,jsonData);
			var data = new google.visualization.DataTable(jsonData);
			var options = {
				width: 700, height: 300,
				title: 'OSC Data'
			};
			var chart = new google.visualization.LineChart(document.getElementById('#diagram'));
			chart.draw(data, options);
//			chart.setRefreshInterval(1);
		}

	var intervalID = setInterval(drawChart, 500);

	</script>


</head>

<body>

   <div id="slidingDiv">
       	<div id="chart_div">
	</div>
    </div>

	<div id="#diagram">
	Diagram
	</div>

	<div id="#summary">
	</div>
	
	<a href="index.php">Back</a>
</div>

</body>
</html>
