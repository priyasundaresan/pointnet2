#!/usr/bin/env python
import os

if __name__=="__main__":
    cmd = "docker build -t priya-pointnet2 ."
    code = os.system(cmd)
