# DevOps CI/CD Projesi

Bu depo, Git ve GitHub Actions kullanarak basit bir CI/CD akışını öğrenmek için hazırlanmıştır.

## Depodaki dosyalar

- `index.html`: Projede kullanılan örnek HTML sayfası.
- `.github/workflows/ci.yml`: GitHub Actions iş akışı.

## CI akışı

Workflow, `master` dalına yapılan her push işleminde çalışır. GitHub Actions:

1. Depoyu sanal makineye indirir.
2. Dosyaları listeler.
3. `index.html` içeriğini ekrana yazar.
4. Akışın tamamlandığını belirten mesajı gösterir.

Çalışma sonucunu GitHub'daki **Actions** sekmesinden görebilirsin.

## Mevcut sınır

Bu workflow şu an bir dağıtım yapmaz ve uygulamayı bir sunucuya yayınlamaz. Yalnızca depoyu indirip dosyaları gösteren temel bir CI demosudur.

## Değişiklik gönderme

1. Yeni bir dal oluştur.
2. Değişikliği bu dalda commit et.
3. GitHub'da `master` dalına bir pull request aç.
4. Pull request birleştirildikten sonra `master` dalına gelen push workflow'u başlatır.
