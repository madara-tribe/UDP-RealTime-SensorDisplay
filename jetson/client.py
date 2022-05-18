import socket
import datetime
import argparse
import time

M_SIZE = 1024
class UDPSender():
    def __init__(self, host, port):
        self.serv_address = (host, port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def udp_sender(self):
        while True:
            try:
                message = now = str(datetime.datetime.now())
                send_len = self.sock.sendto(message.encode('utf-8'), self.serv_address)
                time.sleep(2) 
                #print('Waiting response from Server')
                rx_meesage, addr = self.sock.recvfrom(M_SIZE)
                print(f"[Server]: {rx_meesage.decode(encoding='utf-8')}")

            except KeyboardInterrupt:
                print('closing socket')
                self.sock.close()
                print('done')
                break

def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    # ATS control
    parser.add_argument("--port", default=8890, help="port for UDP")
    parser.add_argument("--host", default="192.168.10.107", help="Main PC host")
    args = parser.parse_args()

    udp_ = UDPSender(args.host, args.port)
    udp_.udp_sender()

if __name__=='__main__':
    main()
