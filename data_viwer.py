import numpy as np
import time
import matplotlib.pyplot as plt


def _show_as_film_x(image, start, end, step=1, sleep_time=1):
    for i in np.arange(start, end, step):
        plt.imshow(image[i, :, :])
        plt.title(f'high: {i}')
        plt.show(block=False)
        time.sleep(sleep_time) if sleep_time != 0 else None
        plt.close()


def _show_as_film_y(image, start, end, step=1, sleep_time=1):
    for i in np.arange(start, end, step):
        plt.imshow(image[:, i, :])
        plt.title(f'high: {i}')
        plt.show(block=False)
        time.sleep(sleep_time) if sleep_time != 0 else None
        plt.close()


def _show_as_film_z(image, start, end, step=1, sleep_time=1):
    for i in np.arange(start, end, step):
        plt.imshow(image[:, :, i])
        plt.title(f'high: {i}')
        plt.show(block=False)
        time.sleep(sleep_time) if sleep_time != 0 else None
        plt.close()


def show_as_film(image, start=0, end=180, step=1, axis='x', sleep_time=1):
    globals()['_show_as_film_' + axis](image, start, end, step, sleep_time)
