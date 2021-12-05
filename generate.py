# Imports
from eth_account import Account
from multiprocessing import Process
import secrets
import argparse

# Constants
MINIMUM_ZEROES = 4
OPTIMAL_ZEROES = 7
PROCESSES_NUM = 8

def zeroesBeforeIndex(address: str, desired: int) -> int:
    interestingZone = address[:desired + 2]
    interestingZone = interestingZone[0] + interestingZone[2:desired + 2]

    for i in range(1, OPTIMAL_ZEROES + 1):
        if interestingZone[i] != "0":
            return i - 1

    return OPTIMAL_ZEROES

def findAddress():
    while True:
        private_key = secrets.token_hex(32)
        acct = Account.from_key(private_key)
        address = acct.address

        zeroes = zeroesBeforeIndex(address, OPTIMAL_ZEROES)
        if zeroes >= MINIMUM_ZEROES:
            print ("Private Key: ", private_key, " | Address: ", acct.address)
            
            filename = "addresses/" + address + ".txt"
            with open(filename, "w+") as outFile:
                outFile.write(private_key)

            if zeroes >= OPTIMAL_ZEROES:
                break

parser = argparse.ArgumentParser()
parser.add_argument("optimal", help="Optimal number of leading zeroes", type=int)
parser.add_argument("minimum", help="Minimum number of leading zeroes", type=int)
args = parser.parse_args()

OPTIMAL_ZEROES = int(args.optimal)
MINIMUM_ZEROES = int(args.minimum)

print("Generating an address with ", OPTIMAL_ZEROES, " zeroes...")

processes = []
for _ in range(PROCESSES_NUM):
    p = Process(target=findAddress)
    processes.append(p)

for i in range(PROCESSES_NUM):
    processes[i].start()

for i in range(PROCESSES_NUM):
    processes[i].join()