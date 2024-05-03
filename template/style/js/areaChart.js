function updateAreaChart() {
    // Check if a chart already exists
    var existingChart = Chart.getChart('areaChartCanvas');

    // If a chart exists, destroy it
    if (existingChart) {
      existingChart.destroy();
    }
    // Replace with your data and chart logic
    var ctx = document.getElementById('areaChartCanvas').getContext('2d');
    var areaChart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
        datasets: [{
          label: 'Area Chart',
          data: [65, 59, 80, 81, 56, 55, 40],
          backgroundColor: 'rgba(75, 192, 192, 0.2)',
          borderColor: 'rgba(75, 192, 192, 1)',
          borderWidth: 1
        }]
      },
      options: {
        maintainAspectRatio: false
    }
    });
  }
  
  function clearAreaChart() {
    // var ctx = document.getElementById('areaChartCanvas').getContext('2d');
    // ctx.clearRect(0, 0, canvas.width, canvas.height);
    const canvas = document.getElementById('areaChartCanvas');
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
}