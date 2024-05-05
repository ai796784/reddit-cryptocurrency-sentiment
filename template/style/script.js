document.getElementById("redditForm").addEventListener("submit", function (event) {
  event.preventDefault();
  const subreddit = document.getElementById("subreddit").value;
  fetchDataAndUpdateCharts(subreddit);
});


document.getElementById("redditForm").addEventListener("reset", function (event) {
  event.preventDefault();
  clearcontent();
});


function fetchDataAndUpdateCharts(subreddit) {
  updatePieChart(pieData);
  updateLineChart(lineData);
  updateBarChart(barData);
  updateDonutChart(donutData);
  // updateHeatMap();
  for (const post of radarData) {
    updateRadarChart(post);
  }
  updateNetworkGraph();
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
  clearLineChart();
  clearBarChart();
  clearDonutChart();
  clearRadarChart();
  clearNetChart();
}
