#np575
<?php

	# Open database connection
	$db = new mysqli("127.0.0.1", "root", "", "stockinfo");
	$db->set_charset('utf8');
	if ($db->connect_errno) {
		header($_SERVER['SERVER_PROTOCOL'] . ' 500 Internal Server Error');
		exit();
	}
	# Read stocks from database
	$stocks = [];
	$query = "SELECT name,volume,price,change,perc_change FROM `2020-17-24`";
	if ($stmt = $db->prepare($query)) {
		$stmt->execute();
		$result = $stmt->get_result();
		$stmt->free_result();
		$stmt->close();
		while ($row = $result->fetch_array(MYSQLI_ASSOC)) {
			$stocks[] = [
				"name"     => $row['name'],
				"volume"    => $row['volume'],
				"price"     => $row['price'],
				"change"      => $row['change'],
				"perc_change" => $row['perc_change']
			];
		}
		# print_r($stocks);		
	}
?>

<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>Stocks</title>
		<style>
			body, h1, h2, h3, h4, h5, h6, ul {
				margin: 0;
				padding: 0;
			}									
			th { text-align: left }
			th,td { min-width: 100px; padding-left: 10px }
			th:first-child, td:first-child { padding-left: 0; text-align: center }
			thead,tr { height: 30px }
			tr:nth-child(even) { background: rgba(0, 0, 0, .05) }
						
		</style>
	</head>
	<body>
		<table>
			<thead>
				<tr>
					<th>Name</th>
					<th>Volume</th>
					<th>Price</th>
					<th>Change</th>
					<th>% Change</th>
				</tr>
			 </thead>
			<?php			
			foreach ($stocks as $stock) {
				echo "<tr>" .
					 "<td>" . $stock['name'] . "</td>" .
					 "<td>" . $stock['volume'] . "</td>" .
					 "<td>" . $stock['price'] . "</td>" .
					 "<td>" . $stock['change'] . "</td>" .
					 "<td>" . $stock['perc_change'] . "</td>" .
					"</tr>";
			}			
			?>
		</table>
	</body>
</html>
