import hashlib

def checksum(data):
    return hashlib.md5(data.encode()).hexdigest()

def make_packet(seq, data):
    chksum = checksum(data)
    return f"{seq}|{data}|{chksum}"

def parse_packet(packet):
    seq, data, chksum = packet.split("|")
    return int(seq), data, chksum

def is_corrupted(data, chksum):
    return checksum(data) != chksum
