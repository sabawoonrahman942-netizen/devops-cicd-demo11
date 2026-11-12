# DevOps CI/CD Projesi

Git ve GitHub Actions kullanarak temel bir CI akışını öğrenmek için hazırlanmış, Türkçe ve mobil uyumlu statik proje sayfası.

## Projeyi görüntüleme

Ek bir paket kurulumu gerekmez. Depoyu indirdikten sonra `index.html` dosyasını tarayıcıda açabilirsin. Güncel workflow durum rozeti, GitHub Actions sayfasına bağlanır.

## Depodaki dosyalar

- `index.html`: Proje sayfasının erişilebilir HTML yapısı.
- `styles.css`: Masaüstü ve telefon ekranlarına uyumlu stiller.
- `.github/workflows/ci.yml`: GitHub Actions iş akışı.

## Mevcut CI akışı

Workflow, `master` dalına push yapıldığında çalışır ve:

1. Depoyu GitHub Actions sanal makinesine indirir.
2. Dosyaları listeler.
3. `index.html` içeriğini loglara yazar.
4. Tamamlandığını bildiren bir mesaj gösterir.

Çalışma geçmişini [Actions sekmesinden](https://github.com/sabawoonrahman942-netizen/devops-cicd-demo11/actions) takip edebilirsin.

## Projenin sınırı

Bu workflow şu an HTML/CSS testi veya sunucuya dağıtım yapmaz. Sayfa statik dosyalardan oluşur ve ek servis gerektirmez.

## Katkı gönderme

1. Yeni bir dal aç.
2. Değişikliği commit et ve GitHub'a gönder.
3. `master` dalına pull request aç.
4. Birleştirilen değişiklik `master` dalına geldiğinde CI workflow'u çalışır.
