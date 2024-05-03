document.getElementById("redditForm").addEventListener("submit", function (event) {
  event.preventDefault();
  const subreddit = document.getElementById("subreddit").value;
  
  // // Make AJAX request to fetch data from PHP script
  // var xhr = new XMLHttpRequest();
  // xhr.open("POST", "../../php/search.php", true);
  // xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  // xhr.onerror = function() {
  //   console.error("An error occurred while making the AJAX request.");
  // };

  // xhr.onreadystatechange = function() {
  //   if (xhr.readyState === XMLHttpRequest.DONE) {
  //     if (xhr.status === 200) {
  //       // Parse the JSON response
  //       console.log(xhr.responseText)
        
  //       var responseData = JSON.parse(xhr.responseText);

  fetchDataAndUpdateCharts(subreddit);
  //fetchDataAndUpdateChart(responseData);

});


document.getElementById("redditForm").addEventListener("reset", function (event) {
  event.preventDefault();
  clearcontent();
});


function fetchDataAndUpdateCharts(subreddit) {
  // Your code to fetch data from Reddit API based on the selected subreddit
  // After fetching data, update the charts accordingly
  // clearcontent();
  updatePieChart();
  updateLineChart();
  updateBarChart(barData);
  updateDonutChart(donutData);
  updateNetworkGraph();



  // updatePieChart(responseText.piePlotData);
  // updateLineChart(responseText.linePlotData);
  // updateBarChart(responseText.barPlotData);
  // updateDonutChart(responseText.donutPlotData);
  // updateNetworkGraph(responseText.networkPlotData);
}


function clearcontent() {
  // Array of canvas IDs you want to clear
  // const canvasIds = ['pieChartCanvas', 'lineChartCanvas', 'barChartCanvas', 'areaChartCanvas','networkGraphCanvas'];

  // canvasIds.forEach(canvasId => {
  //   const canvas = document.getElementById(canvasId);
  //   const ctx = canvas.getContext('2d');
  //   ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
  // });
  clearPieChart();
  clearDonutChart();
  clearBarChart();
  clearLineChart();
  clearNetChart();
}
