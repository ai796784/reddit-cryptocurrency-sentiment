//Note: Need to remove the barData and replace with the main data thing.

var barData = [];

for (var i = 1; i <= 500; i++) {
  barData.push({
    title: "Post " + i,
    num_comments: Math.floor(Math.random() * 100) + 1, // Random number of comments between 0 and 100
    interaction: Math.floor(Math.random() * 50) + 1// Random interaction value between 0 and 50
  });
}

function updateBarChart(data) {
  console.log("Received data:", data); // Log the received data to the console
  // Check if a chart already exists
  var existingChart = Chart.getChart('barChartCanvas');

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

  var ctx = document.getElementById('barChartCanvas').getContext('2d');
  var barChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [{
        label: 'Number of Comments',
        data: numComments,
        backgroundColor: 'blue'
      },
      {
        label: 'Interaction Value',
        data: interaction,
        backgroundColor: 'green'
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
}

// updateBarChart(barData);

function clearBarChart() {
  // var ctx = document.getElementById('barChartCanvas').getContext('2d');
  // ctx.clearRect(0, 0, canvas.width, canvas.height);
  const canvas = document.getElementById('barChartCanvas');
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