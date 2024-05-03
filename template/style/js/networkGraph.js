// var nodes = null;
// var edges = null;
// var network = null;


function updateNetworkGraph() {
  // var ctx = document.getElementById('networkGraphCanvas').getContext('2d');
    // Check if a chart already exists
    var existingChart = Chart.getChart('networkGraphCanvas');

    // If a chart exists, destroy it
    if (existingChart) {
      existingChart.destroy();
    }
  var nodes = new vis.DataSet([
    { id: 1, label: 'Node 1' },
    { id: 2, label: 'Node 2' },
    { id: 3, label: 'Node 3' },
    { id: 4, label: 'Node 4' },
    { id: 5, label: 'Node 5' }
  ]);

  var edges = new vis.DataSet([
    { from: 1, to: 2 },
    { from: 1, to: 3 },
    { from: 2, to: 4 },
    { from: 2, to: 5 },
    { from: 3, to: 5 }
  ]);

  var container = document.getElementById('networkGraphContainer');
  var data = {
    nodes: nodes,
    edges: edges
  };
  var options = {};
  var network = new vis.Network(container, data, options);
}

function clearNetChart() {
  var container = document.getElementById('networkGraphContainer');
  while (container.firstChild) {
    container.removeChild(container.firstChild);
  }
}
