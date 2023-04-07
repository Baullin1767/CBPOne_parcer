#! /usr/bin/env python

import time
import os

from com.dtmilano.android.viewclient import ViewClient

path = 'snapshots/'

count_view = 17
device, serialno = ViewClient.connectToDeviceOrExit(verbose=False)
vc = ViewClient(device, serialno)

for i in range(40):

    start = time.time()
    device.touch(300, 250)
    device.touch(300, 300)
    time.sleep(0.5)
    list1 = vc.dump()
    if len(list1) > count_view:
        device.takeSnapshot(reconnect=True).save(f'{path}brownville/filename{i}.png', 'PNG')

    device.touch(300, 250)
    device.touch(300, 400)
    time.sleep(0.5)
    list1 = vc.dump()
    if len(list1) > count_view:
        device.takeSnapshot(reconnect=True).save(f'{path}calexico_west/filename{i}.png', 'PNG')
    
    device.touch(300, 250)
    device.touch(300, 500)
    time.sleep(0.5)
    list1 = vc.dump()
    if len(list1) > count_view:
        device.takeSnapshot(reconnect=True).save(f'{path}eagle_pass/filename{i}.png', 'PNG')
    
    device.touch(300, 250)
    device.touch(300, 600)
    time.sleep(0.5)
    list1 = vc.dump()
    if len(list1) > count_view:
        device.takeSnapshot(reconnect=True).save(f'{path}hidalgo/filename{i}.png', 'PNG')
    
    device.touch(300, 250)
    device.touch(300, 700)
    time.sleep(0.5)
    list1 = vc.dump()
    if len(list1) > count_view:
        device.takeSnapshot(reconnect=True).save(f'{path}laredo/filename{i}.png', 'PNG')
    
    device.touch(300, 250)
    device.touch(300, 800)
    time.sleep(0.5)
    list1 = vc.dump()
    if len(list1) > count_view:
        device.takeSnapshot(reconnect=True).save(f'{path}nogales/filename{i}.png', 'PNG')
    
    device.touch(300, 250)
    device.touch(300, 900)
    time.sleep(0.5)
    list1 = vc.dump()
    if len(list1) > count_view:
        device.takeSnapshot(reconnect=True).save(f'{path}paso_del_norte/filename{i}.png', 'PNG')
    
    device.touch(300, 250)
    device.touch(300, 1000)
    time.sleep(0.5)
    list1 = vc.dump()
    if len(list1) > count_view:
        device.takeSnapshot(reconnect=True).save(f'{path}san_ysidro/filename{i}.png', 'PNG')