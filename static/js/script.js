document.getElementById("redditForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent default form submission behavior
  
    var subredditName = document.getElementById("subreddit").value;
  
    // Make AJAX request to fetch data from PHP script
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "../../php/search.php", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.onerror = function() {
      console.error("An error occurred while making the AJAX request.");
    };
  
    xhr.onreadystatechange = function() {
      if (xhr.readyState === XMLHttpRequest.DONE) {
        if (xhr.status === 200) {
          // Parse the JSON response
          console.log(xhr.responseText)
          
          var responseData = JSON.parse(xhr.responseText);
  
          // Call functions to create charts with the received data
          // createLineChart(responseData.linePlotData);
          //createBarChart(responseData.barPlotData);
          // createPieChart(responseData.piePlotData);
          //createHeatMap(responseData.heatPlotData);
          // createDonutChart(responseData.piePloData);
          // createRadarChart(responseData.radarPlotData);
          //createNetworkGraph(responseData.networkPlotData);
        } else {
          console.error("AJAX request failed");
        }
      }
    };
  
    // Encode data to be sent in the request body
    var params = "subredditName=" + encodeURIComponent(subredditName);
    xhr.send(params);
  });
  
