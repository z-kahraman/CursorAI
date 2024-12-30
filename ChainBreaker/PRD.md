# Zinciri Kırma (ChainBreaker) - Product Requirements Document

## 1. Ürün Genel Bakış
Zinciri Kırma, kullanıcıların kötü alışkanlıklarını takip edip bunları kırmasına yardımcı olan, aynı zamanda iyi alışkanlıklar geliştirmelerini destekleyen bir mobil uygulamadır.

## 2. Hedef Kitle
- Kötü alışkanlıklarından kurtulmak isteyenler
- Yeni ve iyi alışkanlıklar edinmek isteyenler
- Kişisel gelişimine önem verenler
- 16-65 yaş arası kullanıcılar

## 3. Teknik Gereksinimler

### 3.1 Platform Gereksinimleri
- **iOS Platformu:**
  - iOS 14.0 ve üzeri
  - Swift 5.0
  - SwiftUI
  - Core Data

- **Android Platformu:**
  - Android 8.0 (API level 26) ve üzeri
  - Kotlin
  - Jetpack Compose
  - Room Database

### 3.2 Backend Gereksinimleri
- Firebase
  - Authentication
  - Realtime Database
  - Cloud Storage
  - Analytics
  - Crashlytics

### 3.3 Depolama
- Yerel veritabanı (Core Data/Room)
- Cloud storage (kullanıcı verileri için)
- Çevrimdışı çalışma desteği

## 4. Temel Özellikler

### 4.1 Kullanıcı Yönetimi
- Kayıt ve giriş sistemi
- Profil yönetimi
- Tercihler ve ayarlar
- Bildirim yönetimi

### 4.2 Alışkanlık Takibi
- Alışkanlık oluşturma ve düzenleme
- Günlük, haftalık, aylık hedefler
- İlerleme takibi ve istatistikler
- Başarı rozetleri ve ödüller

### 4.3 Sosyal Özellikler
- Arkadaş ekleme
- Başarı paylaşımı
- Grup hedefleri
- Motivasyon mesajları

### 4.4 Analiz ve Raporlama
- Detaylı istatistikler
- İlerleme grafikleri
- Başarı oranları
- Kişiselleştirilmiş öneriler

## 5. Kullanıcı Arayüzü

### 5.1 Ana Ekranlar
1. **Dashboard**
   - Günlük hedefler
   - Hızlı eylemler
   - İlerleme özeti

2. **Alışkanlık Listesi**
   - Aktif alışkanlıklar
   - Tamamlanan alışkanlıklar
   - Kategori filtreleme

3. **İstatistikler**
   - Grafikler ve analizler
   - Başarı oranları
   - Zaman çizelgeleri

4. **Profil**
   - Kullanıcı bilgileri
   - Başarı rozetleri
   - Arkadaş listesi

### 5.2 Tasarım Prensipleri
- Material Design 3 / iOS Human Interface Guidelines
- Koyu/Açık tema desteği
- Erişilebilirlik standartlarına uygunluk
- Responsive tasarım

## 6. Güvenlik Gereksinimleri
- Güvenli kimlik doğrulama
- Veri şifreleme
- GDPR uyumluluğu
- Düzenli yedekleme

## 7. Performans Gereksinimleri
- Uygulama başlatma süresi < 2 saniye
- Akıcı animasyonlar (60 FPS)
- Düşük internet kullanımı
- Optimize edilmiş pil tüketimi

## 8. Geliştirme Aşamaları

### Faz 1: Temel Özellikler
- Kullanıcı yönetimi
- Temel alışkanlık takibi
- Yerel veritabanı entegrasyonu
- Basit istatistikler

### Faz 2: Gelişmiş Özellikler
- Cloud senkronizasyon
- Detaylı istatistikler
- Bildirim sistemi
- Başarı rozetleri

### Faz 3: Sosyal Özellikler
- Arkadaş sistemi
- Grup hedefleri
- Sosyal paylaşım
- Liderlik tablosu

## 9. Test Gereksinimleri
- Unit testler
- UI testleri
- Entegrasyon testleri
- Beta testing süreci

## 10. Gelecek Özellikler
- AI destekli öneriler
- Sağlık uygulamaları entegrasyonu
- Gelişmiş veri analizi
- Çoklu dil desteği

## 11. Yasal Gereksinimler
- Gizlilik politikası
- Kullanım şartları
- Veri saklama politikası
- App Store ve Play Store gereksinimleri 