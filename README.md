# Debata

Bot obsługujący debatę wyborczą w PLOPŁ, mocno zainspirowany kodem: https://github.com/michkied/PloplDlaWOSP

### Obsługa
Uzytkownicy chcący zadać pytanie, muszą zostać zweryfikowani.

Aby wysłać wiadomość do weryfikacji osób, napisz na kanale `?post`.

Aby wysłać wiadomość do weryfikacji pytań, napisz na kanale `?question`.

Pytanie zostanie wysłane na odpowiedni kanał po weryfikacji przez moderatora.

### Config
Aby bot poprawnie działał, należy poprawnie skonfigurować plik `bot/config`.
- first_alt_name i second_alt_name - imię odpowiednio pierwszego i drugiego kandydata *odmienione w dopełniaczu*
- first_candidates i second_candidates - ID roli dla Sztabu odpowiednio pierwszego i drugiego kandydata
- TOKEN - token bota
- TEACHER_KEY - klucz, który podadzą nauczyciele w celu weryfikacji
- VERIFIER_ROLE - ID roli moderatora (weryfikatora)
- AUCTION_GUILD - ID serwera
- VERIFICATION_CHANNEL - kanał na którym będą pojawiać się wiadomości o weryfikacji osób
- VERIF_QUEST_CHANNEL - kanał na którym będą pojawiać się wiadomości o weryfikacji pytań
- VERIFIED_QUESTION_CHANNEL - kanał na który będą trafiać zweryfikowane pytania
- UNVERIFIED_ROLES - lista ról niezweryfikowanych
- VERIFIED ROLES - lista ról zweryfikowanych
- TEACHERS - lista ID nauczycieli
- STUDENT_DATA - słownik danych uczniów
