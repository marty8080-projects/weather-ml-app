import unittest
from app import app, classify_weather, load_model, weather_classes
import numpy as np

class TestUnit(unittest.TestCase):
	def setUp(self):
		app.testing = True
		self.client = app.test_client()
	
	# Complete this function to test proper handling of missing input field in the input
	def test_post_missing_field(self):
		form_data = {
			'temperature': '270.277',
			'pressure': '1006',
			'humidity': '84',
			# 'wind_speed' is missing
			'wind_deg': '274',
			'rain_1h': '0',
			'rain_3h': '0',
			'snow': '0',
			'clouds': '9'
		}
		response = self.client.post('/', data=form_data)

		self.assertIn(b'Error processing input', response.data)

	# Complete this function to test that the model can be loaded correctly
	def test_model_can_be_loaded(self):
		model = load_model()
		self.assertIsNotNone(model)

		self.assertTrue(hasattr(model, 'predict'))

	# Test model classification is within the 9 classes, each time for a different class with three different inputs
	def test_clear_classification_output(self):
		test_input = np.array([269.686,1002,78,0,23,0,0,0,0]).reshape(1,-1)
		class_result, _ = classify_weather(test_input) 
		# Checking against the 'clear' class at index[0] 
		self.assertEqual(class_result, weather_classes[0])

	def test_rainy_classification_output(self):
		test_input = np.array([279.626,998,99,1,314,0.3,0,0,88]).reshape(1,-1)
		class_result, _ = classify_weather(test_input) 
		# Checking against the 'rainy'/'rain' class at index [6]
		self.assertEqual(class_result, weather_classes[6])

	def test_cloudy_classification_output(self):

		test_input = np.array([291.15,1028,61,1,260,0,0,0,75]).reshape(1,-1)
		class_result, _ = classify_weather(test_input) 
		# Checking against the 'cloudy' class at index [1]
		self.assertEqual(class_result, weather_classes[1])

if __name__ == '__main__':
	unittest.main()
