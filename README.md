Proje Adı: Ürün Yerleştirme Tahmin Sistemi

Proje Hakkında
Bu proje, bir süpermarkette ürünlerin birlikte yerleştirilip yerleştirilmeyeceğini tahmin eden bir Flask uygulamasıdır. İki ürünün Rating (puan) farkına göre, ürünlerin birlikte yerleştirilip yerleştirilemeyeceği belirlenir. Ayrıca, kullanıcıya bu farkı görsel olarak sunan bir progress bar bulunmaktadır.

Kurulum ve Çalıştırma

1. Gereksinimler
   - Python 3.x
   - Flask
   - Pandas
   - Scikit-learn
   - Bootstrap (HTML şablonları için)

2. Gereksinimlerin Yüklenmesi

   Projeyi çalıştırmadan önce gerekli Python kütüphanelerini yüklemeniz gerekiyor. Proje dizininde bir sanal ortam oluşturup gerekli kütüphaneleri yükleyebilirsiniz:

   python -m venv venv
   source venv/bin/activate  # Windows kullanıcıları için: venv\Scripts\activate
   pip install -r requirements.txt

   requirements.txt dosyanız yoksa, aşağıdaki komutla bağımlılıkları yükleyin:

   pip install flask pandas scikit-learn

3. Veri Seti

   Projede kullanılan veri seti supermarket_sales.csv adındaki dosyada bulunmaktadır. Bu dosyanın projenin kök dizininde bulunduğundan emin olun.

4. Projeyi Çalıştırma

   Flask uygulamasını çalıştırmak için terminalde aşağıdaki komutu çalıştırın:

   python app.py

   Uygulama başarıyla çalıştırıldıktan sonra tarayıcınızda http://127.0.0.1:5000/ adresini ziyaret edebilirsiniz.

5. Kullanım

   - İki ürünü seçin.
   - "Tahmin Et" butonuna tıklayın.
   - Ürünlerin birlikte yerleştirilip yerleştirilemeyeceğini öğrenin.
   - İki ürün arasındaki rating farkına göre bir progress bar (güçlü bağ - zayıf bağ) ekranda gösterilecektir.

Proje Yapısı

- app.py: Flask uygulamasını ve tüm işlevleri barındırır.
- templates/: HTML dosyalarının bulunduğu dizin.
  - index.html: Ana sayfa, kullanıcı formu ve sonuçlar.
  - progress.html: Sonuçları ve progress bar'ı gösteren sayfa.
- supermarket_sales.csv: Ürün satış verilerinin bulunduğu veri seti.
- static/: CSS ve diğer statik dosyalar (Bootstrap, JS vs.).

Geliştirici Notları

- Flask uygulamasını geliştirirken debug=True olarak ayarlandığında, değişiklikler otomatik olarak yenilenir.
- Veri seti analizleri için Python ve Pandas kullanılmıştır.
- Ürünler arasındaki ilişkiler Logistic Regression modeli ile analiz edilmiştir.

İletişim

Herhangi bir sorun veya öneri için iletişime geçmekten çekinmeyin.

