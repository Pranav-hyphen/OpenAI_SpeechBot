import json

class C:
    def __init__(self):
        with open('A:\Chatbot\Chatbot\configjson.json') as f:
            self.config = json.load(f)

    def get_value(self,key):
        return self.config[key]

# width = config['capture_images_width']
# height = config['capture_images_height']
# getkey = config['get_key']
# senddata = config['send_url']
# report = config['get_report']
# cam_on_time = config['max_seconds_of_images_recorded']
# packet_size = config['max_length_of_images_packet'] 