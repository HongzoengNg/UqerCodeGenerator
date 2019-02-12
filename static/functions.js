function generate(){
    var start_date = document.getElementById("start").value;
    var end_date = document.getElementById("end").value;
    var params = {};
    for(i = 1; i <= 10; i++){
        var key = document.getElementById("s" + String(i)).value;
        var val = document.getElementById("w" + String(i)).value;
        var e = document.getElementById("e" + String(i));
        var exchange = e.options[e.selectedIndex].value;
        if(key != "" && val != "" && exchange != ""){
            params[key + exchange] = val;
        }
    }
    var strategy = document.querySelector('input[name="strategy"]:checked').value;
    params["start"] = start_date;
    params["end"] = end_date;
    params["strategy"] = strategy;
    if (strategy == "ma"){
        var sma = document.getElementById("sma").value;
        var lma = document.getElementById("lma").value;
        params["strategy"] += "_" + sma + "_" + lma;
    }
    else if (strategy == "macd"){
        var sema = document.getElementById("sema").value;
        var lema = document.getElementById("lema").value;
        var macd = document.getElementById("macdline").value;
        params["strategy"] += "_" + sema + "_" + lema + "_" + macd;
    }
    else if (strategy == "stoch"){
        var fastk = document.getElementById("fastk").value;
        var slowk = document.getElementById("slowk").value;
        var slowd = document.getElementById("slowd").value;
        params["strategy"] += "_" + fastk + "_" + slowk + "_" + slowd;
    }
    var params_json = JSON.stringify(params);
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function(){
        if (xhttp.readyState == 4 && xhttp.status == 200) {
            var response = JSON.parse(xhttp.responseText);
            // console.log(response);
            document.getElementById("code").innerHTML = response["code"];
        }
    };
    xhttp.open("POST", "/generate", true);
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.send(params_json);
};