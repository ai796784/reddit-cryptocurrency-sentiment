// function createPieChart() {
//   // Create an empty dataset with no data
//   var emptyData = [];

//   var ctx = document.getElementById('pieChartCanvas').getContext('2d');
//   var pieChart = new Chart(ctx, {
//       type: 'pie',
//       data: {
//           labels: [''], // One empty label to keep the legend visible
//           datasets: [{
//               label: 'Pie Chart',
//               data: emptyData, // Empty data array
//               backgroundColor: ['rgba(0, 0, 0, 0)'], // Transparent color to hide the pie
//               borderColor: ['rgba(0, 0, 0, 0)'], // Transparent color to hide the borders
//               borderWidth: 0 // No border
//           }]
//       },
//       options: {
//           plugins: {
//               legend: {
//                   display: true // Show legend
//               }
//           }
//       }
//   });
// }

function createPieChart(data) {
    // Sentiment Pie Chart
    var sentimentData = {
        labels: ['Positive', 'Negative', 'Neutral'],
        datasets: [{
            data: [data.Positive, data.Negative, data.Neutral],
            backgroundColor: ['green', 'red', 'gray']
        }]
    };

    var sentimentCtx = document.getElementById('sentimentPieChartCanvas').getContext('2d');
    var sentimentPieChart = new Chart(sentimentCtx, {
        type: 'pie',
        data: sentimentData,
        options: {
            responsive: true,
            maintainAspectRatio: false
        }
    });

}
