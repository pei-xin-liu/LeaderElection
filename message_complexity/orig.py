# -*- generated by 1.0.12 -*-
import da
PatternExpr_676 = da.pat.TuplePattern([da.pat.ConstantPattern('CAPTURE'), da.pat.FreePattern('ph'), da.pat.FreePattern('l'), da.pat.FreePattern('node')])
PatternExpr_687 = da.pat.FreePattern('sender')
PatternExpr_889 = da.pat.TuplePattern([da.pat.ConstantPattern('ACCEPT'), da.pat.FreePattern('ph'), da.pat.FreePattern('l')])
PatternExpr_898 = da.pat.FreePattern('sender')
PatternExpr_969 = da.pat.TuplePattern([da.pat.ConstantPattern('ACK'), da.pat.FreePattern('node')])
PatternExpr_976 = da.pat.FreePattern('sender')
PatternExpr_1010 = da.pat.TuplePattern([da.pat.ConstantPattern('ELECTED'), da.pat.FreePattern('node')])
PatternExpr_1017 = da.pat.FreePattern('sender')
PatternExpr_1045 = da.pat.TuplePattern([da.pat.ConstantPattern('INFORM'), da.pat.FreePattern('x')])
PatternExpr_1052 = da.pat.FreePattern('sender')
PatternExpr_1096 = da.pat.TuplePattern([da.pat.ConstantPattern('OWNER'), da.pat.FreePattern('node')])
PatternExpr_1103 = da.pat.FreePattern('sender')
_config_object = {}
import sys
import math
import random

class P(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_0', PatternExpr_676, sources=[PatternExpr_687], destinations=None, timestamps=None, record_history=None, handlers=[self._P_handler_675]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_1', PatternExpr_889, sources=[PatternExpr_898], destinations=None, timestamps=None, record_history=None, handlers=[self._P_handler_888]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_2', PatternExpr_969, sources=[PatternExpr_976], destinations=None, timestamps=None, record_history=None, handlers=[self._P_handler_968]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_3', PatternExpr_1010, sources=[PatternExpr_1017], destinations=None, timestamps=None, record_history=None, handlers=[self._P_handler_1009]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_4', PatternExpr_1045, sources=[PatternExpr_1052], destinations=None, timestamps=None, record_history=None, handlers=[self._P_handler_1044]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_5', PatternExpr_1096, sources=[PatternExpr_1103], destinations=None, timestamps=None, record_history=None, handlers=[self._P_handler_1095])])

    def setup(self, hCycle, **rest_1270):
        super().setup(hCycle=hCycle, **rest_1270)
        self._state.hCycle = hCycle
        self._state.n = len(self._state.hCycle)
        self._state.m = int((2 ** math.floor(math.log(self._state.n, 2))))
        self._state.k = (self._state.m / (2 ** math.ceil(math.log(math.log(self._state.m, 2), 2))))
        self._state.state = 'candidate'
        self._state.level = 0
        self._state.phase = 1
        self._state.owner = 0
        self._state.ring = [self._state.hCycle[int(((i * self._state.k) % self._state.n))] for i in range(int(math.ceil((self._state.n / self._state.k))))]
        self._state.ringPh2 = []
        self._state.step = 0
        self._state.Received = False
        self._state.Response = 0
        self._state.done = False
        self._state.first_msg = True
        self._state.leaderid = None
        self._state.receiving_flag = False
        self._state.decided = 0
        self._state.nMsg = 0
        if (not (self._state.m == self._state.n)):
            for i in range(1, int(math.ceil((self._state.n / self._state.k)))):
                index = (- int(((i * self._state.k) % self._state.n)))
                if (not (self._state.hCycle[index] in self._state.ring)):
                    self._state.ring.append(self._state.hCycle[index])

    def run(self):
        wake_rate = 0.8
        awaken = random.random()
        if (awaken > wake_rate):
            (self._state.state == 'captured')
        if (self._state.state == 'candidate'):
            self.candidateAct()
        if ((self._state.state == 'captured') and (self._state.leaderid == None)):
            self.capturedAct()
        self.output(int(self._state.nMsg))

    def candidateAct(self):
        while ((self._state.state == 'candidate') and (self._state.phase == 1)):
            if (self._state.level >= len(self._state.ring)):
                self.send(('OWNER', self._id), to=self._state.ring)
                self._state.nMsg = (self._state.nMsg + len(self._state.ring))
                self._state.Response = 0
            else:
                self.send(('CAPTURE', 1, self._state.level, self._id), to=self._state.ring[int(((self._state.level + 1) % len(self._state.ring)))])
                self._state.nMsg = (self._state.nMsg + 1)
            self._state.Received = False
            while ((self._state.state == 'candidate') and (self._state.phase == 1) and (self._state.Received == False)):
                super()._label('_st_label_443', block=False)
                _st_label_443 = 0
                while (_st_label_443 == 0):
                    _st_label_443 += 1
                    if self._state.receiving_flag:
                        _st_label_443 += 1
                    else:
                        super()._label('_st_label_443', block=True)
                        _st_label_443 -= 1
                else:
                    if (_st_label_443 != 2):
                        continue
                if (_st_label_443 != 2):
                    break
                self._state.receiving_flag = False
        if ((self._state.state == 'candidate') and (self._state.phase == 2)):
            self._state.step = 1
            while (self._state.state == 'candidate'):
                self._state.ringPh2 = []
                for i in range(1, int(((2 ** (self._state.step - 1)) + 1))):
                    index = int((((i * self._state.k) / (2 ** self._state.step)) % self._state.n))
                    if (not (self._state.hCycle[index] in self._state.ring)):
                        self._state.ringPh2.append(self._state.hCycle[index])
                if (not (self._state.n == self._state.m)):
                    for i in range(1, int(((2 ** (self._state.step - 1)) + 1))):
                        index = (- int((((i * self._state.k) / (2 ** self._state.step)) % self._state.n)))
                        if (not (self._state.hCycle[index] in (self._state.ring + self._state.ringPh2))):
                            self._state.ringPh2.append(self._state.hCycle[index])
                self.send(('CAPTURE', 2, self._state.step, self._id), to=self._state.ringPh2)
                self._state.nMsg = (self._state.nMsg + len(self._state.ringPh2))
                self._state.Received = False
                self._state.Response = 0
                while ((self._state.state == 'candidate') and (self._state.Received == False)):
                    if (len(self._state.ringPh2) == 0):
                        self._state.step = (self._state.step + 1)
                        if (self._state.step >= (math.log(self._state.k, 2) + 1)):
                            self._state.state = 'leader'
                        break
                    super()._label('_st_label_615', block=False)
                    _st_label_615 = 0
                    while (_st_label_615 == 0):
                        _st_label_615 += 1
                        if self._state.receiving_flag:
                            _st_label_615 += 1
                        else:
                            super()._label('_st_label_615', block=True)
                            _st_label_615 -= 1
                    else:
                        if (_st_label_615 != 2):
                            continue
                    if (_st_label_615 != 2):
                        break
                    self._state.receiving_flag = False
            if (self._state.state == 'leader'):
                self.send(('ELECTED', self._id), to=self._state.hCycle)
                self._state.nMsg = (self._state.nMsg + len(self._state.hCycle))
                self._state.leaderid = self._id

    def capturedAct(self):
        self._state.done = False
        self._state.first_msg = True
        while (self._state.done == False):
            if (self._state.first_msg == True):
                self._state.state = 'captured'
                self._state.owner = 0
                self._state.phase = 1
            super()._label('_st_label_665', block=False)
            _st_label_665 = 0
            while (_st_label_665 == 0):
                _st_label_665 += 1
                if self._state.receiving_flag:
                    _st_label_665 += 1
                else:
                    super()._label('_st_label_665', block=True)
                    _st_label_665 -= 1
            else:
                if (_st_label_665 != 2):
                    continue
            if (_st_label_665 != 2):
                break
            self._state.receiving_flag = False
            self._state.first_msg = False

    def _P_handler_675(self, ph, l, node, sender):
        self._state.receiving_flag = True
        if (self._state.state == 'candidate'):
            if (self._state.phase == 1):
                if (ph == 1):
                    if ((self._state.level < l) or ((self._state.level == l) and (self._id < node))):
                        self.send(('ACCEPT', 1, self._state.level), to=sender)
                        self._state.nMsg = (self._state.nMsg + 1)
                        self._state.state = 'captured'
                    elif (self._id == node):
                        self.send(('ACCEPT', 1, self._state.level), to=sender)
                        self._state.nMsg = (self._state.nMsg + 1)
                elif (ph == 2):
                    self._state.state = 'captured'
                    self._state.phase = 2
                    self.send(('ACCEPT', 2, 0), to=sender)
                    self._state.nMsg = (self._state.nMsg + 1)
            elif (self._state.phase == 2):
                if (ph == 2):
                    if ((l > self._state.step) or ((l == self._state.step) and (node > self._id))):
                        self.send(('ACCEPT', 2, 0), to=sender)
                        self._state.nMsg = (self._state.nMsg + 1)
                        self._state.state = 'captured'
                    elif ((l == self._state.step) and (self._id == node)):
                        self.send(('ACCEPT', 2, 0), to=sender)
                        self._state.nMsg = (self._state.nMsg + 1)
        elif (self._state.state == 'captured'):
            if (ph == 1):
                if (self._state.phase == 1):
                    self.send(('ACCEPT', 1, 0), to=sender)
                    self._state.nMsg = (self._state.nMsg + 1)
            elif (ph == 2):
                if ((self._state.phase == 1) or (self._state.owner == 0)):
                    self.send(('ACCEPT', 2, 0), to=sender)
                    self._state.nMsg = (self._state.nMsg + 1)
                    self._state.phase = 2
                else:
                    self.send(('INFORM', self._state.owner), to=sender)
                    self._state.nMsg = (self._state.nMsg + 1)
    _P_handler_675._labels = None
    _P_handler_675._notlabels = None

    def _P_handler_888(self, ph, l, sender):
        self._state.receiving_flag = True
        if (self._state.state == 'candidate'):
            if ((self._state.phase == 1) and (ph == 1)):
                self._state.level = ((self._state.level + l) + 1)
                self._state.Received = True
            elif ((self._state.phase == 2) and (ph == 2)):
                self._state.Response = (self._state.Response + 1)
                if (self._state.Response >= len(self._state.ringPh2)):
                    self._state.step = (self._state.step + 1)
                    if (self._state.step >= (math.log(self._state.k, 2) + 1)):
                        self._state.state = 'leader'
                    else:
                        self._state.Received = True
    _P_handler_888._labels = None
    _P_handler_888._notlabels = None

    def _P_handler_968(self, node, sender):
        self._state.receiving_flag = True
        if ((self._state.state == 'candidate') and (self._state.phase == 1) and (node == self._id)):
            self._state.Response = (self._state.Response + 1)
            if (self._state.Response >= (len(self._state.ring) - 1)):
                self._state.phase = 2
    _P_handler_968._labels = None
    _P_handler_968._notlabels = None

    def _P_handler_1009(self, node, sender):
        self._state.receiving_flag = True
        if (self._state.state == 'candidate'):
            self._state.state = 'captured'
            self._state.leaderid = node
        elif (self._state.state == 'captured'):
            self._state.done = True
            self._state.leaderid = node
    _P_handler_1009._labels = None
    _P_handler_1009._notlabels = None

    def _P_handler_1044(self, x, sender):
        self._state.receiving_flag = True
        if ((self._state.state == 'candidate') and (self._state.phase == 2)):
            e = self._state.hCycle.index(sender)
            self.send(('CAPTURE', 2, self._state.step, self._id), to=self._state.hCycle[int(((e + x) % self._state.n))])
            self._state.nMsg = (self._state.nMsg + 1)
    _P_handler_1044._labels = None
    _P_handler_1044._notlabels = None

    def _P_handler_1095(self, node, sender):
        self._state.receiving_flag = True
        if ((self._state.state == 'captured') and (self._state.phase == 1)):
            self._state.owner = self._state.hCycle.index(node)
            self._state.phase = 2
            self.send(('ACK', node), to=sender)
            self._state.nMsg = (self._state.nMsg + 1)
        elif ((self._state.state == 'candidate') and (self._state.phase == 1) and (self._id == node)):
            self._state.owner = self._state.hCycle.index(node)
            self.send(('ACK', node), to=sender)
            self._state.nMsg = (self._state.nMsg + 1)
    _P_handler_1095._labels = None
    _P_handler_1095._notlabels = None

class Node_(da.NodeProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._events.extend([])
    _config_object = {'channel': 'fifo'}

    def run(self):
        n = (int(sys.argv[1]) if (len(sys.argv) > 1) else 16)
        ps = list(self.new(P, num=n))
        for (i, p) in enumerate(ps):
            self._setup({p}, ([ps[int(((i + j) % n))] for j in range(n)],))
        self._start(ps)
