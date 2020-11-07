import numpy as np

def toSent(*args, **kwargs):
    print(args[0])
    peep, bpm, t_apn = kwargs['peep'], kwargs['bpm'], kwargs['t_apn']
    print("PEEP: " + str(peep))
    print("bpm: " + str(bpm))
    print("t_apn: " + str(t_apn))
    with open('test.txt', 'wb') as outfile:
        for data_slice in args[0]:
            np.savetxt(outfile, data_slice, fmt='%4.1f')


#y = np.array([1,2,3,4])[..., np.newaxis]
#toSent(y, peep=5, bpm=5, t_apn=2)