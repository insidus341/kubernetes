<?php

if (getenv('DEMO_ENV')) {
    $custom_var = getenv('DEMO_ENV');
} else {
    $custom_var = "";
}

?>

<!DOCTYPE html>
<!-- Contrbuted by GS -->
<html>
<head>
    <style>
    #wrapper {
        margin: 0 auto;
        width: 1200px;
        margin-top: 300px;
        text-align: center;
    }

    h1 {
        color: red;
        font-size: 48px;
    }

    </style>
</head>
<body>
    <div id="wrapper">
        <h1><?php echo gethostname(); ?></h1>
        <h3><?php echo $custom_var; ?></h3>   
    </div>

</body>
</html>
