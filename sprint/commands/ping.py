# Modules
import requests
from time import sleep

from ..utils.logging import error
from ..utils.bases import BaseCommand

# Command class
class Ping(BaseCommand):

    def __init__(self, core):
        self.core = core

    def ping(self, arguments):

        # Fix some flake8 problem
        global error

        # Locate our hostname
        host = None
        if arguments["pos"]:
            host = arguments["pos"][0]

            if not host.startswith("http"):
                host = "http://" + host

        if host is None:
            return error("ArgumentError", "No destination specified to ping.")

        # Locate our amount
        count = 5
        if "count" in arguments["vals"]:
            count = arguments["vals"]["count"]

            if not isinstance(count, int):
                return error("ArgumentError", "The specified count is not a valid integer.")

        # Locate our interval
        interval = 1
        if "interval" in arguments["vals"]:
            interval = arguments["vals"]["interval"]

            if not isinstance(interval, (int, float)):
                return error("ArgumentError", "The interval is invalid, should be either a float/integer.")

        # Fetch our timeout
        timeout = 5
        if "timeout" in arguments["vals"]:
            timeout = arguments["vals"]["timeout"]

            if not isinstance(timeout, (int, float)):
                return error("ArgumentError", "The timeout is invalid, should be either a float/integer.")

        # Begin our ping test
        print(f"Pinging {host} with 1/{interval}s interval")

        n = 0
        while n < count:

            # Perform connection
            try:
                r = requests.get(host, timeout = timeout, stream = True)

                # Print our results
                elapsed = round(r.elapsed.total_seconds() * 1000)
                addr = r.raw._original_response.fp.raw._sock.getpeername()[0]

                print(f"[{n + 1}] Response from {addr} [{elapsed}ms]")

                # Close our socket
                r.close()

                # Since we didn't hit our timeout, wait
                sleep(interval)

            except Exception as error:

                if isinstance(error, requests.exceptions.ConnectTimeout):
                    print(f"[{n + 1}] Failed to reach destination.")

            # Continue up
            n += 1
