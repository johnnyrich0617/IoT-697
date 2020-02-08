import time
import data_temphum_payload as payload
import jsonpickle


class WeatherDisplayMessage:

    def __init__(self, temp, humidity):
        self.data = payload.DataPayload(temp, humidity)
        self.timestamp = time.time()
        timeObj = time.localtime(self.timestamp)
        print('Current TimeStamp is : %d-%d-%d %d:%d:%d' % (
            timeObj.tm_year, timeObj.tm_mon, timeObj.tm_mday,
            timeObj.tm_hour, timeObj.tm_min, timeObj.tm_sec))

    def serialize(self):
        return jsonpickle.encode(self, unpicklable=False)

    def print_raw_content(self):
        print("WeatherDisplayMessage: Timestamp = %d", self.timestamp)
        print("WeatherDisplayMessage: Data = " + self.data.get_data_str())

    def print_serialized_obj(self):
        print(self.serialize())
