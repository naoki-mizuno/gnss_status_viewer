#!/usr/bin/env python2

import rospy
from nmea_msgs.msg import Sentence

quality_table = {
    '': 'Empty GGA',
    '0': 'Invalid',
    '1': 'GPS',
    '2': 'DGPS',
    '4': 'RTK',
    '5': 'FloatRTK',
}

is_first_data = True
prev_quality = None
prev_num_sat = None
prev_hdop = None

def gps_callback(msg):
    global is_first_data
    global prev_quality
    global prev_num_sat
    global prev_hdop

    values = msg.sentence.split(',')
    quality, num_sat, hdop = values[6:9]

    if is_first_data:
        prev_quality = quality
        prev_num_sat = num_sat
        prev_hdop = hdop
        is_first_data = False
        return

    if quality != prev_quality:
        p = quality_table[prev_quality]
        c = quality_table[quality]
        rospy.loginfo('Data quality changed from {0} to {1}'.format(p, c))

    if num_sat == '' or hdop == '':
        return

    if num_sat != prev_num_sat:
        p = int(prev_num_sat)
        c = int(num_sat)
        change = 'increased' if c > p else 'decreased'
        rospy.loginfo('Number of Satellites {0} from {1} to {2}'.format(change, p, c))
    if hdop != prev_hdop:
        p = float(prev_hdop)
        c = float(hdop)
        change = 'increased' if c > p else 'decreased'
        rospy.loginfo('HDOP {0} from {1} to {2}'.format(change, p, c))

    prev_quality = quality
    prev_num_sat = num_sat
    prev_hdop = hdop

rospy.init_node('gnss_status_viewer')
rospy.Subscriber('nmea_sentence', Sentence, gps_callback)

rospy.spin()
