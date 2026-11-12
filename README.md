# DevOps CI/CD Projesi

Git, GitHub Actions, Flask ve SQLite ile küçük bir görev takip uygulaması. Arayüzden eklenen görevler yerel SQLite veritabanında saklanır.

## Gereksinimler

- Python 3.10 veya üzeri
- pip

## Yerel çalıştırma

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Linux veya macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Sonra tarayıcıda [http://127.0.0.1:5000](http://127.0.0.1:5000) adresini aç. Bu sunucu yerel geliştirme içindir.

## Veritabanı ve API

SQLite veritabanı ilk çalıştırmada `instance/tasks.sqlite3` konumunda oluşturulur. `instance/` klasörü Git'e eklenmez; görevler aynı makinede uygulama yeniden başlatıldığında korunur.

| İşlem | Uç nokta | Açıklama |
|---|---|---|
| GET | `/api/tasks` | Görevleri listeler |
| POST | `/api/tasks` | `{"title":"Görev adı"}` ile görev ekler |
| PATCH | `/api/tasks/<id>` | `{"completed":true}` ile tamamlanma durumunu değiştirir |
| DELETE | `/api/tasks/<id>` | Görevi siler |

Görev başlığı zorunludur ve en fazla 120 karakter olabilir. API, geçersiz JSON ve bulunmayan görevler için uygun hata kodları döndürür.

## GitHub Actions

Workflow, `master` dalına push yapıldığında ve `master` hedefli pull request açıldığında çalışır. Mevcut adımlar depoyu indirir, dosyaları listeler ve `index.html` içeriğini loglara yazar. Bu akış henüz Flask uygulamasını test etmez veya sunucuya dağıtmaz.

## Dosyalar

- `app.py`: Flask uygulaması ve JSON API
- `app.js`: Tarayıcı arayüzü ile API arasındaki bağlantı
- `index.html` ve `styles.css`: Mobil uyumlu arayüz
- `requirements.txt`: Python bağımlılığı
- `.gitignore`: Yerel ortam ve SQLite dosyalarını hariç tutar
- `.github/workflows/ci.yml`: GitHub Actions iş akışı
