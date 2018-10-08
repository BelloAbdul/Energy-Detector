#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2018 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
import scipy 
import scipy.special as scs
from gnuradio import gr

class Energy_Detector_ff(gr.decim_block):
    """
    docstring for block Energy_Detector_ff
    """
    def __init__(self, samples,Pfa):
        self.samples = samples
        gr.decim_block.__init__(self,
            name="Energy_Detector_ff",
            in_sig=[numpy.float32 , numpy.float32],
            out_sig=[numpy.float32], decim = self.samples)
        self.Pfa = Pfa


    def work(self, input_items, output_items):
        in0 = input_items[0]
        in1 = input_items[1]
        out = output_items[0]
	#decision = output_items[1]
        # <+signal processing here+>
        # avg is updated using snr
        #for x in samples:
	Avg = scipy.mean(in0)
        signalAvg = round(Avg,8)
        #signalAvg = scipy.log10(Avg)
	print("This is Average signal energy", signalAvg)
        #print("This is signal absolute", Avg)

	#M2 = scipy.mean(abs(in0)**2)
        #M4 = scipy.mean(abs(in0)**4)
        #snr = scipy.sqrt(2*M2*M2 - M4)/(M2 - scipy.sqrt(2*M2*M2 - M4))
	#s = scipy.mean(abs(in0)**2)
	#n = scipy.var(abs(in0))
	#snr = s/n
	#print("signal to noise",snr)
	#print("signal to noise in DB", 10*scipy.log10(snr))
        
        NoisePower = in1**2 
        NoiseAvg = scipy.mean(NoisePower)
	var = scipy.var(NoisePower)
	stdev = scipy.sqrt(var)
	Qinv = scipy.sqrt(2) * scs.erfinv(1 - 2*self.Pfa)
	#avg = stdev * (scipy.sqrt(snr + 1))
        
	#Threshold = scipy.log10(NoiseAvg + Qinv*stdev)
	Threshold = round((NoiseAvg + Qinv*stdev),8)
	print("This is Detection threshold ",Threshold)
	
	
        #out[:] = avg + Qinv*stdev
	#out[:] = Threshold
	#decision[:] = 0.0

        #for x in range(1024):

        #out[:] = NoiseAvg
	if signalAvg > Threshold:
	    out[:] = signalAvg
	    print("signal is present", signalAvg)
        else:
            out[:] = Threshold
	    print("signal is absent", signalAvg)
        return len(output_items[0])

