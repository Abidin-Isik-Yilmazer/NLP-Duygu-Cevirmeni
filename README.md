# 🧠 NLP Duygu Analizi ve Çeviri Aracı 

Bu proje, İngilizce metinlerin duygu durumunu (Sentiment) analiz eden, Türkçeye çeviren ve metni kelime kelime ayrıştırarak detaylı lügat analizi sunan masaüstü tabanlı bir Doğal Dil İşleme (NLP) uygulamasıdır. 

Modern, asenkron ve kullanıcı dostu bir arayüz ile yapay zeka gücünü tek bir platformda birleştirir.

## 🚀 Makine Öğrenmesi & Sistem Mimarisi

Sistemin NLP arka planı **Hugging Face Transformers** altyapısı üzerine inşa edilmiştir.

* **Kullanılan Model:** `distilbert-base-uncased-finetuned-sst-2-english`
* **Görev Tipi:** Binary Text Classification (İkili Metin Sınıflandırma)
* **Çalışma Prensibi:** SST-2 veri seti üzerinde ince ayar (fine-tuning) yapılmış DistilBERT modeli, girilen metnin ağırlıklarını hesaplayarak metni *POSITIVE* (Olumlu) veya *NEGATIVE* (Olumsuz) olarak sınıflandırır.
* **Güven Skoru (Confidence Score):** Çıktı katmanından alınan ham veriler (logits), softmax fonksiyonundan geçirilerek modelin tahminine dair istatistiksel bir güven skoru (%0-100) üretir.
* **Akıllı Tokenizasyon:** Girdi metni noktalama işaretlerinden arındırılır, eşsiz kelime parçalarına (token) ayrılır ve asenkron çeviri işlemi ile detaylı bir çıktı matrisi oluşturulur.

## 🛠️ Kullanılan Teknolojiler ve Kütüphaneler

* **Python 3.x:** Çekirdek programlama dili.
* **PyTorch & Transformers:** Derin öğrenme altyapısı ve NLP pipeline yönetimi.
* **CustomTkinter:** Karanlık tema destekli, modern grafik kullanıcı arayüzü (GUI).
* **Deep-Translator:** Kelime parçalama, asenkron ve batched (gruplanmış) API çeviri işlemleri.
* **Threading:** Arayüz (UI) kilitlenmelerini önlemek amacıyla ağır işlemlerin arka plan işçilerine devredilmesi.

## 🏗️ Proje Mimarisi (OOP Modüler Yapı)

Proje, sürdürülebilirlik ve temiz kod (Clean Code) prensipleri gözetilerek **Nesne Yönelimli Programlama (OOP)** standartlarında sınıflara (class) bölünmüş modüler bir yapıda tasarlanmıştır:

* **`analyzer.py`:** NLP modellerinin (DistilBERT) yüklenmesi, duygu analizi çıkarımları ve asenkron çeviri gibi arka plan (backend) işlemlerini ve mantıksal operasyonları kapsülleyen analiz sınıfını içerir.
* **`gui.py`:** CustomTkinter kullanılarak tasarlanmış modern grafik kullanıcı arayüzü (frontend) sınıfını barındırır. Kullanıcı etkileşimlerini, buton olaylarını ve çıktıların görselleştirilmesini yönetir.
* **`main.py`:** Uygulamanın ana giriş noktasıdır. Arayüz (GUI) ve analiz (Analyzer) nesnelerini örnekleyip bir araya getirerek uygulamanın uyum içinde çalışmasını başlatır.

## ⚙️ Kurulum ve Çalıştırma

**1. Projeyi Klonlayın:**

```bash
git clone https://github.com/Abidin-Isik-Yilmazer/NLP-Duygu-Cevirmeni.git
```

**2. Proje Klasörüne Girin:**

```bash
cd NLP-Duygu-Cevirmeni
```

**3. Gerekli Kütüphaneleri Yükleyin:**

```bash
pip install transformers torch deep-translator customtkinter opencv-python pytesseract
```

**4. Uygulamayı Başlatın:**

```bash
python main.py
```

*(Önemli Not: Uygulama ilk kez çalıştırıldığında DistilBERT modeli Hugging Face sunucularından indirileceği için kısa bir süre bekletebilir. Sonraki kullanımlarda model önbellekten (cache) anında yüklenecektir.)*

