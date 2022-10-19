#!/usr/bin/env python
import sys
import sys
import time
import logging

# EAFP - Easy to Ask Forgiveness than permission
# (É mais fácil pedir perdão do que permissão)

log = logging.Logger("errors")


def try_open_a_file(filepath, retry=1):
    """Tries to open a file, if error, retries n times"""
    for attempt in range(1, retry + 1):
        try:
            return open(filepath).readlines()
        except FileNotFoundError as e:
            log.error("ERRO: %s", str(e))
            time.sleep(2)
        else:
            print("Sucesso!")
        finally:
            print("Execute isso sempre!")
    return []


for line in try_open_a_file("names.txt", retry=5):
    print(line)
