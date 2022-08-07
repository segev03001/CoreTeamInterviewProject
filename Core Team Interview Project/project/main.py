import generator
import os

if __name__ == '__main__':
    path = os.getcwd()
    config_path = (os.path.abspath(os.path.join(path, os.pardir))) + "\config.json"
    output_path = (os.path.abspath(os.path.join(path, os.pardir))) + "\output.json"
    user_answer = input("Do you want to debug? (Y/N)")
    debug = user_answer == "Y"
    generator.generator(config_path, output_path, debug)
