let radarChart; // Declare a global variable to store the chart instance

function createRadarChart(data) {
  var radarData = {
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
  };
  var radarOptions = {
    scales: {
        y: {
            beginAtZero: true,
            max: 1
        }
    },
    responsive: true,
    maintainAspectRatio: false
  };

  var radarCtx = document.getElementById('radarChartCanvas').getContext('2d');

  // Destroy the existing chart instance if it exists
  if (radarChart) {
    radarChart.destroy();
  }

  // Create a new chart instance
  radarChart = new Chart(radarCtx, {
    type: 'radar',
    data: radarData,
    options: radarOptions
  });
}