import configparser
import os


def get_config_path():
    return os.path.join(os.path.split(__file__)[0], 'config.ini')


def get_parser():
    config = configparser.ConfigParser()
    config.read(get_config_path())
    return config


def get_base_url():
    parser = get_parser()
    return parser['test']['base_url']


def get_token():
    parser = get_parser()
    return parser['test']['token']
