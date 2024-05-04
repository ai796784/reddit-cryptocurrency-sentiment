// Sample data for testing Radar Chart
var radarData = [];

// Generate 100 random posts with emotion scores
for (let i = 0; i < 100; i++) {
  const post = {
    // id: i + 1,
    joy: Math.random(),
    sadness: Math.random(),
    anger: Math.random(),
    optimism: Math.random()
  };
  radarData.push(post);
}

// let radarChart; // Declare a global variable to store the chart instance

function updateRadarChart(data) {
  console.log("Received data:", data); // Log the received data to the console
  // Check if a chart already exists
  var existingChart = Chart.getChart('radarChartCanvas');

  // If a chart exists, destroy it
  if (existingChart) {
    existingChart.destroy();
  }

  var ctx = document.getElementById('radarChartCanvas').getContext('2d');
  var radarChart = new Chart(ctx, {
    type: 'radar',
    data: {
      labels: ['Joy', 'Sadness', 'Anger', 'Optimism'],
      datasets: [
        {
          label: 'Emotion Scores',
          data: [data.joy, data.sadness, data.anger, data.optimism],
          backgroundColor: 'rgba(255, 99, 132, 0.2)',
          borderColor: 'rgba(255, 99, 132, 1)',
          borderWidth: 1
        }
      ]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
          max: 1
        }
      },
      responsive: false,
      maintainAspectRatio: false
    }
  });
}
  // Test the updateRadarChart function with the mock data
  // for (const post of radarData) {
  //   updateRadarChart(post);
  // }

function clearRadarChart() {

  const canvas = document.getElementById('radarChartCanvas');
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