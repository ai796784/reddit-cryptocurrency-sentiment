function createLineChart(data) {

    var numComments = data.map(function(item) {
        return item.num_comments;
    });

    var interaction = data.map(function(item) {
        return item.interaction;
    });

    var labels = new Array(data.length).fill('');

    var ctx = document.getElementById('lineChartCanvas').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                    label: 'Number of Comments',
                    data: numComments,
                    borderColor: 'blue',
                    borderWidth: 1
                },
                {
                    label: 'Interaction Value',
                    data: interaction,
                    borderColor: 'green',
                    borderWidth: 1
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false
        }
    });
}
