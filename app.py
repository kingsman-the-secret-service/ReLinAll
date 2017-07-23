from relinall.summary import *
from relinall.server import *
from relinall.service import *
from relinall.putty import *

class App(Server, Service, Summary, Putty):

    def __init__(self):
        app = QApplication(sys.argv)
        super().__init__()
        sys.exit(app.exec_())


if __name__ == "__main__":
	App()