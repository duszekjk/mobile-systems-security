#slide 1
## layout
title
## slide title
Hasło w systemie mobilnym
## subtitle
Nie tylko login do usługi, lecz element większego łańcucha zaufania
## teleprompter:
W klasycznym ujęciu hasło bywa przedstawiane jako prosty sekret wpisywany w formularzu logowania. W praktyce systemów mobilnych to zbyt ubogi model. Hasło użytkownika może uruchamiać proces uwierzytelnienia do usługi sieciowej, może być materiałem wejściowym do funkcji wyprowadzania klucza, może otwierać drogę do odszyfrowania lokalnych danych, może uczestniczyć w odzyskiwaniu dostępu do konta, a czasem współistnieje z biometrią, PIN-em urządzenia, tokenem odświeżającym i kluczem sprzętowym. To oznacza, że bezpieczeństwa haseł nie da się analizować w oderwaniu od architektury całego systemu. W systemie mobilnym mamy aplikację, backend, mechanizmy platformowe, kopie zapasowe, synchronizację między urządzeniami i procesy odzyskiwania konta. Błąd w dowolnym z tych miejsc może osłabić sens nawet poprawnie zaprojektowanego hashowania po stronie serwera. Dlatego ten wykład traktuje hasło nie jako pojedynczy obiekt zapisany w bazie, lecz jako jeden z najsłabszych, ale wciąż bardzo ważnych sekretów w większym układzie zależności technicznych i operacyjnych.

#slide 2
## layout
bullet
## slide title
Dlaczego samo „silne hasło” nie rozwiązuje problemu
## bullets
- Hasło jest zwykle sekretem o niskiej lub średniej entropii
- Użytkownicy powtarzają hasła między usługami
- O bezpieczeństwie decyduje także reset, backup, migracja i sesja
- Wyciek po stronie serwera lub klienta zmienia model ataku
## teleprompter:
Dobre hasło pomaga, ale nie rozwiązuje problemu systemowo. Nawet jeśli użytkownik wybierze hasło lepsze niż przeciętne, wciąż pozostaje ono sekretem zapamiętywanym przez człowieka, a więc zwykle znacznie słabszym od losowego klucza kryptograficznego. Dochodzi do tego zjawisko ponownego użycia haseł w wielu usługach, co otwiera drogę do credential stuffing. Poza tym samo logowanie to tylko fragment pełnego przepływu bezpieczeństwa. Trzeba jeszcze uwzględnić zmianę hasła, reset, odzyskiwanie dostępu po utracie telefonu, działanie tokenów sesyjnych, zachowanie aplikacji po reinstalacji oraz relację między danymi lokalnymi a danymi zdalnymi. W praktyce często nie przegrywa sam formularz logowania, tylko otoczenie tego formularza. Z tego powodu dojrzała analiza haseł nie zaczyna się od pytania, czy użytkownik użył ośmiu czy szesnastu znaków, lecz od pytania, jaką wartość dla napastnika ma przejęcie danego konta i które elementy architektury dają najtańszą drogę do tego celu.

#slide 3
## layout
definition
## term
Hasło użytkownika, PIN urządzenia, klucz kryptograficzny
## definition
Trzy różne byty o innym pochodzeniu, innej entropii, innym modelu użycia i innym miejscu w architekturze bezpieczeństwa.
## teleprompter:
Bardzo częstym błędem pojęciowym jest mieszanie trzech różnych kategorii sekretu. Hasło użytkownika jest sekretem zapamiętywanym przez człowieka i z tej przyczyny ma ograniczoną siłę. PIN urządzenia jest zwykle krótszy, ale osadzony w innym modelu obrony, bo może korzystać z liczników prób, opóźnień, blokad i ochrony sprzętowej urządzenia. Klucz kryptograficzny to z kolei materiał losowy, projektowany nie do zapamiętywania, lecz do wykonywania operacji kryptograficznych. Jeżeli te trzy rzeczy traktuje się jako równoważne, bardzo łatwo popełnić błąd architektoniczny. Przykładowo hasło użytkownika nie powinno być traktowane jak gotowy klucz szyfrujący, a PIN urządzenia nie powinien być automatycznie utożsamiany z sekretem przechowywanym przez aplikację. Różnica między tymi bytami jest kluczowa dla dalszej części wykładu, bo od niej zależy, czy lokalnie przechowujemy właściwy obiekt, czy tylko jego pochodną, i czy aplikacja w ogóle musi znać dany sekret po zakończeniu uwierzytelnienia.

#slide 4
## layout
bullet
## slide title
Gdzie w systemie mobilnym realnie występują sekrety
## bullets
- w bazie uwierzytelniania po stronie serwera
- w pamięci procesu aplikacji podczas logowania
- w tokenach sesyjnych i odświeżających
- w lokalnym magazynie systemowym lub w backupie
## teleprompter:
Gdy mówi się o przechowywaniu haseł, intuicja wielu osób od razu biegnie do tabeli użytkowników w bazie danych. To tylko część obrazu. Sekret pojawia się również w pamięci procesu w chwili logowania, może zostać przekształcony w token sesyjny, może służyć do odblokowania klucza lokalnego, może pośrednio wpływać na dane synchronizowane między urządzeniami, a jego skutki bezpieczeństwa mogą być widoczne jeszcze długo po samym logowaniu. W aplikacji mobilnej bardzo ważne jest rozróżnienie między sekretem użytkownika, sekretem urządzenia, tokenem reprezentującym sesję i kluczem przechowywanym przez platformę. Te obiekty mają inną żywotność i inny poziom wrażliwości. Niektóre powinny istnieć tylko chwilowo, inne powinny być nieeksportowalne, a jeszcze inne nie powinny nigdy trafiać do trwałego storage aplikacji. Dopiero po rozrysowaniu tych miejsc można sensownie oceniać, czy projekt przechowywania haseł jest rozsądny.

#slide 5
## layout
bullet
## slide title
Pełna powierzchnia ataku
## bullets
- serwer uwierzytelniania
- aplikacja mobilna i jej pamięć
- urządzenie oraz jego mechanizmy ochrony
- kopia zapasowa, synchronizacja i odzyskiwanie konta
## teleprompter:
W systemach mobilnych przejęcie konta nie musi zaczynać się od ataku na formularz logowania. Napastnik może celować w bazę hashy po stronie serwera, może przechwytywać artefakty z pamięci aplikacji, może wykorzystać słabe praktyki lokalnego przechowywania, może nadużyć procesu przywracania danych na nowe urządzenie, a może też zaatakować procedurę odzyskiwania dostępu. Android oficjalnie dokumentuje mechanizmy backupu danych aplikacji, a Apple opisuje ochronę danych keychainu oraz znaczenie synchronizacji i odzyskiwania, co pokazuje, że granice systemu nie kończą się na samym urządzeniu. Dlatego poprawna analiza ryzyka musi obejmować nie tylko serwer, ale także klienta mobilnego, właściwości platformy i operacje wykonywane poza codziennym logowaniem. W praktyce to właśnie pełna powierzchnia ataku decyduje, czy dane rozwiązanie jest odporne, czy tylko pozornie poprawne. citeturn272103search0turn272103search1turn272103search9

#slide 6
## layout
definition
## term
Atak online i atak offline
## definition
Atak online wymaga interakcji z żywym systemem uwierzytelniania; atak offline wykorzystuje pozyskany materiał, na przykład bazę hashy, bez dalszego udziału systemu ofiary.
## teleprompter:
To rozróżnienie jest absolutnie podstawowe. Atak online odbywa się przeciwko działającemu systemowi, a więc napastnik napotyka limity prób, blokady, monitoring, CAPTCHA, wykrywanie anomalii i inne mechanizmy operacyjne. Atak offline wygląda inaczej. Gdy napastnik pozyska materiał do analizy, na przykład bazę hashy haseł, może prowadzić zgadywanie bez kontaktu z systemem ofiary i bez ograniczeń narzucanych przez jego politykę logowania. W klasycznym opisie ataku słownikowego Handbook of Applied Cryptography wskazuje właśnie taki scenariusz: przechowywanie obrazu niezabezpieczonej funkcji skrótu i porównywanie go z listą prawdopodobnych haseł. Z punktu widzenia ochrony haseł przejście z modelu online do offline jest momentem zmiany reguł gry, bo od tej chwili obrona nie opiera się już na blokowaniu sesji, tylko na tym, jak kosztowne jest pojedyncze sprawdzenie kandydata. fileciteturn12file8

#slide 7
## layout
title
## slide title
Dlaczego wyciek hashy zmienia reguły gry
## subtitle
Po wycieku przeciwnik przestaje pytać system i zaczyna liczyć sam
## teleprompter:
Dopóki napastnik musi próbować haseł przez publiczny interfejs logowania, system może reagować: spowalniać, blokować, wymagać dodatkowego czynnika, alarmować. Gdy jednak dojdzie do wycieku materiału weryfikacyjnego, na przykład bazy hashy, dynamika ataku się zmienia. Wtedy głównym pytaniem nie jest już, ile prób serwer dopuści w ciągu minuty, tylko ile kandydatów przeciwnik potrafi sprawdzić samodzielnie na własnym sprzęcie. Właśnie dlatego przechowywanie haseł nie może polegać na szybkim hashowaniu z myślą o wygodzie systemu. Po wycieku wygoda obrońcy staje się wygodą napastnika. To jest centralna intuicja całego wykładu: projekt mechanizmu uwierzytelniania trzeba oceniać nie tylko w normalnym trybie pracy, ale przede wszystkim w trybie porażki, gdy część danych już znalazła się poza kontrolą organizacji.

#slide 8
## layout
bullet
## slide title
Reuse haseł i credential stuffing
## bullets
- wyciek z jednej usługi uderza w wiele innych
- poprawne hashowanie nie zatrzymuje ponownego użycia hasła
- mobilność zwiększa liczbę usług i punktów logowania
- problem ma charakter systemowy, nie lokalny
## teleprompter:
Ponowne używanie haseł sprawia, że nawet dobrze zabezpieczony system dziedziczy cudze porażki. Jeśli użytkownik używa tego samego lub podobnego hasła w wielu usługach, wyciek z jednego miejsca otwiera drogę do prób logowania w innych. Credential stuffing nie jest więc przede wszystkim atakiem na funkcję skrótu ani na kryptografię, tylko na ludzkie nawyki i na wspólne granice wielu systemów. W środowisku mobilnym ten problem jest jeszcze bardziej widoczny, bo telefon staje się punktem dostępu do dużej liczby usług: bankowych, społecznościowych, firmowych, komunikacyjnych i zakupowych. Każda z nich może być technicznie poprawna we własnym zakresie, a mimo to pozostawać narażona przez to, co wydarzyło się poza nią. To dobry moment, aby odróżnić bezpieczeństwo lokalnej implementacji od bezpieczeństwa ekosystemu, w którym użytkownik faktycznie funkcjonuje.

#slide 9
## layout
bullet
## slide title
Reset hasła i odzyskiwanie dostępu
## bullets
- recovery jest częścią uwierzytelniania
- procedura awaryjna często omija główną ścieżkę ochrony
- utrata urządzenia nie może prowadzić do utraty kontroli nad kontem
- najsłabszy etap przepływu wyznacza realne bezpieczeństwo
## teleprompter:
Wiele systemów ma poprawnie zaprojektowany ekran logowania, a mimo to daje się obejść przez słabszy mechanizm odzyskiwania konta. Z perspektywy bezpieczeństwa reset hasła nie jest osobną wygodną usługą pomocniczą, lecz częścią tego samego systemu zaufania. Jeżeli odzyskanie dostępu opiera się na słabszych przesłankach niż zwykłe logowanie, napastnik będzie celował właśnie tam. W kontekście mobilnym dochodzi jeszcze scenariusz utraty lub wymiany urządzenia. Użytkownik oczekuje, że po zmianie telefonu odzyska dostęp do konta i danych, ale ta wygoda nie może oznaczać, że przejęcie numeru telefonu, poczty lub kopii zapasowej daje pełną kontrolę nad tożsamością. Z tego powodu projektowanie przechowywania haseł trzeba łączyć z pytaniem, jak system zachowuje się wtedy, gdy użytkownik jest poza swoją standardową ścieżką działania.

#slide 10
## layout
title
## slide title
Mobilność zmienia priorytety bezpieczeństwa
## subtitle
Nie tylko baza użytkowników, lecz całe życie sekretu na urządzeniu i poza nim
## teleprompter:
W systemie webowym łatwo opowiadać o haśle tak, jakby jego historia zaczynała się i kończyła w bazie serwera. W systemie mobilnym to uproszczenie szybko przestaje działać. Telefon jest urządzeniem stale zalogowanym, przechowuje tokeny, obsługuje synchronizację, bywa zabezpieczony lokalnym PIN-em i biometrią, przechodzi migrację na nowe urządzenie i podlega backupowi. Z tego powodu priorytetem staje się nie tylko poprawne przechowywanie hasła po stronie serwera, ale także sensowne rozdzielenie odpowiedzialności między serwer, aplikację i platformę. Często najważniejsze pytanie brzmi nie: jak przechować hasło, lecz: czy aplikacja mobilna po udanym logowaniu musi jeszcze w ogóle znać to hasło. Im szybciej odpowiedź brzmi nie, tym mniejsza powierzchnia ryzyka po stronie klienta.

#slide 11
## layout
definition
## term
Łańcuch zaufania w uwierzytelnianiu mobilnym
## definition
Sekwencja zależności między sekretem użytkownika, mechanizmami platformy, aplikacją, backendem oraz procesami odzyskiwania i synchronizacji.
## teleprompter:
Pojęcie łańcucha zaufania pomaga uniknąć tunelowego spojrzenia na pojedynczy komponent. Hasło użytkownika to tylko jeden element. Dalej pojawia się aplikacja mobilna, która musi je bezpiecznie obsłużyć, system operacyjny, który może chronić klucze lub dane lokalne, backend weryfikujący tożsamość, a obok tego procesy resetu, backupu, przywracania i synchronizacji. Jeżeli którykolwiek z tych elementów ma słabszy model bezpieczeństwa niż reszta, napastnik skieruje się właśnie tam. To rozumowanie jest zgodne z szerokim celem przedmiotu, który kładzie nacisk na myślenie o bezpieczeństwie w projektowaniu, implementacji i wdrażaniu aplikacji mobilnych, a nie tylko na znajomość pojedynczych mechanizmów. Dlatego dalsza część wykładu będzie konsekwentnie sprawdzać, gdzie kończy się bezpieczeństwo samego algorytmu, a zaczyna bezpieczeństwo systemu jako całości. fileciteturn12file9

#slide 12
## layout
bullet
## slide title
Zakres dalszej części wykładu
## bullets
- od funkcji skrótu do password hashing
- od ochrony przed atakiem offline do storage na urządzeniu
- od teorii algorytmów do błędów architektonicznych
- od pojęć ogólnych do przypadków Android i iOS
## teleprompter:
Dalszy ciąg będzie szedł od podstaw kryptograficznych w stronę praktyki inżynierskiej. Najpierw trzeba uporządkować, czym jest funkcja skrótu i dlaczego sama szybkość obliczeń, pożądana w wielu zastosowaniach kryptograficznych, okazuje się wadą przy ochronie haseł. Następnie pojawią się salt, work factor, key stretching i koszt pamięci, czyli elementy projektowane po to, aby podnieść cenę ataku offline. Potem nastąpi przejście do architektury mobilnej: lokalne sekrety, tokeny, storage systemowy, ograniczenia platformowe i sytuacje, w których poprawne użycie API nie wystarcza, bo błąd leży w logice aplikacji albo w procesie odzyskiwania danych. Na końcu ten porządek teoretyczny zostanie zestawiony z rzeczywistymi przypadkami z Androida i iOS.

#slide 13
## layout
definition
## term
Funkcja skrótu
## definition
Funkcja obliczeniowo efektywna, mapująca dane o dowolnej długości na ciąg o ustalonej długości, używany jako ich zwięzły reprezentant.
## teleprompter:
Handbook of Applied Cryptography definiuje funkcję skrótu jako obliczeniowo efektywną funkcję odwzorowującą ciągi binarne dowolnej długości w ciągi o stałej długości. Ta definicja jest z pozoru prosta, ale ważne jest słowo efektywna. Funkcje skrótu są projektowane tak, by działały sprawnie i nadawały się do praktycznych zadań, takich jak integralność danych, podpisy cyfrowe czy inne protokoły kryptograficzne. Właśnie ta efektywność, bardzo cenna w wielu zastosowaniach, staje się problemem przy przechowywaniu haseł. Jeżeli sprawdzenie kandydata jest bardzo tanie dla systemu, to jest również bardzo tanie dla przeciwnika prowadzącego atak offline. Zanim więc padnie słowo bcrypt, scrypt czy Argon2, trzeba najpierw dobrze zrozumieć, do czego zwykła funkcja skrótu została zaprojektowana, a do czego nie została. fileciteturn12file5

#slide 14
## layout
bullet
## slide title
Własności ważne kryptograficznie
## bullets
- odporność na znalezienie preobrazu
- odporność na znalezienie drugiego preobrazu
- odporność na kolizje
- publiczność algorytmu i brak sekretu w samej funkcji
## teleprompter:
Dla zastosowań kryptograficznych funkcja skrótu powinna utrudniać znalezienie danych wejściowych dla danego skrótu, utrudniać znalezienie innego wejścia o tym samym wyniku i utrudniać znalezienie dowolnej pary kolidujących wejść. Handbook of Applied Cryptography wiąże te własności z użyciem skrótów w integralności i podpisach cyfrowych. Warto przy tym zauważyć jeszcze jedną rzecz: standardowa funkcja skrótu jest zwykle publiczna i nie zawiera sekretu. To oznacza, że bezpieczeństwo systemu opartego na hashach nie może polegać na ukrywaniu samego algorytmu. W kontekście przechowywania haseł prowadzi to do ważnego wniosku: napastnik z reguły wie, jaki algorytm zastosowano, i powinien móc to wiedzieć. Obrona musi więc wynikać z właściwości konstrukcji, parametrów kosztu i jakości hasła, a nie z tajemnicy implementacyjnej. fileciteturn12file5turn12file6

#slide 15
## layout
title
## slide title
Dlaczego szybki hash nie jest dobrym magazynem haseł
## subtitle
To, co jest zaletą przy integralności danych, staje się wadą przy zgadywaniu sekretu
## teleprompter:
Jeżeli funkcja skrótu ma być używana do integralności danych lub do wspierania podpisów cyfrowych, pożądana jest wysoka wydajność. System powinien przetwarzać dane szybko i przewidywalnie. Przy hasłach sytuacja jest odwrotna. Napastnik, który zdobył materiał do ataku offline, wykonuje dokładnie tę samą operację obliczeniową co obrońca, tylko w masowej skali. Im tańsze jest pojedyncze przeliczenie, tym niższy koszt zgadywania. To dlatego zwykły szybki hash nie jest wystarczającym magazynem haseł. Diffie i Hellman już w latach siedemdziesiątych opisywali logikę przechowywania nie samego hasła, lecz wartości funkcji jednokierunkowej, ale równocześnie podkreślali, że liczy się asymetria między łatwością obliczenia a praktyczną trudnością odwrócenia. Dzisiejsze password hashing idzie krok dalej: nie tylko utrudnia odwrócenie, lecz celowo zwiększa koszt sprawdzenia każdej próby. fileciteturn12file11turn12file13

#slide 16
## layout
definition
## term
Hasło nie jest kluczem losowym
## definition
Hasło jest sekretem wybieranym lub zapamiętywanym przez człowieka; klucz kryptograficzny jest materiałem losowym tworzonym pod wymagania algorytmu.
## teleprompter:
To rozróżnienie ma bezpośrednie skutki praktyczne. Klucz kryptograficzny jest projektowany tak, aby miał odpowiedni rozmiar i odpowiednią losowość. Hasło użytkownika jest tworzone pod ograniczenia pamięci i wygody człowieka, więc jego rozkład jest daleki od idealnego. To dlatego nie wolno zakładać, że wpis użytkownika może być bezpośrednio użyty wszędzie tam, gdzie potrzebny jest pełnowartościowy klucz. W praktyce hasło często staje się tylko wejściem do procedury wyprowadzania materiału pochodnego. To pochodne, a nie samo hasło, może następnie służyć do dalszych operacji. Na poziomie architektonicznym jest to jedna z najważniejszych granic porządkujących cały temat przechowywania sekretów.

#slide 17
## layout
bullet
## slide title
Entropia użytkownika a entropia kryptograficzna
## bullets
- człowiek wybiera hasła z silnie nierównomiernego rozkładu
- napastnik nie zgaduje losowo, tylko według prawdopodobieństwa
- realna siła hasła zależy od przewidywalności, nie tylko długości
- mechanizm obrony musi zakładać inteligentne zgadywanie
## teleprompter:
W teorii najłatwiej mówić o przestrzeni wszystkich możliwych haseł, ale w praktyce napastnik nie zgaduje w ciemno. Wykorzystuje słowniki, reguły przekształceń, wzorce językowe, dane z wycieków i wiedzę o zachowaniach użytkowników. To oznacza, że realna entropia hasła jest zwykle dużo niższa od entropii wynikającej z czysto kombinatorycznego liczenia długości i alfabetu. Właśnie dlatego obrona nie może opierać się wyłącznie na abstrakcyjnym rozmiarze przestrzeni. Musi też podnosić koszt każdego sprawdzenia kandydata. Z punktu widzenia inżynierii bezpieczeństwa właściwe pytanie brzmi nie tylko, ile istnieje możliwych haseł, ale w jakiej kolejności rozsądny przeciwnik będzie je próbował i jaki jest koszt tej kolejności.

#slide 18
## layout
title
## slide title
Password hashing jako obrona przed atakiem offline
## subtitle
Celem nie jest uczynienie hasła silnym, lecz uczynienie zgadywania drogim
## teleprompter:
To jest centralna idea praktycznego przechowywania haseł. Nie da się magicznie zamienić ludzkiego hasła w sekret o jakości losowego klucza. Można natomiast tak zaprojektować proces weryfikacji, aby każda próba zgadywania była kosztowna. Password hashing nie usuwa słabości użytkownika, ale zmienia ekonomię ataku. W systemie poprawnie zaprojektowanym pojedyncze logowanie legalnego użytkownika pozostaje akceptowalnie drogie, natomiast przetestowanie milionów kandydatów przez napastnika staje się znacząco bardziej kosztowne. To przesunięcie kosztu jest najważniejszym argumentem za specjalizowanymi konstrukcjami do ochrony haseł. Od tej chwili nie myślimy już o skrócie jako o zwięzłym reprezentancie danych, tylko jako o elemencie mechanizmu spowalniającego przeciwnika w scenariuszu po wycieku.

#slide 19
## layout
definition
## term
Salt
## definition
Jawna, unikalna wartość dołączana do procesu hashowania hasła, aby identyczne hasła nie dawały identycznych wyników i aby zneutralizować gotowe tabele preobliczeń.
## teleprompter:
Salt nie jest sekretem i nie ma nim być. Jego rola polega na tym, aby to samo hasło u dwóch użytkowników lub w dwóch rekordach nie prowadziło do identycznego wyniku oraz aby napastnik nie mógł opłacalnie użyć jednej preobliczonej tabeli przeciwko wielu wpisom naraz. W konsekwencji salt rozbija masową opłacalność niektórych technik ataku, ale nie sprawia, że słabe hasło staje się silne. Jeżeli hasło należy do wąskiej listy oczywistych kandydatów, napastnik nadal może je odgadnąć, tylko musi liczyć osobno dla konkretnego rekordu. To bardzo ważne rozróżnienie, bo wokół salt często narasta fałszywa aura rozwiązania całego problemu. Jego znaczenie jest duże, ale precyzyjnie ograniczone.

#slide 20
## layout
title
## slide title
Dlaczego salt nie ukrywa słabego hasła
## subtitle
Chroni przed ponownym użyciem obliczeń, nie przed przewidywalnością użytkownika
## teleprompter:
Jeżeli użytkownik wybiera hasło z grupy najczęściej spotykanych kandydatów, to nawet poprawny salt nie usuwa problemu przewidywalności. Napastnik nie może już w prosty sposób użyć jednego wyniku dla wszystkich rekordów, ale nadal może dla konkretnego użytkownika sprawdzić listę najbardziej prawdopodobnych haseł i porównać wyniki. Dlatego salt należy rozumieć jako element konieczny, ale niewystarczający. Chroni przed identycznością wyników i osłabia sens gotowych tabel preobliczeń, lecz nie zastępuje kosztownego password hash i nie kompensuje słabej jakości sekretu. Ta logika będzie za chwilę rozszerzona o work factor i key stretching, czyli mechanizmy, które mają nie tylko rozdzielać rekordy, ale także podnosić koszt każdego sprawdzenia.

#slide 21
## layout
definition
## term
Pepper
## definition
Dodatkowy sekret systemowy używany w ochronie haseł, przechowywany poza bazą rekordów haseł i mający zwiększyć skutki kompromitacji samej bazy.
## teleprompter:
Pepper jest często przedstawiany jako naturalny kolejny krok po salcie, ale jego sens trzeba rozumieć ostrożnie. Salt ma być jawny i unikalny dla rekordu. Pepper jest wspólnym lub częściowo wspólnym sekretem systemowym, który nie powinien znajdować się w tej samej bazie co rekordy haseł. Jeżeli baza zostaje wykradziona, a pepper pozostaje bezpieczny, przeciwnik nie dostaje od razu pełnego materiału do ataku offline. To może być cenna warstwa obrony. Jednocześnie pepper komplikuje architekturę: trzeba go bezpiecznie przechowywać, rotować, odtwarzać po awarii i rozumieć, co dzieje się po jego kompromitacji. Dlatego pepper ma sens głównie wtedy, gdy organizacja potrafi utrzymać go w silniejszym środowisku, na przykład poza zwykłą bazą aplikacyjną.

#slide 22
## layout
bullet
## slide title
Work factor jako ekonomia ataku
## bullets
- koszt pojedynczej próby ma być niski dla użytkownika, wysoki dla masowego zgadywania
- parametr kosztu należy dobrać do realnego środowiska wykonania
- zbyt niski koszt pomaga napastnikowi
- zbyt wysoki koszt może szkodzić wydajności i dostępności
## teleprompter:
Work factor nie jest ozdobnym parametrem technicznym, tylko narzędziem zmiany ekonomii ataku. Każda legalna weryfikacja hasła i każda nielegalna próba zgadywania przechodzą przez tę samą funkcję. Chodzi więc o takie ustawienie kosztu, aby pojedyncze logowanie pozostawało akceptowalne dla systemu, ale duża kampania zgadywania offline stawała się wyraźnie droższa. Ten koszt nie jest stały raz na zawsze. Zależy od sprzętu, skali systemu, oczekiwanej przepustowości i od tego, czy mówimy o serwerze centralnym czy o urządzeniu mobilnym o ograniczonych zasobach. Dobrze ustawiony work factor wymaga więc nie tylko wiedzy kryptograficznej, ale także dojrzałości operacyjnej i okresowego podnoszenia parametrów wraz ze zmianą realiów sprzętowych.

#slide 23
## layout
definition
## term
Key stretching
## definition
Technika celowego zwiększania kosztu obliczeniowego lub pamięciowego potrzebnego do sprawdzenia kandydata hasła.
## teleprompter:
Key stretching to odpowiedź na prosty fakt: hasło użytkownika jest relatywnie słabe, więc system powinien przynajmniej utrudnić jego masowe sprawdzanie. Zamiast jednego szybkiego przeliczenia stosuje się konstrukcję, która wymaga większego nakładu pracy, a czasem także znaczącej ilości pamięci. Nie chodzi o to, by pojedyncze logowanie stało się spektakularnie wolne, lecz o to, by miliony prób nie były już tanie. To właśnie jest praktyczna treść pojęcia stretching. W tym miejscu warto też pamiętać o intuicji obecnej już u Diffiego i Hellmana: samo przechowywanie obrazu funkcji jednokierunkowej to dopiero początek, a bezpieczeństwo zależy od tego, jak trudne jest praktyczne odwracanie procesu na wielką skalę. fileciteturn12file11turn12file13

#slide 24
## layout
title
## slide title
Memory hardness
## subtitle
W nowoczesnym ataku liczy się nie tylko czas, lecz także koszt pamięci
## teleprompter:
Współczesne ataki offline korzystają z bardzo wydajnego sprzętu równoległego. Gdy obrona opiera się wyłącznie na czasie obliczeń, przeciwnik może częściowo odzyskać przewagę dzięki masowej równoległości. Dlatego nowsze konstrukcje do ochrony haseł zaczęły wykorzystywać także koszt pamięci. Jeżeli każda próba wymaga nie tylko operacji, ale i odpowiednio dużego, trudno współdzielonego zasobu pamięci, atak staje się droższy nie tylko w sensie czasu, ale również w sensie architektury sprzętowej. To przesuwa obronę z prostego spowalniania w stronę kontrolowania całego profilu kosztu przeciwnika. W kontekście mobilnym temat jest szczególnie ciekawy, bo te same parametry trzeba później zestawić z ograniczeniami telefonu, zużyciem energii i doświadczeniem użytkownika.

#slide 25
## layout
title
## slide title
Od szybkiego skrótu do kosztownej weryfikacji
## subtitle
Dlaczego bezpieczne przechowywanie haseł wymaga celowego spowolnienia ataku
## teleprompter:
W poprzednim fragmencie wykładu ustawiliśmy problem haseł jako problem sekretów o niskiej entropii, które w praktyce muszą przetrwać wyciek bazy danych, błędy operacyjne i ataki offline. To prowadzi do bardzo ważnego wniosku: dla przechowywania haseł nie chcemy funkcji po prostu poprawnej kryptograficznie, lecz funkcji, która dodatkowo czyni masowe zgadywanie kosztownym. Zwykła funkcja skrótu została zaprojektowana przede wszystkim do integralności, deduplikacji, podpisów, konstrukcji MAC-ów albo jako element większych prymitywów. W tych zastosowaniach szybkość jest atutem. Dla przechowywania haseł szybkość jest natomiast przewagą atakującego. Jeżeli atakujący może przeliczać miliardy kandydatów szybciej niż obrońca może zweryfikować pojedyncze poprawne logowanie, to przewaga ekonomiczna jest po jego stronie. Dlatego bezpieczne przechowywanie haseł odwraca intuicję typową dla inżynierii wydajności. Nie optymalizujemy funkcji po to, aby była maksymalnie szybka. Projektujemy ją tak, aby legalna weryfikacja była nadal praktyczna, ale każda próba masowego odgadywania kosztowała czas, pamięć i energię. Ten punkt prowadzi nas bezpośrednio do password hashing, key stretching i memory hardness, czyli do narzędzi, które zmieniają ekonomię ataku, a nie tylko postać danych zapisanych w bazie.

#slide 26
## layout
definition
## term
Password hashing
## definition
Zastosowanie funkcji projektowanej do ochrony haseł w taki sposób, aby weryfikacja poprawnego hasła była możliwa, ale masowe odgadywanie kandydatów po wycieku danych było kosztowne obliczeniowo i pamięciowo.
## teleprompter:
Termin password hashing bywa w praktyce używany zbyt luźno. Nie chodzi o dowolne obliczenie skrótu z hasła. Chodzi o użycie takiej konstrukcji, która została dobrana właśnie do obrony przed atakiem na sekret o niskiej entropii. Weryfikator nie musi znać hasła w postaci jawnej. Potrzebuje jedynie takiej reprezentacji, która pozwala porównać wynik uzyskany z hasła podanego przy logowaniu z wartością zapisaną wcześniej. Różnica między zwykłym hashowaniem a password hashing zaczyna się jednak tam, gdzie pojawia się model przeciwnika. Jeżeli przeciwnik przejmie bazę, powinien stanąć przed zadaniem droższym niż jedno szybkie przeliczenie SHA-256 dla miliardów kandydatów. Stąd biorą się parametry kosztu, sól, czasami pieprz, a w nowszych konstrukcjach także twardy koszt pamięci. W praktyce password hashing to nie pojedyncza operacja matematyczna, lecz decyzja architektoniczna obejmująca dobór algorytmu, dobór parametrów, sposób migracji starych hashy i sposób reagowania na wzrost możliwości sprzętowych atakującego.

#slide 27
## layout
bullet
## slide title
Czego chcemy od funkcji do przechowywania haseł
## bullets
- Unikalności wyniku dla tego samego hasła przy użyciu różnych soli
- Regulowanego kosztu obliczeniowego i najlepiej także kosztu pamięciowego
- Odporności na masowe ataki równoległe na GPU, FPGA i ASIC
- Stabilnej, powtarzalnej weryfikacji po stronie serwera
- Możliwości podnoszenia parametrów bez resetowania wszystkich kont
## teleprompter:
Kiedy mówimy o bezpiecznym przechowywaniu haseł, potrzebujemy zestawu własności bardziej praktycznego niż klasyczna lista własności kryptograficznych funkcji skrótu. Po pierwsze, potrzebna jest sól, aby dwa identyczne hasła nie dawały tej samej reprezentacji zapisanej w bazie. Po drugie, potrzebny jest koszt, który można regulować wraz ze zmianą sprzętu i budżetu wydajnościowego. Po trzecie, nowoczesna funkcja musi utrudniać przewagę uzyskiwaną przez silnie równoległy sprzęt, bo współczesny atakujący nie jest już ograniczony do pojedynczego procesora ogólnego przeznaczenia. Po czwarte, cały mechanizm ma być na tyle przewidywalny, by serwer mógł weryfikować logowanie bez chaosu operacyjnego i bez ryzyka utraty kompatybilności między wersjami. Po piąte, system musi pozwalać na stopniową modernizację. Hasła w prawdziwej usłudze żyją latami. Oznacza to, że obrona nie może być jednorazową decyzją podjętą przy pierwszym wdrożeniu. Musi umożliwiać migrację parametrów oraz przechodzenie ze starszych funkcji na nowsze bez wyłączania usługi i bez niepotrzebnego wymuszania resetu wszystkich kont.

#slide 28
## layout
definition
## term
Asymetria kosztu obrony i ataku
## definition
Właściwość dobrze dobranego mechanizmu ochrony haseł polegająca na tym, że pojedyncza legalna weryfikacja pozostaje akceptowalna, ale masowe sprawdzanie kandydatów przez napastnika staje się kosztowne.
## teleprompter:
W przechowywaniu haseł nie chodzi o to, aby legalny użytkownik cierpiał tak samo jak atakujący. Chodzi o wytworzenie kontrolowanej asymetrii. Jedna poprawna próba logowania ma być dla systemu i użytkownika nadal praktyczna, ale milion prób wykonywanych po wycieku bazy ma stać się przedsięwzięciem kosztownym czasowo, pamięciowo i energetycznie. To jest głębszy sens całego bloku o password hashing. Nie projektujemy funkcji po to, aby matematycznie uniemożliwiała odgadnięcie hasła, bo dla sekretu niskoentropijnego to nierealne. Projektujemy ją po to, aby odwrócić relację opłacalności. Obrona ma kupować czas, zmniejszać skalę szkód i odbierać przewagę ekonomiczną masowemu atakowi. Dopiero w tym świetle widać, dlaczego szybkie funkcje skrótu są złym narzędziem do ochrony haseł, nawet jeśli pozostają poprawne kryptograficznie w innych zastosowaniach.

#slide 29
## layout
bullet
## slide title
Dlaczego SHA-256 nie wystarcza do haseł
## bullets
- Jest bardzo szybka, więc sprzyja atakowi offline
- Nie ma wbudowanego parametru kosztu dostrojonego do haseł
- Sama nie rozwiązuje problemu identycznych haseł bez soli
- Nie utrudnia w sposób istotny przewagi sprzętu równoległego
- Jest dobrym prymitywem kryptograficznym, ale nie dobrym password hasherem
## teleprompter:
To rozróżnienie jest absolutnie kluczowe i bardzo często źle rozumiane. SHA-256 nie jest funkcją złą. Jest funkcją bardzo użyteczną, szeroko stosowaną i dobrze uzasadnioną w wielu konstrukcjach kryptograficznych. Problem polega na tym, że jej cel projektowy nie był związany z obroną sekretów niskoentropijnych przed atakiem słownikowym. Jej szybkość, która jest zaletą przy integralności i podpisach, w przechowywaniu haseł staje się wadą. Atakujący po wycieku bazy może testować kandydatów z ogromną prędkością. Sama SHA-256 nie narzuca też kosztu pamięci i nie daje mechanizmu strojenia specjalnie pod przechowywanie haseł. Można oczywiście dobudować do niej dodatkową logikę, na przykład PBKDF2 oparty na HMAC, ale sama pojedyncza funkcja skrótu nie powinna być utożsamiana z nowoczesnym przechowywaniem haseł. W inżynierii bezpieczeństwa ważne jest nie tylko to, czy prymityw jest kryptograficznie poprawny, lecz także to, czy jest właściwy do danego modelu zagrożeń. Tutaj model zagrożeń wymaga czegoś więcej niż szybkiego skrótu.

#slide 30
## layout
title
## slide title
Iteracje to dopiero początek
## subtitle
Samo wielokrotne liczenie pomaga, ale nie rozwiązuje całego problemu równoległego sprzętu
## teleprompter:
Przez długi czas naturalną odpowiedzią na problem szybkich funkcji skrótu było po prostu wielokrotne ich wykonywanie. To poprawia sytuację, bo zwiększa koszt każdej próby. Nie usuwa jednak całej przewagi nowoczesnego sprzętu atakującego. Jeżeli funkcja pozostaje lekka pamięciowo, to bardzo dobrze skaluje się na GPU, FPGA i wyspecjalizowanych układach. Wtedy mnożymy koszt po obu stronach, ale niekoniecznie zmieniamy relację sił na korzyść obrońcy. Stąd wynika przejście od samego iteration count do konstrukcji memory-hard. W tym punkcie wykład przestaje być opowieścią o samej matematyce funkcji skrótu, a staje się opowieścią o architekturze ataku i o ekonomii sprzętu. To nie przypadek, że nowe konstrukcje do haseł mówią nie tylko o czasie wykonania, ale również o ilości pamięci potrzebnej na pojedyncze przeliczenie. W realnym ataku pamięć jest zasobem trudniejszym do miniaturyzacji i replikacji niż czysta liczba prostych operacji.

#slide 31
## layout
definition
## term
Memory hardness
## definition
Własność funkcji utrudniająca efektywne obliczanie dużej liczby prób bez przydzielenia znaczącej pamięci dla każdej z nich, co ogranicza przewagę masowo równoległego sprzętu.
## teleprompter:
Memory hardness jest próbą wyrównania pola gry między obrońcą a atakującym. Jeżeli funkcja wymaga nie tylko czasu, ale i istotnej ilości pamięci dla każdej próby, to przestaje być tak łatwo skalowalna na sprzęcie wyspecjalizowanym do przeliczania ogromnej liczby lekkich zadań. Dla obrońcy oznacza to, że koszt legalnej weryfikacji można dobrać tak, by był akceptowalny przy logowaniu użytkownika. Dla atakującego oznacza to, że setki tysięcy równoległych prób nie są już tylko problemem dostarczenia większej liczby rdzeni, lecz również problemem dostarczenia odpowiednio dużej pamięci i przepustowości pamięci. To przesuwa ciężar ataku z samego czasu na całkowity koszt sprzętu i energii. W praktyce memory hardness nie daje ochrony absolutnej. Bardzo słabe hasło nadal można zgadnąć. Chodzi o to, by masowe łamanie przestało być tanie i przemysłowo skalowalne. W tym sensie pamięciożerność jest jednym z najważniejszych współczesnych narzędzi obrony haseł.

#slide 32
## layout
bullet
## slide title
PBKDF2, bcrypt, scrypt, Argon2id
## bullets
- PBKDF2: klasyczna iteracyjna konstrukcja oparta na funkcji pseudolosowej
- bcrypt: adaptacyjny koszt, ale ograniczenia wejścia i starszy model kosztu
- scrypt: koszt czasu i pamięci, obrona przed tanim równoległym sprzętem
- Argon2id: współczesny punkt odniesienia dla nowych wdrożeń
- W praktyce wybór zależy od środowiska, bibliotek, migracji i polityki parametrów
## teleprompter:
Nie ma jednej historii ewolucji, w której każdy starszy algorytm natychmiast staje się bezużyteczny. Istnieje raczej ciąg rozwiązań odpowiadających kolejnym etapom zrozumienia problemu. PBKDF2 to dojrzała i bardzo szeroko wspierana konstrukcja iteracyjna, nadal istotna zwłaszcza tam, gdzie wymagają jej standardy lub kompatybilność. bcrypt wniósł praktycznie ważną adaptacyjność kosztu i przez wiele lat był domyślną odpowiedzią na pytanie o przechowywanie haseł. scrypt mocniej wyeksponował rolę pamięci jako zasobu obronnego. Argon2id stanowi dziś ważny punkt odniesienia, bo łączy współczesne rozumienie ataków, pamięciożerność i dobre własności praktyczne. W realnym systemie wybór algorytmu nie zależy jednak tylko od teorii. Zależy od dostępności bibliotek, od jakości implementacji, od możliwości migracji starych kont, od tego, czy system działa na serwerze ogólnego przeznaczenia, czy w środowisku mobilnym z ograniczeniami zasobów, oraz od tego, czy organizacja umie bezpiecznie zarządzać parametrami i aktualizacjami.

#slide 33
## layout
definition
## term
PBKDF2
## definition
Funkcja wyprowadzania klucza oparta na powtarzanym użyciu funkcji pseudolosowej, szeroko standaryzowana i nadal spotykana, lecz pozbawiona pamięciożerności charakterystycznej dla nowszych konstrukcji.
## teleprompter:
PBKDF2 to ważny etap rozwoju praktyki ochrony haseł i nadal trzeba go rozumieć, bo występuje w wielu systemach, bibliotekach i standardach. Jego idea jest prosta: zamiast pojedynczego szybkiego przeliczenia używamy wielokrotnego, kontrolowanego przetwarzania opartego zwykle na HMAC. Dzięki temu weryfikacja hasła staje się droższa i trudniej przeliczać ogromne słowniki kandydatów. Jednocześnie PBKDF2 pozostaje konstrukcją przede wszystkim czasową, a nie pamięciową. To oznacza, że jego odporność na współczesny równoległy sprzęt nie jest tak silna jak w przypadku scrypt czy Argon2id. Mimo to PBKDF2 bywa nadal akceptowalnym wyborem tam, gdzie liczy się zgodność ze starszym ekosystemem, certyfikacjami lub gotowymi komponentami. Inżyniersko istotne jest, by nie traktować go jako rozwiązania przestarzałego z definicji, ale też nie mylić z najlepszym wyborem dla nowego wdrożenia. Wykład na wyższym poziomie wymaga właśnie takiego niuansu: rozumienia kompromisów zamiast prostego dzielenia świata na algorytmy dobre i złe.

#slide 34
## layout
definition
## term
bcrypt
## definition
Adaptacyjna funkcja do haszowania haseł oparta na koszcie regulowanym parametrem pracy, historycznie bardzo ważna, ale obciążona ograniczeniem długości wejścia i słabszym modelem obrony niż nowsze funkcje pamięciożerne.
## teleprompter:
bcrypt odegrał ogromną rolę w praktyce bezpieczeństwa aplikacji. Jego znaczenie wynikało z prostego, ale bardzo użytecznego pomysłu: koszt weryfikacji ma być parametryzowany i można go stopniowo zwiększać wraz z rozwojem sprzętu. To duży krok naprzód względem prostego skrótu. Dzisiaj trzeba jednak mówić o bcrypt bardziej precyzyjnie. Nadal bywa wystarczający w systemach legacy i w wielu dojrzałych wdrożeniach, ale ma ograniczenia, których nie wolno ignorować. Najbardziej znane jest ograniczenie długości wejścia w typowych implementacjach, zwykle do 72 bajtów. To może prowadzić do nieintuicyjnych problemów przy bardzo długich hasłach oraz przy błędnym pre-hashingu. Drugim problemem jest to, że bcrypt nie jest konstrukcją pamięciożerną w nowoczesnym sensie. Jego koszty da się skalować, ale nie wykorzystuje pamięci jako głównego narzędzia ograniczania przewagi sprzętu równoległego. Dlatego współcześnie traktuje się go częściej jako solidne rozwiązanie zastane lub kompromis zgodności niż jako pierwszy wybór dla nowego projektu.

#slide 35
## layout
definition
## term
scrypt
## definition
Funkcja wyprowadzania klucza i haszowania haseł projektowana tak, aby koszt ataku zależał nie tylko od czasu, ale także od pamięci potrzebnej do wykonania każdej próby.
## teleprompter:
scrypt jest ważnym krokiem w rozwoju obrony haseł, bo wprowadza do praktyki główną intuicję memory hardness. Nie chodzi już tylko o to, by operacja trwała długo. Chodzi o to, aby wymagała pamięci w skali utrudniającej bardzo tanią równoległość. To zmienia model ataku, szczególnie w środowiskach, gdzie przeciwnik liczy na przewagę GPU lub sprzętu projektowanego pod masowe, lekkie obliczenia. W sensie historycznym scrypt jest bardzo cenny, bo pokazuje przejście od myślenia iteracyjnego do myślenia zasobowego. W sensie praktycznym pozostaje sensowną opcją, zwłaszcza gdy Argon2id nie jest dostępny w danym ekosystemie. Jednocześnie wymaga starannego strojenia parametrów i świadomości, że sama obecność pamięciowego kosztu nie zwalnia z innych obowiązków, takich jak unikalna sól, właściwa migracja hashy i obrona przed atakami online. Z punktu widzenia projektowania systemów mobilnych scrypt jest też dobrym mostem do rozmowy o tym, kto płaci za koszt obliczeń i czy dany fragment kosztu ma być ponoszony wyłącznie przez serwer.

#slide 36
## layout
definition
## term
Argon2id
## definition
Współczesna pamięciożerna funkcja do haszowania haseł i wyprowadzania kluczy, łącząca ochronę przed częścią ataków side-channel z kosztami utrudniającymi masowe ataki równoległe.
## teleprompter:
Argon2id jest dziś naturalnym punktem odniesienia dla nowych wdrożeń przechowywania haseł. Dokument RFC 9106 opisuje Argon2 jako pamięciożerną funkcję dla password hashing i proof-of-work, wskazuje Argon2id jako główny wariant oraz zaleca unikalną sól, przy czym dla password hashing rekomenduje 16 bajtów soli. Sens tej konstrukcji nie polega na jednym magicznym parametrze. Argon2id pozwala stroić pamięć, liczbę przebiegów i równoległość, a więc modelować koszt legalnej weryfikacji i koszt ataku bardziej elastycznie niż starsze podejścia. Ważne jest też to, że współczesne wskazówki praktyczne, takie jak OWASP Password Storage Cheat Sheet, preferują Argon2id dla nowych aplikacji, a scrypt i bcrypt traktują odpowiednio jako alternatywę lub opcję legacy. Wykład na poziomie zaawansowanym nie powinien jednak kończyć się na haśle „użyj Argon2id”. Prawdziwe pytanie brzmi: z jakimi parametrami, na jakim sprzęcie, przy jakiej polityce migracji, i czy organizacja potrafi utrzymać te parametry w czasie.

#slide 37
## layout
bullet
## slide title
Parametry Argon2id w praktyce
## bullets
- Koszt pamięci określa, ile RAM zużywa pojedyncza weryfikacja
- Liczba iteracji steruje kosztem czasu
- Równoległość określa liczbę pasm pracy
- Parametry muszą wynikać z pomiaru na własnej infrastrukturze
- Celem nie jest maksimum, lecz koszt akceptowalny dla produkcji i dotkliwy dla ataku
## teleprompter:
W praktyce projektowej największy błąd polega na mechanicznym kopiowaniu parametrów bez uwzględnienia własnego środowiska. Argon2id daje duży zakres strojenia, ale to oznacza również odpowiedzialność po stronie zespołu. Koszt pamięci ma znaczenie nie tylko dla atakującego, lecz także dla serwera w godzinach szczytu. Liczba iteracji zwiększa czas pojedynczej weryfikacji. Równoległość wpływa na wykorzystanie dostępnych zasobów sprzętowych. Dobór parametrów jest więc zadaniem inżynierskim, a nie tylko kryptograficznym. OWASP publikuje przykładowe profile parametrów o porównywalnym poziomie obrony, różniące się kompromisem między CPU a RAM. To dobry punkt startowy, ale nie substytut własnego benchmarku. W systemie mobilnym pytanie staje się jeszcze ciekawsze: gdzie wykonywany jest koszt? Na serwerze przy logowaniu online? Lokalnie na urządzeniu przy odblokowaniu danych? W obu miejscach kompromisy są inne. Parametry bez kontekstu są tylko liczbami. Parametry osadzone w konkretnym modelu ruchu, sprzętu i zagrożeń stają się polityką bezpieczeństwa.

#slide 38
## layout
bullet
## slide title
Aktualne wskazówki praktyczne
## bullets
- OWASP preferuje Argon2id dla nowych wdrożeń
- scrypt jest zalecany, gdy Argon2id nie jest dostępny
- bcrypt pozostaje opcją głównie dla systemów starszych lub ograniczonych środowisk
- NIST wymaga bloklisty, pełnej weryfikacji hasła i ochrony kanału
- Polityka haseł to także ograniczanie online guessing, nie tylko przechowywanie hashy
## teleprompter:
Dwie rzeczy warto rozdzielić. Jedna to wybór algorytmu przechowywania hasła po stronie weryfikatora. Druga to polityka samego uwierzytelniania. OWASP Password Storage Cheat Sheet preferuje dziś Argon2id dla nowych wdrożeń i podaje konkretne profile parametrów. Jeżeli Argon2id nie jest dostępny, zaleca scrypt, a bcrypt pozostawia przede wszystkim dla zgodności i starszych środowisk. Z kolei NIST SP 800-63B przypomina, że bezpieczeństwo haseł nie kończy się na zapisie hashy. Wymaga bloklisty haseł powszechnie używanych lub skompromitowanych, pełnej weryfikacji całego hasła bez sztucznego obcinania, braku arbitralnej cyklicznej wymiany oraz ochrony kanału transportowego. To bardzo ważne, bo nawet najlepszy Argon2id nie obroni systemu, który pozwala na nieograniczone zgadywanie online, przyjmuje hasła z listy najpopularniejszych wycieków albo ujawnia, czy konto istnieje. W praktyce bezpieczeństwo uwierzytelniania jest sumą kilku warstw, a nie triumfem jednego algorytmu.

#slide 39
## layout
definition
## term
Rainbow table
## definition
Wstępnie obliczona struktura danych służąca do odwracania wielu skrótów naraz dla niesolonych haseł przez zamianę kosztu obliczeń na koszt wcześniejszego przygotowania i przechowywania.
## teleprompter:
Tęczowe tablice są dobrym przykładem na to, jak teoria ataku i praktyka obrony wzajemnie się kształtują. Ich podstawowa idea polega na przeniesieniu dużej części kosztu z chwili ataku do fazy wcześniejszego przygotowania. Jeżeli atakujący może wcześniej obliczyć ogromną liczbę relacji między kandydatami a skrótami, to późniejszy wyciek bazy niesolonych hashy staje się znacznie łatwiejszy do wykorzystania. W tradycyjnej dydaktyce tęczowe tablice bywają przedstawiane jako centralny problem przechowywania haseł. Dzisiaj trzeba to ująć bardziej precyzyjnie. Są ważne historycznie, bo doskonale pokazują sens soli. Jednocześnie nie wyczerpują współczesnego pejzażu zagrożeń. Nowoczesny atak częściej opiera się na szybkich atakach słownikowych, maskowych i hybrydowych z użyciem wyspecjalizowanego sprzętu niż na klasycznych, statycznych tęczowych tablicach. Mimo to pojęcie pozostaje bardzo wartościowe, bo uczy, że niesolony hash nie jest tylko skrótem. Jest również indeksem, który można porównywać w skali przemysłowej.

#slide 40
## layout
bullet
## slide title
Dlaczego sól zabija tęczowe tablice
## bullets
- Każda sól zmienia wejście funkcji dla tego samego hasła
- To samo hasło daje różne wyniki w różnych rekordach
- Nie da się użyć jednej prekomputacji dla całej bazy
- Atakujący musi atakować każdy rekord osobno
- Sól nie wzmacnia słabego hasła, ale niszczy ekonomię ataku zbiorczego
## teleprompter:
Sól jest jedną z najprostszych, a jednocześnie najpotężniejszych idei w obronie haseł. Jeżeli każde hasło łączymy z unikalną losową wartością, to ten sam sekret użytkownika nie daje już wspólnego identyfikatora w bazie. To ma dwa skutki. Po pierwsze, nie można z miejsca zauważyć, które konta współdzielą to samo hasło, patrząc jedynie na zapisane wartości. Po drugie, znika przewaga ataku opartego na jednej prekomputacji dla wielu rekordów jednocześnie. Atakujący nie może przygotować jednej uniwersalnej tabeli, która odwraca wszystkie hashe w bazie. Musi pracować osobno dla każdej soli i każdego rekordu. To dramatycznie podnosi koszt ataku zbiorczego. Warto jednak nie przypisywać soli właściwości, których nie ma. Sól nie czyni hasła losowym. Hasło słabe nadal pozostaje słabe. Sól nie zastępuje też kosztownego hashowania. Jej rola polega na zniszczeniu ekonomii wspólnego ataku i na zapewnieniu unikalności reprezentacji między rekordami.

#slide 41
## layout
definition
## term
Atak z prekomputacją
## definition
Strategia polegająca na wcześniejszym obliczeniu dużej liczby relacji między kandydatami haseł a wynikami funkcji, aby po wycieku danych skrócić koszt właściwego ataku.
## teleprompter:
Rainbow tables są tylko jednym szczególnym przypadkiem szerszej idei, którą warto nazwać wprost: atakiem z prekomputacją. Napastnik inwestuje zasoby wcześniej, zanim jeszcze pozna konkretną bazę ofiary, po to, aby później wykorzystać przygotowany materiał na dużą skalę. To bardzo ważna intuicja, bo pokazuje, że obrońca nie walczy wyłącznie z mocą obliczeniową wykonywaną po incydencie. Walczy także z możliwością wcześniejszego przygotowania sobie przewagi przez przeciwnika. Właśnie tu sól okazuje się tak skuteczna. Jeżeli każdy rekord ma własną losową wartość, wcześniejsze przygotowanie uniwersalnego materiału przestaje się opłacać. Atakujący nie może już użyć jednej wspólnej bazy obliczeń wobec całego wycieku. Musi zejść do poziomu pojedynczych rekordów, a to niszczy efekt skali, który był istotą prekomputacji.

#slide 42
## layout
bullet
## slide title
Atak offline po wycieku bazy
## bullets
- Atakujący pracuje bez kontaktu z usługą i bez ograniczeń tempa po stronie serwera
- O sukcesie decydują entropia hasła, koszt funkcji i jakość słowników
- Sól zmusza do pracy per rekord
- Memory hardness zwiększa koszt infrastruktury atakującego
- To najważniejszy model zagrożeń dla przechowywania haseł
## teleprompter:
Atak offline jest centralnym scenariuszem dla całego tematu przechowywania haseł. W przeciwieństwie do zgadywania online, tutaj obrońca traci bezpośrednią kontrolę nad tempem prób. Nie ma już rate limiting, CAPTCHA, monitoringu anomalii ani blokady konta po kolejnych błędach. Atakujący otrzymuje materiał, który może analizować we własnym tempie, na własnym sprzęcie i z własnymi słownikami. Dlatego wszystkie decyzje projektowe dotyczące przechowywania haseł trzeba oceniać przede wszystkim pod kątem tego modelu. Jeżeli system upadnie przy wycieku bazy, to nie pomoże fakt, że panel logowania miał estetyczny formularz i dobrą walidację po stronie klienta. Sól, koszt czasu, koszt pamięci, a czasem pepper są właśnie odpowiedzią na tę sytuację. To także ważne przejście myślowe dla bezpieczeństwa mobilnego. Użytkownik często kojarzy hasło z ekranem logowania, ale inżynier bezpieczeństwa musi kojarzyć je z tym, co zostanie po incydencie, kiedy przeciwnik przestanie pytać system o pozwolenie na każdą kolejną próbę.

#slide 43
## layout
bullet
## slide title
Ataki słownikowe, maskowe i hybrydowe
## bullets
- Słownikowy: kandydaci z list najczęstszych haseł i wycieków
- Maskowy: systematyczne warianty typu sezon, rok, znak specjalny, schemat firmowy
- Hybrydowy: słowo bazowe plus reguły modyfikacji
- Skuteczność wynika z przewidywalności ludzi, nie z łamania matematyki funkcji
- Obrona wymaga bloklist, polityki wyboru hasła i kosztownej weryfikacji
## teleprompter:
W praktyce mało kto łamie hasła, zaczynając od pełnego brute force całej przestrzeni znaków. To byłoby zbyt drogie i zbyt mało inteligentne. Zamiast tego atakujący korzystają z wiedzy o ludziach i o organizacjach. Atak słownikowy używa słów, fraz i haseł pochodzących z wcześniejszych wycieków. Atak maskowy eksploatuje regularności takie jak imię plus rok, nazwa usługi plus wykrzyknik, sezon plus numer. Atak hybrydowy łączy oba podejścia, stosując reguły transformacji do słów bazowych. Właśnie dlatego polityka bezpieczeństwa nie może ograniczać się do abstrakcyjnych wymagań typu jedna wielka litera i jedna cyfra. Tego rodzaju reguły często zwiększają przewidywalność zamiast realnej siły. Współczesna obrona polega raczej na odrzucaniu haseł powszechnie używanych lub skompromitowanych, na ułatwianiu użycia menedżerów haseł i na takim przechowywaniu hashy, aby nawet dobry słownik atakującego pracował jak najdrożej.

#slide 44
## layout
definition
## term
Credential stuffing
## definition
Automatyczne wykorzystywanie znanych par login–hasło pochodzących z innych wycieków w celu przejmowania kont w nowej usłudze.
## teleprompter:
Credential stuffing jest doskonałym przykładem na to, że temat haseł nie ogranicza się do bazy hashy. Nawet jeśli nasz własny system przechowuje hasła wzorowo, użytkownicy mogą używać tych samych sekretów w innych usługach, które miały gorsze zabezpieczenia. Wtedy przeciwnik nie musi łamać naszego hasha. Wystarczy, że weźmie pary login–hasło z obcego wycieku i spróbuje ich u nas. To zmienia punkt ciężkości obrony. Oprócz bezpiecznego przechowywania potrzebujemy wykrywania nietypowych prób logowania, ograniczania tempa, sygnałów ryzyka, czasem dodatkowego czynnika uwierzytelniającego i sensownej polityki resetu po podejrzeniu przejęcia. W systemach mobilnych problem jest szczególnie ważny, bo urządzenie często staje się trwałym punktem dostępu do konta. Jedno skuteczne przejęcie sesji lub refresh tokena może mieć długie konsekwencje. Dlatego wykład o hasłach na poziomie zaawansowanym musi pokazać, że bezpieczne przechowywanie hasha jest konieczne, ale nie wystarczające wobec współczesnych kampanii przejmowania kont.

#slide 45
## layout
definition
## term
Password spraying
## definition
Próba logowania do wielu kont przy użyciu niewielkiej liczby bardzo prawdopodobnych haseł, tak aby unikać blokad wyzwalanych przez wiele błędów na jednym koncie.
## teleprompter:
Password spraying odwraca intuicję klasycznego brute force online. Zamiast atakować jedno konto wieloma kandydatami, przeciwnik wybiera małą liczbę bardzo prawdopodobnych haseł i rozrzuca je po dużej liczbie kont. Dzięki temu może długo pozostawać poniżej progów alarmowych ustawionych per użytkownik. To jeden z powodów, dla których sama blokada po kilku błędnych próbach na pojedynczym koncie nie wystarcza. Obrona wymaga patrzenia na zjawisko globalnie: wiele kont, jedno hasło, wspólna infrastruktura źródłowa, nietypowe rozkłady prób w czasie. W praktyce spraying korzysta z tego samego faktu co ataki offline: ludzie wybierają przewidywalne sekrety. Z perspektywy przechowywania haseł jest to przypomnienie, że polityka haseł i polityka logowania muszą tworzyć jeden system. Można znakomicie przechowywać hashe, a mimo to przegrać z kampanią online, jeżeli popularne hasła nie są odrzucane, a analiza logowań nie wykrywa wzorca rozproszonego zgadywania.

#slide 46
## layout
definition
## term
Account enumeration
## definition
Ujawnianie, wprost lub pośrednio, czy dane konto istnieje, na podstawie różnic w odpowiedzi systemu, czasie przetwarzania lub przebiegu procesu odzyskiwania dostępu.
## teleprompter:
Enumeration to temat często traktowany jako drobiazg UX-owy, a w rzeczywistości będący elementem łańcucha ataku na hasła. Jeżeli system zdradza, które adresy e-mail są zarejestrowane, przeciwnik nie musi zgadywać nazw kont i może skupić się od razu na logowaniu, sprayingu albo phishingu. Ujawnienie może być jawne, na przykład przez komunikat „użytkownik nie istnieje”, ale może też być subtelne: inny czas odpowiedzi, inna ścieżka resetu, różnica w treści maila, odmienna walidacja po stronie API. W aplikacjach mobilnych enumeration bywa widoczne nie tylko w interfejsie, ale również w odpowiedziach backendu, logach debugowych, telemetryce i śladach pozostawianych w lokalnym cache. Dlatego dojrzała architektura uwierzytelniania stara się ujednolicać odpowiedzi, ograniczać różnice czasowe i nie dostarczać atakującemu taniego kanału rozpoznania. To nie zastępuje bezpiecznego przechowywania haseł, ale znacząco ogranicza liczbę skutecznych prób i jakość danych wejściowych dla przeciwnika.

#slide 47
## layout
bullet
## slide title
Mobilny wymiar ataków na hasła
## bullets
- Hasło często współistnieje z tokenem sesyjnym, biometrią i lokalnym sekretem urządzenia
- Przejęcie konta może oznaczać długotrwały dostęp dzięki tokenom odświeżania
- Błędy w aplikacji mobilnej mogą osłabić skutki nawet poprawnego password hashingu na serwerze
- Model ataku obejmuje backend, API, urządzenie, backup i proces odzyskiwania konta
- Bezpieczeństwo hasła trzeba oceniać w całym łańcuchu uwierzytelniania
## teleprompter:
To jest miejsce, w którym wykład wyraźnie przechodzi z klasycznego web security do bezpieczeństwa systemów mobilnych. W aplikacji mobilnej hasło zwykle nie jest jedynym sekretem, który decyduje o dostępie. Obok niego istnieją tokeny sesyjne, refresh tokeny, klucze lokalne, PIN urządzenia, biometria oraz często stan utrzymywany przez długi czas na urządzeniu. Oznacza to, że nawet doskonale przechowywane hasło po stronie serwera nie kończy problemu. Jeżeli aplikacja mobilna źle obchodzi się z tokenem, zapisuje go w niewłaściwym miejscu, wycieka go przez logi lub backup albo pozwala na jego użycie po przejęciu urządzenia, to realne bezpieczeństwo konta nadal będzie słabe. W modelu mobilnym trzeba więc patrzeć na cały łańcuch: od jakości hasła i kosztu jego weryfikacji, przez proces logowania i resetu, po to, co dzieje się na urządzeniu po skutecznym uwierzytelnieniu. To przygotowuje grunt pod kolejny duży blok wykładu, czyli secure storage na Androidzie i iOS oraz granice ochrony, jaką dają mechanizmy platformowe.

#slide 48
## layout
title
## slide title
Od hashy do architektury uwierzytelniania
## subtitle
Dalszy krok: tokeny, secure storage, platformowe magazyny sekretów i ich ograniczenia
## teleprompter:
W tym miejscu widać już wyraźnie, że temat przechowywania haseł nie jest zamkniętym rozdziałem o jednej funkcji kryptograficznej. Dobrze dobrany password hasher, sól, koszt obliczeniowy i polityka haseł są konieczne, ale w systemach mobilnych stanowią dopiero fundament. Po poprawnym uwierzytelnieniu pojawia się pytanie, co aplikacja przechowuje dalej, gdzie to przechowuje, jak długo to żyje i jakie gwarancje naprawdę daje platforma. To prowadzi do problemów lokalnych sekretów, tokenów dostępowych i odświeżających, kluczy nieeksportowalnych, Keychain, Keystore, klas dostępności, backupu oraz kompromitacji procesu aplikacji. W kolejnej części nie będziemy już pytać wyłącznie, jak utrudnić odgadnięcie hasła po wycieku bazy. Zaczniemy pytać, jak zbudować cały łańcuch uwierzytelniania tak, aby urządzenie mobilne nie stało się miejscem, w którym zwycięstwo odniesione po stronie serwera zostaje przegrane przez błędną architekturę klienta.

#slide 49
## layout
title
## slide title
Rehash przy logowaniu
## subtitle
Migracja parametrów bez jednoczesnego resetowania wszystkich haseł
## teleprompter:
Bezpieczne przechowywanie haseł nie jest decyzją podjętą raz na zawsze. Sprzęt atakującego staje się z czasem tańszy i szybszy, biblioteki dojrzewają, a organizacja zyskuje lepsze dane o wydajności własnego systemu. Z tego powodu zapis hasła powinien zawierać nie tylko sam wynik funkcji, lecz także informację o użytym schemacie i kosztach, aby można było rozpoznać, czy dany rekord odpowiada aktualnemu standardowi. Najpraktyczniejszą metodą modernizacji jest rehash przy poprawnym logowaniu. Użytkownik podaje prawidłowe hasło, system najpierw weryfikuje je według starego schematu zapisanego przy rekordzie, a następnie natychmiast oblicza nowy hash zgodny z bieżącą polityką i zastępuje stary zapis. Dzięki temu migracja rozkłada się w czasie, nie wymaga zbiorowego resetu wszystkich kont i nie tworzy sztucznego kryzysu operacyjnego. Taka strategia ma jednak granice. Konta nieaktywne mogą nigdy nie zostać zaktualizowane, dlatego organizacja musi wiedzieć, ile rekordów nadal opiera się na przestarzałych parametrach i czy pewna część bazy nie wymaga w końcu wymuszonego resetu. Rehash przy logowaniu jest więc nie tylko techniką kryptograficzną, ale elementem utrzymania systemu, który łączy bezpieczeństwo z realiami produkcyjnymi.

#slide 50
## layout
bullet
## slide title
Pepper w praktyce architektonicznej
## bullets
- Pepper ma sens tylko jako dodatkowa warstwa, nie jako substytut poprawnego password hashingu
- Najbezpieczniej utrzymywać go poza bazą danych, np. w HSM, KMS albo dedykowanym menedżerze sekretów
- Utrata peppera zmienia model incydentu, ale nie naprawia słabych haseł ani słabego algorytmu
- Rotacja peppera jest trudniejsza niż rotacja soli i może wymagać ponownej weryfikacji haseł
- Im bardziej złożona architektura sekretów, tym większe ryzyko błędu operacyjnego
## teleprompter:
Pepper bywa atrakcyjny, bo obiecuje dodatkową barierę między wyciekiem bazy a skutecznym atakiem offline. To jest prawda, ale tylko wtedy, gdy traktuje się go jako element większego systemu, a nie jako magiczną poprawkę. Jeżeli organizacja trzyma szybkie hashe i liczy na to, że wspólny sekret poza bazą wszystko uratuje, to w rzeczywistości buduje bardzo kruchą konstrukcję. Pepper działa sensownie dopiero wtedy, gdy podstawy są już poprawne: per-user salt, odpowiedni algorytm, koszt i możliwość podnoszenia parametrów w czasie. W praktyce najtrudniejsze nie jest samo dodanie peppera do obliczenia. Trudne jest jego życie operacyjne: gdzie go utrzymywać, kto ma do niego dostęp, jak go odtwarzać po awarii, jak reagować na podejrzenie kompromitacji i jak uniknąć sytuacji, w której jedna błędna konfiguracja odcina cały system logowania. W tym sensie pepper dobrze pokazuje napięcie typowe dla bezpieczeństwa. Dodatkowa warstwa może podnieść odporność, ale jednocześnie zwiększa złożoność i tym samym pole na błąd. Dojrzała architektura stosuje go rozważnie i tylko tam, gdzie organizacja potrafi udźwignąć jego konsekwencje operacyjne.

#slide 51
## layout
definition
## term
Work factor budget
## definition
Praktyczna granica kosztu weryfikacji hasła, wynikająca z wydajności serwera, oczekiwanego czasu odpowiedzi, liczby równoległych prób logowania i odporności systemu na przeciążenie.
## teleprompter:
Łatwo powiedzieć, że koszt funkcji powinien być jak najwyższy. Trudniej utrzymać usługę, która ma realnych użytkowników, szczyty ruchu i przeciwnika gotowego wykorzystać każdy drogi mechanizm do przeciążenia systemu. Dlatego dobór parametrów nie jest abstrakcyjnym wyborem kryptograficznym, lecz decyzją o budżecie kosztu. Trzeba wiedzieć, jaki czas pojedynczej weryfikacji jest akceptowalny, ile prób logowania może pojawić się równolegle, jak działają mechanizmy kolejkowania i jakie są granice skalowania infrastruktury. Zbyt niski koszt ułatwia atak offline po wycieku bazy. Zbyt wysoki koszt może otworzyć drogę do ataku na dostępność albo po prostu pogorszyć jakość usługi dla legalnych użytkowników. Dobra polityka nie polega więc na ustawieniu maksymalnej możliwej wartości raz na zawsze, lecz na takim doborze parametrów, który daje wyraźny koszt dla atakującego i jednocześnie nie destabilizuje systemu pod normalnym obciążeniem. To właśnie dlatego wytyczne praktyczne mówią o eksperymentowaniu na własnym środowisku, a nie o jednej uniwersalnej liczbie dobrej dla wszystkich usług.

#slide 52
## layout
title
## slide title
Hasło jako wektor DoS
## subtitle
Mechanizm ochronny może stać się punktem przeciążenia, jeśli koszt nie jest skoordynowany z architekturą usługi
## teleprompter:
Każdy koszt nałożony na napastnika jest równocześnie kosztem, który musi ponieść obrońca przy legalnej weryfikacji. To prowadzi do ważnego napięcia. Jeżeli mechanizm przechowywania haseł stanie się bardzo drogi, przeciwnik może próbować wymuszać ogromną liczbę kosztownych operacji i w ten sposób uderzać nie w poufność, lecz w dostępność. To nie znaczy, że należy wrócić do szybkich hashy. Oznacza to, że przechowywanie haseł trzeba projektować razem z resztą systemu: rate limitingiem, kolejkami, ochroną per IP i per konto, mechanizmami antyautomatyzacyjnymi, wykrywaniem anomalii oraz zdolnością poziomego skalowania. Dobre ustawienie kosztu jest zawsze lokalnym kompromisem między odpornością na offline cracking a odpornością na przeciążenie ścieżki logowania. W systemach mobilnych problem jest szczególnie praktyczny, ponieważ logowanie często odbywa się falami po aktualizacjach aplikacji, zmianach sesji albo migracji urządzeń. Wtedy błędny dobór parametrów może uderzyć w użytkowników dokładnie w momencie, w którym usługa powinna działać najsprawniej.

#slide 53
## layout
bullet
## slide title
Co warto mierzyć w procesie uwierzytelniania
## bullets
- Liczbę nieudanych prób w ujęciu per konto, per IP, per ASN i per urządzenie
- Rozkład czasów weryfikacji i skutki zmian parametrów hashy
- Udział kont z przestarzałym algorytmem lub starym work factorem
- Nienaturalne wzorce resetów hasła, sprayingu i credential stuffingu
- Udział logowań zakończonych rehashingiem oraz tempo migracji rekordów
## teleprompter:
W dojrzałym systemie przechowywanie haseł nie kończy się na schemacie rekordu w bazie. Potrzebna jest telemetria, która pozwala zrozumieć, czy polityka działa i gdzie system traci odporność. Sama liczba nieudanych logowań niewiele mówi. Trzeba patrzeć na rozkład prób między kontami, adresami sieciowymi, urządzeniami i przedziałami czasowymi. Trzeba rozumieć, czy wzrost błędnych logowań oznacza zwykłe problemy użytkowników po aktualizacji aplikacji, czy raczej kampanię sprayingu albo credential stuffingu. Warto też mierzyć, jak szybko znikają stare rekordy po wprowadzeniu nowej polityki parametrów oraz jaki odsetek kont nadal opiera się na technicznym długu. Bez takich danych organizacja nie wie, czy migracja naprawdę zachodzi, czy tylko istnieje na papierze. Telemetria nie ma oczywiście zastąpić bezpiecznego projektu. Ma jednak ujawniać to, czego nie widać w samej kryptografii: wzorce nadużyć, punkty przeciążenia i miejsca, w których bezpieczeństwo logowania zaczyna przegrywać z rzeczywistym ruchem produkcyjnym.

#slide 54
## layout
title
## slide title
Migracja ze starych hashy
## subtitle
Jak przejść od długu kryptograficznego do nowoczesnej polityki bez paraliżu usługi
## teleprompter:
Niemal każdy starszy system uwierzytelniania nosi ślady wcześniejszych epok: zbyt szybkie algorytmy, niewystarczający koszt, brak możliwości odczytu parametrów z rekordu albo dziedziczone formaty z dawnych frameworków. Najgorszą odpowiedzią jest udawanie, że problem nie istnieje. Drugą złą odpowiedzią jest próba gwałtownej, masowej zmiany bez planu dla użytkowników i operacji. Dobra migracja zaczyna się od inwentaryzacji: które konta używają jakiego formatu, które rekordy są niejednoznaczne, gdzie istnieje możliwość rehashu przy logowaniu, a gdzie konieczny będzie reset. Następnie potrzebna jest strategia przejściowa. System musi umieć rozpoznać kilka starszych schematów, bezpiecznie je zweryfikować i po sukcesie zapisać wynik w nowym formacie. W praktyce oznacza to przez pewien czas współistnienie starego i nowego świata, ale pod kontrolą i z planem wygaszania. W ten sposób bezpieczeństwo staje się procesem modernizacji, a nie jednorazową rewolucją, która kończy się frustracją użytkowników i pośpiesznymi wyjątkami w kodzie.

#slide 55
## layout
bullet
## slide title
Sygnały długu technicznego w magazynie haseł
## bullets
- Rekord nie zawiera informacji o algorytmie i parametrach
- W bazie współistnieją szybkie hashe bez planu wygaszania
- Nie ma mechanizmu rehash przy logowaniu
- Nie wiadomo, które konta korzystają z przestarzałego formatu
- Zespół nie potrafi oszacować skutków wycieku bazy hashy
## teleprompter:
Dług techniczny w obszarze haseł rzadko objawia się dramatycznym komunikatem o błędzie. Zwykle jest ukryty w rzeczach pozornie niewinnych: w nieczytelnym formacie rekordu, w starym polu bazy z nieudokumentowanym skrótem, w kodzie warunkowym pozostawionym po dawnej migracji albo w braku odpowiedzi na bardzo proste pytanie, jaką część kont da się dziś zweryfikować nowoczesnym schematem. To wszystko są sygnały, że organizacja nie kontroluje własnego magazynu haseł. Szczególnie groźna jest sytuacja, w której zespół nie potrafi oszacować skutków incydentu. Jeżeli nie wiadomo, które konta są chronione mocno, a które słabo, to po wycieku nie da się sensownie ustalić priorytetów reakcji. Dług techniczny w tym obszarze jest więc długiem bezpieczeństwa w bardzo dosłownym sensie. Dopóki nie zostanie nazwany, zmierzony i zaplanowany do spłaty, system pozostaje zależny od historii swoich dawnych błędów.

#slide 56
## layout
title
## slide title
Po wycieku bazy hashy
## subtitle
Incydent nie kończy się na stwierdzeniu, że hasła były zahashowane
## teleprompter:
W praktyce organizacje zbyt często traktują fakt użycia hashowania jak rodzaj immunitetu wizerunkowego. Tymczasem po wycieku pytanie nie brzmi tylko, czy hasła były zapisane jako jawny tekst. Pytanie brzmi, jakim algorytmem były chronione, z jakimi parametrami, czy rekordy były solone, czy istniał pepper, jaki odsetek bazy nadal używał starych formatów i jak szybko użytkownicy wielokrotnie używanych haseł mogą paść ofiarą przejęć w innych usługach. Reakcja po incydencie musi więc być warstwowa. Obejmuje analizę techniczną formatu rekordów, ocenę kosztu ataku offline, priorytetyzację kont wrażliwych, reset lub wymuszoną rotację, monitoring prób credential stuffingu oraz komunikację do użytkowników, która nie zaciera rzeczywistego poziomu ryzyka. Hash sam w sobie nie jest gwarancją bezpieczeństwa po incydencie. Jest tylko jednym z czynników, które decydują o tym, jak poważne będą skutki wycieku i ile czasu obrońca kupił przed skutecznym łamaniem haseł.

#slide 57
## layout
bullet
## slide title
Czego nie logować
## bullets
- Jawnych haseł, nawet chwilowo i nawet w trybie debug
- Tokenów dostępowych i odświeżających
- Kodów resetu, OTP i linków jednorazowych w pełnej postaci
- Materiału pozwalającego odtworzyć sekret z urządzenia lub z API
- Treści odpowiedzi różnicujących istnienie konta i stan procesu odzyskiwania
## teleprompter:
Jednym z najbardziej przyziemnych sposobów utraty bezpieczeństwa jest zapisanie w logach dokładnie tego, czego system miał pilnować. Problem pojawia się zarówno po stronie backendu, jak i po stronie aplikacji mobilnej. W trybach debugowych, podczas diagnozowania trudnych błędów lub przy integracji z zewnętrzną telemetrią zespół może niepostrzeżenie wyciec hasła, tokeny, kody resetu albo szczegóły odpowiedzi API, które pomagają w enumeracji. Szczególnie zdradliwe są sytuacje, w których log nie zawiera całego sekretu, ale zawiera wystarczająco dużo, by w połączeniu z innymi danymi stał się użyteczny dla napastnika. W systemach mobilnych dochodzi do tego jeszcze problem logów lokalnych, raportów awarii i usług analitycznych stron trzecich. Dlatego polityka logowania powinna być traktowana jako część architektury bezpieczeństwa, a nie jako luźny zwyczaj deweloperski. W przeciwnym razie organizacja może zbudować poprawny magazyn haseł i jednocześnie sama stworzyć boczny kanał ujawniający to, co miało pozostać tajne.

#slide 58
## layout
title
## slide title
Backend nadal pozostaje krytyczny
## subtitle
Mobile nie usuwa serwera z modelu zagrożeń, tylko dodaje do niego nowe warstwy
## teleprompter:
W dyskusji o systemach mobilnych łatwo ulec wrażeniu, że najważniejsze dzieje się wyłącznie na urządzeniu. To złudzenie. Serwer nadal jest miejscem, które weryfikuje hasła, wydaje tokeny, obsługuje reset, wymusza rehash, wykrywa kampanie zgadywania i przechowuje centralne dane o tożsamości użytkownika. Jeżeli backend jest zły, to nawet najlepszy Keychain czy Keystore nie uratują systemu. Jednocześnie backend nie może być projektowany tak, jakby klient był wyłącznie przeglądarką z prostym formularzem. W środowisku mobilnym serwer musi brać pod uwagę trwałe sesje, wielourządzeniowość, backup, migracje urządzeń, offline-first fragmenty logiki oraz różne sygnały ryzyka pochodzące z platformy. To podwójne spojrzenie jest bardzo ważne. Bezpieczne przechowywanie haseł zaczyna się na serwerze, ale nie kończy się na nim. Dopiero teraz można sensownie przejść do pytania, co dzieje się po udanym logowaniu i jakie sekrety pozostają na samym urządzeniu.

#slide 59
## layout
title
## slide title
Mobilny klient nie jest cienkim frontendem
## subtitle
Po zalogowaniu urządzenie przejmuje trwałą część stanu bezpieczeństwa użytkownika
## teleprompter:
W klasycznym myśleniu o logowaniu aplikacja kliencka bywa jedynie interfejsem do usługi, a cała powaga bezpieczeństwa spoczywa na serwerze. W systemach mobilnych taki obraz jest zbyt ubogi. Telefon przechowuje lokalny stan sesji, często utrzymuje możliwość działania po chwilowej utracie sieci, synchronizuje dane między uruchomieniami, obsługuje odblokowanie lokalne i staje się długotrwałym punktem dostępu do konta. To oznacza, że urządzenie nie jest wyłącznie miejscem wprowadzenia hasła. Jest aktywnym uczestnikiem architektury zaufania. Jeśli po udanym logowaniu na urządzeniu zostają sekrety, tokeny albo klucze, to ich przechowywanie staje się równie ważne jak sam magazyn hashy na serwerze. Z tego powodu wykład o hasłach w mobilności musi poszerzyć pole widzenia. Pytamy już nie tylko, jak bezpiecznie zweryfikować sekret użytkownika, lecz także jak nie zamienić telefonu w repozytorium artefaktów, których przejęcie pozwoli obejść cały koszt ochrony zbudowany po stronie backendu.

#slide 60
## layout
bullet
## slide title
Różne sekrety, różne role
## bullets
- Hasło użytkownika służy do uwierzytelnienia wobec usługi
- Token dostępowy reprezentuje już wynik uwierzytelnienia w ograniczonym czasie
- Refresh token pozwala odzyskać nową sesję bez ponownego pytania o hasło
- Lokalny klucz urządzenia może chronić dane zapisane na samym telefonie
- PIN i biometria często odblokowują użycie sekretu, a nie zastępują go w pełni
## teleprompter:
Jednym z najczęstszych źródeł błędów projektowych jest mieszanie różnych bytów w jedno słowo sekret. Hasło użytkownika, refresh token, lokalny klucz szyfrujący dane i PIN urządzenia nie pełnią tej samej funkcji. Hasło dowodzi wiedzy użytkownika wobec zdalnej usługi. Token dostępowy zwykle potwierdza, że to uwierzytelnienie już się odbyło i że klient otrzymał prawo do wykonania konkretnych operacji przez pewien czas. Refresh token umożliwia odnowienie sesji bez ponownego pytania o hasło, więc jego kradzież może mieć bardzo poważne skutki. Lokalny klucz urządzenia może natomiast w ogóle nie służyć do komunikacji z serwerem, lecz jedynie do ochrony danych przechowywanych lokalnie. PIN albo biometria często nie są samodzielnym sekretem usługi, tylko mechanizmem odblokowującym użycie czegoś już przechowywanego przez system. Rozdzielenie tych ról jest konieczne, bo każda z nich wymaga innego miejsca przechowywania, innego czasu życia i innego modelu obrony.

#slide 61
## layout
title
## slide title
Czy aplikacja mobilna powinna znać hasło po logowaniu
## subtitle
Najczęściej nie, chyba że projekt świadomie przewiduje lokalne wyprowadzenie klucza z sekretu użytkownika
## teleprompter:
W dobrze zaprojektowanym systemie mobilnym hasło użytkownika powinno pojawić się na urządzeniu jako dane wejściowe do jednorazowej operacji uwierzytelnienia, a nie jako trwały obiekt zapisany na później. Po poprawnym logowaniu aplikacja zwykle nie potrzebuje już hasła, ponieważ dalszą pracę wykonuje na tokenach, sesji albo lokalnych kluczach powiązanych z kontem. Trzymanie hasła lokalnie tylko po to, aby wygodniej odnawiać sesję, jest niemal zawsze złą decyzją. Otwiera drogę do przejęcia sekretu, który ma znaczenie globalne, bo bywa współużywany przez użytkownika także gdzie indziej. Wyjątek wymaga bardzo ostrożnego uzasadnienia. Czasem hasło służy jako wejście do lokalnego KDF i z niego wyprowadza się klucz do odszyfrowania lokalnych danych, ale nawet wtedy celem nie jest przechowywanie samego hasła. Celem jest użycie go w kontrolowany sposób i możliwie szybkie usunięcie z pamięci roboczej. Granica jest więc jasna: aplikacja może chwilowo przetwarzać hasło, lecz nie powinna traktować go jako wygodnego, długoterminowego sekretu lokalnego.

#slide 62
## layout
definition
## term
Refresh token
## definition
Długowieczny artefakt autoryzacyjny pozwalający klientowi uzyskać nowy token dostępowy bez ponownego przedstawiania hasła użytkownika.
## teleprompter:
Refresh token ma w praktyce wagę bezpieczeństwa znacznie większą, niż sugerowałaby jego nazwa. Nie jest tylko techniczną wygodą skracającą ścieżkę do odnowienia sesji. Jest trwałym biletem do odzyskania dostępu bez pytania użytkownika o hasło. Z punktu widzenia napastnika bywa więc równie atrakcyjny jak samo hasło, a czasem nawet bardziej, bo od razu działa w kontekście konkretnej usługi i nie wymaga zgadywania. To właśnie dlatego mobilna architektura uwierzytelniania nie może kończyć dyskusji na bezpiecznym password hashingu. Jeżeli hasło jest dobrze chronione na serwerze, ale refresh token leży w złym miejscu na urządzeniu albo w backupie, to cały system nadal może zostać przejęty. W praktyce oznacza to, że tokeny długowieczne muszą być traktowane jak sekrety wysokiej wartości: z minimalnym zakresem uprawnień, z kontrolą czasu życia, z możliwością unieważnienia po stronie serwera i z takim miejscem przechowywania, które utrudnia zarówno ekstrakcję, jak i nieuprawnione użycie.

#slide 63
## layout
title
## slide title
Lokalne odblokowanie danych a logowanie do usługi
## subtitle
To dwa różne problemy, choć użytkownik często widzi tylko jeden ekran odblokowania
## teleprompter:
Użytkownik może mieć wrażenie, że jeden ekran PIN-u albo biometrii rozwiązuje wszystko naraz: odblokowuje aplikację i uwierzytelnia go wobec usługi. Architektonicznie to są jednak dwa różne procesy. Lokalny mechanizm odblokowania może jedynie udzielić dostępu do danych przechowywanych na urządzeniu albo odblokować użycie klucza lokalnego. Nie musi i często nie powinien mieć tej samej mocy co hasło wobec serwera. Jeżeli aplikacja zaciera tę granicę, zaczynają się problemy z modelem ryzyka. Utrata urządzenia i obejście lokalnej blokady mogłyby wtedy automatycznie oznaczać pełne przejęcie konta zdalnego. Dobra architektura rozdziela więc poziomy zaufania. Jedno jest pytaniem, czy osoba trzymająca urządzenie może uzyskać dostęp do lokalnych danych lub wznowić istniejącą sesję. Drugie jest pytaniem, czy zdalna usługa uznaje tę osobę za poprawnie uwierzytelnioną do działań o określonej wadze. To rozróżnienie będzie później kluczowe przy omawianiu Keychainu, Keystore i wymagań uwierzytelnienia użytkownika dla użycia klucza.

#slide 64
## layout
definition
## term
Hasło jako wejście do KDF
## definition
Użycie hasła wyłącznie jako danych wejściowych do wyprowadzenia klucza lokalnego, bez trwałego zapisywania samego hasła na urządzeniu.
## teleprompter:
W niektórych projektach mobilnych hasło użytkownika ma jeszcze jedną rolę poza zdalnym logowaniem. Może służyć jako materiał wejściowy do lokalnego wyprowadzenia klucza, którym szyfrowane są dane przechowywane na urządzeniu. Taki wzorzec jest sensowny tylko wtedy, gdy projekt wyraźnie rozdziela funkcje i rozumie ograniczenia. Hasło użytkownika nie staje się przez to nagle losowym kluczem wysokiej entropii. Nadal pozostaje sekretem ludzkim, więc potrzebuje odpowiednio kosztownego KDF, właściwej soli i ostrożności przy obsłudze w pamięci. Zaletą tego podejścia jest to, że urządzenie nie musi przechowywać samego hasła. Wady pojawiają się tam, gdzie projekt próbuje używać jednego sekretu do zbyt wielu celów naraz albo gdzie użytkownik zmienia hasło zdalne, a lokalne dane pozostają związane ze starą pochodną. Dlatego użycie hasła jako wejścia do KDF ma sens tylko w świadomie zaprojektowanym modelu życia kluczy, a nie jako improwizowany sposób na wygodne trzymanie tajemnicy na telefonie.

#slide 65
## layout
bullet
## slide title
Kiedy lokalnie przechowuje się tylko klucz pochodny
## bullets
- Gdy celem jest ochrona lokalnej bazy lub plików, a nie ponowne logowanie do serwera hasłem
- Gdy klucz można związać z mechanizmem platformowym ograniczającym eksport i użycie
- Gdy lokalne odszyfrowanie ma być możliwe po odblokowaniu urządzenia lub aplikacji
- Gdy projekt przewiduje osobny cykl życia dla klucza lokalnego i dla hasła konta
- Gdy usunięcie aplikacji lub utrata urządzenia może bezpiecznie unieważnić lokalny stan
## teleprompter:
Przechowywanie lokalnego klucza pochodnego ma sens wtedy, gdy celem jest ochrona danych na urządzeniu, a nie utrzymywanie tajnego odpowiednika hasła użytkownika. To ważne rozróżnienie. Klucz pochodny może być związany z konkretną instalacją, konkretnym urządzeniem albo konkretnym stanem odblokowania. Dzięki temu nawet jeśli użytkownik posiada to samo konto na kilku urządzeniach, lokalne sekrety nie muszą być identyczne. Taki model pozwala też lepiej pogodzić bezpieczeństwo z użytecznością. Aplikacja może odblokowywać lokalne dane po spełnieniu warunków platformowych, na przykład po uwierzytelnieniu użytkownika, bez konieczności każdorazowego wysyłania hasła do serwera. Warunkiem jest jednak dyscyplina projektowa: jasne rozdzielenie cyklu życia lokalnego klucza od cyklu życia konta, świadomość konsekwencji reinstalacji i utraty urządzenia oraz unikanie pokusy, by lokalny sekret pochodny zaczął pełnić rolę uniwersalnego klucza do wszystkiego.

#slide 66
## layout
title
## slide title
Kiedy lokalnie trzyma się token, a nie hasło
## subtitle
Zwykle właśnie tak powinien wyglądać trwały stan po poprawnym uwierzytelnieniu mobilnym
## teleprompter:
Po jednorazowym, poprawnym logowaniu aplikacja najczęściej potrzebuje nie hasła, lecz możliwości kontynuowania sesji. To właśnie jest naturalne miejsce dla tokenów. Jeżeli architektura jest poprawna, klient zachowuje artefakt o bardziej ograniczonej funkcji niż hasło i o kontrolowanym czasie życia. Zyski są duże. Kradzież tokena nadal jest poważnym incydentem, ale zwykle można go unieważnić, ograniczyć zakresem uprawnień, skrócić jego czas ważności albo powiązać z dodatkowymi sygnałami ryzyka. Hasło ma natomiast zbyt duży zasięg, by leżało lokalnie dla wygody. Problem polega na tym, że zbyt wiele systemów traktuje refresh token jako niewinny detal implementacyjny. Tymczasem z perspektywy atakującego jest to często dokładnie to, czego potrzeba do długotrwałego przejęcia sesji. Dlatego poprawna odpowiedź na pytanie, co trzymać po logowaniu, brzmi zwykle: minimalny zestaw tokenów i kluczy potrzebnych do kontynuacji pracy, ale nie samo hasło użytkownika.

#slide 67
## layout
title
## slide title
Po utracie urządzenia
## subtitle
Bezpieczeństwo konta zależy wtedy od tego, jakie sekrety przetrwały na telefonie i jak szybko można je unieważnić
## teleprompter:
Utrata telefonu jest jednym z najbardziej realistycznych scenariuszy zagrożeń w bezpieczeństwie mobilnym. W tym momencie bardzo szybko widać, czy architektura była rozsądna. Jeżeli na urządzeniu przechowywano tylko ograniczone artefakty, związane z blokadą urządzenia, z możliwością zdalnego unieważnienia i z krótkim czasem życia, skutki incydentu mogą być ograniczone. Jeżeli jednak aplikacja zostawiła tam długowieczne tokeny bez dodatkowych zabezpieczeń, lokalne klucze bez kontroli użycia albo nawet samo hasło użytkownika, utrata urządzenia staje się utratą konta. Dlatego projektując magazyn sekretów na telefonie, trzeba zawsze zadawać pytanie o scenariusz kradzieży, zgubienia lub przejęcia urządzenia przez osobę mającą czas na analizę jego stanu. Reakcja po stronie serwera, możliwość wylogowania wszystkich sesji, unieważnienie refresh tokenów i ponowna rejestracja urządzenia nie są dodatkami. Są częścią samego projektu. Bez nich przechowywanie lokalnych sekretów staje się bardziej aktem wiary niż inżynierii bezpieczeństwa.

#slide 68
## layout
definition
## term
Root / jailbreak
## definition
Stan, w którym naruszone zostają zwykłe granice kontroli platformy nad aplikacjami i danymi, przez co założenia o izolacji procesu, integralności środowiska i ochronie sekretów stają się słabsze.
## teleprompter:
Mechanizmy bezpiecznego przechowywania na Androidzie i iOS opierają się na założeniu, że platforma zachowuje pewien minimalny poziom integralności i izolacji. Root albo jailbreak nie oznaczają automatycznie, że każdy sekret natychmiast wypływa, ale oznaczają, że model zaufania staje się gorszy. Atakujący może mieć większą kontrolę nad systemem plików, procesami, hookingiem funkcji, debugowaniem i obchodzeniem polityk narzuconych zwykłej aplikacji. Z punktu widzenia architektury najważniejsze jest nie to, czy istnieje idealny detektor roota lub jailbreaku. Takiego rozwiązania nie ma. Ważniejsze jest to, by wiedzieć, jakie gwarancje platformy znikają lub słabną w środowisku skompromitowanym i jakie decyzje podejmuje wtedy backend. Niektóre operacje mogą wymagać ponownego uwierzytelnienia, krótszego czasu życia tokenów, dodatkowego sygnału ryzyka albo całkowitej odmowy działania. Root i jailbreak są więc mniej tematem binarnym, a bardziej pytaniem o to, jak system reaguje, gdy zaufanie do urządzenia nie jest już pełne.

#slide 69
## layout
bullet
## slide title
Debug builds i logi jako cichy kanał wycieku
## bullets
- Wersja debug może udostępniać więcej informacji, funkcji testowych i punktów zaczepienia
- android:debuggable zwiększa ryzyko niezamierzonego dostępu i ingerencji
- Logi lokalne i zdalne mogą ujawniać hasła, tokeny, identyfikatory sesji i odpowiedzi API
- Raporty awarii oraz narzędzia analityczne stron trzecich mogą wynosić dane poza kontrolę zespołu
- Secure storage nie pomoże, jeśli sekret sam wychodzi przez telemetrię i diagnostykę
## teleprompter:
Część najbardziej bolesnych wycieków nie wynika z przełamania skomplikowanej kryptografii, lecz z pozostawionych funkcji testowych i nadmiernie gadatliwej diagnostyki. Wersja debug bywa wygodna dla zespołu, ale jej wygoda jest zwykle dokładnie tym, czego nie chcemy w wersji produkcyjnej. Możliwość podłączenia debuggera, ukryte panele administracyjne, obejścia walidacji, dane wypisywane do logów i raporty awarii wysyłane do zewnętrznych usług mogą razem stworzyć bardzo skuteczny boczny kanał wycieku. To szczególnie ważne przy sekretach mobilnych, ponieważ część diagnostyki odbywa się na samym urządzeniu, poza wzrokiem zespołu backendowego. Jeżeli aplikacja starannie umieszcza token w Keychainie albo Keystore, a następnie ten sam token trafia do logu, cały wysiłek przestaje mieć znaczenie. Dlatego bezpieczeństwo buildów, logowania i telemetrii należy traktować jak integralną część tematu przechowywania sekretów, a nie jak odrębną sprawę procesową.

#slide 70
## layout
title
## slide title
Backup, eksport danych i synchronizacja
## subtitle
Sekret bywa bezpieczny w jednym miejscu, a problematyczny w kopii, migracji albo odtworzeniu na nowym urządzeniu
## teleprompter:
Bardzo wiele błędnych założeń o secure storage bierze się z patrzenia tylko na stan bieżący urządzenia. Tymczasem aplikacje żyją także w kopiach zapasowych, w procesach migracji, przy wymianie telefonu i podczas przywracania danych. To właśnie wtedy sekrety mogą pojawić się w innych miejscach niż zakładał projektant. Na Androidzie część danych aplikacji może trafić do mechanizmów backupu zależnie od konfiguracji. Na iOS znaczenie mają klasy dostępności, zasady keychainu, synchronizacja i recovery. Dlatego pytanie nie brzmi wyłącznie, czy sekret jest dziś zaszyfrowany na bieżącym telefonie. Pytanie brzmi także, czy ten sam sekret przetrwa w kopii, czy odtworzy się na nowym urządzeniu, czy zmieni swoje właściwości po migracji i czy użytkownik lub atakujący mogą wykorzystać tę drogę do obejścia lokalnych zabezpieczeń. Backup i synchronizacja nie są detalem wdrożeniowym. Są częścią modelu życia sekretu i bardzo często miejscem, w którym abstrakcyjnie poprawna architektura przegrywa z realnym zachowaniem platformy.

#slide 71
## layout
definition
## term
Ochrona przed ekstrakcją a ochrona przed użyciem
## definition
Rozróżnienie między utrudnieniem wyeksportowania klucza lub sekretu z urządzenia a utrudnieniem nieuprawnionego wykonania operacji przy użyciu tego sekretu.
## teleprompter:
To jedno z najważniejszych rozróżnień w całym obszarze secure storage. System może bardzo skutecznie utrudniać ekstrakcję materiału kluczowego z urządzenia, a mimo to nie zapobiegać temu, że skompromitowany proces aplikacji użyje tego klucza zgodnie z udostępnionym API. Dla bezpieczeństwa różnica jest ogromna. W pierwszym przypadku atakujący nie może po prostu skopiować sekretu i wynieść go do własnego środowiska. W drugim nadal może wykonywać operacje w imieniu aplikacji tak długo, jak kontroluje jej wykonanie albo spełnia warunki użycia klucza. Dlatego zdanie klucz jest nieeksportowalny nie zamyka tematu. Trzeba jeszcze zapytać, kto i w jakich okolicznościach może go użyć, czy wymagane jest świeże uwierzytelnienie użytkownika, czy backend widzi sygnały ryzyka i czy krytyczne operacje mają dodatkowe bariery. Bez tego secure storage bywa błędnie rozumiany jako gwarancja absolutna, podczas gdy w rzeczywistości daje on głównie bardzo ważne, ale ograniczone wzmocnienie pewnej części modelu zagrożeń.

#slide 72
## layout
title
## slide title
Granica odpowiedzialności: aplikacja, system, backend
## subtitle
Bezpieczne przechowywanie sekretów działa tylko wtedy, gdy te trzy warstwy nie przerzucają ryzyka jedna na drugą
## teleprompter:
Na końcu tego bloku warto zebrać najważniejszy wniosek. Żadna pojedyncza warstwa nie rozwiązuje sama problemu sekretów w systemie mobilnym. Aplikacja odpowiada za to, co naprawdę przechowuje, jak długo, gdzie i z jaką dyscypliną obchodzi się z danymi w pamięci, logach, cache i backupie. System operacyjny dostarcza mechanizmy izolacji, bezpiecznego magazynu i ograniczeń użycia kluczy, ale tylko w ramach określonego modelu zaufania i tylko dla tych operacji, które aplikacja rzeczywiście projektuje zgodnie z tym modelem. Backend pozostaje miejscem, które ocenia ryzyko, wydaje i unieważnia tokeny, reaguje na utratę urządzenia, wymusza ponowne uwierzytelnienie i ostatecznie decyduje, jaki poziom zaufania jest potrzebny dla danej operacji. Gdy jedna warstwa zakłada, że inna zrobi za nią całą pracę, powstaje luka architektoniczna. Gdy role są rozdzielone świadomie, można zbudować system, w którym hasło jest tylko jednym z elementów, a nie jedyną linią obrony. To domyka przejście od serwerowego przechowywania hashy do właściwego problemu mobilności: bezpiecznego życia sekretu na urządzeniu.

#slide 73
## layout
title
## slide title
Android storage landscape
## subtitle
Pliki, SharedPreferences, SQLite i Keystore nie pełnią tej samej roli bezpieczeństwa
## teleprompter:
Na Androidzie bardzo łatwo powiedzieć ogólnie, że aplikacja coś przechowuje lokalnie, ale z punktu widzenia bezpieczeństwa to sformułowanie jest zbyt grube. Plik w prywatnym katalogu aplikacji, wpis w SharedPreferences, rekord w SQLite i klucz wygenerowany w Android Keystore to nie są równoważne byty. Różnią się zarówno sposobem dostępu, jak i tym, co w razie kompromitacji procesu albo błędu implementacyjnego da się odczytać, wyeksportować albo użyć. Zwykły plik i zwykła baza danych przechowują dane w postaci, nad którą sama aplikacja ma bezpośrednią kontrolę. Jeżeli aplikacja sama zapisze tam token, klucz albo materiał pozwalający odtworzyć sekret, to później sama musi go bezpiecznie chronić we wszystkich scenariuszach życia programu: przy logowaniu, migracji danych, backupie, crashu, debugowaniu i eksporcie. Keystore działa inaczej. Jego główna wartość polega nie na tym, że jest kolejnym pojemnikiem na dowolne dane, ale na tym, że pozwala wygenerować albo utrzymać klucz w taki sposób, by aplikacja nie musiała znać jego surowej postaci. To fundamentalna różnica. Androidowy pejzaż storage nie jest więc skalą od gorszego do lepszego folderu, tylko zbiorem mechanizmów o różnych własnościach, które trzeba dobierać do roli sekretu.

#slide 74
## layout
title
## slide title
Dlaczego zwykły sandbox nie wystarcza
## subtitle
Izolacja aplikacji jest ważna, ale nie usuwa błędów logiki, I/O i błędnego zaufania do danych wejściowych
## teleprompter:
Sandbox aplikacji jest jedną z podstawowych warstw obrony Androida, ale bardzo niebezpiecznie byłoby uznać go za wystarczającą odpowiedź na problem lokalnych sekretów. Sandbox ogranicza bezpośredni dostęp innych aplikacji do prywatnych danych programu, lecz nie naprawia błędów popełnionych przez samą aplikację. Jeśli proces z własnej woli ujawni sekret przez logi, zapisze go do niewłaściwej lokalizacji, przekaże go przez nieostrożnie zaprojektowany interfejs IPC albo nadpisze własne pliki pod wpływem niezweryfikowanego wejścia, to sandbox nie zatrzyma tego błędu. Podobnie nie pomoże wtedy, gdy aplikacja trzyma dane w miejscu, które później trafia do backupu, albo gdy używa mechanizmu współdzielenia plików bez kontroli ścieżek i nazw. Warto też pamiętać o jeszcze jednym ograniczeniu: sandbox chroni głównie granicę między aplikacjami, a nie granicę między aplikacją a jej własnym przejętym procesem. Jeżeli przeciwnik uzyska możliwość wykonywania kodu w kontekście danej aplikacji, to staje się niestety uczestnikiem tej samej przestrzeni zaufania, w której działają wszystkie lokalne decyzje programu. Dlatego bezpieczeństwo storage na Androidzie nie może opierać się wyłącznie na założeniu, że prywatny katalog aplikacji rozwiązuje problem.

#slide 75
## layout
definition
## term
Android Keystore
## definition
Mechanizm systemowy służący do generowania i używania kluczy kryptograficznych w sposób, który może uniemożliwiać ich eksport i ograniczać warunki użycia zależnie od właściwości systemu i urządzenia.
## teleprompter:
Android Keystore trzeba rozumieć precyzyjnie, bo wokół niego narosło wiele uproszczeń. To nie jest po prostu specjalny katalog na sekrety i nie jest uniwersalnym sejfem na wszystkie dane aplikacji. Jego podstawowym zadaniem jest obsługa kluczy kryptograficznych. Klucz może zostać wygenerowany tak, aby aplikacja korzystała z niego przez operacje kryptograficzne dostarczane przez system, bez konieczności odczytu jego surowej wartości. Ta różnica jest bardzo ważna, ponieważ zmienia pytanie z gdzie trzymam klucz na czy aplikacja kiedykolwiek musi zobaczyć klucz jako zwykły ciąg bajtów. W silniejszym modelu odpowiedź brzmi nie. Android pozwala też wiązać klucz z określonymi ograniczeniami, na przykład z wymaganiem uwierzytelnienia użytkownika, określonym przeznaczeniem klucza albo cechami środowiska wykonania. Nie znaczy to jednak, że Keystore sam z siebie gwarantuje pełne bezpieczeństwo całej aplikacji. Gwarantuje jedynie określone własności dotyczące materiału kluczowego i warunków jego użycia, a reszta nadal zależy od architektury programu, od jakości implementacji i od rzeczywistych właściwości danego urządzenia.

#slide 76
## layout
title
## slide title
Klucz nieeksportowalny
## subtitle
Największa wartość secure storage pojawia się wtedy, gdy aplikacja może używać klucza, ale nie może go odczytać
## teleprompter:
Jednym z najważniejszych pojęć w praktyce mobilnego bezpieczeństwa jest klucz nieeksportowalny. W zwykłym modelu aplikacja ma sekret jako dane i sama przekazuje go bibliotekom kryptograficznym. Taki projekt jest kruchy, bo gdziekolwiek aplikacja potrafi odczytać klucz, tam może go też przez błąd, log, crash, debug albo podatność pośrednio ujawnić. Model nieeksportowalny działa inaczej. System przechowuje materiał kluczowy we własnym mechanizmie, a aplikacja otrzymuje jedynie możliwość zażądania operacji: podpisania, odszyfrowania albo zaszyfrowania. Dzięki temu znacznie trudniej jest przeciwnikowi po prostu ukraść klucz i używać go poza urządzeniem. To bardzo silna własność, ale trzeba widzieć jej granicę. Brak eksportu nie oznacza braku nadużycia. Jeżeli proces aplikacji został przejęty, napastnik może próbować wywoływać te same operacje, do których prawo ma legalny kod aplikacji. Nie wyciąga wtedy klucza jako bajtów, ale nadal może wykorzystać go funkcjonalnie. To rozróżnienie między ekstrakcją a użyciem będzie powracało wielokrotnie, bo właśnie ono najlepiej pokazuje, gdzie kończy się moc secure storage, a zaczyna problem zaufania do logiki aplikacji.

#slide 77
## layout
bullet
## slide title
Hardware-backed storage, TEE i StrongBox
## bullets
- Hardware-backed keystore oznacza, że ochrona klucza opiera się na mechanizmach sprzętowych, a nie wyłącznie programowych
- TEE izoluje część operacji i materiału kluczowego od zwykłego środowiska systemowego
- StrongBox to jeszcze silniej odseparowany komponent bezpieczeństwa na części urządzeń
- Nie każde urządzenie oferuje ten sam poziom ochrony sprzętowej
- Z punktu widzenia backendu i audytu trzeba rozróżniać deklarowaną funkcję od rzeczywistego poziomu gwarancji
## teleprompter:
W dokumentacji Androida łatwo natknąć się na pojęcia hardware-backed, TEE albo StrongBox i potraktować je jako synonimy ogólnego bezpieczeństwa. Lepiej widzieć tu warstwy. Hardware-backed storage oznacza, że klucz jest chroniony z użyciem właściwości sprzętowych urządzenia, a nie tylko przez kod systemu operacyjnego. TEE, czyli Trusted Execution Environment, daje odseparowaną przestrzeń dla pewnych operacji i części materiału kluczowego. StrongBox idzie jeszcze dalej i na wspieranych urządzeniach korzysta z dedykowanego, silniej izolowanego komponentu bezpieczeństwa. Dla projektanta aplikacji najważniejsza jest jednak praktyczna konsekwencja: różne urządzenia są nierówne. Ta sama aplikacja może działać na telefonie z bardzo mocną ochroną klucza i na urządzeniu, które oferuje słabszy model. Jeśli architektura systemu ma zależeć od właściwości storage, trzeba umieć rozpoznać, jaki poziom ochrony rzeczywiście został uzyskany. Inaczej bardzo łatwo pomylić dostępność API z równoważnością gwarancji bezpieczeństwa, a to byłby błąd zarówno projektowy, jak i audytowy.

#slide 78
## layout
title
## slide title
KeyMint i nierówność urządzeń
## subtitle
To samo API nie oznacza tego samego poziomu zaufania w całym ekosystemie Androida
## teleprompter:
Jednym z mniej intuicyjnych problemów Androida jest to, że bezpieczeństwo aplikacji nie zależy tylko od kodu samej aplikacji. Zależy również od jakości i właściwości konkretnego urządzenia. Warstwa KeyMint i związane z nią mechanizmy określają, w jaki sposób urządzenie deklaruje i realizuje własności kluczy, ich pochodzenie oraz ograniczenia użycia. Dla wykładu najważniejsze nie jest zapamiętanie wszystkich szczegółów interfejsu, tylko zrozumienie skutku architektonicznego. Programista nie może zakładać, że skoro użył Keystore, to wszędzie uzyskał jednakowo silny rezultat. W praktyce trzeba pytać, czy klucz jest sprzętowo wspierany, czy istnieje wiarygodna attestation, czy urządzenie oferuje komponent typu StrongBox i czy polityka systemu odpowiada temu, czego oczekuje backend albo model zagrożeń. Android jest ekosystemem zróżnicowanym, a zróżnicowanie urządzeń zawsze osłabia pokusę prostych twierdzeń. Secure storage na Androidzie jest mocne tam, gdzie właściwości urządzenia naprawdę to uzasadniają, a nie tam, gdzie sama aplikacja tylko zakłada najlepszy scenariusz.

#slide 79
## layout
definition
## term
User authentication gating
## definition
Powiązanie użycia klucza z wcześniejszym uwierzytelnieniem użytkownika na urządzeniu, tak aby sama obecność aplikacji nie wystarczała do wykonania operacji kryptograficznej.
## teleprompter:
Nie każdy lokalny sekret powinien być używalny bez żadnego udziału użytkownika. Dlatego Android pozwala wiązać użycie klucza z faktem, że użytkownik niedawno uwierzytelnił się na urządzeniu, na przykład PIN-em, hasłem urządzenia albo biometrią zgodnie z polityką systemu. Taki mechanizm bardzo zmienia praktyczny profil ryzyka. Kradzież samego odblokowanego telefonu przez krótki moment i przejęcie sesji aplikacji to nie to samo, co uzyskanie możliwości wykonania operacji wymagającej świeżego potwierdzenia obecności użytkownika. Warto jednak pilnować precyzji. Gating nie oznacza, że biometria staje się nowym sekretem usługi. Zwykle oznacza tylko, że system pozwala odblokować użycie klucza już istniejącego na urządzeniu. To istotna różnica, bo wpływa na to, jak projektuje się odzyskiwanie dostępu, zmianę urządzenia i reakcję na utratę telefonu. Gating pomaga więc ograniczyć użycie sekretu, ale nie zmienia natury tego sekretu ani nie zastępuje serwerowego modelu uwierzytelniania tam, gdzie potrzebne jest zaufanie usługi do tożsamości użytkownika.

#slide 80
## layout
title
## slide title
Key attestation
## subtitle
Backend nie powinien ufać wyłącznie deklaracji klienta, że klucz powstał w bezpiecznym środowisku
## teleprompter:
Jeżeli system ma opierać jakąś decyzję na tym, że klucz został wygenerowany albo przechowywany w określonych warunkach bezpieczeństwa, to samo stwierdzenie aplikacji nie wystarcza. Potrzebny jest mechanizm, który pozwala backendowi uzyskać wiarygodne informacje o właściwościach klucza i środowiska. Tu pojawia się attestation. W praktyce chodzi o to, by serwer nie wierzył na słowo, że ma do czynienia z kluczem wygenerowanym sprzętowo, kluczem nieeksportowalnym albo kluczem związanym z określoną polityką użycia. Attestation nie rozwiązuje wszystkich problemów zaufania do klienta, ale pozwala ograniczyć pewną klasę błędów: takich, w których aplikacja albo urządzenie tylko udają określony poziom ochrony. To znowu dobrze pokazuje architektoniczną lekcję. Bezpieczne przechowywanie lokalne zaczyna mieć znaczenie systemowe dopiero wtedy, gdy backend potrafi odróżnić zwykłe twierdzenie klienta od wiarygodnego dowodu właściwości klucza. W przeciwnym razie secure storage pozostaje lokalną cechą implementacji, której serwer nie umie rozsądnie wykorzystać.

#slide 81
## layout
title
## slide title
Czego Android Keystore nie rozwiązuje
## subtitle
Chroni klucz przed prostą ekstrakcją, ale nie naprawia błędnej architektury aplikacji
## teleprompter:
To jest jeden z najważniejszych slajdów całego bloku. Android Keystore daje bardzo cenne własności, ale łatwo przypisać mu więcej, niż naprawdę zapewnia. Nie rozwiązuje problemu złej logiki autoryzacyjnej. Nie rozwiązuje błędnej obsługi plików, URI i IPC. Nie naprawia logowania sekretów, niewłaściwego backupu ani złego projektu tokenów sesyjnych. Nie sprawi też, że aplikacja nagle stanie się odporna na przejęcie własnego procesu. Jeżeli architektura używa silnie chronionego klucza tylko po to, by odszyfrować długotrwały sekret, który następnie aplikacja trzyma w pamięci, zapisuje do pliku tymczasowego albo przekazuje do nieostrożnego modułu, to realny poziom bezpieczeństwa może spaść bardzo szybko. Keystore jest więc narzędziem o wąskim, ale ważnym zakresie działania. Trzeba rozumieć dokładnie, co chroni i czego nie dotyka. Gdy ten zakres zostaje rozszerzony w wyobraźni projektanta, powstaje bardzo niebezpieczna iluzja bezpieczeństwa: przekonanie, że skoro klucz siedzi w czymś systemowym, to reszta aplikacji nie wymaga już równie rygorystycznego projektu.

#slide 82
## layout
title
## slide title
Przejęty proces aplikacji nadal może używać klucza
## subtitle
Ochrona przed eksportem nie jest tożsama z ochroną przed nadużyciem legalnych operacji
## teleprompter:
Oficjalna dokumentacja Androida bardzo wyraźnie zaznacza granicę, o której trzeba mówić bez niedomówień. Jeżeli atakujący uzyska możliwość działania w procesie aplikacji, może nadal wywoływać operacje kryptograficzne dostępne dla tej aplikacji, nawet jeśli sam klucz nie jest eksportowalny. To jest niezwykle ważne, bo porządkuje myślenie o secure storage. Nie chodzi tylko o to, czy sekret da się skopiować na inne urządzenie. Chodzi też o to, czy da się wymusić jego użycie tam, gdzie legalnie używa go sama aplikacja. Przejęty proces może podpisywać, odszyfrowywać albo odblokowywać dane dokładnie tak długo, jak długo system uważa, że żądania pochodzą od uprawnionej aplikacji i spełnione są warunki użycia klucza. Dlatego walka o bezpieczeństwo nie kończy się na wyborze API do storage. Obejmuje także hardening aplikacji, ograniczanie powierzchni ataku, kontrolę debugowalności, bezpieczne aktualizacje, ograniczenie niepotrzebnych komponentów IPC i rozsądne projektowanie czasu życia sekretów. Secure storage kupuje bardzo dużo, ale nie kupuje odporności na przejęcie całej logiki klienta.

#slide 83
## layout
title
## slide title
Błędne I/O i IPC obchodzą nawet poprawny storage
## subtitle
Sekret można stracić nie tylko przez zły magazyn, lecz także przez zły przepływ danych
## teleprompter:
W praktyce mobilnej wiele incydentów nie zaczyna się od pytania, gdzie klucz został zapisany, tylko od pytania, jak aplikacja obchodzi się z danymi pochodzącymi z zewnątrz i jak wystawia własne interfejsy. Plik pobrany z zewnętrznego źródła, URI przekazane przez inny komponent, nieostrożny ContentProvider, błędna walidacja ścieżek, tymczasowy plik wrażliwych danych albo eksportowany komponent bez właściwej kontroli to wszystko może obejść sens nawet dobrze dobranego secure storage. Jeśli aplikacja trzyma token w poprawnym miejscu, ale potem sama nadpisuje swój katalog, ujawnia dane przez błędne kopiowanie albo przekazuje sekret do nieufnego modułu, to realna ochrona znika. To bardzo ważne dla zrozumienia systemów mobilnych. Storage jest tylko jednym odcinkiem łańcucha życia sekretu. Trzeba jeszcze kontrolować wejście, wyjście, formaty danych, tymczasowe artefakty, integracje z bibliotekami i mechanizmy współdzielenia. W przeciwnym razie projektant skupia się na sejfie, a ignoruje wszystkie korytarze prowadzące do sejfu i z sejfu.

#slide 84
## layout
title
## slide title
EncryptedSharedPreferences
## subtitle
Dobra warstwa ochronna dla części danych, ale nie zamiennik dla właściwego modelu klucza i sekretu
## teleprompter:
Mechanizmy takie jak EncryptedSharedPreferences są użyteczne, ale trzeba przypisywać im dokładnie to, co naprawdę oferują. Pozwalają one zaszyfrować pewne dane aplikacyjne przy użyciu kluczy zarządzanych przez platformę, co jest zdecydowanie lepsze niż trzymanie wartości jawnie w zwykłych preferencjach. Problem zaczyna się wtedy, gdy projektant uznaje ten mechanizm za rozwiązanie wszystkich problemów storage. To nadal nie odpowiada na pytanie, czy dana wartość w ogóle powinna istnieć lokalnie, jak długo ma żyć, czy nie jest jedynie pochodną innego sekretu, czy nie trafi do backupu, czy nie zostanie ujawniona przez logowanie, crash reporting albo błędne API współdzielenia. EncryptedSharedPreferences pomaga chronić dane w spoczynku w obrębie aplikacji, ale nie zmienia ich semantyki. Token pozostaje tokenem, refresh token pozostaje bardzo wrażliwym artefaktem, a lokalne hasło nadal nie powinno być przechowywane tylko dlatego, że da się je zaszyfrować. To narzędzie jest wartościowe, kiedy wspiera poprawny projekt, a nie wtedy, gdy ma ukryć błędną decyzję architektoniczną.

#slide 85
## layout
bullet
## slide title
Gdzie jeszcze uciekają sekrety na Androidzie
## bullets
- W logach aplikacji i raportach awarii
- W backupie danych aplikacji lub w eksporcie użytkownika
- W plikach tymczasowych i cache'u
- W nieostrożnie udostępnianych URI, załącznikach i mechanizmach share
- W artefaktach deweloperskich, testowych i debugowych
## teleprompter:
Najbardziej zdradliwe wycieki sekretów często nie mają nic wspólnego z głównym magazynem danych. Dzieją się na obrzeżach systemu, tam gdzie zespół przestaje myśleć o bezpieczeństwie, bo jest zajęty diagnostyką, integracją albo wygodą użytkownika. Logi, raporty awarii i zewnętrzna telemetria bardzo łatwo przechwytują tokeny, identyfikatory sesji i szczegóły odpowiedzi API. Backup danych aplikacji może utrwalić to, co miało żyć tylko chwilowo. Pliki tymczasowe oraz cache są wygodne dla programisty, ale często nie przechodzą tej samej dyscypliny projektowej, co główny storage. Mechanizmy share i eksportu plików także bywają traktowane jak neutralne narzędzia interfejsu, choć w praktyce mogą stać się drogą wyniesienia sekretu poza granice aplikacji. Wreszcie jest jeszcze świat buildów testowych, flag debugowych i bibliotek pomocniczych. Tam bardzo często powstają skróty, które nie trafiają do dokumentacji architektury, ale trafiają do realnej powierzchni ataku. Dlatego przegląd bezpieczeństwa lokalnych sekretów musi obejmować nie tylko sejf, lecz cały ekosystem miejsc, do których aplikacja może sama wynieść własne dane.

#slide 86
## layout
title
## slide title
Wersja systemu i jakość implementacji OEM
## subtitle
Android to ekosystem, więc własności bezpieczeństwa zależą także od platformy, a nie tylko od kodu aplikacji
## teleprompter:
W środowisku webowym programista często myśli przede wszystkim o swoim kodzie, bibliotece i serwerze. W Androidzie trzeba do tego dodać jeszcze jedną warstwę zmienności: urządzenie i jego implementację platformową. Dwa telefony mogą uruchamiać tę samą aplikację, a mimo to oferować różny poziom ochrony klucza, różne wsparcie dla komponentów sprzętowych, różny stan aktualizacji bezpieczeństwa i różną wiarygodność właściwości deklarowanych przez system. To nie jest detal poboczny. Jeśli architektura logowania lub ochrony lokalnych danych zakłada określony poziom cech sprzętowych, trzeba brać pod uwagę, że część ekosystemu tych cech nie dostarczy albo dostarczy je słabiej. Z tego powodu bezpieczny projekt mobilny musi być odporny na heterogeniczność. Nie wolno budować bezpieczeństwa na nieudokumentowanym założeniu, że każdy klient działa na urządzeniu klasy premium z idealnie zaimplementowanym hardware-backed storage. W praktyce oznacza to potrzebę pomiaru, attestation, bezpiecznych ustawień domyślnych i polityk degradacji, które nie zamieniają słabszych urządzeń w całkowicie niebronione punkty systemu.

#slide 87
## layout
bullet
## slide title
Co sprawdzać w przeglądzie bezpieczeństwa aplikacji Android
## bullets
- Czy aplikacja przechowuje lokalnie tylko te sekrety, które są rzeczywiście konieczne
- Czy klucze są nieeksportowalne i czy wiadomo, jaki mają poziom ochrony sprzętowej
- Czy istnieje kontrola backupu, logów, plików tymczasowych i eksportowanych komponentów
- Czy wejście z zewnątrz nie pozwala nadpisywać lub ujawniać danych aplikacji
- Czy backend rozumie właściwości klienta, zamiast ślepo ufać jego deklaracjom
## teleprompter:
Dobry przegląd bezpieczeństwa Androida nie może zatrzymać się na sprawdzeniu, czy w kodzie pojawia się słowo Keystore. To byłaby kontrola czysto ceremonialna. Trzeba zacząć wcześniej: jakie sekrety w ogóle istnieją lokalnie, które z nich są naprawdę potrzebne, a które zostały zapisane wyłącznie dla wygody albo przez przypadek. Następnie trzeba ocenić model klucza: czy jest nieeksportowalny, czy ma sensowne ograniczenia użycia, czy da się potwierdzić poziom ochrony sprzętowej i czy aplikacja nie degraduje go przez późniejsze obchodzenie się z danymi. Równie ważna jest kontrola całej otoczki: backupu, logów, cache'u, tymczasowych plików, komponentów eksportowanych i danych wejściowych z innych aplikacji. Wreszcie trzeba połączyć perspektywę klienta i backendu. Jeżeli serwer nie umie sensownie interpretować sygnałów o właściwościach urządzenia i klucza, to część zabezpieczeń po stronie klienta pozostaje niewykorzystana. Przegląd bezpieczeństwa Androida jest więc oceną całego łańcucha życia sekretu, a nie wyłącznie obecności jednego API.

#slide 88
## layout
title
## slide title
Wniosek po części androidowej
## subtitle
Secure storage jest potrzebne, ale nie zastępuje bezpiecznej architektury aplikacji i bezpiecznego backendu
## teleprompter:
Po przejściu przez Androida warto zatrzymać jedną myśl przewodnią. Bezpieczne przechowywanie lokalne ma ogromną wartość wtedy, gdy ogranicza eksport klucza, pozwala sterować warunkami jego użycia i daje systemowi oraz backendowi wiarygodne sygnały o poziomie ochrony. To bardzo dużo. Ale równie ważne jest to, czego nie robi. Nie projektuje za nas modelu tokenów. Nie waliduje danych z zewnętrznych providerów. Nie usuwa skutków debugowania, logowania i złej obsługi backupu. Nie gwarantuje, że przejęty proces aplikacji nie będzie mógł wywołać legalnych operacji kryptograficznych. Wnioskiem nie jest więc sceptycyzm wobec Keystore, lecz precyzja. Trzeba korzystać z niego tam, gdzie naprawdę wzmacnia system, i jednocześnie nie przypisywać mu odpowiedzialności za błędy, które leżą całkowicie poza jego zakresem. Dopiero z takim nastawieniem można przejść do iOS. Tam mechanizmy są inne, część gwarancji jest silniejsza, ale ogólna lekcja pozostaje zaskakująco podobna: mocny storage jest warunkiem potrzebnym, lecz nigdy nie jest warunkiem wystarczającym.

#slide 89
## layout
title
## slide title
iOS storage landscape
## subtitle
Sandbox, pliki, plist, Keychain i Secure Enclave mają różne role i różne gwarancje
## teleprompter:
Tak samo jak na Androidzie, także na iOS nie istnieje jedno pojęcie lokalnego storage, które można bezpiecznie stosować do wszystkiego. Aplikacja ma własny sandbox i może zapisywać pliki, ustawienia, bazy oraz inne dane robocze. To jednak nie są mechanizmy projektowane specjalnie do trwałego przechowywania najbardziej wrażliwych sekretów tożsamości. Rolę uprzywilejowanego magazynu pełni Keychain, a w pewnych scenariuszach dochodzi do tego jeszcze Secure Enclave, czyli odseparowany komponent odpowiedzialny za szczególnie wrażliwe operacje i materiał kluczowy. Trzeba więc od razu odróżnić dwa porządki. Pierwszy to zwykłe dane aplikacyjne, które mogą być chronione przez ogólny model ochrony danych systemu. Drugi to sekrety, dla których Apple przewiduje specjalny mechanizm z własnymi klasami dostępności, powiązaniem z backupem i dodatkowymi właściwościami ochrony. Jeżeli te porządki się pomiesza, łatwo popełnić ten sam błąd co na Androidzie: uznać, że skoro plik leży w sandboxie, to nadaje się do przechowywania wszystkiego. W iOS również trzeba dobierać mechanizm do roli sekretu.

#slide 90
## layout
title
## slide title
Dlaczego Keychain jest inną klasą mechanizmu
## subtitle
To nie tylko wygodne API, lecz systemowy model ochrony sekretów o innych własnościach niż zapis pliku
## teleprompter:
Keychain nie jest po prostu lepszym plikiem ani szyfrowanym słownikiem aplikacji. Jego znaczenie polega na tym, że system traktuje przechowywane w nim elementy jako sekrety wymagające innego modelu ochrony niż zwykłe dane aplikacyjne. Stąd wynikają praktyczne konsekwencje: własne klasy dostępności, odmienne relacje z blokadą urządzenia, szczególne znaczenie dla tokenów i haseł oraz integracja z szerszym modelem ochrony danych Apple. W projektowaniu aplikacji mobilnej to rozróżnienie ma ogromne znaczenie. Jeśli zespół traktuje Keychain jak wygodniejsze miejsce zapisu dowolnych danych, traci z pola widzenia pytanie o semantykę tego, co zapisuje. Tymczasem właśnie semantyka jest kluczowa. Sekret uwierzytelniający, refresh token, klucz do odszyfrowania lokalnej bazy i zwykła preferencja interfejsu nie powinny być przechowywane według tej samej logiki. Keychain jest mocny dlatego, że platforma oferuje dla niego odrębny model bezpieczeństwa. Ten model trzeba jednak świadomie wykorzystać, a nie jedynie wywołać API i założyć, że od tej chwili problem zniknął.

#slide 91
## layout
definition
## term
Keychain
## definition
Systemowy magazyn sekretów na iOS przeznaczony do przechowywania takich danych jak hasła, tokeny i krótkie materiały kluczowe, chroniony według zasad dostępności i ochrony danych określonych przez platformę.
## teleprompter:
Gdy mówimy o Keychainie, warto zachować równowagę między prostotą a dokładnością. To systemowy magazyn sekretów, ale nie oznacza to, że każda tajna informacja powinna tam trafić ani że wszystko, co tam trafi, automatycznie otrzymuje optymalny poziom ochrony. Keychain najlepiej nadaje się do przechowywania danych krótkich, bardzo wrażliwych i semantycznie powiązanych z tożsamością lub dostępem: haseł, tokenów, tajnych kluczy aplikacyjnych w określonych scenariuszach. Jego siła bierze się z tego, że Apple nie traktuje tych danych jak zwykłych plików użytkownika, lecz obejmuje je własnym systemem ochrony, klasami dostępności i związkiem z blokadą urządzenia. Dla projektanta aplikacji najważniejsze jest to, że Keychain wymusza myślenie nie tylko o tym, co przechowuję, ale kiedy to ma być dostępne, jak ma się zachowywać po restarcie, po odblokowaniu, w backupie i przy odzyskiwaniu urządzenia. To właśnie te pytania oddzielają dojrzałe użycie Keychainu od prostego odruchu wrzućmy to do bezpiecznego magazynu.

#slide 92
## layout
title
## slide title
Secure Enclave
## subtitle
Izolacja części operacji i materiału kluczowego od głównego procesora wzmacnia ochronę, ale nie usuwa błędów aplikacji
## teleprompter:
Secure Enclave jest jednym z najbardziej rozpoznawalnych elementów bezpieczeństwa Apple, dlatego tym bardziej trzeba mówić o nim precyzyjnie. Jego podstawową wartością jest izolacja od głównego procesora dla wybranych operacji i materiału kluczowego. W praktyce wzmacnia to ochronę kluczy, ogranicza możliwość ich prostego przejęcia i pozwala zbudować mocniejsze powiązanie między lokalnym odblokowaniem a użyciem sekretu. Jednak nawet tutaj trzeba zachować ostrożność. Secure Enclave nie naprawia złej architektury aplikacji. Nie sprawia, że token źle przechowywany gdzie indziej staje się bezpieczny. Nie powstrzyma aplikacji przed zalogowaniem sekretu albo przed nadużyciem legalnego dostępu przez przejętą logikę programu. Jego rola jest bardzo konkretna i dlatego bardzo cenna. Wzmacnia ochronę określonych kluczy i operacji. Ale tak jak w Androidzie, również tutaj silny komponent platformy jest tylko jedną z warstw. Jeżeli reszta aplikacji jest zaprojektowana źle, to nawet bardzo mocny komponent sprzętowy może zostać w praktyce wykorzystany jedynie do ochrony czegoś, co później i tak zostanie bezpiecznie wyprowadzone poza jego granice.

#slide 93
## layout
title
## slide title
Ochrona metadanych i wartości wpisu
## subtitle
Na iOS nawet wewnątrz Keychainu nie wszystkie elementy ochrony działają identycznie dla każdej części rekordu
## teleprompter:
To bardzo ciekawy fragment modelu Apple, bo pokazuje, że secure storage nie jest jednolitą czarną skrzynką. Ochrona wpisu keychainu obejmuje zarówno jego wartość, jak i metadane potrzebne systemowi do zarządzania i wyszukiwania elementów. Apple opisuje te warstwy odrębnie, co jest ważne dydaktycznie, bo pomaga zrozumieć, że w prawdziwych systemach bezpieczeństwo to zawsze kompromis między izolacją, użytecznością i wydajnością. Nie wszystko działa w identyczny sposób dla każdego aspektu wpisu, ponieważ system musi jednocześnie chronić sekret i umożliwiać sprawne operacje na magazynie. Dla projektanta aplikacji praktyczna lekcja jest taka, że nie należy upraszczać działania Keychainu do hasła wszystko tam jest po prostu zaszyfrowane. To bardziej złożony model, którego własności trzeba znać przynajmniej na poziomie konsekwencji. Im bardziej rozumie się, że platforma chroni różne części wpisu w różny sposób, tym łatwiej unikać zbyt szerokich założeń i tym lepiej można dopasować storage do znaczenia przechowywanego sekretu.

#slide 94
## layout
title
## slide title
Klasy dostępności
## subtitle
Najważniejsza decyzja projektowa przy Keychainie dotyczy często nie tego, czy go użyć, lecz jaką dostępność nadać wpisowi
## teleprompter:
W praktyce iOS najwięcej błędów nie bierze się z całkowitego braku Keychainu, tylko ze złego wyboru klasy dostępności. To ona określa, kiedy dany sekret ma być osiągalny: po pierwszym odblokowaniu, tylko gdy urządzenie jest odblokowane, czy według jeszcze innej polityki powiązanej z ochroną danych i migracją. Ta decyzja ma ogromne skutki praktyczne. Zbyt szeroka dostępność może uczynić sekret używalnym w momentach, w których nie powinien być osiągalny. Zbyt restrykcyjna może złamać działanie aplikacji w tle, po restarcie albo przy określonym przepływie synchronizacji. Właśnie tutaj widać, że secure storage nie jest tylko sprawą szyfrowania. To także projektowanie czasu życia i okna dostępności sekretu. Klasa dostępności staje się więc parametrem bezpieczeństwa tak samo ważnym jak wybór algorytmu w serwerowym password hashingu. W obu przypadkach błędny wybór nie musi wyglądać jak jawna podatność w kodzie. Może po prostu przesunąć system w stronę zbyt szerokiego zaufania albo zbyt dużej ekspozycji sekretu.

#slide 95
## layout
title
## slide title
Kiedy sekret jest dostępny po starcie urządzenia
## subtitle
Granica między restartem, pierwszym odblokowaniem i dalszym działaniem systemu ma duże znaczenie bezpieczeństwa
## teleprompter:
Dla wielu projektów mobilnych kluczowe jest pytanie nie tylko gdzie sekret jest przechowywany, ale od jakiego momentu po uruchomieniu urządzenia może zostać użyty. To nie jest detal systemowy, tylko realny parametr bezpieczeństwa. Inne ryzyko wiąże się z sekretem, który staje się osiągalny dopiero po pierwszym odblokowaniu przez użytkownika, a inne z takim, który może być dostępny wcześniej lub pozostaje używalny szerzej w trakcie późniejszej pracy systemu. Decyzja ta wpływa na zachowanie aplikacji po restarcie, na możliwość działania w tle, na scenariusze odzyskiwania urządzenia i na konsekwencje kradzieży albo fizycznego przejęcia telefonu. Dla projektanta aplikacji praktyczny sens jest prosty: nie wolno mówić, że sekret jest bezpiecznie zapisany, dopóki nie wiadomo jeszcze, w jakich fazach życia urządzenia będzie on dostępny. To właśnie różni dojrzałe projektowanie storage od podejścia czysto API-centric, w którym sukcesem jest samo zapisanie czegoś do Keychainu bez refleksji nad dalszym cyklem życia tego wpisu.

#slide 96
## layout
title
## slide title
Backup, synchronizacja i odzyskiwanie urządzenia
## subtitle
Bezpieczeństwo sekretu zależy nie tylko od jego magazynu, lecz także od relacji z kopią zapasową i migracją między urządzeniami
## teleprompter:
Jedna z najważniejszych granic bezpieczeństwa na iOS przebiega między samym Keychainem a szerszym modelem backupu, synchronizacji i odzyskiwania urządzenia. To właśnie tutaj bardzo łatwo o błędne założenie, że sekret raz zapisany w bezpiecznym magazynie będzie zachowywał się tak samo we wszystkich scenariuszach życia konta i telefonu. Tymczasem pytania o to, czy element jest migrowany, czy może zostać odtworzony z backupu, jak zachowuje się przy zmianie urządzenia i jakie relacje ma z iCloud albo z procesem recovery, mają bezpośredni wpływ na bezpieczeństwo. Czasem wzmacniają wygodę użytkownika, ale równocześnie rozszerzają powierzchnię ryzyka. To bardzo cenna lekcja dla całego wykładu. Storage nie kończy się na zapisie. Obejmuje również podróż sekretu przez cały cykl życia urządzenia: tworzenie, użycie, backup, migrację, odtworzenie i usunięcie. Jeśli którykolwiek z tych etapów zostanie źle zrozumiany, można zbudować aplikację, która wygląda na bezpieczną w normalnym użyciu, a traci ochronę dokładnie w momencie odzyskiwania po awarii albo przenoszenia konta na nowe urządzenie.

#slide 97
## layout
definition
## term
This device only
## definition
Klasa ochrony wpisu Keychain, w której sekret pozostaje związany z konkretnym urządzeniem i po odtworzeniu backupu na innym urządzeniu nie daje się użyć w tej samej postaci.
## teleprompter:
W praktyce iOS jedno z najważniejszych rozróżnień dotyczy tego, czy sekret ma tylko przetrwać na urządzeniu, czy także migrować wraz z użytkownikiem na nowe urządzenie. Właśnie dlatego atrybuty typu This device only są tak istotne. Ich sens nie polega jedynie na dodaniu kolejnego wariantu API, lecz na świadomym ograniczeniu mobilności sekretu. Apple opisuje, że odpowiedniki klas z dopiskiem This device only są chronione w taki sposób, aby po skopiowaniu z urządzenia w ramach backupu były bezużyteczne po odtworzeniu na innym urządzeniu. To fundamentalna decyzja architektoniczna. Jeśli dany sekret ma silnie wiązać się z konkretnym egzemplarzem urządzenia, z lokalnym stanem ochrony i z fizyczną kontrolą użytkownika nad telefonem, to migracja może być wadą, a nie zaletą. Z drugiej strony zbyt szerokie użycie tej klasy może utrudnić zmianę telefonu, odzyskiwanie konta albo transparentną migrację aplikacji. W systemach mobilnych bezpieczeństwo bardzo często jest właśnie sztuką wybierania, które sekrety powinny podróżować z użytkownikiem, a które nie powinny opuszczać jednego urządzenia nawet kosztem wygody.

#slide 98
## layout
title
## slide title
Backup i recovery zmieniają model zagrożeń
## subtitle
Sekret przechowywany poprawnie w normalnej pracy może zachowywać się inaczej w scenariuszu odtworzenia urządzenia
## teleprompter:
Bardzo wiele analiz bezpieczeństwa zatrzymuje się na pytaniu, czy sekret jest bezpieczny w normalnym użyciu aplikacji. To za mało. W systemach mobilnych równie ważne są sytuacje graniczne: backup, przywrócenie urządzenia, migracja na nowy telefon, odzyskiwanie po awarii i odtwarzanie środowiska użytkownika. W tych momentach nagle okazuje się, że bezpieczeństwo lokalnego sekretu zależy nie tylko od magazynu, ale od całego ekosystemu usług platformowych. Sekret, który w zwykłej pracy aplikacji jest związany z blokadą urządzenia i z określoną klasą ochrony, może uzyskać inne własności po stronie kopii zapasowej, synchronizacji albo migracji. To nie znaczy, że backup jest czymś z natury niebezpiecznym. Oznacza jednak, że architekt musi osobno przeanalizować scenariusz normalnego działania i scenariusz odzyskiwania. Dopiero wtedy widać, czy wygoda użytkownika nie została osiągnięta kosztem zbyt szerokiego przenoszenia sekretu, albo odwrotnie, czy zbyt restrykcyjna polityka nie uniemożliwia sensownego odtworzenia stanu po utracie urządzenia.

#slide 99
## layout
title
## slide title
Lokalne uwierzytelnienie nie jest tożsamością wobec usługi
## subtitle
Biometria, PIN urządzenia i odblokowanie klucza mówią coś o obecności użytkownika przy telefonie, a nie o całym modelu zaufania systemu
## teleprompter:
To rozróżnienie jest absolutnie kluczowe dla bezpieczeństwa mobilnego. Uwierzytelnienie lokalne, takie jak biometria albo kod urządzenia, mówi głównie o tym, że system uznał obecną osobę za uprawnioną do odblokowania określonej funkcji telefonu. Nie znaczy to jeszcze, że usługa sieciowa powinna na tej podstawie automatycznie ufać tożsamości użytkownika w każdym sensie. Lokalna obecność, odblokowanie dostępu do klucza i zdalne uwierzytelnienie wobec backendu to trzy różne warstwy. Czasem da się je elegancko powiązać, lecz nie wolno ich utożsamiać. Jeśli aplikacja zaczyna traktować wynik lokalnego odblokowania jak pełnoprawny substytut serwerowego modelu tożsamości, bardzo łatwo pojawiają się błędy w odzyskiwaniu konta, w zmianie urządzenia, w obsłudze wycofania dostępu i w analizie nadużyć. Secure storage pomaga ograniczyć użycie sekretu do sytuacji, w których użytkownik jest obecny, ale to nadal nie jest kompletna odpowiedź na pytanie, czy i dlaczego backend ma ufać temu stanowi.

#slide 100
## layout
bullet
## slide title
Czego Keychain i Secure Enclave nie rozwiązują
## bullets
- Nie naprawiają złej architektury tokenów i sesji
- Nie cofają skutków logowania sekretów przez aplikację lub biblioteki
- Nie chronią przed błędnym doborem klas dostępności i migracji
- Nie zastępują decyzji o backupie, recovery i rotacji sekretów
- Nie eliminują skutków przejęcia samej logiki aplikacji
## teleprompter:
Wokół bezpiecznego magazynu na iOS łatwo zbudować mitologię, w której sam wybór Keychainu i Secure Enclave kończy temat. To nieprawda. Nawet bardzo mocny mechanizm platformowy nie naprawi złego modelu sesji, w którym refresh token żyje zbyt długo, nie jest rotowany albo bywa rejestrowany przez warstwy diagnostyczne. Nie naprawi też błędów semantycznych, gdy zespół wybiera klasę dostępności dlatego, że coś działa wygodniej, a nie dlatego, że odpowiada ona ryzyku i cyklowi życia sekretu. Keychain nie zdecyduje również za architekta, czy sekret ma migrować na nowe urządzenie, czy ma wygasnąć przy zmianie środowiska, czy wymagać ponownej aktywacji po odzyskaniu urządzenia. Najgłębsze ograniczenie jest jeszcze inne. Jeżeli legalny kod aplikacji, działający w swoim własnym procesie, potrafi pobrać albo użyć sekret w określonym scenariuszu, to przejęta logika aplikacji będzie próbowała wykorzystać dokładnie ten sam legalny interfejs. Platforma wzmacnia ochronę, ale nie usuwa potrzeby bezpiecznej architektury całego przepływu.

#slide 101
## layout
title
## slide title
Dwa rzeczywiste przypadki
## subtitle
Granice secure storage najlepiej widać wtedy, gdy problem powstał obok samego magazynu sekretów
## teleprompter:
Po zbudowaniu modelu Androida i iOS warto zobaczyć dwa rzeczywiste przypadki, bo to one najlepiej pokazują, gdzie kończą się intuicje oparte na samym haśle bezpieczny magazyn. W obu przykładach problem nie sprowadza się do prostego stwierdzenia, że ktoś nie użył właściwego API do przechowywania sekretu. Przeciwnie, kłopot ujawnia się na granicy między bezpiecznym magazynem a resztą systemu. W Androidzie jest to granica między prywatną przestrzenią aplikacji a nieostrożnym przetwarzaniem zewnętrznego wejścia i operacji na plikach. W iOS jest to granica między ochroną keychainu a zachowaniem danych w scenariuszu backupu i odtworzenia. Te przypadki są wartościowe właśnie dlatego, że nie dają się streścić jako prosty błąd brakowało szyfrowania. Pokazują raczej, że mobilne bezpieczeństwo jest sztuką panowania nad całym cyklem życia sekretu oraz nad wszystkimi interfejsami, które mogą na ten sekret pośrednio wpłynąć.

#slide 102
## layout
title
## slide title
Przypadek Android: Dirty Stream
## subtitle
W 2024 roku Microsoft opisał wzorzec podatności, w którym złośliwa aplikacja mogła doprowadzić do nadpisania plików w prywatnej przestrzeni innej aplikacji
## teleprompter:
Dirty Stream jest bardzo dobrym przykładem na to, dlaczego temat lokalnych sekretów na Androidzie nie może ograniczać się do pytania, czy aplikacja używa Keystore. Microsoft opisał w 2024 roku wzorzec podatności związany z nieprawidłowym zaufaniem do danych pochodzących od zewnętrznego ContentProvidera. W praktyce aplikacja ofiary pobierała dane albo nazwę pliku z zewnętrznego źródła i zapisywała je w swojej prywatnej przestrzeni w sposób, który pozwalał napastnikowi wpłynąć na cel operacji. W efekcie złośliwa aplikacja mogła doprowadzić do nadpisania krytycznych plików wewnątrz katalogu prywatnego ofiary. To bardzo mocne uderzenie w naiwną intuicję, że sandbox rozwiązuje temat lokalnego bezpieczeństwa. Sandbox nie pomógł, bo to sama aplikacja ofiary wykonała niebezpieczną operację, ufając nieuprawnionemu wejściu. Problem nie polegał więc na braku izolacji systemowej, ale na błędzie w architekturze i obsłudze I O.

#slide 103
## layout
title
## slide title
Mechanizm Dirty Stream
## subtitle
Nieufne wejście, nazwa pliku i operacja zapisu spotkały się w jednym błędnym przepływie
## teleprompter:
Istota Dirty Stream jest bardzo inżynierska i właśnie dlatego cenna. Zewnętrzny provider albo powiązany mechanizm przekazywał dane, którym aplikacja ofiary nadała zbyt wysoki poziom zaufania. Zamiast odseparować wejście od własnych krytycznych plików i użyć bezpiecznych nazw tymczasowych, część aplikacji pozwalała, by właściwości dostarczonego obiektu wpłynęły na to, co i gdzie zostanie zapisane. Microsoft opisał to jako wzorzec podatności, a Android opublikował później osobne wytyczne o nieufnych nazwach plików dostarczanych przez ContentProvider oraz o ryzyku path traversal. To pokazuje, że problem nie był jednorazową ciekawostką, lecz reprezentował szerszą klasę błędów. Z perspektywy sekretów najważniejsze jest to, że atak nie musiał łamać Keystore ani wydobywać klucza sprzętowego. Wystarczyło skierować legalny kod aplikacji na niebezpieczną operację zapisu i w ten sposób uderzyć w pliki, które miały pozostać prywatne i integralne.

#slide 104
## layout
bullet
## slide title
Skutki Dirty Stream
## bullets
- Nadpisanie plików w katalogu prywatnym ofiary
- Kradzież tokenów lub innych sekretów zależnie od implementacji aplikacji
- Potencjalne przejęcie sesji lub eskalacja skutków przez modyfikację danych roboczych
- W niektórych scenariuszach możliwość wykonania kodu opisana przez Microsoft
- Skala problemu wynikała z powtarzalnego wzorca obecnego w popularnych aplikacjach
## teleprompter:
Najważniejsze w skutkach Dirty Stream jest to, że nie były one abstrakcyjne. Microsoft opisał scenariusze obejmujące kradzież tokenów oraz, zależnie od implementacji konkretnej aplikacji, nawet wykonanie kodu. To bardzo istotne, bo pokazuje, jak szybko błąd pozornie techniczny, dotyczący nazwy pliku albo operacji kopiowania, przechodzi w pełnoprawne naruszenie tożsamości użytkownika i bezpieczeństwa sesji. Jeżeli aplikacja trzyma lokalnie wrażliwe dane, to każda ścieżka pozwalająca nadpisać albo ujawnić plik może pośrednio stać się atakiem na uwierzytelnienie. Właśnie dlatego w mobilnym bezpieczeństwie trzeba myśleć o sekretach szerzej niż tylko przez pryzmat magazynu. Sekret przegrywa nie tylko wtedy, gdy jest wprost zapisany w złym miejscu. Przegrywa także wtedy, gdy aplikacja daje przeciwnikowi możliwość modyfikacji lub odczytu plików, które otaczają jego użycie.

#slide 105
## layout
title
## slide title
Jak Dirty Stream naprawiono
## subtitle
Naprawa dotyczyła logiki aplikacji i walidacji ścieżek, a nie wymiany jednego magazynu sekretów na inny
## teleprompter:
To jest być może najcenniejsza część tego przypadku. Naprawa nie polegała na prostym zaleceniu używajcie Keystore zamiast plików. Microsoft i dokumentacja Androida wskazały przede wszystkim potrzebę bezpiecznej obsługi danych z zewnętrznych providerów: nie ufać nazwom plików dostarczanym z zewnątrz, stosować walidację i canonicalization ścieżek, używać własnych nazw tymczasowych, ograniczać eksport komponentów i pilnować, by zewnętrzny URI nie prowadził do lokalnych plików aplikacji. Innymi słowy, rozwiązanie dotyczyło kontroli granicy wejścia oraz integralności operacji na plikach. To idealnie pokazuje tezę całego wykładu. Nawet jeśli klucz lub token jest przechowywany w relatywnie mocnym magazynie, to aplikacja nadal może go utracić przez błędny przepływ wejścia wyjścia. Secure storage jest wtedy warstwą ważną, lecz niewystarczającą. Prawdziwa naprawa wymaga poprawy architektury programu.

#slide 106
## layout
title
## slide title
Lekcja z Androida
## subtitle
Najgroźniejszy bywa nie brak sejfu, lecz to, że aplikacja sama otwiera złą ścieżkę do własnych danych
## teleprompter:
Dirty Stream warto zapamiętać nie jako nazwę konkretnej kampanii, lecz jako wzorzec myślenia. W aplikacji mobilnej prywatny katalog, sandbox i nawet mocny magazyn kluczy nie gwarantują bezpieczeństwa, jeśli sama logika programu pozwala na zapis lub odczyt w niewłaściwym miejscu pod wpływem nieufnego wejścia. To zmienia sposób myślenia o sekretach. Zamiast pytać wyłącznie gdzie to zapisano, trzeba pytać jakie operacje otaczają ten sekret, jakie komponenty mają wpływ na pliki wokół niego, skąd pochodzą nazwy, ścieżki i URI, oraz czy aplikacja potrafi odróżnić dane własne od obcych. Gdy spojrzy się na problem w ten sposób, okazuje się, że secure storage to nie oddzielny temat od bezpieczeństwa plików i IPC, lecz jeden fragment większej architektury zaufania.

#slide 107
## layout
title
## slide title
Przypadek iOS: CVE-2025-24221
## subtitle
Apple opisał problem, w którym wrażliwe dane Keychain mogły być dostępne z kopii zapasowej iOS
## teleprompter:
Przypadek iOS jest inny od Dirty Stream, ale równie pouczający. Apple w opisie poprawek bezpieczeństwa dla iOS 18.4 i iPadOS 18.4 wskazał CVE-2025-24221 jako problem, w którym wrażliwe dane Keychain mogły być dostępne z backupu iOS. Już samo to sformułowanie jest bardzo wartościowe dydaktycznie, bo pokazuje, że granica bezpieczeństwa nie przebiega wyłącznie wewnątrz API Keychainu. Przebiega również między keychainem a mechanizmem kopii zapasowej oraz odtworzenia danych. To dokładnie ten rodzaj scenariusza, który bywa pomijany przy pobieżnym myśleniu o secure storage. W codziennym użyciu aplikacji wszystko może wyglądać poprawnie, a problem ujawnia się dopiero w chwili, gdy sekret zmienia kontekst i trafia do procesu backupu, migracji albo odzyskiwania. Wtedy okazuje się, że prawdziwy model zagrożeń jest szerszy niż sam magazyn danych.

#slide 108
## layout
definition
## term
Improved data access restriction
## definition
Formuła użyta przez Apple w opisie poprawki CVE-2025-24221, wskazująca, że naprawa polegała na zaostrzeniu zasad dostępu do danych, a nie jedynie na kosmetycznej zmianie implementacyjnej.
## teleprompter:
Apple z zasady publikuje opisy poprawek w dość oszczędnej formie, ale nawet ten skrót mówi sporo. W przypadku CVE-2025-24221 firma podała, że problem został rozwiązany przez improved data access restriction. Nie dostajemy pełnego raportu technicznego, lecz dostajemy to, co najważniejsze dla analizy architektonicznej. Źródłem problemu była granica dostępu do danych, a więc relacja między tajnym materiałem a kontekstem, w którym stawał się osiągalny. To bardzo zgodne z wcześniejszymi wnioskami z wykładu. Bezpieczeństwo nie jest własnością samego kontenera, lecz własnością całego zbioru reguł określających kto, kiedy, w jakiej fazie życia urządzenia i w jakim scenariuszu systemowym może dotknąć sekretu. Właśnie dlatego nawet platforma z bardzo silnym modelem keychainu musi stale korygować reguły dostępu tam, gdzie praktyka pokazuje zbyt szerokie możliwości.

#slide 109
## layout
title
## slide title
Lekcja z iOS
## subtitle
Bezpieczny magazyn sekretów trzeba analizować razem z backupem, migracją i semantyką klas dostępności
## teleprompter:
Z przypadku CVE-2025-24221 płynie kilka bardzo mocnych wniosków. Po pierwsze, użycie Keychainu nie kończy projektu bezpieczeństwa. Nadal trzeba rozumieć, czy sekret ma być związany z urządzeniem, czy może być migrowany, oraz jakie skutki ma backup i odzyskiwanie. Po drugie, klasy dostępności i warianty This device only nie są kosmetyką, tylko rzeczywistym narzędziem ograniczania ryzyka. Po trzecie, bezpieczeństwo platformy jest żywe. Nawet dobrze zaprojektowany system wymaga poprawek, gdy okazuje się, że jakiś scenariusz daje zbyt szeroki dostęp do wrażliwych danych. Dla architekta aplikacji mobilnej to jest cenna przestroga. Nie wolno projektować lokalnego przechowywania sekretów na podstawie samej nazwy mechanizmu. Trzeba analizować cały cykl życia wpisu, od utworzenia po przywrócenie urządzenia, bo to właśnie tam często ukrywa się realna granica bezpieczeństwa.

#slide 110
## layout
title
## slide title
Android i iOS: wspólna lekcja
## subtitle
W obu platformach problem pojawia się na styku secure storage z resztą systemu, a nie tylko w samym magazynie sekretów
## teleprompter:
Choć Dirty Stream i CVE-2025-24221 dotyczą innych platform i różnych mechanizmów, razem prowadzą do bardzo podobnego wniosku. Bezpieczeństwo sekretu mobilnego nie zależy wyłącznie od tego, czy istnieje dedykowany sejf. Zależy od tego, jak aplikacja obchodzi się z wejściem z zewnątrz, jak zapisuje pliki, jak ustawia klasy dostępności, co dzieje się przy backupie, jakie są reguły migracji i czy legalny kod aplikacji nie potrafi wykonać zbyt szerokich operacji na materiale wrażliwym. Android pokazuje problem integralności i zaufania do danych wejściowych. iOS pokazuje problem granic dostępu w backupie i recovery. Oba przypadki razem rozbijają bardzo popularny skrót myślowy, zgodnie z którym secure storage jest gotową odpowiedzią na temat lokalnych sekretów. W rzeczywistości jest on jedną z warstw, a bezpieczeństwo powstaje dopiero z prawidłowego połączenia tej warstwy z architekturą całej aplikacji.

#slide 111
## layout
bullet
## slide title
Antywzorce przechowywania sekretów w aplikacji mobilnej
## bullets
- Trzymanie haseł użytkownika lokalnie bez wyraźnej konieczności i bez precyzyjnego modelu ryzyka
- Traktowanie tokenu sesyjnego jak zwykłej preferencji aplikacji
- Uznanie, że sam sandbox lub sam Keychain Keystore rozwiązuje cały problem
- Projektowanie migracji i recovery bez rozróżnienia sekretów urządzeniowych i przenaszalnych
- Logowanie, cache'owanie i tymczasowe kopiowanie danych wrażliwych poza głównym magazynem
## teleprompter:
Najwięcej szkód w praktyce nie bierze się z egzotycznych błędów kryptograficznych, lecz z antywzorców projektowych. Pierwszy z nich to lokalne przechowywanie czegoś tylko dlatego, że jest to wygodne, bez odpowiedzi na pytanie, czy dany sekret musi istnieć na urządzeniu. Drugi to semantyczne spłaszczenie wszystkiego do kategorii dane aplikacji. Gdy refresh token, identyfikator sesji, hasło użytkownika i zwykłe ustawienie interfejsu lądują w podobnych miejscach albo przechodzą przez te same warstwy cache'u i logów, zaczyna się chaos bezpieczeństwa. Trzeci antywzorzec jest czysto mentalny. Zespół wierzy, że ponieważ korzysta z Keychainu albo Keystore, temat został załatwiony. Tymczasem najgroźniejsze wycieki często dzieją się obok głównego magazynu. Czwarty błąd pojawia się przy migracji i odzyskiwaniu konta, gdy system nie odróżnia sekretu powiązanego z urządzeniem od sekretu, który ma podróżować z użytkownikiem. Ostatni antywzorzec to wynoszenie danych wrażliwych do telemetrii, cache'u i warstw pomocniczych. To właśnie tam bardzo często kończy się prawdziwa historia kompromitacji.

#slide 112
## layout
title
## slide title
Wzorzec serwerowy
## subtitle
Hasło użytkownika powinno być weryfikowane po stronie usługi, a na urządzeniu zwykle nie powinno być przechowywane wprost
## teleprompter:
Najzdrowszy wzorzec architektoniczny jest prosty, choć nie zawsze wygodny. Hasło użytkownika jest sekretem służącym do zdalnego uwierzytelnienia wobec usługi i z tego powodu jego główne życie powinno toczyć się po stronie serwera w formie bezpiecznie haszowanej i parametryzowanej zgodnie z aktualnymi zaleceniami. Na urządzeniu mobilnym zwykle nie ma dobrego powodu, by przechowywać hasło wprost. To, co aplikacja może realnie potrzebować lokalnie, to raczej token sesyjny, odświeżający, lokalny klucz do ochrony danych albo uchwyt do klucza nieeksportowalnego. Gdy to rozróżnienie zostaje zatarte, aplikacja zaczyna przechowywać za dużo i zwiększa wartość łupu dla napastnika. Mobilna architektura sekretów powinna więc zmierzać do minimalizacji: urządzenie przechowuje tylko to, co musi być dostępne lokalnie, a nie pełny materiał uwierzytelniający użytkownika do wszystkich celów.

#slide 113
## layout
title
## slide title
Wzorzec minimalnego życia sekretu
## subtitle
Najbezpieczniejszy sekret lokalny to często taki, który istnieje krótko, ma wąskie przeznaczenie i łatwo go unieważnić
## teleprompter:
Jedną z najbardziej praktycznych zasad w bezpieczeństwie mobilnym jest skracanie życia sekretu i zawężanie jego roli. Jeżeli lokalny token ma krótki czas użyteczności, jest związany z jedną funkcją albo z jednym urządzeniem i może zostać szybko unieważniony po stronie backendu, to skutki kompromitacji maleją radykalnie. Odwrotnie, długowieczne sekrety o szerokich uprawnieniach są zaproszeniem do katastrofy. To podejście nie zastępuje bezpiecznego magazynu, lecz współpracuje z nim. Nawet najlepiej chroniony sekret staje się ryzykowny, jeśli daje dostęp zbyt długo i zbyt szeroko. W systemach mobilnych ma to szczególne znaczenie, bo urządzenie jest stale narażone na utratę, kradzież, analizę poawaryjną, błędy integracyjne i nieprzewidziane interakcje z backupem. Sekret, który żyje krótko i ma ograniczony zasięg, daje architektowi dodatkową warstwę bezpieczeństwa nawet wtedy, gdy jedna z pozostałych warstw zawiedzie.

#slide 114
## layout
title
## slide title
Wzorzec związania z obecnością użytkownika
## subtitle
Lokalny klucz wysokiej wartości powinien często wymagać aktualnej obecności użytkownika przy urządzeniu
## teleprompter:
Nie każdy sekret lokalny powinien być używalny automatycznie i bezwarunkowo. Tam, gdzie stawka jest wysoka, sensowne staje się związanie użycia klucza z aktualną obecnością użytkownika przy urządzeniu, na przykład przez systemowe uwierzytelnienie lokalne. Taki wzorzec nie zmienia natury zdalnego uwierzytelnienia wobec usługi, ale bardzo poprawia odporność na pewne klasy nadużyć lokalnych. Kradzież odblokowanego telefonu na krótki czas, przejęcie pozostawionego urządzenia albo próba automatycznego użycia sekretu przez komponent działający bez wiedzy użytkownika stają się trudniejsze. Trzeba jednak uważać, by nie zamienić tego w fałszywą obietnicę pełnego bezpieczeństwa. Obecność użytkownika jest ważnym warunkiem dla pewnych operacji, lecz nie eliminuje potrzeby rotacji, unieważniania, bezpiecznego recovery i kontroli po stronie serwera. To kolejny przykład zasady, że warstwa lokalna wzmacnia system, ale nie zastępuje reszty architektury zaufania.

#slide 115
## layout
title
## slide title
Wzorzec świadomej migracji
## subtitle
Każdy sekret powinien mieć jasno określone zachowanie przy backupie, odtworzeniu i zmianie urządzenia
## teleprompter:
Dojrzała architektura mobilna nie zostawia backupu i migracji jako skutku ubocznego platformy. Traktuje je jako część projektu bezpieczeństwa. Oznacza to, że dla każdego ważnego sekretu trzeba umieć odpowiedzieć, czy ma być przenoszony na nowe urządzenie, czy ma wygasnąć, czy po przywróceniu backupu ma wymagać ponownej aktywacji, i jakie są konsekwencje utraty starego telefonu. To podejście porządkuje także temat klas dostępności i wariantów This device only. Zamiast wybierać je na ślepo, architekt wiąże je z pytaniem o to, czy sekret reprezentuje tożsamość użytkownika, stan urządzenia, czy może tylko lokalną wygodę. Gdy te decyzje są niejawne, migracja zaczyna produkować niespodzianki bezpieczeństwa. Gdy są jawne, można zbudować spójne reguły, w których użytkownik rozumie, co zostanie przeniesione, a co trzeba będzie odtworzyć lub ponownie autoryzować.

#slide 116
## layout
bullet
## slide title
Pytania kontrolne dla architekta aplikacji mobilnej
## bullets
- Czy ten sekret naprawdę musi istnieć lokalnie
- Czy musi być eksportowalny albo migrowalny
- Czy jego użycie powinno wymagać obecności użytkownika
- Co stanie się z nim po backupie, restarcie i zmianie urządzenia
- Jak szybko można go unieważnić po stronie usługi
## teleprompter:
Dobry projekt mobilny da się często rozpoznać po jakości pytań zadanych na początku. Czy sekret w ogóle musi istnieć lokalnie, czy tylko tak jest wygodniej w implementacji. Czy musi być eksportowalny, czy może wystarczy nieeksportowalny klucz powiązany z urządzeniem. Czy jego użycie powinno wymagać obecności użytkownika, czy może chodzi o mechanizm działający w tle. Co stanie się z nim po restarcie telefonu, po backupie, po migracji na nowy sprzęt i po odzyskaniu konta. I wreszcie, jak szybko da się go unieważnić, jeśli urządzenie zostanie utracone albo jeśli backend wykryje nadużycie. Te pytania nie są dodatkiem do kryptografii. One są praktyczną formą zastosowania kryptografii w architekturze systemu mobilnego. Bez nich nawet dobre API i dobry algorytm łatwo zostają użyte w zły sposób.

#slide 117
## layout
title
## slide title
Gdzie kończy się hasło
## subtitle
W dojrzałym systemie mobilnym hasło staje się tylko jednym z elementów większej architektury sekretów i zaufania
## teleprompter:
To właściwy moment, by wrócić do tytułowego tematu wykładu i zobaczyć go szerzej. Hasło nadal istnieje, nadal bywa potrzebne i nadal trzeba je bezpiecznie przechowywać po stronie usługi. Ale w systemach mobilnych nie jest już jedynym ani nawet najciekawszym elementem architektury bezpieczeństwa. Obok niego pojawiają się tokeny, lokalne klucze, mechanizmy związania z urządzeniem, biometryczne odblokowanie użycia klucza, polityki backupu, recovery i migracji. Im dojrzalszy system, tym wyraźniej widać, że pytanie jak przechowywać hasła prowadzi do szerszego pytania jak projektować życie sekretów w środowisku, które jest częściowo zaufane, częściowo publiczne i stale narażone na utratę urządzenia. To właśnie jest wyższy poziom tego tematu. Hasło pozostaje ważne, ale przestaje być jedyną osią myślenia o bezpieczeństwie mobilnym.

#slide 118
## layout
title
## slide title
Kiedy odchodzić od hasła jako głównego sekretu
## subtitle
Im więcej można oprzeć na kluczach, związaniu z urządzeniem i silniejszym uwierzytelnieniu, tym mniejsza zależność od sekretu niskoentropijnego
## teleprompter:
Hasła mają jedną cechę, która ciągle wraca jak ograniczenie fizyczne: są sekretami niskoentropijnymi i podatnymi na ponowne użycie, phishing, credential stuffing oraz błędy polityki użytkownika. Dlatego dojrzała architektura mobilna stara się ograniczać swoją zależność od hasła, zwłaszcza po pierwszym uwierzytelnieniu i w codziennym działaniu aplikacji. Nie oznacza to magicznego zniknięcia problemu tożsamości. Oznacza raczej przesunięcie ciężaru na lepiej kontrolowane mechanizmy: klucze związane z urządzeniem, krócej żyjące tokeny, silniejsze odblokowanie użycia sekretu i protokoły, które nie wymagają wielokrotnego przesyłania tego samego hasła. To podejście nie neguje potrzeby bezpiecznego haszowania haseł na serwerze. Pokazuje jednak, że w systemach mobilnych najlepszą obroną bywa często to, że hasło przestaje być w centrum codziennego obiegu sekretów.

#slide 119
## layout
title
## slide title
Synteza wykładu
## subtitle
Bezpieczne przechowywanie haseł w systemie mobilnym oznacza projektowanie całego życia sekretu, a nie tylko wybór funkcji skrótu lub magazynu
## teleprompter:
Jeśli spojrzeć na cały wykład jako na jedną linię argumentu, prowadzi ona od prostego pytania o hashowanie do znacznie dojrzalszego obrazu. Tak, trzeba znać różnicę między zwykłą funkcją skrótu a password hashingiem, rozumieć sens soli, key stretchingu, memory hardness i kosztu ataku offline. To jest fundament. Ale w systemie mobilnym fundament szybko okazuje się niewystarczający, jeśli nie połączy się go z architekturą klienta, cyklem życia tokenów, właściwościami Android Keystore i iOS Keychain, rolą Secure Enclave, backupem, migracją i rzeczywistymi ścieżkami wycieku poza głównym magazynem. Najważniejsza lekcja nie brzmi więc użyj właściwego algorytmu albo właściwego API. Brzmi: zaprojektuj sekret tak, aby jego przechowywanie, użycie, migracja i unieważnienie tworzyły spójny system obrony.

#slide 120
## layout
definition
## term
Bezpieczne przechowywanie sekretu mobilnego
## definition
Stan, w którym sekret ma minimalny zakres, minimalny czas życia, właściwy magazyn, właściwe reguły użycia, właściwe zachowanie przy backupie i recovery oraz możliwość szybkiego unieważnienia po stronie systemu.
## teleprompter:
Na końcu warto zostawić jedną definicję roboczą, która spina cały wykład. Bezpieczne przechowywanie sekretu mobilnego nie jest cechą pojedynczego miejsca ani pojedynczego algorytmu. Jest stanem architektonicznym. Sekret powinien mieć możliwie mały zakres działania, możliwie krótki czas życia, właściwie dobrany magazyn, świadomie ustawione reguły użycia i jasno określone zachowanie przy backupie, migracji oraz odzyskiwaniu urządzenia. Do tego musi istnieć możliwość szybkiego cofnięcia jego wartości po stronie usługi, kiedy telefon zostanie utracony albo gdy zostanie wykryte nadużycie. Tylko przy takim spojrzeniu hasło, token, lokalny klucz i secure storage zaczynają układać się w jedną spójną architekturę. To właśnie odróżnia projektowanie bezpieczeństwa od samego użycia komponentów bezpieczeństwa.
