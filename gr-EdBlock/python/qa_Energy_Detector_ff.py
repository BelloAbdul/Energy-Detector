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

from gnuradio import gr, gr_unittest
from gnuradio import blocks
from Energy_Detector_ff import Energy_Detector_ff

class qa_Energy_Detector_ff (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        # set up fg
        src_data = (0.1, 1, -2, 5.5, -0.5, 0.1, 1, -2, 5.5, -0.5)
        expected_result= (0.81999999999999995)
        src = blocks.vector_source_f(src_data)
        threshold = Energy_Detector_ff(10,0.5)
        snk = blocks.vector_sink_f()
        self.tb.connect(src,threshold)
        self.tb.connect(threshold,snk)
        self.tb.run ()
        # check data
        result_data = snk.data()
        self.assertEqual(expected_result, result_data)

if __name__ == '__main__':
    gr_unittest.run(qa_Energy_Detector_ff, "qa_Energy_Detector_ff.xml")
