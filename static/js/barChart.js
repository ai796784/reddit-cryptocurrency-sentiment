function createBarChart(data) {
    var labels = data.map(function(item) {
        return item.title;
    });

    var numComments = data.map(function(item) {
        return item.num_comments;
    });

    var interaction = data.map(function(item) {
        return item.interaction;
    });

    var ctx = document.getElementById('barChartCanvas').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Number of Comments',
                data: numComments,
                backgroundColor: 'blue'
            },
            {
                label: 'Interaction Value',
                data: interaction,
                backgroundColor: 'green'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
}
