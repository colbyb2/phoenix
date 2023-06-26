import os
import json

class ConfigManager:
    def __init__(self):
         data = self.get_config_data()
         self.key = data['API_KEY'] if data != None else None
    
    def get_config_data(self):
        config_path = os.path.expanduser('~/.phoenixconfig')

        # If the config file exists, read the name from it.
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                config = json.load(f)
            return config
        else:
            return None

    def save_config_data(self):
        config_path = os.path.expanduser('~/.phoenixconfig')

        with open(config_path, 'w') as f:
            json.dump({
                'API_KEY':self.key
            }, f)