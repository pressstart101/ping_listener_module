import platform    # For getting the operating system name
import subprocess  # For executing a shell command
import sys
import re
from subprocess import PIPE, STDOUT, Popen
import os
import asyncio
from fcntl import fcntl, F_GETFL, F_SETFL
from os import O_NONBLOCK, read
import json





class PingListener():
    def __init__(self):
        self.process = None
        self.parsed_pings = []
        self.buffer = bytearray()


    def start_listening(self):
        self.process = kickoff_tcpdump()
        return 



    def stop_listening(self):

        self.process.kill()

    def get_pings(self, max_number_of_pings=10):
        
        while len(self.parsed_pings) < max_number_of_pings:
            new_line_index = self.buffer.find(b'\n')
            if new_line_index != -1:
                raw_ping = self.buffer[:new_line_index]

                self.buffer = self.buffer[new_line_index+1:]

                grep_time = "(?P<time>\\d\\d:\\d\\d:\\d\\d)"
                grep_ip = '(?P<source_ip>\\b([0-9]{1,3}\.){3}[0-9]{1,3}\\b)'
                grep_seq = "seq (?P<seq>\\d+)"
                grep = re.match(f'{grep_time}.*?{grep_ip}.*?{grep_seq}', raw_ping.decode('ascii'))
                

                if grep:
                    self.parsed_pings.append(grep.groupdict())
            else:    
                try:
                    self.buffer.extend(read(self.process.stdout.fileno(), 1024))




                except(BlockingIOError):
                    print("buffer is empty") 
                    break

        num_of_pings = min(len(self.parsed_pings), max_number_of_pings)

        output_in_popen = [self.parsed_pings.pop(0) for _ in range(num_of_pings)]

        return output_in_popen



    def clear_data(self):
        pass





def kickoff_tcpdump():

    process = subprocess.Popen(["tcpdump", "-l", "-nni", "eth0", "-e", "icmp[icmptype]==8"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    flags = fcntl(process.stdout, F_GETFL) # get current p.stdout flags
    fcntl(process.stdout, F_SETFL, flags | O_NONBLOCK)


    return process



def test_ping():

    server.ping_init.start_listening()

    time.sleep(3)
    p = server.ping_init.get_pings()

    return p


