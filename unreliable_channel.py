import random
import time

def unreliable_send(sock, addr, message, mode):
    print(f"[CANAL] Modo selecionado: {mode}")

    if mode == 2:  # corrupção
        message = message[:-1] + "X"
        print("[CANAL] Pacote corrompido")

    if mode == 3:  # atraso
        print("[CANAL] Atraso artificial aplicado")
        time.sleep(3)

    sock.sendto(message.encode(), addr)
