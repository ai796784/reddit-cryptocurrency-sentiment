import requests

# Define the URL of the endpoint
url = "http://localhost:5000/sentiment_analysis"

# Define the data you want to send
data = {"text": "I am very sad"}

# Send the POST request to the endpoint
response = requests.post(url, json=data)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract the sentiment score from the response
    sentiment_score = response.json()['sentiment_score']
    # Print the sentiment score
    print("Sentiment Score:", sentiment_score)
else:
    # Print an error message if the request was not successful
    print("Error:", response.text)
