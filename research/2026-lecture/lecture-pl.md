#slide 1
## layout
title
## slide title
Zaawansowane exploity i łańcuchy ataku
## subtitle
Wykład uniwersytecki dla ekspertów cybersecurity
## teleprompter:
Ten wykład analizuje mechanikę czterech klas incydentów: kompromitacji łańcucha dostaw, nadużycia pipeline publikacyjnego, przejęcia kanału aktualizacji oraz exploitów parserów i pamięci. Celem nie jest przegląd medialny, tylko techniczna rekonstrukcja: wejście, założenie zaufania, primitive exploita, efekt i obrona.

#slide 2
## layout
bullet
## slide title
Cel wykładu
## bullets
- Rozumieć, jak powstaje exploit chain, a nie tylko jaki był jego skutek.
- Rozróżniać powierzchnię ataku, primitive exploita i końcowy payload.
- Umieć analizować przypadki z supply chain, CI/CD, update infrastructure i parser exploitation.
- Wyciągać wnioski obronne, które działają na poziomie architektury, a nie wyłącznie incydentu.
## teleprompter:
Publiczność zna podstawy bezpieczeństwa, więc nie wracamy do definicji z poziomu wstępu. Skupiamy się na tym, co zwykle ginie w skrótach: jak atak został złożony z kilku kroków, gdzie leżało zaufanie, co dokładnie zostało wykorzystane i dlaczego wykrycie było trudne.

#slide 3
## layout
definition
## term
Exploit chain
## definition
Łańcuch zależnych działań, w którym pojedyncze decyzje architektoniczne, błędy implementacyjne i założenia zaufania składają się na końcowy kompromis, eskalację lub trwały dostęp.
## teleprompter:
To pojęcie obejmuje zarówno kompromitację pakietu npm, jak i overflow w parserze obrazu. W obu przypadkach atakujący nie potrzebuje jednego „magicznego” błędu, tylko sekwencji kroków, które razem tworzą możliwość nadużycia.

#slide 4
## layout
bullet + image
## slide title
Dwa światy analiz
## bullets
- Łańcuch dostaw i parser exploitation opierają się na innym typie zaufania.
- W pierwszym przypadku celem jest kanał dystrybucji i publikacji.
- W drugim przypadku celem jest błąd interpretacji danych wejściowych.
- Te dwa światy wymagają innej analizy mechanizmu, ale tej samej dyscypliny dowodowej.
## image
assets/ai_vuln/01_chain_overview.png
## teleprompter:
To rozróżnienie prowadzi cały wykład. W supply chain atakujący wykorzystuje infrastrukturę dystrybucji i proces publikacji. W parser exploitation atakujący manipuluje danymi, które mają zostać poprawnie zinterpretowane przez program. Mechanika końcowa jest inna, ale sposób myślenia analitycznego jest podobny.

#slide 5
## layout
bullet
## slide title
Jak będziemy analizować każdy przypadek
## bullets
- Jaki był punkt wejścia?
- Gdzie dokładnie leżało zaufanie?
- Co umożliwiło wykonanie lub propagację?
- Jaki był payload: exfiltration, persistence, propagation, corruption?
- Co utrudniało wykrycie i reakcję?
## teleprompter:
Ten schemat będzie powtarzany, ale nie w formie pustego szablonu. Każdy przypadek ma własny kontekst, własne ograniczenia i własny typ błędu, dlatego patrzymy na te same pytania, ale odpowiadamy na nie inaczej.

#slide 6
## layout
definition
## term
Granica zaufania
## definition
Miejsce, w którym system zaczyna traktować dane lub akcję jako wiarygodne mimo tego, że mogły zostać dostarczone, zmodyfikowane lub wywołane przez stronę nieuprzywilejowaną.
## teleprompter:
Granica zaufania jest ważniejsza niż sam komponent. To ona decyduje, czy paczka z registry, workflow w GitHub Actions, update z serwera producenta albo obraz w parserze będzie traktowany jako bezpieczny.

#slide 7
## layout
definition
## term
Primitive exploita
## definition
Minimalna techniczna własność, którą atakujący uzyskuje nad systemem: wykonanie kodu, kontrola przepływu, zła alokacja pamięci, exfiltration, trwałość lub możliwość dalszej propagacji.
## teleprompter:
W tym wykładzie primitive exploita nie jest końcowym celem. To środek do celu. Warto zawsze odróżnić, co daje sam błąd i co dopiero daje połączenie tego błędu z kontekstem wdrożeniowym.

#slide 8
## layout
bullet
## slide title
Metoda badawcza
## bullets
- Czytanie patchy i diffów
- Analiza przepływu danych i zależności sterowania
- Porównanie wersji i reżimów wykonania
- Rekonstrukcja łańcucha z perspektywy atakującego
- Testowanie hipotez przez harness i debugger
## teleprompter:
To nie jest wykład o „co się wydarzyło”, tylko o tym, jak odzyskuje się mechanikę. Dlatego patch diff, flow analysis i harnessing są tu ważniejsze niż narracja medialna. Na poziomie eksperckim liczy się dowód mechanizmu, a nie opis skutku.

#slide 9
## layout
bullet
## slide title
Dlaczego źródła są ważne
## bullets
- Paper pokazuje metodę i ograniczenia.
- Advisory i postmortem pokazują zasięg i chronologię.
- Patch i diff pokazują techniczny punkt złamania.
- Blogi techniczne często ujawniają detale, których nie ma w newsach.
- ARGUS i ChainFuzz wspierają analizę workflow oraz upstream supply chain.
- SoK i badania nad npm ecosystem porządkują klasy ryzyka i generalizację.
- ZygoSec blog dostarcza materiał do rekonstrukcji exploita parsera i pamięci.
## teleprompter:
Źródła są uzupełniające. Publikacje pomagają zbudować aparat pojęciowy, a raporty i blogi dostarczają fakty. Dopiero razem dają materiał do rzetelnej analizy.

#slide 10
## layout
bullet
## slide title
Case 1: kompromitacja pakietu npm
## bullets
- Atak na zaufanie do publikacji pakietu
- Złośliwy kod aktywowany przy instalacji
- Drugi etap pobierany w kontekście ofiary
- Duży blast radius przez downstream
## image
assets/ai_vuln/02_data_sources.png
## teleprompter:
Pierwszy przypadek pokazuje, jak łatwo zamienić ekosystem pakietów w kanał wykonania kodu. Atakujący nie musi wchodzić do systemu bezpośrednio. Wystarczy, że zainfekuje ścieżkę dystrybucji lub konto publikujące.

#slide 11
## layout
bullet
## slide title
Case 1: gdzie leży zaufanie
## bullets
- npm traktuje publikację jako legalny mechanizm dostarczenia kodu.
- Instalacja zakłada, że paczka reprezentuje intencję maintenera.
- Skrypty instalacyjne wykonują się w zaufanym środowisku.
- Tokeny, sekrety i cache bywają dostępne w chwili instalacji.
## teleprompter:
To jest klasyczny przykład przeniesienia zaufania z człowieka i procesu na mechanizm techniczny. Jeśli paczka może uruchomić kod w trakcie instalacji, to sama instalacja staje się powierzchnią ataku.

#slide 12
## layout
bullet
## slide title
Case 1: mechanika ataku
## bullets
- Zmiana zawartości paczki lub jej zależności
- Wykonanie kodu w phase install lub postinstall
- Pobranie drugiego etapu z zewnętrznego źródła
- Użycie środowiska ofiary do dalszego działania
## teleprompter:
Najważniejszy krok to nie sam upload do registry, tylko to, co dzieje się po stronie ofiary. Skrypt instalacyjny albo zależność uruchomiona w trakcie builda tworzy kanał, przez który atakujący może pobrać payload i zbierać dane.

#slide 13
## layout
bullet
## slide title
Case 1: co atakujący osiąga
## bullets
- Dostęp do sekretów i tokenów
- Możliwość dalszej kompromitacji CI
- W niektórych wariantach również trwałość i exfiltration
- Duży zasięg bez bezpośredniego wejścia do hosta
## teleprompter:
Jeżeli kompromitacja zaczyna się na etapie instalacji, to atakujący widzi dokładnie to środowisko, w którym ofiara zaufanie uznała za bezpieczne. W praktyce oznacza to skrypty, sekrety, konfigurację i często możliwość przejścia dalej.

#slide 14
## layout
bullet
## slide title
Case 1: obrona
## bullets
- Ograniczać skrypty instalacyjne
- Odcinać sekrety od nieufnych etapów builda
- Monitorować zmiany w zależnościach
- Wymuszać provenance i kontrolę publikacji
## teleprompter:
Wniosek nie polega na „nie używaj npm”, tylko na tym, żeby zminimalizować skutki automatycznego zaufania. W praktyce najważniejsze są polityki uruchamiania, kontrola pochodzenia i ograniczanie uprawnień środowiska build.

#slide 15
## layout
bullet
## slide title
Case 2: atak na pipeline publikacyjny
## bullets
- Zamiast samej paczki celem staje się workflow publikujący.
- Przejęcie jednej części pipeline może rozlać się na wiele artefaktów.
- Zaufany publisher staje się kanałem dystrybucji ataku.
- CI/CD przestaje być wyłącznie narzędziem obrony.
## image
assets/ai_vuln/04_graph_views.png
## teleprompter:
Ten przypadek jest bardziej interesujący niż prosty kompromitowany package, bo atak skierowany jest w automat publikujący. To oznacza, że złośliwe artefakty mogą pojawić się szybko, masowo i w sposób bardzo wiarygodny.

#slide 16
## layout
bullet
## slide title
Case 2: co jest podatne
## bullets
- Zbyt szerokie uprawnienia workflow
- Poleganie na zaufanym tokenie publikacyjnym
- Cache i artefakty jako wektor uboczny
- Brak ścisłej separacji etapów build, test i release
## teleprompter:
Problem nie polega na jednym błędzie składni workflow. Problemem jest architektura uprawnień. Jeśli pipeline łączy wiele etapów w jednym zaufanym kontekście, to pojedyncze nadużycie może dotknąć wielu pakietów jednocześnie.

#slide 17
## layout
bullet
## slide title
Case 2: łańcuch nadużycia
## bullets
- Atak na publikujący workflow
- Publikacja złośliwych wersji wielu pakietów
- Szybka propagacja przez registry
- Trudność w odróżnieniu legalnego release od kompromitacji
## teleprompter:
W takim scenariuszu atakujący wykorzystuje wiarygodność procesu publikacji. Z perspektywy downstream wszystko wygląda jak normalny release, dopóki nie pojawią się anomalie w zachowaniu pakietu albo sygnał z incydentu.

#slide 18
## layout
bullet
## slide title
Case 2: obrona
## bullets
- Ograniczyć scope tokenów publikacyjnych
- Rozdzielić build, test i release
- Wymagać jawnego potwierdzenia dla ryzykownych kroków
- Monitorować nie tylko kod, ale i pipeline
## teleprompter:
Jeżeli pipeline publikacyjny ma zbyt dużo władzy, to jego kompromitacja jest bardziej groźna niż kompromitacja pojedynczego repozytorium. Obrona musi więc obejmować sam proces release, a nie tylko kod źródłowy.

#slide 19
## layout
bullet
## slide title
Case 3: update server jako punkt ataku
## bullets
- Zaufanie do kanału aktualizacji jest bardzo silne.
- Jeden kompromitowany update może objąć wiele hostów.
- Security product ma wysoki autorytet po stronie ofiary.
- Atak na update infrastrukturę jest szczególnie efektywny.
## image
assets/ai_vuln/14_repair_loop.png
## teleprompter:
To przypadek, w którym producent i klient zakładają, że update jest legalny. Gdy ktoś przejmie ten kanał, zyskuje niezwykle silny mechanizm dystrybucji.

#slide 20
## layout
bullet
## slide title
Case 3: co robi atakujący
## bullets
- Podmienia lub modyfikuje komponent aktualizacyjny
- Utrzymuje obecność przez mechanizmy persistence
- Próbuje utrudnić usuwanie lub naprawę
- Wykorzystuje autorytet oprogramowania bezpieczeństwa
## teleprompter:
W takim ataku nie chodzi tylko o wprowadzenie złośliwego binarium. Chodzi o to, żeby przetrwać w systemie i jednocześnie blokować naprawę, bo to maksymalizuje czas działania i wpływ.

#slide 21
## layout
bullet
## slide title
Case 3: dlaczego to jest groźne
## bullets
- Aktualizacje są z definicji akceptowane przez ofiarę.
- Security software zwykle ma wysokie uprawnienia.
- Kompromitacja kanału może wyglądać jak normalny maintenance.
- Reakcja jest wolniejsza, bo zaufanie działa przeciw ofierze.
## teleprompter:
To jest jedna z najbardziej asymetrycznych klas incydentów. Ofiara już wcześniej zgodziła się ufać temu kanałowi, więc odróżnienie ataku od legalnego update’u jest kosztowne i czasochłonne.

#slide 22
## layout
bullet
## slide title
Case 3: obrona
## bullets
- Weryfikacja podpisów i integralności aktualizacji
- Izolacja mechanizmów update od reszty systemu
- Monitoring zachowania po update
- Szybka możliwość odcięcia kanału dostawcy
## teleprompter:
Obrona musi obejmować także scenariusz, w którym sam dostawca lub jego infrastruktura zostaje nadużyta. To wymusza wielowarstwową weryfikację i możliwość awaryjnego wyłączenia kanału.

#slide 23
## layout
bullet
## slide title
Case 4: exploit parsera obrazu
## bullets
- Wejściem jest złośliwie przygotowany plik
- Atak opiera się na błędzie obliczeniowym lub alokacyjnym
- Celem jest kontrolowany wpływ na pamięć
- Kluczowe są dane i ich interpretacja, nie zaufanie do publishera
## image
assets/ai_vuln/03_code_gadget.png
## teleprompter:
To inna klasa problemu. Tu nie interesuje nas upstream, tylko sposób, w jaki parser interpretuje dane. Jeśli obliczenia rozmiarów, bloków albo struktur pomocniczych są błędne, można dojść do poważnych skutków pamięciowych.

#slide 24
## layout
bullet
## slide title
Case 4: od patch diff do bug class
## bullets
- Porównanie wersji ujawnia punkt naprawy
- Zmienna pośrednia może przepełniać się przed alokacją
- `malloc(0)` lub zbyt mała alokacja tworzy podatny stan
- Błąd staje się exploitable dopiero w konkretnym kontekście parsowania
## teleprompter:
Najważniejsza jest tu arytmetyka. Jeżeli rozmiar obiektu albo bufora jest wyliczany błędnie, wejście może doprowadzić program do alokacji mniejszej niż potrzebna i uruchomić klasyczny problem pamięciowy.

#slide 25
## layout
bullet
## slide title
Case 4: od błędu do prymitywu
## bullets
- Overflow arytmetyczny
- Underallocation
- Nadpisanie pamięci lub niezgodność struktur
- Możliwość dalszej kontroli przepływu lub awarii
## teleprompter:
W exploit development kluczowe jest przejście od buga do prymitywu. Sam overflow nie wystarcza. Trzeba pokazać, że prowadzi do kontrolowanej sytuacji pamięciowej, którą da się wykorzystać.

#slide 26
## layout
bullet
## slide title
Case 4: harness i walidacja
## bullets
- Minimalny input testowy
- Powtarzalna reprodukcja
- Debugger i obserwacja stanu pamięci
- Hipoteza -> test -> korekta -> potwierdzenie
## teleprompter:
Tu nie ma miejsca na intuicję bez potwierdzenia. Dobry exploit development wymaga harnessu, który pozwala powtarzalnie wracać do tego samego stanu i obserwować, gdzie dokładnie program zaczyna zachowywać się niebezpiecznie.

#slide 27
## layout
bullet
## slide title
Dlaczego screenshot nie wystarcza
## bullets
- Wiele figur w PDF nie ma widocznej ramki.
- Często trzeba analizować strukturę PDF, a nie bitmapę.
- Wydobycie obrazu z page renderu może zgubić logikę obiektu.
- Dobre narzędzie musi rozumieć obiekt PDF, nie tylko piksele.
## image
assets/ai_vuln/06_graph_limits.png
## teleprompter:
To ważne dla naszej pracy z literaturą. Jeśli figura jest częścią struktury PDF, trzeba ją odzyskać z danych dokumentu. Sam zrzut ekranu bywa zbyt ubogi i może obciąć istotne fragmenty.

#slide 28
## layout
comparison
## slide title
Co różni supply chain od parser exploitation
## left title
Supply chain
## left bullets
- Atak na zaufanie
- Wiele ofiar pośrednich
- Trwałość przez dystrybucję
- Często exfiltration lub propagation
## right title
Parser exploitation
## right bullets
- Atak na interpretację danych
- Jedna precyzyjna ofiara w chwili przetwarzania
- Trwałość zwykle wynika z późniejszej eskalacji
- Często corruption, crash lub code execution
## teleprompter:
To porównanie porządkuje cały wykład. W supply chain atakujący chce skorzystać z istniejącego zaufania do procesu dystrybucji. W parser exploitation atakujący chce złamać założenie poprawności danych wejściowych. Różne są punkty wejścia, ale podobna jest potrzeba precyzyjnej analizy łańcucha.

#slide 29
## layout
bullet
## slide title
Wspólny model obrony
## bullets
- Ograniczyć zaufanie do automatyzacji
- Rozdzielać role i etapy wykonania
- Weryfikować źródło i integralność danych
- Mierzyć ryzyko nie tylko po severity, ale też po wykorzystaniu
## teleprompter:
Nie ma jednego rozwiązania, które zamknie wszystkie cztery klasy problemów. Jest za to wspólny motyw: minimalizacja nadmiernego zaufania i zwiększanie obserwowalności w całym łańcuchu przetwarzania.

#slide 30
## layout
bullet
## slide title
Metodologia dla badaczy i obrońców
## bullets
- Patrzeć na patch, nie tylko na advisory
- Sprawdzać, co jest wejściem, a co sinkiem
- Rozróżniać publiczny opis od technicznej przyczyny
- Szukać sygnałów, które da się automatyzować
## teleprompter:
To jest praktyczny zestaw na co dzień. Jeśli ma powstać lepsza detekcja albo lepsza triage, trzeba pracować na mechanizmach, nie na headline’ach.

#slide 31
## layout
bullet
## slide title
Jak czytać literaturę
## bullets
- Metoda i ograniczenia
- Rodzaj etykiet
- Jakość splitu
- Generalizacja poza benchmark
- Zgodność z realnym procesem pracy
## teleprompter:
W badaniach nad bezpieczeństwem „dobry wynik” bez metodologii jest w praktyce bezwartościowy. Najpierw trzeba wiedzieć, na jakich danych i przy jakim podziale powstał, a dopiero potem pytać o sens operacyjny.

#slide 32
## layout
bullet
## slide title
Co powinno zostać po tym wykładzie
## bullets
- Umiejętność rekonstrukcji łańcucha ataku
- Umiejętność odróżnienia źródła problemu od skutku
- Umiejętność pracy na patchach, diffach i pipeline
- Świadomość, gdzie kończy się opis i zaczyna mechanika
## teleprompter:
To jest poziom, na którym ma działać ten materiał. Nie chodzi o pamiętanie nazw incydentów, tylko o umiejętność samodzielnego przejścia od źródła do skutku i od skutku do obrony.

#slide 33
## layout
comparison
## slide title
Jedno pytanie dla wszystkich przypadków
## left title
Jeśli jesteś atakującym
## left bullets
- Gdzie wejść najłatwiej?
- Który trust boundary jest najsłabszy?
- Co daje największy efekt przy najmniejszym hałasie?
## right title
Jeśli jesteś obrońcą
## right bullets
- Gdzie ograniczyć zaufanie?
- Co trzeba monitorować najbliżej źródła?
- Który krok ma największy koszt błędu?
## teleprompter:
To pytanie scala cały wykład. Dla atakującego liczy się najbardziej opłacalny punkt wejścia. Dla obrońcy liczy się najsłabsze miejsce, które warto wzmocnić, zanim stanie się exploit chain.

#slide 34
## layout
bullet
## slide title
Źródła analityczne do dalszej pracy
## bullets
- ARGUS dla workflow analysis
- ChainFuzz dla upstream supply chain
- SoK o bezpieczeństwie supply chain
- Badania nad npm ecosystem
- Blog ZygoSec dla exploit development
## teleprompter:
Ta literatura nie jest ozdobą, tylko narzędziem. Jedne prace pomagają analizować workflow, inne opisują ryzyko ekosystemów pakietów, a jeszcze inne wspierają rekonstrukcję exploita pamięciowego.

#slide 35
## layout
bullet
## slide title
Wnioski końcowe
## bullets
- Zaufanie jest powierzchnią ataku.
- Pipeline jest częścią systemu bezpieczeństwa.
- Aktualizacje są krytycznym kanałem dystrybucji.
- Parsery muszą być analizowane jak potencjalne źródło prymitywów exploita.
## teleprompter:
To są cztery punkty, które warto zapamiętać. Każdy z nich dotyczy innej warstwy systemu, ale wszystkie pokazują to samo: jeśli zaufanie jest zbyt szerokie, atakujący znajdzie sposób, by je wykorzystać.

#slide 36
## layout
title
## slide title
Dziękuję
## subtitle
Pytania i dyskusja techniczna
## teleprompter:
Na tym etapie dyskusja może iść w stronę konkretnych exploitów, technik detekcji, analizy patchy albo metod obrony. Najważniejsze jest przejście od historii incydentu do modelu, który da się zastosować także do nowych przypadków.
