//Note: Need to remove the lineData and replace with the main data thing.

// Sample data for testing Line Chart
var lineData = [];

// Generate sample data for 500 posts
for (var i = 1; i <= 100; i++) {
    lineData.push({
        title: "Post " + i,
        num_comments: Math.floor(Math.random() * 100), // Random number of comments (0 to 99)
        interaction: Math.floor(Math.random() * 100) // Random interaction value (0 to 99)
    });
}


function updateLineChart(data) {
  console.log("Received data:", data); // Log the received data to the console
  // Check if a chart already exists
  var existingChart = Chart.getChart('lineChartCanvas');

  // If a chart exists, destroy it
  if (existingChart) {
    existingChart.destroy();
  }
  var numComments = data.map(function (item) {
    return item.num_comments;
  });

  var interaction = data.map(function (item) {
    return item.interaction;
  });

  var labels = new Array(data.length).fill(''); // Empty array for labels
  console.log("numComments:", numComments); // Log numComments array to the console
  console.log("interaction:", interaction); // Log interaction array to the console
  var ctx = document.getElementById('lineChartCanvas').getContext('2d');
  var myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: labels,
      datasets: [{
        label: 'Number of Comments',
        data: numComments,
        borderColor: 'blue',
        borderWidth: 1
      },
      {
        label: 'Interaction Value',
        data: interaction,
        borderColor: 'green',
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false
    }
  });
}



function clearLineChart() {
  // var ctx = document.getElementById('lineChartCanvas').getContext('2d');
  // ctx.clearRect(0, 0, canvas.width, canvas.height);
  const canvas = document.getElementById('lineChartCanvas');
  const ctx = canvas.getContext('2d');
  ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
  // canvas.addEventListener("mouseover", function (event) {
  //   event.preventDefault();
  // });

  // canvas.addEventListener("mouseout", function (event) {
  //   event.preventDefault();
  // });

  // canvas.addEventListener("mousein", function (event) {
  //   event.preventDefault();
  // });
}