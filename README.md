# DevOps CI/CD Projesi

Git ve GitHub Actions kullanarak temel bir CI akışını öğrenmek için hazırlanmış, Türkçe ve mobil uyumlu statik proje sayfası.

## Projeyi görüntüleme

Ek bir paket kurulumu gerekmez. Depoyu indirdikten sonra `index.html` dosyasını tarayıcıda açabilirsin. Güncel workflow durum rozeti, GitHub Actions sayfasına bağlanır.

## Depodaki dosyalar

- `index.html`: Proje sayfasının erişilebilir HTML yapısı.
- `styles.css`: Masaüstü ve telefon ekranlarına uyumlu stiller.
- `.github/workflows/ci.yml`: GitHub Actions iş akışı.

## Mevcut CI akışı

Workflow, `master` dalına pull request açıldığında ve `master` dalına push yapıldığında çalışır. GitHub Actions:

1. Depoyu sanal makineye indirir.
2. Dosyaları listeler.
3. `index.html` içeriğini loglara yazar.
4. Tamamlandığını bildiren bir mesaj gösterir.

Çalışma geçmişini [Actions sekmesinden](https://github.com/sabawoonrahman942-netizen/devops-cicd-demo11/actions) takip edebilirsin.

## Projenin sınırı

Bu workflow şu an HTML/CSS testi veya sunucuya dağıtım yapmaz. CI adımları tamamlandığında iş akışı başarılı olur; bu, sayfanın gerçek bir sunucuya yayınlandığı anlamına gelmez.

## Katkı gönderme

1. Yeni bir dal aç.
2. Değişikliği commit et ve GitHub'a gönder.
3. `master` dalına pull request aç.
4. Pull request için CI workflow sonucu otomatik çalışır.
5. Birleştirme sonrası `master` dalına gelen push da workflow'u çalıştırır.
