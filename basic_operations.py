import json
import os
import sys
import re


def dump_json(data, json_filename):
    with open(json_filename, 'w') as handler:
        json.dump(data, handler)


def load_json(json_filename):
    with open(json_filename) as data:
        return json.load(data)


def write_pid():
    prefix = os.path.splitext(os.path.basename(sys.argv[0]))[0]
    previous_pid = find_previous_pid(prefix)
    if previous_pid:
        print("\nRemoving {}...".format(previous_pid))
        os.remove(previous_pid)
    pid_fname = '{}_{}.pid'.format(prefix, str(os.getpid()))
    print("Writing {}\n".format(pid_fname))
    with open(pid_fname, 'w') as handler:
        handler.write(str())
    return pid_fname


def delete_pid(pid_fname):
    try:
        os.remove(pid_fname)
    except FileNotFoundError as e:
        print(str(e))


def find_previous_pid(prefix):
    for fname in os.listdir('.'):
        if re.fullmatch(r'{}_\d+\.pid'.format(prefix), fname):
            return fname
