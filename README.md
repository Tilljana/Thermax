# Machine Learning Deployment

Aplikasi web untuk deployment model machine learning menggunakan Flask.

## Fitur
- Model prediksi menggunakan Logistic Regression
- REST API dengan Flask
- Deploy-ready untuk Vercel

## Teknologi
- Python 3.x
- Flask
- Scikit-learn
- NumPy

## Instalasi Lokal

1. Clone repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Jalankan aplikasi:
```bash
python app.py
```

## Deploy ke Vercel

1. Install Vercel CLI:
```bash
npm i -g vercel
```

2. Deploy:
```bash
vercel
```

## Struktur Project
```
.
├── app.py              # Aplikasi Flask utama
├── model/              # Folder model ML
│   ├── trained_logreg_model.pkl
│   └── scaler.pkl
├── templates/          # HTML templates
│   └── index.html
├── requirements.txt    # Python dependencies
├── vercel.json        # Konfigurasi Vercel
└── Procfile           # Konfigurasi deployment
```

## License
MIT
