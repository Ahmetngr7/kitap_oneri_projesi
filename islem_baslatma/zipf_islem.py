import subprocess
import datetime
import os

def calistir(dosya_adi, log_adi):
    log_klasoru = "ciktilar/zipf_dosyaları"
    os.makedirs(log_klasoru, exist_ok=True)

    zaman_damgasi = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_yolu = os.path.join(log_klasoru, f"{log_adi}_{zaman_damgasi}.log")

    print(f"{dosya_adi} çalıştırılıyor... (log: {log_yolu})")

    with open(log_yolu, "w") as log_dosyasi:
        process = subprocess.Popen(
            ["python", dosya_adi],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
        for satir in process.stdout:
            print(satir, end="")
            log_dosyasi.write(satir)
        process.wait()

        if process.returncode == 0:
            print(f"{dosya_adi} başarıyla tamamlandı.\n")
        else:
            print(f"HATA: {dosya_adi} çalıştırılırken hata oluştu! ({process.returncode})")

if __name__ == "__main__":
    calistir("code/zipf_code/zipf_lema.py", "lema_log")
    calistir("code/zipf_code/zipf_stem.py", "stem_log")
