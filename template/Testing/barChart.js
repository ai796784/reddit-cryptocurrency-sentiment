function createBarChart(data) {
    console.log("Received data:", data); // Log the received data to the console

    var numComments = data.map(function(item) {
        return item.num_comments;
    });

    var interaction = data.map(function(item) {
        return item.interaction;
    });

    var labels = new Array(data.length).fill(''); // Empty array for labels
    console.log("numComments:", numComments); // Log numComments array to the console
    console.log("interaction:", interaction); // Log interaction array to the console

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
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}
