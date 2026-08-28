import gzip
import struct
import numpy as np

def load_mnist_images(path):
    """MNISTのデータセットから画像を取り出す．

    Args:
        path (string): MNISTのデータセットのパス

    Returns:
        np.ndarray: 画像を格納した配列
    """
    with gzip.open(path, "rb") as f:
        magic, num, rows, cols = struct.unpack(">IIII", f.read(16))
        images = np.frombuffer(f.read(), dtype=np.uint8)
        images = images.reshape(num, rows, cols)
    return images


def load_mnist_labels(path):
    """MNISTのデータセットからラベルを取り出す．

    Args:
        path (string): MNISTのデータセットのパス

    Returns:
        np.ndarray: ラベルを格納した配列
    """
    with gzip.open(path, "rb") as f:
        magic, num = struct.unpack(">II", f.read(8))
        labels = np.frombuffer(f.read(), dtype=np.uint8)
    return labels
