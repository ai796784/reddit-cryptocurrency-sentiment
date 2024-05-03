// // Sample data for testing Bar chart
// var testData = [];

// for (var i = 1; i <= 500; i++) {
//     testData.push({
//         title: "Post " + i,
//         num_comments: Math.floor(Math.random() * 100) +1, // Random number of comments between 0 and 100
//         interaction: Math.floor(Math.random() * 50) +1// Random interaction value between 0 and 50
//     });
// }

// createBarChart(testData);

/////////////////////////////////////////////////////////////////////////////////////



// Sample data for testing Line Chart
// var sampleData = [];

// // Generate sample data for 500 posts
// for (var i = 1; i <= 500; i++) {
//     sampleData.push({
//         title: "Post " + i,
//         num_comments: Math.floor(Math.random() * 100), // Random number of comments (0 to 99)
//         interaction: Math.floor(Math.random() * 100) // Random interaction value (0 to 99)
//     });
// }

// // Call the createLineChart function with the sample data
// createLineChart(sampleData);


/////////////////////////////////////////////////////////////////////////////////////

// // Sample data for testing Radar Chart
// const mockData = [];

// // Generate 100 random posts with emotion scores
// for (let i = 0; i < 100; i++) {
//   const post = {
//     id: i + 1, // Assign a unique ID to each post
//     joy: Math.random(), // Generate a random value between 0 and 1 for joy
//     sadness: Math.random(), // Generate a random value between 0 and 1 for sadness
//     anger: Math.random(), // Generate a random value between 0 and 1 for anger
//     optimism: Math.random() // Generate a random value between 0 and 1 for optimism
//   };
//   mockData.push(post);
// }

// // Test the createRadarChart function with the mock data
// for (const post of mockData) {
//   createRadarChart(post);
// }

/////////////////////////////////////////////////////////////////////////////////////

// Sample data for testing Pie Chart

// function getRandomInt(min, max) {
//     return Math.floor(Math.random() * (max - min + 1)) + min;
// }

// const mockData = {
//     Positive: getRandomInt(100, 300), // Random number between 100 and 300
//     Negative: getRandomInt(50, 200),  // Random number between 50 and 200
//     Neutral: getRandomInt(50, 150)     // Random number between 50 and 150
// };

// // Call the function with mock data
// createSentimentPieChart(mockData);


/////////////////////////////////////////////////////////////////////////////////////

// Sample data for testing Donut Chart

// function getRandomInt(min, max) {
//     return Math.floor(Math.random() * (max - min + 1)) + min;
//   }
  
//   const mockData = {
//     Text: getRandomInt(100, 300), // Random number between 100 and 300
//     Image: getRandomInt(50, 200),  // Random number between 50 and 200
//     Video: getRandomInt(50, 150),     // Random number between 50 and 150
//     Link: getRandomInt(50, 150)     // Random number between 50 and 150
//   };
//   createMediaTypeDonutChart(mockData);
  



/////////////////////////////////////////////////////////////////////////////////////

// Generate random sample data for testing Heat Map

// Function to generate a random integer between min and max (inclusive)
// function getRandomInt(min, max) {
//     return Math.floor(Math.random() * (max - min + 1)) + min;
// }

// var sampleData = [];
// for (var i = 0; i < 100; i++) {
//     var post = {
//         timestamp: '2024-05-' + getRandomInt(1, 30), // Assuming posts are from May 2024
//         interaction: getRandomInt(1, 20), // Random interaction value between 1 and 20
//         score: getRandomInt(1, 10), // Random score between 1 and 10
//         num_comments: getRandomInt(0, 15) // Random number of comments between 0 and 15
//     };
//     sampleData.push(post);
// }

// // Call the createHeatmap function with the sample data
// createHeatmap(sampleData);


// Sample data for testing
var sampleData = [
    { timestamp: '2024-05-01', interaction: 10, score: 8, num_comments: 5 },
    { timestamp: '2024-05-02', interaction: 5, score: 6, num_comments: 3 },
    // Add more sample data as needed
];

// Call the createHeatmap function with the sample data
createHeatmap(sampleData);
