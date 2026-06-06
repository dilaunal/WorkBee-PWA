import os
from PIL import Image

# Orijinal logonun adı
original_logo = "WorkBeeAppIcon.png"


def resize_image():
    if not os.path.exists(original_logo):
        print(
            f"❌ Hata: Klasörün içinde '{original_logo}' adında bir dosya bulunamadı!"
        )
        print("Lütfen arı logonu bu klasöre atıp kodu tekrar çalıştır.")
        return

    try:
        # Resmi açıyoruz
        img = Image.open(original_logo)

        # 192x192 boyutunda kaydet
        img_192 = img.resize((192, 192), Image.Resampling.LANCZOS)
        img_192.save("icon-192.png", "PNG")
        print("✅ icon-192.png başarıyla oluşturuldu.")

        # 512x512 boyutunda kaydet
        img_512 = img.resize((512, 512), Image.Resampling.LANCZOS)
        img_512.save("icon-512.png", "PNG")
        print("✅ icon-512.png başarıyla oluşturuldu.")

    except Exception as e:
        print(f"❌ Bir hata oluştu: {e}")


if __name__ == "__main__":
    resize_image()