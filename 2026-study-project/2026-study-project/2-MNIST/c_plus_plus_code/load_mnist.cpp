#include <iostream>
#include <fstream>
#include <zlib.h>
#include <cstring>

#include "load_mnist.hpp"

// 色空間のサイズ gray scaleなので1
constexpr int COLOR_SPACE_SIZE = 1;

void load_mnist_images(const std::string &path,
                       int &rows_image,
                       int &cols_image,
                       std::vector<std::vector<uint8_t>> &images)
{
    gzFile fp = gzopen(path.data(), "rb");
    if (!fp)
    {
        throw std::runtime_error("Failed to open file.");
    }
    // 先頭16Byteからmagic, 画像数, 画像のrows, 画像のcolsを取得
    uint8_t *buf = new uint8_t[16];
    gzread(fp, buf, 16);

    uint32_t *magic_num_rows_cols = new uint32_t[4];

    // ビッグエンディアンをリトルエンディアンに変換
    for (int i = 0; i < 4; i++)
    {
        magic_num_rows_cols[i] = (uint32_t(buf[i * 4 + 0]) << 24) |
                                 (uint32_t(buf[i * 4 + 1]) << 16) |
                                 (uint32_t(buf[i * 4 + 2]) << 8) |
                                 uint32_t(buf[i * 4 + 3]);
    }

    const uint32_t &num = magic_num_rows_cols[1];
    rows_image = magic_num_rows_cols[2];
    cols_image = magic_num_rows_cols[3];

    // 画像1枚あたりの大きさ
    const uint32_t image_size = rows_image * cols_image * COLOR_SPACE_SIZE;

    // 画像のメモリ確保
    images.resize(num);

    for (int i = 0; i < num; i++)
    {
        // 画像のメモリ確保
        images[i].resize(image_size);
        gzread(fp, images[i].data(), image_size);
    }

    // メモリの解放処理
    delete buf;
    delete magic_num_rows_cols;
    gzclose(fp);
}

void load_mnist_labels(const std::string &path,
                       std::vector<uint8_t> &labels)
{
    gzFile fp = gzopen(path.data(), "rb");
    if (!fp)
    {
        throw std::runtime_error("Failed to open file.");
    }
    // 先頭8Byteからmagic, ラベル数
    uint8_t *buf = new uint8_t[8];
    gzread(fp, buf, 8);

    uint32_t *magic_num = new uint32_t[2];

    // ビッグエンディアンをリトルエンディアンに変換
    for (int i = 0; i < 2; i++)
    {
        magic_num[i] = (uint32_t(buf[i * 4 + 0]) << 24) |
                                 (uint32_t(buf[i * 4 + 1]) << 16) |
                                 (uint32_t(buf[i * 4 + 2]) << 8) |
                                 uint32_t(buf[i * 4 + 3]);
    }

    const uint32_t &num = magic_num[1];
    labels.resize(num);

    for (int i = 0; i < num; i++)
    {
        gzread(fp, &labels[i], sizeof(uint8_t));
    }

    // メモリの解放処理
    delete buf;
    delete magic_num;
    gzclose(fp);
}
