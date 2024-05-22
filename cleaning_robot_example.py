# Bu script, temizlik robotu senaryosunu içeren günlük hayat örneğini içerir.
#
# İçerdiği Sınıflar ve Fonksiyonlar:
#
# 1. CleaningRobot:
#    - Açıklama: Bu sınıf, bir temizlik robotunu temsil eder. Robot, belirli bir eşik değere göre ayrıntılı veya hızlı temizlik yapar.
#    - Özellikler:
#        - threshold: Temizlik türünü belirlemek için kullanılan eşik değer (metrekare cinsinden).
#
# 2. clean_room(self, room_size):
#    - Açıklama: Bu fonksiyon, verilen oda boyutuna göre temizlik yapar. Oda boyutu eşik değerin altında ise ayrıntılı temizlik, üstünde ise hızlı temizlik yapılır.
#    - Girdi: room_size (metrekare cinsinden oda boyutu).
#    - Çıktı: Temizlik işlemi hakkında açıklayıcı bir çıktı verir.
#
# Bu script, temizlik robotunun farklı boyutlardaki odalarda nasıl çalıştığını simüle ederek algoritmaların çalışma mantığını açıklar.
# Eşik değeri (20 m²) altında olan odalar için ayrıntılı temizlik, üstündeki odalar için ise hızlı temizlik uygulanır.
# Bu senaryo, günlük hayatta karşılaşılan bir durumu basit bir şekilde modellemektedir.


class CleaningRobot:
    def __init__(self, threshold=20):
        """
        Temizlik robotu, odaların büyüklüğüne göre farklı temizlik yöntemleri kullanır.
        threshold: Küçük ve büyük odaları ayıran eşik değeri (metrekare cinsinden).
        """
        self.threshold = threshold

    def detailed_cleaning(self, room_size):
        """
        Küçük odalar için ayrıntılı temizlik yöntemi.
        room_size: Odanın büyüklüğü (metrekare cinsinden).
        """
        print(f"Ayrıntılı temizlik yapılıyor. Oda boyutu: {room_size} m²")
        # Ayrıntılı temizlik işlemleri burada tanımlanabilir
        # Örneğin, her köşeyi ve yüzeyi ayrı ayrı temizleme
        # ...

    def quick_cleaning(self, room_size):
        """
        Büyük odalar için hızlı temizlik yöntemi.
        room_size: Odanın büyüklüğü (metrekare cinsinden).
        """
        print(f"Hızlı temizlik yapılıyor. Oda boyutu: {room_size} m²")
        # Hızlı temizlik işlemleri burada tanımlanabilir
        # Örneğin, geniş alanları hızlıca temizleme
        # ...

    def clean_room(self, room_size):
        """
        Oda boyutuna göre uygun temizlik yöntemini seçer ve uygular.
        room_size: Odanın büyüklüğü (metrekare cinsinden).
        """
        if room_size <= self.threshold:
            print(
                f"Oda boyutu {room_size} m². Bu boyut {self.threshold} m² eşik değerinin altında olduğu için ayrıntılı temizlik yöntemi seçildi.")
            self.detailed_cleaning(room_size)
        else:
            print(
                f"Oda boyutu {room_size} m². Bu boyut {self.threshold} m² eşik değerinin üstünde olduğu için hızlı temizlik yöntemi seçildi.")
            self.quick_cleaning(room_size)


if __name__ == "__main__":
    robot = CleaningRobot(threshold=20)

    # Farklı boyutlardaki odalar için temizlik yap
    room_sizes = [10, 25, 15, 30]  # Örnek oda boyutları
    for size in room_sizes:
        robot.clean_room(size)