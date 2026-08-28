#ifndef LOAD_MNIST_HPP
#define LOAD_MNIST_HPP

#include <string>
#include <vector>
#include <cstdint>

/**
 * @brief MNISTのデータセットから画像を取り出す．
 *
 * @param path MNISTのデータセットのパス
 * @param rows_image データセットの画像の高さ
 * @param cols_image データセットの画像の幅
 * @param images 画像を格納した配列
 */
void load_mnist_images(const std::string &path,
                       int &rows_image,
                       int &cols_image,
                       std::vector<std::vector<uint8_t>> &images);

/**
 * @brief MNISTのデータセットからラベルを取り出す．
 *
 * @param path MNISTのデータセットのパス
 * @param labels ラベルを格納した配列
 */
void load_mnist_labels(const std::string &path,
                       std::vector<uint8_t> &labels);

#endif
