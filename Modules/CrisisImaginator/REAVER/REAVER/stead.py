import seisbench.data as sbd

'''
    Fubction to get the STEAD data with a specified sampling rate

'''
def get_stead(sampling_rate=100):
    data = sbd.STEAD(sampling_rate=sampling_rate)
    return data.train_dev_test()

