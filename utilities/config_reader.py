import configparser, os

current_script_directory = os.path.dirname(__file__)
absolute_path = os.path.join(current_script_directory, '..')
relative_path = r"configurations\app_config.ini"
full_path = os.path.join(absolute_path, relative_path)

config = configparser.RawConfigParser()
config.read(full_path)


class ReadConfig:

    @staticmethod
    def get_app_base_url():
        return config.get('app_data', 'base_url')

    @staticmethod
    def get_user_creds():
        return config.get('user_data', 'login'), config.get('user_data', 'password')

    @staticmethod
    def get_test_data():
        return config.get('test_data', 'email')

    @staticmethod
    def get_browser_id():
        return config.get('browser_data', 'browser_id')
