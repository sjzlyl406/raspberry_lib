#! /usr/bin/env python


from __future__ import print_function

with open('/proc/cpuinfo') as f:
    for line in f:
        if line.strip():
            if line.rstrip('\n').startswith('model name'):
                model_name = line.rstrip('\n').split(':')[1]
                print(model_name)


