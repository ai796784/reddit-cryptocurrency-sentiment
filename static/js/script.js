document.getElementById("redditForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent default form submission behavior
  
    var subredditName = document.getElementById("subreddit").value;
  
    // Make AJAX request to fetch data from PHP script
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "search.php", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.onerror = function() {
      console.error("An error occurred while making the AJAX request.");
    };
  
    xhr.onreadystatechange = function() {
      if (xhr.readyState === XMLHttpRequest.DONE) {
        if (xhr.status === 200) {
          // Parse the JSON response
          var responseData = JSON.parse(xhr.responseText);
  
          // Call functions to create charts with the received data
          createLineChart(responseData);
          createBarChart(responseData);
          //createPieChart(responseData);
          //createAreaChart(responseData);
          //createNetworkGraph(responseData);
        } else {
          console.error("AJAX request failed");
        }
      }
    };
  
    // Encode data to be sent in the request body
    var params = "subredditName=" + encodeURIComponent(subredditName);
    xhr.send(params);
  });
  
