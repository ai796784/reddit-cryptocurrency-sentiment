function createSentimentPieChart(data) {
    console.log("Received data:", data);
  
    const sentimentData = {
      labels: ['Positive', 'Negative', 'Neutral'],
      datasets: [{
        data: [data.Positive, data.Negative, data.Neutral],
        backgroundColor: ['green', 'red', 'gray']
      }]
    };
  
    const sentimentCtx = document.getElementById('pieChartCanvas').getContext('2d');
    const sentimentPieChart = new Chart(sentimentCtx, {
      type: 'pie',
      data: sentimentData,
      options: {
        responsive: false,
        maintainAspectRatio: false
      }
    });
  }