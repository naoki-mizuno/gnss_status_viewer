#!/usr/bin/env python2


class Status:
    FIX_QUALITY = {
        None: 'No Data',
        '': 'Empty GGA',
        '0': 'Invalid',
        '1': 'GPS',
        '2': 'DGPS',
        '4': 'RTK',
        '5': 'FloatRTK',
    }

    def __init__(self, gga):
        self.is_gga = False
        self.fix = None
        self.num_sat = None
        self.hdop = None

        tokens = gga.strip().split(',')
        if tokens[0] != '$GPGGA':
            return
        if any([t == '' for t in tokens]):
            return

        self.fix = tokens[6]
        self.num_sat = int(tokens[7])
        self.hdop = float(tokens[8])
        self.is_gga = True

    def __str__(self):
        q = 'Quality : {0:>9}'.format(Status.FIX_QUALITY[self.fix])
        s = 'Num Sat : {0:>9}'.format(self.num_sat)
        h = 'HDOP    : {0:>9}'.format(self.hdop)
        return '\n'.join((q, s, h))

    def __eq__(self, other):
        if not isinstance(other, Status):
            return False
        return self.fix == other.fix and \
            self.num_sat == other.num_sat and \
            self.hdop == other.hdop

    def __ne__(self, other):
        return not self.__eq__(other)

    @staticmethod
    def get_status_change(a, b):
        """
        Returns a list of the string that represents the change from a to b

        :param a: status before
        :param b: status after
        :return the strings representing the changes between a and b
        """
        if not isinstance(a, Status) or not isinstance(b, Status):
            return ''

        s = []
        if a.fix != b.fix:
            s.append('Fix quality changed from {0} to {1}'.format(
                Status.FIX_QUALITY[a.fix],
                Status.FIX_QUALITY[b.fix]
            ))
        if a.num_sat != b.num_sat:
            s.append('Number of satellites {0} from {1} to {2}'.format(
                Status.__get_change_str__(a.num_sat, b.num_sat),
                a.num_sat,
                b.num_sat
            ))
        if a.hdop != b.hdop:
            s.append('HDOP {0} from {1} to {2}'.format(
                Status.__get_change_str__(a.hdop, b.hdop),
                a.hdop,
                b.hdop
            ))
        return s

    @staticmethod
    def __get_change_str__(a, b):
        return 'increased' if a < b else 'decreased'
