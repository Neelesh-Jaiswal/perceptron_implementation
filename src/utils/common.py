import yaml

def read_config(config_path):
    with open(config_path) as config_file:
        content = yaml.safe_load(config_file)
        print(content)
    return content

# if __name__ == '__main__':
#     read_config('C:\\Users\Lenovo\Downloads\Ineuron\9th_Jan_2022_Perceptron\perceptron_implementation\config.yaml')