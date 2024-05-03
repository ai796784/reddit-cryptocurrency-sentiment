// function updateNetworkGraph() {
//     // Sample data (replace with your own data fetching and processing)
//     var nodes = new vis.DataSet([
//         { id: 1, label: 'Node 1' },
//         { id: 2, label: 'Node 2' },
//         { id: 3, label: 'Node 3' },
//         { id: 4, label: 'Node 4' },
//     ]);
//     var edges = new vis.DataSet([
//         { from: 1, to: 2 },
//         { from: 2, to: 3 },
//         { from: 3, to: 4 },
//         { from: 4, to: 1 },
//     ]);

//     // Create a network
//     var container = document.getElementById('networkGraphCanvas');
//     var data = {
//         nodes: nodes,
//         edges: edges,
//     };
//     var options = {};
//     var network = new vis.Network(container, data, options);
// }


function createNetworkGraph(networkPlotData) {
    // Parse the JSON data
    var edges = JSON.parse(networkPlotData);

    // Define dimensions for the SVG container
    var width = 800;
    var height = 600;

    // Create an SVG element
    var svg = d3.select("#networkGraphContainer")
                .append("svg")
                .attr("width", width)
                .attr("height", height);

    // Create a force simulation
    var simulation = d3.forceSimulation()
                       .force("link", d3.forceLink().id(function(d) { return d.id; }))
                       .force("charge", d3.forceManyBody())
                       .force("center", d3.forceCenter(width / 2, height / 2));

    // Add edges to the simulation
    var link = svg.selectAll(".link")
                  .data(edges)
                  .enter().append("line")
                  .attr("class", "link");

    // Add nodes to the simulation
    var node = svg.selectAll(".node")
                  .data(d3.merge([edges.map(function(d) { return d.source; }), edges.map(function(d) { return d.target; })]))
                  .enter().append("circle")
                  .attr("class", "node")
                  .attr("r", 5)
                  .attr("fill", "steelblue")
                  .call(d3.drag()
                          .on("start", dragstarted)
                          .on("drag", dragged)
                          .on("end", dragended));

    // Add labels to the nodes
    var label = svg.selectAll(".label")
                   .data(d3.merge([edges.map(function(d) { return d.source; }), edges.map(function(d) { return d.target; })]))
                   .enter().append("text")
                   .attr("class", "label")
                   .attr("dy", ".35em")
                   .text(function(d) { return d; });

    // Add tick function for simulation
    simulation.nodes(d3.merge([edges.map(function(d) { return d.source; }), edges.map(function(d) { return d.target; })]))
              .on("tick", ticked);

    simulation.force("link").links(edges);

    function ticked() {
        link.attr("x1", function(d) { return d.source.x; })
            .attr("y1", function(d) { return d.source.y; })
            .attr("x2", function(d) { return d.target.x; })
            .attr("y2", function(d) { return d.target.y; });

        node.attr("cx", function(d) { return d.x; })
            .attr("cy", function(d) { return d.y; });

        label.attr("x", function(d) { return d.x + 10; })
             .attr("y", function(d) { return d.y - 10; });
    }

    function dragstarted(d) {
        if (!d3.event.active) simulation.alphaTarget(0.3).restart();
        d.fx = d.x;
        d.fy = d.y;
    }

    function dragged(d) {
        d.fx = d3.event.x;
        d.fy = d3.event.y;
    }

    function dragended(d) {
        if (!d3.event.active) simulation.alphaTarget(0);
        d.fx = null;
        d.fy = null;
    }
}
