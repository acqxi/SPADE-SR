! /usr/python
import os, time, glob
paths = list( glob.glob('./demo/data/fe_black_scen1/*.npy'))
paths = sorted(paths, reverse=False, key=lambda x : int(x[-9:-4]))
for i in paths:
    time.sleep(0.2)
    os.system(f"cp {i} ./demo/receive_raw_thermal.npy")