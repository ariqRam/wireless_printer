# wireless_printer
A Python script for Linux that handles wireless printing through Gmail.

## English instructions

The script receives files from Gmail. The incoming emails will be filtered by the subject, this will be the password to access your printer. Be aware of this password, and be careful on the API credentials (Client ID and Client Key), as it can control your Gmail account.

To run the script, you need all of the following,
1. Any Raspberry Pi board (with WiFi card or WiFi adapter)
2. A USB-attached printer
3. An internet connection on the Raspberry Pi board

### Steps
1. Install [CUPS](https://www.cups.org/), a printing protocol for Linux.
2. Setup your printer using CUPS, see [instructions](https://www.linux.com/training-tutorials/add-printer-linux-cups-web-utility/).
3. Setup a Google [API](https://developers.google.com/gmail/api) Application using the [Google Developer Console](https://console.developers.google.com/) and follow the instructions.
4. Download the `credentials.json` file and place it in the same directory as `script.py`.
5. Define all the optional variables (PASSWORD, SCOPE, etc.) in `script.py` (see commented codes in the script).
6. Set the `script.py` to run on startup, see [instructions](https://www.instructables.com/id/Raspberry-Pi-Launch-Python-script-on-startup/).


## Instruksi Bahasa Indonesia
Script ini menerima file melalui Gmail. Email yang masuk akan disaring berdasarkan subjek. Subjek ini akan berperan sebagai password, yang membuat email diteruskan ke printer. Berhati-hatilah akan password printer yang anda tentukan (di `script.py`), dan berhati-hatilah dalam menggunakan izin dari Gmail API, karena API ini dapat membuat script yang anda jalankan mengakses akun Gmail anda.

Untuk menjalankan script, anda memerlukan :
1. Board Raspberry Pi apapun (dengan WiFi card atau WiFi adapter)
2. Printer yang disambungkan melalui kabel USB
3. Koneksi internet pada Raspberry Pi

### Cara kerja
1. Install [CUPS](https://www.cups.org/), sebuah protokol printing pada Linux
2. Atur printer ada menggunakan CUPS, lihat [instruksi pengaturan](https://www.linux.com/training-tutorials/add-printer-linux-cups-web-utility/).
3. Atur [API](https://developers.google.com/gmail/api) Application using the [Google Developer Console](https://console.developers.google.com/) Google dan ikuti instruksi pada web tersebut.
4. Unduh file `credentials.json` dan letakan file di folder yang sama dengan file `script.py`.
5. Tentukan variabel opsional (PASSWORD, SCOPE, dll) pada  `script.py` (lihat kode yang terkomen).
6. Atur `script.py` untuk dijalankan saat startup, lihat [instruksi pengaturan](https://www.instructables.com/id/Raspberry-Pi-Launch-Python-script-on-startup/).

If there is any question please contact me on GitHub, or email me at ariqathallah38@gmail.com.
If you find this useful, please leave a star. Thank you.
