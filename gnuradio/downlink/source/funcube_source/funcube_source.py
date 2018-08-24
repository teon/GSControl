#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: GPL-3.0
#
##################################################
# GNU Radio Python Flow Graph
# Title: Funcube Source
# Generated: Fri Aug 24 18:39:29 2018
# GNU Radio version: 3.7.12.0
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import zeromq
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import fcdproplus
import sys
from gnuradio import qtgui


class funcube_source(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Funcube Source")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Funcube Source")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "funcube_source")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.frequency_offset = frequency_offset = 20e3
        self.frequency = frequency = 435275000

        ##################################################
        # Blocks
        ##################################################
        self._frequency_offset_range = Range(-40e3, 40e3, 10, 20e3, 200)
        self._frequency_offset_win = RangeWidget(self._frequency_offset_range, self.set_frequency_offset, 'Frequency Offset', "counter_slider", float)
        self.top_grid_layout.addWidget(self._frequency_offset_win)
        self._frequency_tool_bar = Qt.QToolBar(self)
        self._frequency_tool_bar.addWidget(Qt.QLabel('Frequency'+": "))
        self._frequency_line_edit = Qt.QLineEdit(str(self.frequency))
        self._frequency_tool_bar.addWidget(self._frequency_line_edit)
        self._frequency_line_edit.returnPressed.connect(
        	lambda: self.set_frequency(int(str(self._frequency_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._frequency_tool_bar)
        self.zeromq_pub_sink_0 = zeromq.pub_sink(gr.sizeof_gr_complex, 1, 'tcp://*:20001', 100, False, -1)
        self.fcdproplus_fcdproplus_0 = fcdproplus.fcdproplus('',1)
        self.fcdproplus_fcdproplus_0.set_lna(0)
        self.fcdproplus_fcdproplus_0.set_mixer_gain(1)
        self.fcdproplus_fcdproplus_0.set_if_gain(10)
        self.fcdproplus_fcdproplus_0.set_freq_corr(0)
        self.fcdproplus_fcdproplus_0.set_freq(frequency+frequency_offset)




        ##################################################
        # Connections
        ##################################################
        self.connect((self.fcdproplus_fcdproplus_0, 0), (self.zeromq_pub_sink_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "funcube_source")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_frequency_offset(self):
        return self.frequency_offset

    def set_frequency_offset(self, frequency_offset):
        self.frequency_offset = frequency_offset
        self.fcdproplus_fcdproplus_0.set_freq(self.frequency+self.frequency_offset)

    def get_frequency(self):
        return self.frequency

    def set_frequency(self, frequency):
        self.frequency = frequency
        Qt.QMetaObject.invokeMethod(self._frequency_line_edit, "setText", Qt.Q_ARG("QString", str(self.frequency)))
        self.fcdproplus_fcdproplus_0.set_freq(self.frequency+self.frequency_offset)


def main(top_block_cls=funcube_source, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
