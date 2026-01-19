@echo off
echo ========================================
echo Script Upload ke GitHub
echo ========================================
echo.

REM Cek apakah git sudah terinstall
git --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Git belum terinstall!
    echo Download di: https://git-scm.com/download/win
    pause
    exit /b 1
)

echo [1/6] Inisialisasi Git Repository...
git init
if errorlevel 1 (
    echo Git sudah diinisialisasi sebelumnya
)
echo.

echo [2/6] Menambahkan semua file...
git add .
echo.

echo [3/6] Commit file...
git commit -m "Initial commit: Flask ML deployment app"
echo.

echo [4/6] Setup GitHub Repository
echo.
echo PENTING: Buat repository baru di GitHub terlebih dahulu!
echo 1. Buka https://github.com/new
echo 2. Beri nama repository (contoh: ml-flask-deployment)
echo 3. JANGAN centang "Initialize with README"
echo 4. Klik "Create repository"
echo.
set /p GITHUB_URL="Masukkan URL repository GitHub (contoh: https://github.com/username/repo-name.git): "

if "%GITHUB_URL%"=="" (
    echo ERROR: URL tidak boleh kosong!
    pause
    exit /b 1
)

echo.
echo [5/6] Menghubungkan dengan GitHub...
git remote remove origin >nul 2>&1
git remote add origin %GITHUB_URL%
echo.

echo [6/6] Push ke GitHub...
git branch -M main
git push -u origin main

if errorlevel 1 (
    echo.
    echo ERROR: Push gagal!
    echo Kemungkinan penyebab:
    echo - URL repository salah
    echo - Belum login ke GitHub
    echo - Repository sudah ada isinya
    echo.
    echo Coba login dulu dengan: git config --global user.name "Nama Kamu"
    echo                         git config --global user.email "email@kamu.com"
    pause
    exit /b 1
)

echo.
echo ========================================
echo SUCCESS! Project berhasil di-upload ke GitHub!
echo ========================================
echo.
echo URL Repository: %GITHUB_URL%
echo.
pause
