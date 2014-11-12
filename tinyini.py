"""tinyini.py

The MIT License (MIT)

Copyright (c) 2014 Benjamin Mallin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

"""


def parse(filepath):
    """Parses a ini file.

    :param filepath: Path to ini file.
    :return: A dict representing the ini file contents.
    """

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
            elif line.find('=') > -1 or line.find(':') > -1:
                key, value = map(str.strip, max(line.split('='),
                                                line.split(':'), key=len))
                config[last_section][key] = value
            else:
                config[last_section][line] = None

    return config


if __name__ == '__main__':
    pass