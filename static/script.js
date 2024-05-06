// Define plotPaths variable globally
var plotPaths = {};

document.getElementById("redditForm").addEventListener("submit", function (event) {
  event.preventDefault(); // Prevent default form submission behavior

  var subredditName = document.getElementById("subreddit").value;

  // Make AJAX request to fetch data from PHP script
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "../php/search.php", true);
  xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  xhr.onerror = function () {
    console.error("An error occurred while making the AJAX request.");
  };

  xhr.onreadystatechange = function () {
    if (xhr.readyState === XMLHttpRequest.DONE) {
      if (xhr.status === 200) {
        handleResponse(xhr.responseText);
      } else {
        console.error("AJAX request failed");
      }
    }
  };

  // Encode data to be sent in the request body
  var params = "subredditName=" + encodeURIComponent(subredditName);
  xhr.send(params);
});

function handleResponse(responseText) {
  // Parse the JSON response
  var responseData = JSON.parse(responseText);
  var newDirectory = "../reddit_data/plots/";

  // Update global plotPaths variable
  plotPaths = {
    "line": responseData.linePlotResponse,
    "pie": responseData.piePlotResponse,
    "donut": responseData.donutPlotResponse,
    "heat": responseData.heatPlotResponse,
    "radar": responseData.radarPlotResponse,
    "network": responseData.networkPlotResponse
  };

  // Update chart images on the webpage
  for (var plotType in plotPaths) {
    if (plotPaths.hasOwnProperty(plotType)) {
      updateChartImage(plotType, newDirectory + plotPaths[plotType]);
    }
  }
}

function updateChartImage(plotType, newPath) {
  var container = document.getElementById(plotType + "ChartCanvas");
  // Remove existing image elements
  while (container.firstChild) {
    container.removeChild(container.firstChild);
  }
  // Create a new image element
  var img = document.createElement('img');
  // Set the source of the image
  img.src = newPath;
  // Append the image to the container div
  container.appendChild(img);
}

document.getElementById("redditForm").addEventListener("reset", function (event) {
  // Clear chart images on form reset
  for (var plotType in plotPaths) {
    if (plotPaths.hasOwnProperty(plotType)) {
      clearChartImage(plotType);
      deleteImage(plotPaths[plotType]);
    }
  }
});

function clearChartImage(plotType) {
  var container = document.getElementById(plotType + "ChartCanvas");
  while (container.firstChild) {
    container.removeChild(container.firstChild);
  }
}

function deleteImage(imagePath) {
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "../php/delete_image.php", true);
  xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhr.onreadystatechange = function () {
    if (xhr.readyState == XMLHttpRequest.DONE) {
      if (xhr.status == 200) {
        console.log("Image deleted successfully");
      } else {
        console.error("Error deleting image:", xhr.statusText);
      }
    }
  };
  xhr.send("imagePath=" + imagePath);
}
