#!/usr/bin/python3

import subprocess

class wacom:
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0

    def __init__(self, x1, y1, x2, y2):
        self.x1 = str(x1)
        self.y1 = str(y1)
        self.x2 = str(x2)
        self.y2 = str(y2)

    def adjust(self):
        stylus_id = self.fetch_stylus_id()

        os_params = ['xsetwacom', '--set', str(stylus_id), 'area', self.x1, self.y1, self.x2, self.y2]
        os_call = subprocess.run(os_params, stdout=subprocess.PIPE)
        lines = os_call.stdout.decode('utf-8').split('\n')


    def fetch_stylus_id(self):
        id = 0

        os_call = subprocess.run(['xsetwacom', '--list', 'devices'], stdout=subprocess.PIPE)
        lines = os_call.stdout.decode('utf-8').split('\n')

        for line in lines:
            if ("STYLUS" in line):
                parts = line.split(':')
                id_part = parts[1]
                id = id_part.split('\t')[0].replace(' ', '')

        return id

# you will have to adjust this values!
w = wacom(-12900, 0, 21600, 13500)
w.adjust()