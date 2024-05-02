function createRadarChart(data) {
    var radarData = {
        labels: ['Joy', 'Sadness', 'Anger', 'Optimism'],
        datasets: [{
            label: 'Emotion Scores',
            data: [data.joy, data.sadness, data.anger, data.optimism],
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 1
        }]
    };

    var radarOptions = {
        scale: {
            ticks: {
                beginAtZero: true,
                max: 1 // Assuming emotion scores are normalized between 0 and 1
            }
        },
        responsive: true,
        maintainAspectRatio: false
    };

    var radarCtx = document.getElementById('radarChartCanvas').getContext('2d');
    var radarChart = new Chart(radarCtx, {
        type: 'radar',
        data: radarData,
        options: radarOptions
    });
}
