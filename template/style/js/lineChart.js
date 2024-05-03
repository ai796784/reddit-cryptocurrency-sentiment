function updateLineChart() {
    // Check if a chart already exists
    var existingChart = Chart.getChart('lineChartCanvas');

    // If a chart exists, destroy it
    if (existingChart) {
      existingChart.destroy();
    }
    // Replace with your data and chart logic
    var ctx = document.getElementById('lineChartCanvas').getContext('2d');
    var lineChart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
        datasets: [{
          label: 'Line Chart',
          data: [65, 59, 80, 81, 56, 55, 40],
          borderColor: 'rgb(75, 192, 192)',
          fill: false
        }]
      },
      options: {
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
}