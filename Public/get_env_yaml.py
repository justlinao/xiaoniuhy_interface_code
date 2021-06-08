import yaml
import os


def read_config():
    f = open(os.path.abspath(os.path.dirname(__file__)) + r'/config.yaml')
    y = yaml.load(f, Loader=yaml.SafeLoader)
    return y['timer']



