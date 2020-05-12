#!/usr/bin/python3

import random
import time
from prometheus_client import CollectorRegistry, Gauge, Counter, push_to_gateway

def main():
    registry = CollectorRegistry()
    c = Counter('number_builds', 'Number of builds', registry=registry)
    g = Gauge('build_last_success_unixtime', 'Last time a build job successfully finished', registry=registry)
    t = Gauge('build_time', 'How long it takes to build', registry=registry)
    while True:
        c.inc()
        g.set_to_current_time()
        t.set(random.randint(30, 60))
        push_to_gateway('localhost:9091', job='nightly_build', registry=registry)
        print("Pushed metrics")
        time.sleep(10)

if __name__ == '__main__':
    main()
