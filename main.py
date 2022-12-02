import argparse
import sys, os
import signal
from udp_utils import UdpServer, UdpClient

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--qt', action='store_true', help='Pyside for GUI')
    parser.add_argument('--height', type=int, default=840, help='height of movie')
    parser.add_argument('--width', type=int, default=840, help='width of of movie')
    parser.add_argument('--host', type=str, default='192.168.10.107', help='host url')
    parser.add_argument('--port', type=int, default=7000, help='port number')
    opt = parser.parse_args()
    return opt
 
def run_pyside_gui(opt):
    from PySide6.QtWidgets import QApplication
    from qtWidgets.SingleCamWidget import SingleCamWidget
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = QApplication(sys.argv)
    udp_server = UdpServer(opt.host, opt.port)
    try:
        w = SingleCamWidget(server=udp_server)
        w.setWindowTitle("PySide Layout on QMainWindow")
        w.resize(opt.width, opt.height)
        w.show()
        app.exec_()
    except KeyboardInterrupt:
        app.shutdown()
    sys.exit()
    
def main(opt):
    if opt.qt:
        run_pyside_gui(opt)
    else:
        udp_client = UdpClient(opt.host, opt.port)
        udp_client.send_()
        
if __name__ == '__main__':
    opt = get_parser()
    main(opt)

