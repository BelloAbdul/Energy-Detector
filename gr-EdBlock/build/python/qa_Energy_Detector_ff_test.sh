#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/bello/Detect/gr-EdBlock/python
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/bello/Detect/gr-EdBlock/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/home/bello/Detect/gr-EdBlock/build/swig:$PYTHONPATH
/usr/bin/python2 /home/bello/Detect/gr-EdBlock/python/qa_Energy_Detector_ff.py 
