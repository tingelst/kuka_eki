from kuka_eki import EKIDriver


d = EKIDriver((('192.168.250.20', 54600)))
d.start()


s = d._conn


