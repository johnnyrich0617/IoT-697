

class DataPayload:
    
    def __init__(self, temp, hum):
        self.temperature = temp
        self.humidity = hum
        
    
    def get_data_str(self):
        return "Temperature: " + self.temperature + ", Humidity: " + self.humidity
    