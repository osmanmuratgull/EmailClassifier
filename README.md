# Email Classifier

Bu basit bir e-posta sınıflandırma uygulamasıdır. Kullanıcıdan e-posta adresleri alır, bunları bir veri yapısında saklar ve daha sonra kullanıcının seçimine göre e-postaları farklı kategorilere ayırır.

## Kullanım

1. Uygulama çalıştırıldığında, kullanıcıdan e-posta adresleri alınır ve sınıflandırılır.
2. Kullanıcı daha sonra aşağıdaki seçeneklerden birini seçerek e-postaları filtreleyebilir:
    - Spam Olmayan E-postaları Göster
    - Spam Olan E-postaları Göster
    - Reklam E-postaları Göster
    - Uygulamadan Çık

## Nasıl Çalışır?

- Kullanıcıdan alınan e-posta adresleri, bir sözlükte saklanır.
- E-postalar, belirli kriterlere göre sınıflandırılır:
    - Belirli alanlar içeren e-postalar spam olmayabilir.
    - "noreply@" ile başlayanlar reklam olabilir.
    - Diğer durumlarda e-postalar spam olarak işaretlenir.
