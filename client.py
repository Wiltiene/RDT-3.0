import socket
import time
from utils import *
from unreliable_channel import unreliable_send

SERVER_ADDR = ('localhost', 12000)
TIMEOUT = 3

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.settimeout(TIMEOUT)

seq = 0

print("MENU DO CANAL")
print("1 - Entrega normal")
print("2 - Corromper dados")
print("3 - Inserir atraso")
mode = int(input("Escolha: "))

data = input("Digite a mensagem: ")
packet = make_packet(seq, data)

while True:
    print(f"[CLIENTE] Enviando pacote: SEQ={seq}, DATA={data}")
    unreliable_send(client, SERVER_ADDR, packet, mode)

    try:
        ack, _ = client.recvfrom(1024)
        ack = ack.decode()
        print(f"[CLIENTE] ACK recebido: {ack}")

        if ack == f"ACK{seq}":
            seq = 1 - seq
            print("[CLIENTE] Transmissão concluída com sucesso")
            break

    except socket.timeout:
        print("[CLIENTE] TIMEOUT! Retransmitindo pacote...")
