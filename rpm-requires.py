#!/usr/bin/env python

print ",".join(
    line.strip() for line in open("rpm-requirements.txt").readlines())
