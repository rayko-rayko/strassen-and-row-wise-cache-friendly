# Strassen ve Row-Wise Cache-Friendly Algoritmaları ile Matris Çarpımı

Bu proje, Strassen algoritması ve row-wise cache-friendly algoritmasını birleştirerek matris çarpımı gerçekleştiren bir Python uygulamasıdır. Ayrıca, günlük hayattan temizlik robotu örneği ile algoritmaların işleyişini açıklamaktadır.

## Proje İçeriği

- `strassen_rowwise.py`: Strassen algoritması ve row-wise cache-friendly matris çarpımı algoritmasını birleştiren fonksiyonlar.
- `cleaning_robot_example.py`: Temizlik robotu senaryosunu içeren günlük hayat örneği.
- `main.py`: Hem matris çarpımı hem de temizlik robotu senaryosunu çalıştıran ana dosya.

## Gereksinimler

- Python 3.x
- NumPy kütüphanesi

## Kurulum

1. Bu projeyi bilgisayarınıza klonlayın:
    ```bash
    git clone https://github.com/rayko-rayko/strassen-and-row-wise-cache-friendly
    cd strassen-and-row-wise-cache-friendly
    ```

2. Sanal ortam oluşturun ve gerekli bağımlılıkları yükleyin:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Windows için: .venv\Scripts\activate
    pip install numpy
    ```

## Kullanım

### Matris Çarpımı

Matris çarpımı için `strassen_multiply` fonksiyonunu kullanıyoruz. Bu fonksiyon, belirli bir boyutun altında olduğunda row-wise cache-friendly algoritmasını, üstünde olduğunda ise Strassen algoritmasını kullanır.

### Temizlik Robotu

Temizlik robotu senaryosu, belirli bir boyutun altında ayrıntılı, üstünde ise hızlı temizlik yapar.

### `main.py` Dosyası

`main.py` dosyasını çalıştırarak hem matris çarpımı hem de temizlik robotu senaryosunu çalıştırabilirsiniz.

```bash
python main.py
