import imp
import os
import sys
import zmq

sys.path.append(os.path.join(os.path.dirname(__file__), '../build/integration_tests'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../PWSat2OBC/integration_tests'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import response_frames
from binascii import hexlify
from experiment_file import ExperimentFileParser
from utils import ensure_string

from radio.radio_receiver import *
from radio.radio_sender import *
from tools.remote_files import *
from tools.parse_beacon import *
from telecommand import *
from response_frames import common
from devices import comm
from devices.camera import *
from tools.tools import SimpleLogger
import datetime
import pprint
import time

# Experiment settings
correlation_id = 2
delay = datetime.timedelta(0)
file_name_base = 'photo_test_20171009_1300'

def get_beacon():
    try:
        sender.send(SendBeacon())
        recv = receiver.receive_frame()
        return recv
    except zmq.Again:
        return None

def take_picture(sender, receiver, camera, resolution, qty, delay, filename_base):
    while True:
        print("Requesting photo {}, {}, {}, {}, {}".format(str(camera), str(resolution), qty, delay, filename_base))
        sender.send(tc.photo.TakePhotoTelecommand(10, camera, resolution, qty, delay, "filename_base"))
        recv = receiver.receive_frame()
        print(recv)
        if isinstance(recv, common.PhotoSuccessFrame):
            logger.log(recv.payload())
            break
        print("PhotoSuccessFrame received")

    time.sleep(5)

    while True:
        print("Waiting for photo file")
        sender.send(ListFiles(13, '/'))
        recv = receiver.receive_frame()
        print(recv)

        file_list = []
        if isinstance(recv, common.FileListSuccessFrame):
            file_list = RemoteFileTools.parse_file_list(recv)
            logger.log(file_list)
            print("File list taken, analyzing")

            file_to_be_present = None
            for f in file_list:
                if f['File'] == "{}_{}".format(filename_base, qty-1):
                    file_to_be_present = f
                    break
            if file_to_be_present != None:
                break


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument('-f', '--file', required=True,
                        help="Log file path")

    args = parser.parse_args()

    sender = Sender()
    receiver = Receiver()
    receiver.timeout(10000)
    logger = SimpleLogger(args.file)
    logger.log('Start of the script')

    # 0. Save experiment settings to log file
    logger.log('Photo Experiment')

    take_picture(sender, receiver, CameraLocation.Wing, PhotoResolution.p128, 0, delay, 'script')
