import unittest
from app import app, weather_classes  # Import your Flask app and the dynamic class list
import numpy as np

class TestModelAppIntegration(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()
        
    def test_model_app_integration(self):
        # Valid test input that should work with the trained model
        form_data = {
            'temperature': '275.15',   # Kelvin
            'pressure': '1013',        # hPa
            'humidity': '85',          # %
            'wind_speed': '3.6',       # m/s
            'wind_deg': '180',         # degrees
            'rain_1h': '0',            # mm
            'rain_3h': '0',            # mm
            'snow': '0',               # mm
            'clouds': '20'             # %
        }

        response = self.client.post('/', data=form_data)
        
        # Ensure that the result page (response.data) should include a weather prediction
        self.assertIn(b'Weather', response.data)
    
        # Ensure that the result page should include a prediction time
        self.assertIn(b'Prediction time', response.data)

        html_text = response.data.decode('utf-8').lower()
        
        # Use the dynamic list from the app instead of hardcoding strings.
        # This makes the test robust to spelling changes (like rainy -> rain).
        found = any(weather in html_text for weather in weather_classes)
        
        # Ensure that classification is in valid classes, provide an error message if not.
        self.assertTrue(found, "No valid weather class found in HTML response")

if __name__ == '__main__':
    unittest.main()
