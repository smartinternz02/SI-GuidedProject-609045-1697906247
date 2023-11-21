$(document).ready(function() {
    $("#dataForm").submit(function(e) {
        e.preventDefault();

        // Gather input data
        const data = {
            temperature: parseFloat($("#temperature").val()),
            humidity: parseFloat($("#humidity").val()),
            tvoc: parseFloat($("#tvoc").val()),
            eco2: parseFloat($("#eco2").val()),
            rawH2: parseFloat($("#rawH2").val()),
            raw_ethanol: parseFloat($("#raw_ethanol").val()),
            pressure: parseFloat($("#pressure").val()),
            nc_05: parseFloat($("#nc_05").val())
        };

        // Send data to your API using the Fetch API
        fetch('http://localhost:8080/model', {
            method: 'POST',
            body: JSON.stringify(data),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
            if (response.status === 200) {
                return response.json(); // Assuming the response is in JSON format
            } else if (response.status === 422) {
                throw Error('422 Error: Invalid data format');
            } else if (response.status === 500) {
                throw new Error('500 Error: Internal Server Error');
            } else {
                throw new Error('Server returned status ' + response.status);
            }
        })
        .then(data => {
            // Log the response for inspection
            console.log(data);

            // Display result with warning symbol and color
            if (data.ans === 1) {
                $("#result").html("API Response: <span class='smoke-detected-symbol'>⚠️</span> Smoke is detected <span class='smoke-detected-symbol'>⚠️</span>").addClass("smoke-detected");
            } else {
                $("#result").html("API Response: Smoke is not detected").removeClass("smoke-detected");
            }
        })
        .catch(error => {
            $("#result").html("Error: " + error.message).removeClass("smoke-detected");
        });
    });
});
