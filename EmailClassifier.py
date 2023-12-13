# @osmanmuratgull
email_memory = {}
non_spam_domains = ["@gmail.com", "@hotmail.com", "@outlook.com"]

while True:
    email = input("E-posta adresini girin (Çıkmak için 'exit' yazın): ")

    if email.lower() == "exit":
        break

    if email not in email_memory:
        email_memory[email] = 1
    else:
        email_memory[email] += 1

    if any(domain in email for domain in non_spam_domains):
        print("Bu e-posta spam değil.")
    elif email.startswith("noreply@"):
        print("Bu e-posta reklam olabilir.")
    else:
        print("Bu e-posta spam olabilir.")

while True:
    print("\n1 - Spam Olmayan E-postaları Göster")
    print("2 - Spam Olan E-postaları Göster")
    print("3 - Reklam E-postaları Göster")
    print("4 - Uygulamadan Çık")

    choice = input("Seçiminizi yapın: ")

    if choice == "1":
        for email in email_memory:
            if any(domain in email for domain in non_spam_domains):
                print(email)
    elif choice == "2":
        for email in email_memory:
            if all(domain not in email for domain in non_spam_domains) and not email.startswith("noreply@"):
                print(email)
    elif choice == "3":
        for email in email_memory:
            if email.startswith("noreply@"):
                print(email)
    elif choice == "4":
        break
    else:
        print("Geçersiz seçim.")
