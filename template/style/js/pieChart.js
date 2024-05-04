//Note: Need to remove the pieData and replace with the main data thing.

function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

var pieData = {
    Positive: getRandomInt(100, 300), // Random number between 100 and 300
    Negative: getRandomInt(50, 200),  // Random number between 50 and 200
    Neutral: getRandomInt(50, 150)     // Random number between 50 and 150
};


function updatePieChart(data) {
  // Check if a chart already exists
  var existingChart = Chart.getChart('pieChartCanvas');

  // If a chart exists, destroy it
  if (existingChart) {
    existingChart.destroy();
  }
  var ctx = document.getElementById('pieChartCanvas').getContext('2d');
  var pieChart = new Chart(ctx, {

    type: 'pie',
    data: {
      labels: ['Positive', 'Negative', 'Neutral'],
      datasets: [{
        data: [data.Positive, data.Negative, data.Neutral],
        backgroundColor: [
          'rgba(255, 99, 132, 0.2)',
          'rgba(54, 162, 235, 0.2)',
          'rgba(255, 206, 86, 0.2)'
        ],
        borderColor: [
          'rgba(255, 99, 132, 1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)'
        ],
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false
    }
  });
}


function clearPieChart() {
  const canvas = document.getElementById('pieChartCanvas');
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