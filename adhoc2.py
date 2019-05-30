#!/usr/bin/python

import sys

from mininet.log import setLogLevel, info
from mn_wifi.link import wmediumd, adhoc
from mininet.node import Controller
from mn_wifi.cli import CLI_wifi
from mn_wifi.net import Mininet_wifi
from mn_wifi.wmediumdConnector import interference

def topology():
    "Create a network."
    net = Mininet_wifi(controller=Controller, link=wmediumd, wmediumd_mode=interference)

    info("*** Creating nodes\n")

    sta1 = net.addStation('sta1', mac='00:00:00:00:00:02', ip='10.0.0.2/8',
                   min_x=10, max_x=30, min_y=50, max_y=70, min_v=5, max_v=10)
    sta2 = net.addStation('sta2', mac='00:00:00:00:00:03', ip='10.0.0.3/8',
                   min_x=10, max_x=30, min_y=50, max_y=70, min_v=5, max_v=10)
    sta3 = net.addStation('sta3', mac='00:00:00:00:00:04', ip='10.0.0.4/8',
                   min_x=10, max_x=30, min_y=50, max_y=70, min_v=5, max_v=10)
    sta4 = net.addStation('sta4', mac='00:00:00:00:00:05', ip='10.0.0.5/8',
                   min_x=10, max_x=30, min_y=50, max_y=70, min_v=5, max_v=10)
    sta5 = net.addStation('sta5', mac='00:00:00:00:00:06', ip='10.0.0.6/8',
                   min_x=10, max_x=30, min_y=50, max_y=70, min_v=5, max_v=10)
    sta6 = net.addStation('sta6', mac='00:00:00:00:00:07', ip='10.0.0.7/8',
                   min_x=10, max_x=30, min_y=50, max_y=70, min_v=5, max_v=10)

    c1 = net.addController('c1', controller=Controller)

    info("*** Configuring Propagation Model\n")

    net.setPropagationModel(model="logDistance", exp=4)

    info("*** Configuring wifi nodes\n")

    net.configureWifiNodes()

    info("*** Creating links\n")

    net.addLink(sta1, cls=adhoc, ssid='adhocNet',
                mode='g', channel=5, ht_cap='HT40+')
    net.addLink(sta2, cls=adhoc, ssid='adhocNet',
                mode='g', channel=5)
    net.addLink(sta3, cls=adhoc, ssid='adhocNet',
                mode='g', channel=5, ht_cap='HT40+')
    net.addLink(sta4, cls=adhoc, ssid='adhocNet',
                mode='g', channel=5, ht_cap='HT40+')
    net.addLink(sta5, cls=adhoc, ssid='adhocNet',
                mode='g', channel=5)
    net.addLink(sta6, cls=adhoc, ssid='adhocNet',
                mode='g', channel=5, ht_cap='HT40+')

    net.plotGraph(max_x=100, max_y=100)
    # net.startMobility(time=0, model='RandomWayPoint',
    #                       min_x = 10, min_y = 10,
    #                       max_x=100, max_y=100,
    #                       min_v=0.5, max_v=0.8, seed=20)

    net.setMobilityModel(time=0, model='RandomDirection', max_x=100, max_y=100, seed=10)

    info("*** Starting network\n")
    net.build()
    c1.start()

    info("*** Running CLI\n")
    CLI_wifi(net)

    info("*** Stopping network\n")
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    #autoTxPower = True if '-a' in sys.argv else False
    #topology(autoTxPower)
    topology()
