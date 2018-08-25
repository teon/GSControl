#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: GPL-3.0
#
##################################################
# GNU Radio Python Flow Graph
# Title: Rtl Sdr Source
# Generated: Sat Aug 25 21:31:50 2018
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
import osmosdr
import sys
import time
from gnuradio import qtgui


class rtl_sdr_source(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Rtl Sdr Source")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Rtl Sdr Source")
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

        self.settings = Qt.QSettings("GNU Radio", "rtl_sdr_source")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.variable_qtgui_label_0 = variable_qtgui_label_0 = ''
        self.samp_rate = samp_rate = 192000
        self.rf_gain = rf_gain = 10
        self.if_gain = if_gain = 20
        self.frequency_offset = frequency_offset = 20e3
        self.frequency = frequency = 435275000

        ##################################################
        # Blocks
        ##################################################
        self._rf_gain_tool_bar = Qt.QToolBar(self)
        self._rf_gain_tool_bar.addWidget(Qt.QLabel('RF Gain (dB)'+": "))
        self._rf_gain_line_edit = Qt.QLineEdit(str(self.rf_gain))
        self._rf_gain_tool_bar.addWidget(self._rf_gain_line_edit)
        self._rf_gain_line_edit.returnPressed.connect(
        	lambda: self.set_rf_gain(int(str(self._rf_gain_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._rf_gain_tool_bar, 4, 0, 1, 1)
        for r in range(4, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._if_gain_tool_bar = Qt.QToolBar(self)
        self._if_gain_tool_bar.addWidget(Qt.QLabel('IF Gain (dB)'+": "))
        self._if_gain_line_edit = Qt.QLineEdit(str(self.if_gain))
        self._if_gain_tool_bar.addWidget(self._if_gain_line_edit)
        self._if_gain_line_edit.returnPressed.connect(
        	lambda: self.set_if_gain(int(str(self._if_gain_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._if_gain_tool_bar, 5, 0, 1, 1)
        for r in range(5, 6):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._frequency_offset_range = Range(-40e3, 40e3, 10, 20e3, 200)
        self._frequency_offset_win = RangeWidget(self._frequency_offset_range, self.set_frequency_offset, 'Frequency Offset (Hz)', "counter_slider", float)
        self.top_grid_layout.addWidget(self._frequency_offset_win, 3, 0, 1, 1)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._frequency_tool_bar = Qt.QToolBar(self)
        self._frequency_tool_bar.addWidget(Qt.QLabel('PW-Sat2 Frequency (Hz)'+": "))
        self._frequency_line_edit = Qt.QLineEdit(str(self.frequency))
        self._frequency_tool_bar.addWidget(self._frequency_line_edit)
        self._frequency_line_edit.returnPressed.connect(
        	lambda: self.set_frequency(int(str(self._frequency_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._frequency_tool_bar, 2, 0, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.zeromq_pub_sink_0 = zeromq.pub_sink(gr.sizeof_gr_complex, 1, 'tcp://*:20001', 100, False, -1)
        self._variable_qtgui_label_0_tool_bar = Qt.QToolBar(self)

        if None:
          self._variable_qtgui_label_0_formatter = None
        else:
          self._variable_qtgui_label_0_formatter = lambda x: str(x)

        self._variable_qtgui_label_0_tool_bar.addWidget(Qt.QLabel('Keep the same offset frequency here as well as in demodulator'+": "))
        self._variable_qtgui_label_0_label = Qt.QLabel(str(self._variable_qtgui_label_0_formatter(self.variable_qtgui_label_0)))
        self._variable_qtgui_label_0_tool_bar.addWidget(self._variable_qtgui_label_0_label)
        self.top_grid_layout.addWidget(self._variable_qtgui_label_0_tool_bar, 0, 0, 2, 1)
        for r in range(0, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(frequency+frequency_offset, 0)
        self.rtlsdr_source_0.set_freq_corr(0, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(0, 0)
        self.rtlsdr_source_0.set_gain_mode(False, 0)
        self.rtlsdr_source_0.set_gain(rf_gain, 0)
        self.rtlsdr_source_0.set_if_gain(if_gain, 0)
        self.rtlsdr_source_0.set_bb_gain(20, 0)
        self.rtlsdr_source_0.set_antenna('', 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)




        ##################################################
        # Connections
        ##################################################
        self.connect((self.rtlsdr_source_0, 0), (self.zeromq_pub_sink_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "rtl_sdr_source")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_variable_qtgui_label_0(self):
        return self.variable_qtgui_label_0

    def set_variable_qtgui_label_0(self, variable_qtgui_label_0):
        self.variable_qtgui_label_0 = variable_qtgui_label_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_0_label, "setText", Qt.Q_ARG("QString", self.variable_qtgui_label_0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)

    def get_rf_gain(self):
        return self.rf_gain

    def set_rf_gain(self, rf_gain):
        self.rf_gain = rf_gain
        Qt.QMetaObject.invokeMethod(self._rf_gain_line_edit, "setText", Qt.Q_ARG("QString", str(self.rf_gain)))
        self.rtlsdr_source_0.set_gain(self.rf_gain, 0)

    def get_if_gain(self):
        return self.if_gain

    def set_if_gain(self, if_gain):
        self.if_gain = if_gain
        Qt.QMetaObject.invokeMethod(self._if_gain_line_edit, "setText", Qt.Q_ARG("QString", str(self.if_gain)))
        self.rtlsdr_source_0.set_if_gain(self.if_gain, 0)

    def get_frequency_offset(self):
        return self.frequency_offset

    def set_frequency_offset(self, frequency_offset):
        self.frequency_offset = frequency_offset
        self.rtlsdr_source_0.set_center_freq(self.frequency+self.frequency_offset, 0)

    def get_frequency(self):
        return self.frequency

    def set_frequency(self, frequency):
        self.frequency = frequency
        Qt.QMetaObject.invokeMethod(self._frequency_line_edit, "setText", Qt.Q_ARG("QString", str(self.frequency)))
        self.rtlsdr_source_0.set_center_freq(self.frequency+self.frequency_offset, 0)


def main(top_block_cls=rtl_sdr_source, options=None):

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
