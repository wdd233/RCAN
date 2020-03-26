from data import common
from data import srdata
from data import div2k

class Water(srdata.SRData):
    def __init__(self, args, train=True):
        super(Water, self).__init__(args, train)
        self.repeat = args.test_every // (args.n_train // args.batch_size)

    def _scan(self):
        list_hr = []
