function createMediaTypeDonutChart(data) {
    console.log("Received data:", data);
  
    var mediaTypeData = {
      labels: ['Text', 'Image', 'Video', 'Link'],
      datasets: [{
        data: [data.Text, data.Image, data.Video, data.Link],
        backgroundColor: ['blue', 'green', 'red', 'orange']
      }]
    };
  
    var mediaTypeCtx = document.getElementById('donutChartCanvas').getContext('2d');
    var mediaTypeDonutChart = new Chart(mediaTypeCtx, {
      type: 'doughnut',
      data: mediaTypeData,
      options: {
        responsive: true,
        maintainAspectRatio: false
      }
    });
  }