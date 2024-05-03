//Note: Need to remove the donutData and replace with the main data thing.

function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

const donutData = {
  Text: getRandomInt(100, 300), // Random number between 100 and 300
  Image: getRandomInt(50, 200),  // Random number between 50 and 200
  Video: getRandomInt(50, 150),     // Random number between 50 and 150
  Link: getRandomInt(50, 150)     // Random number between 50 and 150
};

function updateDonutChart(donutData) {
  console.log("Received data:", donutData);
  // Check if a chart already exists
  var existingChart = Chart.getChart('donutChartCanvas');

  // If a chart exists, destroy it
  if (existingChart) {
    existingChart.destroy();
  }

  var mediaTypeData = {
    labels: ['Text', 'Image', 'Video', 'Link'],
    datasets: [{
      data: [donutData.Text, donutData.Image, donutData.Video, donutData.Link],
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

// createMediaTypeDonutChart(donutData);
function clearDonutChart() {
  // var ctx = document.getElementById('barChartCanvas').getContext('2d');
  // ctx.clearRect(0, 0, canvas.width, canvas.height);
  const canvas = document.getElementById('donutChartCanvas');
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