function createAreaChart() {
  // Create an empty dataset with no data
  var emptyData = [];

  var ctx = document.getElementById('areaChartCanvas').getContext('2d');
  var areaChart = new Chart(ctx, {
      type: 'line',
      data: {
          labels: [], // No labels to hide the x-axis
          datasets: [{
              label: 'Area Chart',
              data: emptyData, // Empty data array
              backgroundColor: 'rgba(0, 0, 0, 0)', // Transparent color to hide the area
              borderColor: 'rgba(0, 0, 0, 0)', // Transparent color to hide the borders
              borderWidth: 0 // No border
          }]
      },
      options: {
          scales: {
              x: {
                  display: true // Show x-axis
              },
              y: {
                  display: true // Show y-axis
              }
          }
      }
  });
}