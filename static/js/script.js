document.getElementById("redditForm").addEventListener("submit", function(event) {
    event.preventDefault();
    const subreddit = document.getElementById("subreddit").value;
    fetchDataAndUpdateCharts(subreddit);
  });
  
  function fetchDataAndUpdateCharts(subreddit) {
    // Your code to fetch data from Reddit API based on the selected subreddit
    // After fetching data, update the charts accordingly
    // Example:
    updateLineChart();
    updateBarChart();
    updatePieChart();
    updateAreaChart();
  }
  