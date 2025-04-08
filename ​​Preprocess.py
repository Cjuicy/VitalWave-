import numpy as np
from scipy.signal import savgol_filter
from scipy.interpolate import CubicSpline

# 均值滤波去高频噪声
def mean_filter(signal, window_size=5):
    return np.convolve(signal, np.ones(window_size)/window_size, mode='same')

# 基线漂移校正（三次样条插值）
def remove_baseline(signal, peaks):
    cs = CubicSpline(peaks, signal[peaks])
    baseline = cs(np.arange(len(signal)))
    return signal - baseline