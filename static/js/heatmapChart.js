function createHeatMap(data) {
    // Extract relevant data for correlation computation
    var correlationData = data.map(function(item) {
        return [item.interaction, item.score, item.num_comments];
    });

    // Compute correlation matrix
    var correlations = [];
    for (var i = 0; i < correlationData.length; i++) {
        correlations[i] = [];
        for (var j = 0; j < correlationData.length; j++) {
            correlations[i][j] = pearsonCorrelation(correlationData[i], correlationData[j]);
        }
    }

    // Create heatmap data
    var heatmapData = {
        labels: ['Interaction', 'Score', 'Number of Comments'],
        datasets: [{
            label: 'Correlation Heatmap',
            data: correlations,
            borderWidth: 1,
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgba(255, 99, 132, 1)'
        }]
    };

    var heatmapOptions = {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            xAxes: [{
                ticks: {
                    autoSkip: false
                }
            }],
            yAxes: [{
                ticks: {
                    autoSkip: false
                }
            }]
        }
    };

    // Render heatmap
    var heatmapCtx = document.getElementById('heatmapCanvas').getContext('2d');
    var heatmapChart = new Chart(heatmapCtx, {
        type: 'heatmap',
        data: heatmapData,
        options: heatmapOptions
    });
}

// Function to compute Pearson correlation coefficient
function pearsonCorrelation(x, y) {
    var sumX = 0,
        sumY = 0,
        sumXY = 0,
        sumXX = 0,
        sumYY = 0,
        n = x.length;

    for (var i = 0; i < n; i++) {
        sumX += x[i];
        sumY += y[i];
        sumXY += x[i] * y[i];
        sumXX += x[i] * x[i];
        sumYY += y[i] * y[i];
    }

    var numerator = n * sumXY - sumX * sumY;
    var denominator = Math.sqrt((n * sumXX - sumX * sumX) * (n * sumYY - sumY * sumY));

    if (denominator === 0) return 0; // Avoid division by zero
    return numerator / denominator;
}
