function updateLineChart() {
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
  
