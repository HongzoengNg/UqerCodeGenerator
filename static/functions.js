function generate(){
    var start_date = document.getElementById("start").value;
    var end_date = document.getElementById("end").value;
    var params = {};
    for(i = 1; i <= 10; i++){
        var key = document.getElementById("s" + String(i)).value;
        var val = document.getElementById("w" + String(i)).value;
        params[key] = val;
    }
    var strategy = document.querySelector('input[name="strategy"]:checked').value;
    params["start"] = start_date;
    params["end"] = end_date;
    params["strategy"] = strategy;
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