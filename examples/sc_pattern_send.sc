s.boot;

(
NetAddr.broadcastFlag = true;
~netaddr = NetAddr("192.168.1.255", 12345);


~sender = {|oscname, ev|
        ev.postln;
        ~netaddr.sendMsg(oscname,ev[\note],ev[\vel],ev[\sustain]);

};

TempoClock.default.tempo = 1.5;

p = Pbind(
        \note, Pn(Pseries(40, 5, 3), inf),
        \dur, Pn(Pgauss(0.25,0.05),inf),
        \vel, Pn(Pseries(60,10,4),inf),
        \sustain, 100,
        \sender, Pfunc({|ev| ~sender.value("/notas1",ev)}),
        ).play;

)

p.free;
p.stop;
p.start;
