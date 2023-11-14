def config_parser(config_path):
    with open(config_path, 'r') as config_file:
        config = {}
        lines = config_file.readlines()
        for line in lines:
            attr, value = line.split(' = ')
            config[attr] = value.split('\n')[0]
        return config
