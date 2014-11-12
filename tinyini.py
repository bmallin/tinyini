def parse(filepath):
    with open(filepath, 'r', encoding='utf-8') as fp:
        config = {}
        last_section = None

        for line in fp:
            line = line.strip()
            if not line:
                continue

            if line.startswith('#') or line.startswith(';'):
                continue
            elif line.startswith('['):
                section = line[1:-1]
                config[section] = {}
                last_section = section
            elif line.find('=') > -1:
                key, value = map(str.strip, line.split('='))
                config[last_section][key] = value
            elif line.find(':') > -1:
                key, value = map(str.strip, line.split(':'))
                config[last_section][key] = value
            else:
                config[last_section][line] = None

    return config


if __name__ == '__main__':
    pass