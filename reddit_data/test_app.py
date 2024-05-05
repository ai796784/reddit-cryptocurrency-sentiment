import unittest
from app import app


class TestAppEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_reddit_data_endpoint(self):
        response = self.app.get('/reddit_data', query_string={'subreddit': 'BTC', 'limit': '1'})
        self.assertEqual(response.status_code, 200)


    def test_sentiment_analysis_endpoint(self):
        response = self.app.post('/sentiment_analysis', json={'text': 'This is a test sentence.'})
        self.assertEqual(response.status_code, 200)

    def test_emotion_analysis_endpoint(self):
        response = self.app.post('/emotion_analysis', json={'text': 'This is a test sentence.'})
        self.assertEqual(response.status_code, 200)


    def test_invalid_subreddit(self):
        response = self.app.get('/reddit_data', query_string={'subreddit': 'InvalidSubreddit123', 'limit': '1'})
        self.assertEqual(response.status_code, 500)

    def test_missing_parameters_reddit_data(self):
        response = self.app.get('/reddit_data')
        self.assertEqual(response.status_code, 400)
    
    
    def test_missing_parameters_sentiment_analysis(self):
        response = self.app.post('/sentiment_analysis')
        self.assertEqual(response.status_code, 415)

    def test_missing_parameters_emotion_analysis(self):
        response = self.app.post('/emotion_analysis')
        self.assertEqual(response.status_code, 415)
    
    def test_empty_text_sentiment_analysis(self):
        response = self.app.post('/sentiment_analysis', json={'text': ''})
        self.assertEqual(response.status_code, 200)
    
    def test_empty_text_emotion_analysis(self):
        response = self.app.post('/emotion_analysis', json={'text': ''})
        self.assertEqual(response.status_code, 200)
    
    def test_long_text_sentiment_analysis(self):
        long_text = "a" * 10001  # Assuming there's a character limit of 10,000
        response = self.app.post('/sentiment_analysis', json={'text': long_text})
        self.assertEqual(response.status_code, 200)
    
    def test_long_text_emotion_analysis(self):
        long_text = "a" * 10001  # Assuming there's a character limit of 10,000
        response = self.app.post('/emotion_analysis', json={'text': long_text})
        self.assertEqual(response.status_code, 400)
    

if __name__ == '__main__':
    unittest.main()
