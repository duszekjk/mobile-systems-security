#slide 1
## layout
title
## slide title
Podstawowe pojęcia kryptologii
## subtitle
Poufność danych, terminologia i proste szyfry
## teleprompter:
Kryptologia zajmuje się systematycznym badaniem metod ochrony informacji oraz metod przełamywania tej ochrony. W najbardziej klasycznym ujęciu jej centrum stanowi problem poufności, czyli takie przekształcenie wiadomości, aby dla osoby nieuprawnionej utraciła ona bezpośrednią czytelność. To właśnie od tego punktu zaczyna się tradycyjna teoria szyfrów. W praktyce bardzo szybko okazuje się jednak, że samo ukrycie treści nie wyczerpuje całego problemu bezpieczeństwa informacji. Oprócz poufności pojawiają się także integralność, uwierzytelnienie oraz inne własności związane z bezpieczną komunikacją. Na początku potrzebny jest jednak porządek pojęciowy. Trzeba odróżnić wiadomość od jej reprezentacji, klucz od algorytmu, schemat szyfrowania od pojedynczego użycia oraz kryptografię od kryptoanalizy. Ten wykład pozostaje blisko klasycznego rdzenia tematu. Jego osią jest język opisu szyfrowania oraz proste konstrukcje, które pozwalają zobaczyć zarówno intuicję ochrony informacji, jak i ograniczenia najwcześniejszych metod kryptograficznych.

#slide 2
## layout
bullet
## slide title
Kryptologia i jej dwa główne nurty
## bullets
- kryptografia projektuje metody ochrony informacji
- kryptoanaliza bada sposoby przełamywania ochrony
- kryptologia obejmuje oba te obszary łącznie
## teleprompter:
Słowo kryptologia obejmuje całość zagadnień związanych z ochroną informacji za pomocą metod kryptograficznych i z analizą odporności tych metod. W tym sensie jest pojęciem szerszym niż sama kryptografia. Kryptografia koncentruje się na konstruowaniu mechanizmów szyfrowania, uwierzytelniania i innych narzędzi ochrony danych. Kryptoanaliza zajmuje się natomiast badaniem słabości tych mechanizmów, czyli próbą wydobycia informacji bez znajomości uprawnionego klucza albo naruszenia zakładanych własności bezpieczeństwa. To rozróżnienie jest bardzo ważne, ponieważ bezpieczeństwo systemu kryptograficznego nigdy nie wynika wyłącznie z pomysłowości konstruktora. O jego wartości rozstrzyga również odporność na analizę przeciwnika. Już najprostsze szyfry historyczne dobrze pokazują tę dwoistość. To, co dla jednej strony jest metodą ukrycia wiadomości, dla drugiej staje się obiektem systematycznego ataku opartego na strukturze języka, przewidywalności komunikacji i własnościach użytego klucza.

#slide 3
## layout
definition
## term
Kryptografia
## definition
Dyscyplina zajmująca się metodami zapewniania bezpieczeństwa informacji, w szczególności przez szyfrowanie i pokrewne mechanizmy ochrony.
## teleprompter:
Kryptografia w sensie klasycznym kojarzy się przede wszystkim z szyfrowaniem, ale już w podstawowych opracowaniach jest ujmowana szerzej, jako część bezpieczeństwa informacji zajmująca się technikami ochrony danych. Jej centralny problem historycznie stanowiła tajność korespondencji, a więc takie przekształcenie tekstu jawnego, aby bez odpowiedniego klucza nie można było odtworzyć jego treści. Wraz z rozwojem systemów teleinformatycznych zakres kryptografii rozszerzył się o inne usługi bezpieczeństwa, takie jak integralność czy uwierzytelnienie. Mimo tego rozszerzenia punkt wyjścia pozostaje ten sam: dane trzeba przedstawić w takiej formie, aby określone własności były osiągalne nawet w środowisku, któremu nie można w pełni zaufać. Dlatego na początku najwygodniej wejść do tematu przez szyfrowanie. To ono najczytelniej pokazuje relację między wiadomością, kluczem, algorytmem i przeciwnikiem obserwującym komunikację.

#slide 4
## layout
definition
## term
Kryptoanaliza
## definition
Dziedzina badająca metody odzyskiwania informacji chronionej lub naruszania własności bezpieczeństwa bez posiadania uprawnionego klucza.
## teleprompter:
Kryptoanaliza stanowi naturalny odpowiednik kryptografii. Jeżeli kryptografia projektuje mechanizmy ochronne, to kryptoanaliza sprawdza, czy i w jakim zakresie można je obejść. W najprostszym ujęciu jej celem jest odzyskanie tekstu jawnego albo klucza na podstawie obserwowanych szyfrogramów. W ujęciu szerszym chodzi o każde naruszenie zakładanych własności bezpieczeństwa, nawet wtedy, gdy pełne odszyfrowanie nie następuje. To bardzo ważne, bo bezpieczeństwo nie jest stanem absolutnym, lecz relacją między konstrukcją systemu a możliwościami przeciwnika. W historii prostych szyfrów kryptoanaliza bardzo szybko wykazała, że samo przekształcenie liter nie gwarantuje jeszcze realnej ochrony. Częstotliwość występowania symboli, przewidywalne słowa, sztywna struktura języka i powtarzalność klucza mogą prowadzić do skutecznego ataku. Z tego powodu o systemie szyfrowania nie można mówić poważnie bez jednoczesnego uwzględnienia perspektywy analitycznej.

#slide 5
## layout
bullet
## slide title
Usługi bezpieczeństwa informacji
## bullets
- poufność
- integralność
- uwierzytelnienie
## teleprompter:
W podstawowym słowniku kryptografii bardzo wcześnie pojawia się pojęcie usług bezpieczeństwa. Są to własności lub funkcje ochronne, których potrzebuje system przetwarzający i przesyłający informacje. W tym wykładzie najważniejsza będzie poufność, ponieważ to ona prowadzi bezpośrednio do klasycznego modelu szyfrowania i do prostych szyfrów. Nie można jednak całkowicie pominąć dwóch innych pojęć, które wyznaczają szerszy kontekst komunikacji: integralności i uwierzytelnienia. Integralność dotyczy tego, czy dane pozostały niezmienione w sposób nieuprawniony. Uwierzytelnienie dotyczy tego, czy można uznać tożsamość strony albo pochodzenie komunikatu za wiarygodne. Już to proste zestawienie pokazuje, że bezpieczeństwo informacji nie sprowadza się do jednego pytania o tajność treści. Można przecież mieć dane zaszyfrowane, ale zmodyfikowane, albo wiadomość poprawnie ukrytą, lecz pochodzącą od podmiotu, który podszywa się pod kogoś innego. Dlatego uporządkowanie tych trzech pojęć jest potrzebne jeszcze przed wejściem w terminologię samych szyfrów.

#slide 6
## layout
definition
## term
Poufność
## definition
Własność polegająca na tym, że informacja nie jest ujawniana ani udostępniana podmiotom, procesom lub urządzeniom nieuprawnionym.
## teleprompter:
Poufność jest klasycznym i najbardziej intuicyjnym celem kryptografii. Chodzi o to, aby treść informacji była dostępna wyłącznie dla stron uprawnionych, nawet wtedy, gdy sam zapis danych zostanie przechwycony albo zaobserwowany przez przeciwnika. Z punktu widzenia teorii szyfrów oznacza to potrzebę takiego przekształcenia wiadomości, by bez odpowiedniego klucza nie dawała się odczytać lub poprawnie zinterpretować. Warto zauważyć, że poufność dotyczy informacji, a nie tylko fizycznego nośnika. Można utracić kontrolę nad kopią danych, a mimo to zachować poufność, jeżeli treść pozostaje praktycznie nieosiągalna dla strony nieuprawnionej. To właśnie ten sposób myślenia prowadzi do odróżnienia ochrony logicznej od samej ochrony fizycznej. W dalszej części wykładu poufność będzie osią porządkującą, bo na jej gruncie najłatwiej zbudować formalny model szyfrowania, wprowadzić pojęcie klucza i zacząć analizować skuteczność prostych metod kryptograficznych.

#slide 7
## layout
definition
## term
Integralność
## definition
Własność polegająca na tym, że dane nie zostały zmienione ani zniszczone w sposób nieuprawniony i niewykryty.
## teleprompter:
Integralność odpowiada na inne pytanie niż poufność. Nie chodzi już o to, czy przeciwnik poznał treść informacji, lecz o to, czy treść pozostała poprawna i nie została potajemnie zmodyfikowana. Można łatwo wyobrazić sobie sytuację, w której wiadomość pozostaje tajna, ale nie jest wiarygodna, bo ktoś zmienił jej fragment po drodze. W takim przypadku samo szyfrowanie nie rozwiązuje całego problemu bezpieczeństwa. Integralność jest więc własnością dotyczącą poprawności i nienaruszalności danych. W klasycznych prostych szyfrach ten problem nie był jeszcze ujmowany tak szeroko jak dzisiaj, ale już przy modelu komunikacji przez niezaufany kanał staje się oczywiste, że przeciwnik może nie tylko podsłuchiwać, lecz także ingerować w transmisję. W tym wykładzie integralność pojawia się jako punkt odniesienia, który pozwala odróżnić ochronę tajności od ochrony treści przed nieuprawnioną zmianą.

#slide 8
## layout
definition
## term
Uwierzytelnienie
## definition
Usługa związana z identyfikacją encji oraz potwierdzeniem pochodzenia informacji.
## teleprompter:
Uwierzytelnienie porządkuje pytanie inne niż to, które stawia sama poufność. Nie chodzi już o to, czy treść wiadomości została ukryta, lecz o to, czy wiadomość rzeczywiście pochodzi od deklarowanego źródła oraz czy strona uczestnicząca w komunikacji jest tym, za kogo się podaje. W literaturze to pojęcie bywa rozdzielane na uwierzytelnienie encji i uwierzytelnienie pochodzenia danych, ale na tym etapie ważne jest przede wszystkim uchwycenie wspólnego rdzenia. Odbiorca chce mieć podstawę, by uznać, że komunikuje się z właściwym podmiotem albo że otrzymany komunikat został rzeczywiście wygenerowany przez uprawnionego nadawcę. To pokazuje, że bezpieczeństwo komunikacji nie sprowadza się do ukrycia treści. Można wyobrazić sobie wiadomość zaszyfrowaną poprawnie, lecz pochodzącą od nieuprawnionej strony, która podszywa się pod kogoś innego. W takim przypadku poufność może być zachowana, a mimo to bezpieczeństwo systemu pozostaje naruszone.

#slide 9
## layout
definition
## term
Niezaprzeczalność
## definition
Usługa uniemożliwiająca podmiotowi zaprzeczanie wcześniejszym działaniom lub zobowiązaniom.
## teleprompter:
Niezaprzeczalność dotyczy sytuacji, w której po wykonaniu określonego działania uczestnik nie może później wiarygodnie twierdzić, że do tego działania nie doszło albo że nie był jego autorem. To pojęcie wychodzi poza samą tajność i poza zwykłe rozpoznanie nadawcy w chwili komunikacji. Chodzi o trwałą możliwość powiązania zdarzenia z określonym podmiotem. W świecie dokumentów papierowych częściowym odpowiednikiem bywa odręczny podpis, pieczęć albo zapis proceduralny. W świecie cyfrowym problem jest trudniejszy, bo kopiowanie danych jest łatwe, a sama obecność komunikatu w systemie nie wystarcza jeszcze do przypisania go danej osobie. W tym wykładzie niezaprzeczalność pojawia się jedynie jako element porządkujący mapę pojęć. Jej pełna realizacja wymaga zwykle narzędzi silniejszych niż proste szyfry klasyczne. Warto jednak od początku widzieć, że kryptografia nie jest jednowymiarowa.

#slide 10
## layout
bullet
## slide title
Dlaczego tutaj najważniejsza jest poufność
## bullets
- to klasyczny punkt wyjścia teorii szyfrów
- prowadzi bezpośrednio do formalnego modelu szyfrowania
- pozwala naturalnie wprowadzić proste szyfry historyczne
## teleprompter:
Spośród podstawowych usług bezpieczeństwa właśnie poufność prowadzi do najbardziej przejrzystego modelu formalnego. Najłatwiej na jej gruncie zdefiniować wiadomość jawną, szyfrogram, klucz, przestrzeń wiadomości, przestrzeń kluczy i relację między szyfrowaniem a odszyfrowaniem. Dzięki temu możliwe jest wejście do kryptologii przez uporządkowany język, a nie przez zbiór luźnych przykładów. Proste szyfry klasyczne dobrze nadają się do tego celu również dlatego, że są intuicyjne i zarazem ujawniają ważne ograniczenia. Pokazują, że ochrona informacji zależy nie tylko od samego faktu przekształcenia tekstu, lecz także od struktury języka, modelu przeciwnika i własności klucza. Skupienie na poufności nie oznacza więc, że pozostałe usługi bezpieczeństwa są mniej istotne. Oznacza jedynie, że tutaj budowany jest fundament pojęciowy, na którym później można bez chaosu umieścić bardziej złożone zagadnienia.

#slide 11
## layout
bullet
## slide title
Poufność a postać informacji
## bullets
- informacja może być tekstem, liczbą, obrazem lub kodem
- przedmiotem ochrony jest treść, niekoniecznie sam nośnik
- celem szyfrowania jest uczynienie danych nieczytelnymi bez klucza
## teleprompter:
Poufność nie jest związana wyłącznie z jednym rodzajem danych. Informacja, którą chce się chronić, może występować jako tekst naturalny, rekord liczbowy, obraz, sekwencja rozkazów, fragment programu albo inna struktura symboliczna. Z perspektywy kryptografii wspólny pozostaje jeden problem: jak przekształcić tę treść tak, aby osoba nieuprawniona nie mogła jej odczytać lub poprawnie zinterpretować. To od razu pokazuje, że przedmiotem ochrony nie jest sam materiał fizyczny, lecz znaczenie informacji zapisanej w określonej postaci. Nośnik może być widoczny, transmisja może zostać przechwycona, a mimo to treść ma pozostać nieujawniona. W praktyce właśnie dlatego szyfrowanie jest traktowane jako mechanizm logiczny, a nie wyłącznie fizyczny. Nie zamyka danych w sejfie, tylko zmienia ich reprezentację na taką, która bez właściwego klucza nie odsłania zamierzonego sensu.

#slide 12
## layout
bullet
## slide title
Poufność w świecie cyfrowym
## bullets
- informację elektroniczną łatwo kopiować
- kopie mogą być nieodróżnialne od oryginału
- dlatego ochrona nie może opierać się wyłącznie na fizycznym nośniku
## teleprompter:
Świat cyfrowy zmienia problem ochrony informacji w sposób zasadniczy. W przypadku dokumentów papierowych lub przedmiotów materialnych samo ograniczenie fizycznego dostępu bywało często znaczącą częścią ochrony. W przypadku danych elektronicznych taka intuicja szybko przestaje wystarczać. Informację można kopiować bardzo łatwo, szybko i bez pogarszania jakości. Co więcej, kopia może być funkcjonalnie nieodróżnialna od oryginału. To oznacza, że utrata wyłącznej kontroli nad nośnikiem nie musi wiązać się z usunięciem informacji z miejsca źródłowego. Przeciwnik może jednocześnie pozyskać treść i pozostawić system w stanie pozornie niezmienionym. Właśnie z tego powodu współczesna ochrona danych nie może opierać się tylko na fizycznym odgrodzeniu zasobu. Potrzebne są metody, które chronią sens informacji nawet wtedy, gdy jej zapis przemieszcza się przez środowisko, któremu nie można zaufać. Szyfrowanie staje się więc naturalnym narzędziem przeniesienia ciężaru ochrony z nośnika na samą reprezentację danych.

#slide 13
## layout
title
## slide title
Dostęp do danych a znajomość informacji
## subtitle
Widzieć zapis nie znaczy jeszcze rozumieć jego treść
## teleprompter:
Jedna z najważniejszych intuicji kryptografii polega na odróżnieniu dostępu do zapisu danych od dostępu do informacji w znaczeniu semantycznym. Przeciwnik może przechwycić plik, ramkę sieciową, wiadomość tekstową albo wydruk i mimo to nie uzyskać tego, co dla stron komunikacji stanowi właściwą treść. To rozróżnienie nie jest tylko filozoficzną subtelnością. Właśnie ono uzasadnia sens szyfrowania jako techniki ochrony. Gdyby samo wejście w posiadanie zapisu zawsze oznaczało automatycznie poznanie informacji, kryptografia nie mogłaby działać. W praktyce chodzi więc o takie przekształcenie reprezentacji danych, aby dla osoby nieuprawnionej pozostawała ona obserwowalna, ale nieinterpretowalna w sposób prowadzący do odzyskania zamierzonego sensu. To rozróżnienie dobrze porządkuje wcześniejsze uwagi o nośniku i treści. Nośnik może być skopiowany, transmisja może zostać podsłuchana, a zapis może być widoczny, jednak poufność może nadal pozostawać zachowana, jeżeli z obserwowanego obiektu nie da się wydobyć użytecznej wiedzy o wiadomości bez znajomości odpowiedniego sekretu.

#slide 14
## layout
definition
## term
Szyfrowanie
## definition
Odwracalne przekształcenie tekstu jawnego w szyfrogram, określone przez algorytm i klucz.
## teleprompter:
Po uporządkowaniu celu ochrony można wreszcie nazwać centralną operację klasycznej kryptografii. Szyfrowanie jest przekształceniem wiadomości jawnej w inną reprezentację, zwaną szyfrogramem, przy użyciu określonej metody i klucza. Ważne są tu dwa elementy. Po pierwsze, nie chodzi o dowolne zniekształcenie danych, lecz o transformację kontrolowaną, zdefiniowaną przez pewien schemat. Po drugie, transformacja ta ma być odwracalna dla strony uprawnionej, czyli taka, aby przy odpowiedniej informacji pomocniczej można było odzyskać wiadomość pierwotną. To właśnie odróżnia szyfrowanie od zwykłego ukrywania, maskowania czy niszczenia danych. Szyfrowanie nie usuwa treści, ale zmienia jej postać według reguły, która dla uprawnionego odbiorcy pozostaje wykonalna w przeciwnym kierunku. W prostych szyfrach historycznych ta odwracalność bywa bardzo intuicyjna, ponieważ polega na cofnięciu przesunięcia, odwróceniu podstawienia albo wykonaniu odwrotnej permutacji. Już na tym poziomie widać też, że sama obserwacja szyfrogramu nie wystarcza jeszcze do odzyskania tekstu jawnego, jeżeli brakuje wiedzy o użytej regule lub o konkretnym kluczu.

#slide 15
## layout
definition
## term
Deszyfrowanie
## definition
Operacja odzyskiwania tekstu jawnego z szyfrogramu przy użyciu właściwego klucza.
## teleprompter:
Deszyfrowanie jest operacją odwrotną względem szyfrowania, ale nie należy traktować go jako czysto mechanicznego dodatku do pierwszej z tych czynności. W dobrze zdefiniowanym schemacie szyfrowania relacja między obiema transformacjami stanowi warunek poprawności całego systemu. Oznacza to, że wiadomość zaszyfrowana właściwym kluczem ma dawać się odtworzyć przez uprawnioną stronę w sposób jednoznaczny i przewidywalny. Dzięki temu możliwe jest odróżnienie systemu kryptograficznego od zwykłego przekształcania symboli bez gwarancji odzyskania pierwotnej treści. W prostych szyfrach klasycznych deszyfrowanie często wygląda bardzo podobnie do szyfrowania, ale z użyciem odwrotnej reguły. W szyfrze przesuwającym cofa się przesunięcie, w szyfrze afinicznym stosuje się odwrotność odpowiedniej funkcji, a w szyfrze przestawieniowym odwraca się permutację. To ważne, ponieważ pokazuje, że klucz nie jest dekoracją do algorytmu, lecz elementem rozstrzygającym o tym, która dokładnie operacja odwrotna pozwala wrócić od szyfrogramu do wiadomości mającej sens dla odbiorcy.

#slide 16
## layout
bullet
## slide title
Algorytm i klucz to nie to samo
## bullets
- algorytm opisuje ogólną metodę przekształcenia
- klucz wybiera konkretną instancję tej metody
- bezpieczeństwo nie powinno zależeć od ukrycia samego algorytmu
## teleprompter:
Jednym z najczęstszych nieporozumień na początku nauki kryptografii jest mieszanie algorytmu z kluczem. Algorytm to opis metody działania systemu, czyli zbiór reguł określających, jak przekształca się wiadomość. Klucz jest natomiast parametrem wybierającym konkretną postać tej transformacji spośród wielu możliwych. W szyfrze Cezara algorytm mówi, że każdą literę należy przesunąć o pewną liczbę pozycji w alfabecie, natomiast klucz wskazuje, jaka to liczba. Takie rozróżnienie ma znaczenie fundamentalne, bo dopiero ono pozwala myśleć o systemie szyfrowania jako o rodzinie transformacji, a nie jako o jednym z góry ustalonym triku. W nowożytnej teorii bezpieczeństwa z tego wynika jeszcze ważniejsza zasada: przeciwnik może znać metodę działania systemu, a mimo to nie powinien umieć odczytać wiadomości bez znajomości sekretu. Ochrona ma więc spoczywać przede wszystkim na kluczu, nie na tajemnicy samego algorytmu. To rozróżnienie stanie się szczególnie istotne, gdy wykład przejdzie od intuicji opisowych do bardziej formalnego modelu schematu szyfrowania.

#slide 17
## layout
bullet
## slide title
Granice samej poufności
## bullets
- ukrycie treści nie mówi jeszcze, kto nadał wiadomość
- ukrycie treści nie gwarantuje braku zmian w transmisji
- sama tajność nie rozwiązuje problemu dystrybucji kluczy
## teleprompter:
Skoro podstawowym celem tego wykładu jest poufność, warto jasno nazwać także granice takiego skupienia. Sam fakt, że przeciwnik nie może odczytać treści, nie odpowiada jeszcze na wszystkie pytania, które pojawiają się w realnej komunikacji. Odbiorca nadal może nie wiedzieć, kto rzeczywiście jest nadawcą. Może też nie mieć pewności, czy wiadomość nie została po drodze zmodyfikowana albo czy do kanału nie wstrzyknięto nowej treści. Dodatkowo pozostaje praktyczny problem uzgodnienia i ochrony kluczy, bez których szyfrowanie nie może działać. Już na poziomie elementarnym widać więc, że poufność jest warunkiem bardzo ważnym, ale nie jedynym. Trzeba ją rozumieć jako jeden z głównych składników bezpieczeństwa informacji, a nie jako jego pełny odpowiednik. Takie ustawienie sprawy pozwala zachować porządek dalszego wykładu. Najpierw budowany jest model szyfrowania i jego terminologia, bo to najczytelniejszy punkt wejścia do kryptologii. Jednocześnie od początku pozostaje widoczne, że ukrycie treści nie wyczerpuje wszystkich wymagań, jakie stawia komunikacja prowadzona przez środowisko, któremu nie można bezwarunkowo ufać.

#slide 18
## layout
title
## slide title
Od celu ochrony do języka opisu
## subtitle
Aby mówić o poufności precyzyjnie, trzeba najpierw uporządkować terminologię
## teleprompter:
Na tym etapie samo ogólne stwierdzenie, że chcemy chronić poufność informacji, już nie wystarcza. Potrzebny jest język, który pozwala rozłożyć problem na elementy i relacje między nimi. Bez takiej terminologii bardzo łatwo mieszać poziomy opisu: utożsamiać wiadomość z jej reprezentacją, algorytm z kluczem, system z pojedynczym użyciem systemu, a przeciwnika z każdym podmiotem zewnętrznym bez rozróżnienia jego możliwości. Właśnie dlatego dalsza część wykładu przechodzi od ogólnego celu ochrony do słownika pojęć, które tworzą klasyczny model szyfrowania. Pojawią się więc alfabet, przestrzeń wiadomości, tekst jawny, przestrzeń szyfrogramów, przestrzeń kluczy, transformacja szyfrująca i transformacja deszyfrująca. Każdy z tych elementów wydaje się prosty osobno, ale dopiero po ich uporządkowaniu można mówić o schemacie szyfrowania z należytą precyzją. Ten porządek terminologiczny jest niezbędny nie tylko dla teorii. Bez niego trudno też sensownie porównywać nawet bardzo proste historyczne szyfry.

#slide 19
## layout
definition
## term
Alfabet
## definition
Skończony zbiór symboli, z których buduje się wiadomości i szyfrogramy.
## teleprompter:
Pojęcie alfabetu jest bardziej podstawowe, niż może się na pierwszy rzut oka wydawać. W kryptologii alfabet nie oznacza wyłącznie liter języka naturalnego. Jest to dowolny skończony zbiór symboli, na których operuje dany system. Mogą to być litery, cyfry, znaki interpunkcyjne, pary bitów, bajty albo inne elementy dyskretne. Ustalenie alfabetu jest konieczne, bo dopiero ono określa, z jakich jednostek wolno budować wiadomości i szyfrogramy. Bez tej decyzji nie wiadomo, co dokładnie jest dopuszczalnym wejściem i wyjściem dla transformacji kryptograficznych. W klasycznych szyfrach alfabet często bywa ograniczony do liter bez polskich znaków, spacji i interpunkcji, co upraszcza operacje, ale równocześnie zmienia własności tekstu. W systemach cyfrowych alfabet może być dużo bogatszy, lecz zasada pozostaje ta sama. Każdy model szyfrowania zaczyna się od ustalenia, na jakim zbiorze symboli pracuje. To właśnie ten poziom bazowy pozwala później definiować przestrzenie wiadomości, szyfrogramów i reguły transformacji.

#slide 20
## layout
definition
## term
Przestrzeń wiadomości
## definition
Zbiór dopuszczalnych wiadomości jawnych budowanych z symboli ustalonego alfabetu.
## teleprompter:
Przestrzeń wiadomości porządkuje odpowiedź na pytanie, jakie komunikaty dany schemat w ogóle dopuszcza jako wejście. Nie każda możliwa sekwencja symboli musi należeć do tego zbioru. W zależności od przyjętego modelu przestrzeń wiadomości może obejmować wszystkie skończone ciągi nad alfabetem albo tylko pewną ich klasę, na przykład komunikaty o określonej długości czy strukturze. To ważne, ponieważ bezpieczeństwo bywa silnie związane z tym, co przeciwnik wie o możliwych wiadomościach. Im bardziej ograniczona jest przestrzeń wiadomości, tym więcej informacji może wynikać z samego kontekstu użycia systemu. W prostych szyfrach klasycznych często zakłada się komunikaty tekstowe tworzone z alfabetu języka, co natychmiast wprowadza regularności statystyczne. Właśnie dlatego zdefiniowanie przestrzeni wiadomości nie jest drobnym technicznym szczegółem, lecz elementem wpływającym na realny poziom ochrony. Kiedy wiadomo, jakie komunikaty są dopuszczalne, łatwiej zrozumieć, co dokładnie ukrywa szyfrowanie i jakie ślady struktury wiadomości mogą mimo wszystko pozostać widoczne.

#slide 21
## layout
definition
## term
Tekst jawny
## definition
Wiadomość przed zaszyfrowaniem.
## teleprompter:
Tekst jawny to najprostszy i zarazem centralny element modelu szyfrowania. Jest to wiadomość w postaci, którą strony uznają za znaczącą i bezpośrednio interpretowalną przed zastosowaniem mechanizmu ochrony. W klasycznym przykładzie będzie to zdanie zapisane literami, ale w sensie ogólnym może to być dowolny obiekt należący do przestrzeni wiadomości. Ważne jest, aby nie traktować tekstu jawnego wyłącznie jako zwykłego napisu czy dokumentu. W modelu formalnym jest to element wejściowy dla transformacji szyfrującej. To właśnie jego treść ma zostać ukryta przed przeciwnikiem. W zależności od konstrukcji systemu część własności tekstu jawnego może jednak pozostawać pośrednio widoczna, na przykład długość wiadomości albo niektóre zależności strukturalne. Już samo nazwanie tego elementu tekstem jawnym przypomina więc, że szyfrowanie nie tworzy informacji z niczego, lecz przekształca określoną wiadomość wejściową w inną reprezentację, która dla strony nieuprawnionej ma utracić bezpośrednią czytelność.

#slide 22
## layout
definition
## term
Przestrzeń szyfrogramów
## definition
Zbiór dopuszczalnych tekstów zaszyfrowanych.
## teleprompter:
Tak jak istnieje przestrzeń wiadomości, tak istnieje również przestrzeń szyfrogramów, czyli zbiór rezultatów, które mogą pojawić się po stronie wyjścia procesu szyfrowania. To pojęcie porządkuje model od strony obserwatora. Przeciwnik zazwyczaj nie widzi wiadomości jawnej, ale widzi albo przechwytuje elementy należące właśnie do tej przestrzeni. W zależności od systemu przestrzeń szyfrogramów może pokrywać się z przestrzenią wiadomości, być od niej różna albo mieć inną strukturę długości i symboli. W prostych szyfrach podstawieniowych często operuje się na tym samym alfabecie po obu stronach, co tworzy złudzenie, że szyfrogram jest jedynie inną wersją zwykłego tekstu. To jednak nie zmienia faktu, że formalnie jest to odrębny zbiór obiektów, stanowiący wynik działania konkretnej transformacji. Oddzielenie przestrzeni wiadomości od przestrzeni szyfrogramów jest ważne, bo pomaga nie mieszać treści chronionej z jej zakodowaną reprezentacją oraz porządkować pytanie o to, co dokładnie przeciwnik może obserwować.

#slide 23
## layout
definition
## term
Szyfrogram
## definition
Wynik działania transformacji szyfrującej na tekście jawnym.
## teleprompter:
Szyfrogram jest rezultatem szyfrowania, czyli postacią wiadomości po zastosowaniu odpowiedniej transformacji i wybranego klucza. To właśnie ten obiekt przemieszcza się przez kanał i to on zwykle staje się przedmiotem obserwacji przeciwnika. W dobrze uporządkowanym opisie nie można utożsamiać szyfrogramu z samym szyfrem jako metodą. Szyfr jest schematem lub rodziną reguł, natomiast szyfrogram jest konkretnym wynikiem użycia tego schematu dla określonej wiadomości i określonego klucza. To rozróżnienie jest konieczne, ponieważ jedna metoda szyfrowania może generować bardzo wiele różnych szyfrogramów, a ten sam szyfrogram ma sens tylko w odniesieniu do ustalonego modelu i przestrzeni symboli. W praktyce analiza bezpieczeństwa często zaczyna się właśnie od pytania, ile informacji o wiadomości można wydobyć z obserwowanego szyfrogramu. Z tego powodu szyfrogram nie jest tylko technicznym skutkiem ubocznym działania algorytmu, lecz centralnym punktem styku między legalną komunikacją a możliwościami przeciwnika.

#slide 24
## layout
definition
## term
Przestrzeń kluczy
## definition
Zbiór dopuszczalnych kluczy używanych przez dany schemat szyfrowania.
## teleprompter:
Przestrzeń kluczy określa, jakie sekrety mogą zostać użyte w ramach danego schematu. Nie jest to po prostu zbiór wszystkich ciągów symboli, jakie da się zapisać, lecz dokładnie ten zbiór, który system uznaje za dopuszczalny i znaczący. To pojęcie ma duże znaczenie praktyczne, ponieważ liczność i struktura przestrzeni kluczy wpływają na odporność systemu na próby przeszukiwania oraz na sposób zarządzania sekretami. W prostych szyfrach klasycznych przestrzeń kluczy bywa stosunkowo mała, co samo w sobie może stanowić problem bezpieczeństwa. Jednak nawet duża przestrzeń kluczy nie gwarantuje jeszcze ochrony, jeśli różne klucze prowadzą do łatwo rozpoznawalnych wzorców albo jeśli struktura tekstu ujawnia zbyt wiele informacji. Wprowadzenie tego pojęcia jest więc potrzebne po to, by odróżnić ogólny opis systemu od konkretnego wyboru sekretu użytego w pojedynczej komunikacji. Dopiero na tle całej przestrzeni kluczy widać, czym jest pojedynczy klucz i jaką funkcję pełni w wyborze jednej z możliwych transformacji.

#slide 25
## layout
definition
## term
Klucz
## definition
Parametr wybierający konkretną transformację szyfrującą i odpowiadającą jej transformację odszyfrowującą.
## teleprompter:
Klucz jest najważniejszym sekretem w klasycznym modelu szyfrowania. Nie jest samą metodą, lecz parametrem, który wybiera jedną konkretną instancję działania spośród wielu możliwych przewidzianych przez schemat. Dzięki temu ten sam ogólny system może być używany wielokrotnie przez różne strony albo w różnych sesjach bez konieczności zmiany całej konstrukcji. To rozróżnienie między metodą a kluczem ma ogromne znaczenie dla bezpieczeństwa. Dobrze zaprojektowany system nie powinien wymagać ukrywania całego algorytmu przed światem. Wystarczy, że tajny pozostaje konkretny użyty klucz. W prostych szyfrach historycznych klucz bywał czasem utożsamiany z tajną tabelą podstawień lub z liczbą przesunięcia alfabetu. W systemach współczesnych ma postać bardziej formalną, lecz zasada jest identyczna: klucz określa, która transformacja ma zostać użyta po stronie nadawcy i jaka operacja odwracająca jest właściwa po stronie odbiorcy. Bez tego elementu szyfrowanie byłoby jedynie publiczną, stałą konwersją tekstu.

#slide 26
## layout
definition
## term
Transformacja szyfrująca
## definition
Odwzorowanie przypisujące wiadomości jawnej odpowiadający jej szyfrogram dla danego klucza.
## teleprompter:
Transformacja szyfrująca jest formalnym opisem operacji, która zamienia element przestrzeni wiadomości na element przestrzeni szyfrogramów. Kluczowe jest to, że nie działa ona w próżni. Zawsze trzeba wskazać zarówno schemat, jak i klucz, ponieważ dopiero ich połączenie określa konkretną regułę przekształcenia. W prostych szyfrach podstawieniowych transformacja szyfrująca może oznaczać zastąpienie każdej litery inną według ustalonego przyporządkowania. W szyfrach przestawieniowych może oznaczać zmianę kolejności symboli bez zmiany ich wartości. W sensie ogólnym nie ma jednak znaczenia, czy operacja wygląda intuicyjnie prosto czy matematycznie złożenie. Ważne jest to, że wiadomość jawna zostaje odwzorowana w szyfrogram w sposób przewidziany przez system. Dzięki takiemu formalnemu ujęciu można mówić o poprawności, odwracalności i bezpieczeństwie bez ograniczania się do pojedynczych przykładów. Transformacja szyfrująca stanowi więc rdzeń operacyjny całego procesu ochrony poufności.

#slide 27
## layout
definition
## term
Transformacja deszyfrująca
## definition
Odwzorowanie, które dla właściwego klucza odzyskuje tekst jawny z szyfrogramu.
## teleprompter:
Transformacja deszyfrująca jest dopełnieniem transformacji szyfrującej. Jej zadaniem nie jest wykonanie dowolnej obróbki szyfrogramu, lecz odzyskanie wiadomości jawnej wtedy, gdy użyto właściwej informacji kluczowej. W poprawnym schemacie relacja między szyfrowaniem a deszyfrowaniem musi być tak zbudowana, aby legalny odbiorca mógł wrócić do pierwotnej treści bez utraty znaczenia. To od razu pokazuje, że szyfrowanie nie może być przypadkowym zniekształceniem wiadomości. Musi być transformacją kontrolowaną, odwracalną dla strony uprawnionej i zarazem nieużyteczną dla strony nieuprawnionej. W klasycznych szyfrach podstawieniowych operacja deszyfrująca bywa po prostu odwróceniem tablicy przyporządkowań. W innych konstrukcjach może mieć postać bardziej złożoną. Formalne ujęcie pozostaje jednak niezmienne: istnieje reguła, która dla odpowiedniego klucza przekształca szyfrogram z powrotem w wiadomość. To właśnie ta relacja odwracalności będzie za chwilę punktem wyjścia do definicji poprawności całego schematu.

#slide 28
## layout
definition
## term
Schemat szyfrowania
## definition
Rodzina transformacji szyfrujących i odpowiadających im transformacji deszyfrujących, powiązanych przez przestrzeń kluczy.
## teleprompter:
Schemat szyfrowania nie jest pojedynczym szyfrogramem ani pojedynczym przekształceniem zastosowanym raz w konkretnej sytuacji. Jest uporządkowaną rodziną reguł działania, w której przestrzeń kluczy wskazuje, jak dobrać odpowiednią transformację szyfrującą oraz odpowiadającą jej transformację deszyfrującą. To pojęcie pozwala oddzielić poziom ogólnej konstrukcji od poziomu konkretnego użycia. Dzięki temu można mówić o własnościach systemu niezależnie od tego, jaka dokładnie wiadomość była przetwarzana w danym przypadku. W literaturze takie ujęcie jest niezbędne, bo bezpieczeństwo nie dotyczy pojedynczej wiadomości w izolacji, lecz klasy wszystkich dopuszczalnych użyć systemu. Schemat opisuje więc, jakie są zbiory wejść, jakie są zbiory wyjść, jakie klucze można wybrać i jak przebiega relacja między szyfrowaniem a deszyfrowaniem. Dopiero na tym poziomie można sensownie porównywać różne rozwiązania i mówić o ich sile, ograniczeniach oraz zgodności z określonym modelem zagrożeń.

#slide 29
## layout
bullet
## slide title
Relacja między pojęciami
## bullets
- alfabet buduje wiadomości
- wiadomość należy do przestrzeni wiadomości
- klucz wybiera transformację szyfrującą
- wynikiem jest szyfrogram z przestrzeni szyfrogramów
## teleprompter:
Dopiero zestawienie wcześniejszych definicji w jeden ciąg pokazuje pełny sens modelu. Najpierw istnieje alfabet, czyli skończony zbiór symboli. Z niego budowane są dopuszczalne wiadomości, które tworzą przestrzeń wiadomości. Jedna konkretna wiadomość staje się tekstem jawnym, gdy ma zostać przekazana i chroniona. Następnie wybierany jest klucz należący do przestrzeni kluczy. Ten wybór określa, która transformacja szyfrująca ma zostać użyta. Wynikiem działania jest szyfrogram, czyli element przestrzeni szyfrogramów. Po stronie odbiorcy odpowiednia transformacja deszyfrująca ma odzyskać wiadomość pierwotną. Taki łańcuch zależności wydaje się prosty, ale właśnie on tworzy formalny szkielet całej klasycznej kryptografii poufności. Każdy spór o bezpieczeństwo konkretnego rozwiązania dotyczy w gruncie rzeczy któregoś miejsca tego łańcucha: czy przestrzeń kluczy jest wystarczająca, czy transformacja ukrywa strukturę wiadomości, czy przeciwnik wie zbyt wiele o przestrzeni wiadomości, czy szyfrogram ujawnia niepożądane zależności.

#slide 30
## layout
definition
## term
Nadawca
## definition
Uprawniona strona wysyłająca wiadomość.
## teleprompter:
Nadawca jest stroną inicjującą przekaz chronionej informacji. W modelu klasycznym to on dysponuje tekstem jawnym, wybiera lub posiada odpowiedni klucz i wykonuje operację szyfrowania przed przesłaniem komunikatu przez kanał. Definicja jest z pozoru oczywista, ale ma znaczenie, ponieważ porządkuje role w komunikacji. Bez jasnego wskazania nadawcy trudno mówić o pochodzeniu danych, o odpowiedzialności za użycie klucza i o tym, kto właściwie przekształca wiadomość do postaci szyfrogramu. W systemach rzeczywistych jedna encja może pełnić wiele funkcji jednocześnie, lecz model podstawowy rozdziela role po to, aby opis był przejrzysty. Nadawca nie jest więc tylko osobą wysyłającą tekst w potocznym sensie. Jest jedną z uprawnionych stron uczestniczących w schemacie bezpieczeństwa, a jego działania są częścią formalnego procesu. To rozróżnienie będzie potrzebne później także przy definiowaniu przeciwnika oraz przy odróżnianiu zwykłej obserwacji kanału od legalnej komunikacji między stronami.

#slide 31
## layout
definition
## term
Odbiorca
## definition
Uprawniona strona, do której wiadomość jest adresowana.
## teleprompter:
Odbiorca stanowi drugą legalną stronę klasycznego modelu komunikacji szyfrowanej. To do niego adresowany jest szyfrogram przesyłany przez kanał i to on ma dysponować informacją pozwalającą odzyskać tekst jawny. W najprostszym przypadku odbiorca posiada ten sam klucz co nadawca albo klucz łatwo z nim powiązany. Znaczenie tej roli nie ogranicza się jednak do samego faktu odebrania danych. Odbiorca jest punktem, w którym można ocenić, czy schemat spełnia warunek poprawności, czyli czy po legalnym odszyfrowaniu uzyskiwana jest dokładnie ta wiadomość, którą wprowadził nadawca. To właśnie z perspektywy odbiorcy najlepiej widać różnicę między skutecznym zabezpieczeniem a losowym zniekształceniem danych. Jeżeli system nie pozwala uprawnionej stronie odzyskać treści w sposób pewny i jednoznaczny, nie realizuje poprawnie swojej funkcji. Dlatego para nadawca–odbiorca nie jest tylko wygodnym obrazem komunikacji, lecz podstawowym układem odniesienia dla całego modelu.

#slide 32
## layout
definition
## term
Przeciwnik
## definition
Strona inna niż nadawca i odbiorca, próbująca naruszyć usługę bezpieczeństwa realizowaną między nimi.
## teleprompter:
Przeciwnik nie jest w kryptologii figurą przypadkową ani psychologiczną, lecz elementem modelu. To podmiot inny niż legalne strony komunikacji, którego celem jest naruszenie usługi bezpieczeństwa, na przykład poznanie treści wiadomości, zmiana jej zawartości albo zakłócenie poprawnego działania systemu. Taka definicja ma bardzo ważną konsekwencję: bezpieczeństwa nie ocenia się w oderwaniu od przyjętego modelu przeciwnika. Trzeba określić, co potrafi obserwować, jakie ma możliwości działania i jakie informacje zna o systemie. W klasycznym podejściu nie zakłada się, że przeciwnik jest nieświadomy mechanizmu. Wręcz przeciwnie, opis systemu może być publicznie znany. Tajny ma pozostać przede wszystkim klucz. Dzięki temu analiza bezpieczeństwa nie opiera się na ukrywaniu całej metody, ale na odporności schematu nawet przy szerokiej wiedzy o jego konstrukcji. Już samo wprowadzenie przeciwnika jako formalnej roli sprawia, że kryptografia przestaje być wyłącznie sztuką kodowania tekstu, a staje się dyscypliną projektowania ochrony wobec jasno określonych zagrożeń.

#slide 33
## layout
definition
## term
Kanał
## definition
Środek przekazywania informacji od jednej encji do drugiej.
## teleprompter:
Kanał to sposób, w jaki informacja przemieszcza się między stronami komunikacji. Może mieć postać fizycznego medium, łącza sieciowego, połączenia radiowego albo dowolnego mechanizmu transmisji. W modelu kryptologicznym istotne jest jednak nie tyle techniczne medium samo w sobie, ile jego własności bezpieczeństwa. To właśnie przez kanał przepływa szyfrogram, a zatem to wobec kanału formułuje się pytanie, czy przeciwnik może podsłuchiwać, usuwać, zmieniać albo wstrzykiwać komunikaty. Już na tym etapie warto zauważyć, że termin „kanał” nie oznacza automatycznie środowiska zaufanego lub niezaufanego. Jest po prostu środkiem przekazu, którego charakter bezpieczeństwa trzeba dopiero określić. W klasycznych wyobrażeniach o szyfrowaniu kanał bywał traktowany jak tło dla wymiany wiadomości. W nowoczesnym opisie jest jednym z głównych elementów modelu zagrożeń. To właśnie jego właściwości decydują o tym, czy w ogóle potrzebne jest szyfrowanie i jakie inne mechanizmy ochronne powinny towarzyszyć samej poufności.

#slide 34
## layout
definition
## term
Kanał fizycznie bezpieczny
## definition
Kanał niedostępny fizycznie dla przeciwnika.
## teleprompter:
Kanał fizycznie bezpieczny to taki kanał, do którego przeciwnik nie ma fizycznego dostępu. W takim modelu możliwość podsłuchu lub ingerencji jest wykluczona nie przez samą kryptografię, lecz przez warunki środowiskowe i organizacyjne. Historycznie taki kanał mógł oznaczać przekaz osobisty, zamknięty obieg dokumentów albo inne rozwiązanie, które odcinało osoby nieuprawnione od medium transmisji. Z punktu widzenia teorii jest to model bardzo wygodny, bo upraszcza problem bezpieczeństwa komunikacji. W praktyce jednak bywa trudny do utrzymania, zwłaszcza przy komunikacji rozproszonej, zdalnej i masowej. Właśnie dlatego nowoczesna kryptografia coraz częściej zakłada, że kanał nie jest fizycznie bezpieczny i należy projektować ochronę mimo tej nieufności. Wprowadzenie tego pojęcia jest potrzebne również po to, by lepiej zrozumieć różnicę między bezpieczeństwem wynikającym z kontroli środowiska a bezpieczeństwem wynikającym z własności matematycznych schematu szyfrowania. To nie są te same rzeczy i nie należy ich utożsamiać.

#slide 35
## layout
definition
## term
Kanał niezabezpieczony
## definition
Kanał, z którego nieuprawnione strony mogą odczytywać, usuwać, wstawiać lub przestawiać informacje.
## teleprompter:
Kanał niezabezpieczony jest przeciwieństwem kanału fizycznie bezpiecznego. Zakłada się tu, że osoby nieuprawnione mogą mieć dostęp do transmisji i że ich możliwości nie ograniczają się jedynie do biernego podsłuchu. Mogą również usuwać komunikaty, wstawiać własne albo zmieniać kolejność przesyłanych informacji. Ta definicja jest bardzo ważna, ponieważ rozszerza obraz zagrożeń poza samą utratę poufności. Jeśli przeciwnik może aktywnie ingerować w kanał, problem bezpieczeństwa obejmuje już nie tylko tajność wiadomości, ale także integralność, autentyczność i odporność na manipulację przebiegiem komunikacji. Właśnie ten model jest w praktyce bliższy współczesnym sieciom komputerowym niż idealizowane założenie kanału całkowicie odciętego od przeciwnika. Dlatego nawet w wykładzie skoncentrowanym głównie na poufności warto od razu zapamiętać to pojęcie. Ujawnia ono, że szyfrowanie jest odpowiedzią na nieufne środowisko transmisji, a nie jedynie elegancką techniką ukrywania tekstu.

#slide 36
## layout
bullet
## slide title
Język klasycznej komunikacji szyfrowanej
## bullets
- nadawca
- odbiorca
- tekst jawny
- szyfrogram
- klucz
- kanał
- przeciwnik
## teleprompter:
W tym miejscu podstawowy słownik jest już prawie kompletny. Komunikację można opisać jako relację między nadawcą i odbiorcą, którzy chcą bezpiecznie przekazać tekst jawny. Do ochrony wykorzystują klucz i określony schemat szyfrowania, którego rezultatem staje się szyfrogram. Ten szyfrogram przechodzi przez kanał, wobec którego trzeba przyjąć odpowiedni model bezpieczeństwa. Całość obserwuje lub próbuje naruszyć przeciwnik, którego możliwości nie są nieokreślonym strachem, ale częścią formalnego opisu systemu. Tak zebrane pojęcia tworzą język klasycznej komunikacji szyfrowanej. To właśnie za jego pomocą można później zapisać prosty model działania systemu, mówić o poprawności deszyfrowania, opisywać szyfry symetryczne i analizować słabości prostych metod podstawieniowych oraz przestawieniowych. Bez tego etapu każdy dalszy opis pozostawałby intuicyjny i zbyt nieostry. Teraz można już przejść od samego słownika do pokazania, jak te elementy współpracują w jednym, uporządkowanym modelu operacyjnym.

#slide 37
## layout
title
## slide title
Od teorii tajności do praktyki komunikacji
## subtitle
Dlaczego sama poufność nie wyczerpuje problemu bezpieczeństwa
## teleprompter:
Do tej pory zasadnicza część wykładu dotyczyła języka klasycznej tajności. Pojawiły się pojęcia tekstu jawnego, szyfrogramu, klucza, przestrzeni wiadomości, przestrzeni kluczy, nadawcy, odbiorcy i przeciwnika. Taki słownik jest konieczny, bo bez niego nie da się mówić precyzyjnie o szyfrowaniu. Sam słownik nie wyczerpuje jednak problemu bezpieczeństwa komunikacji. Już w podstawowych źródłach kryptologii widać, że prywatność informacji jest tylko jedną z usług bezpieczeństwa, obok integralności, uwierzytelnienia i niezaprzeczalności. Diffie i Hellman ujmowali ten problem jeszcze szerzej: rozwój sieci i teleprzetwarzania sprawił, że nie wystarcza już model, w którym dwie strony w jakiś nieproblematyczny sposób mają wcześniej wspólny sekret, a później jedynie ukrywają treść wiadomości przed podsłuchującym. W realnym systemie dochodzi pytanie, czy kanał jest godny zaufania, czy ktoś może do niego wstrzykiwać wiadomości, czy można bezpiecznie posługiwać się kluczami na większą skalę i czy legalny odbiorca ma podstawę, by uznać źródło otrzymanej wiadomości. Ten moment nie oznacza porzucenia klasycznej teorii tajności. Oznacza raczej, że uzyskane wcześniej pojęcia zaczynają pracować w pełnym modelu komunikacji. Od tego miejsca kryptografia przestaje wyglądać jak technika prostego ukrywania tekstu, a zaczyna być widziana jako sposób budowania ochrony ponad środowiskiem, które może być obserwowane, zakłócane i częściowo kontrolowane przez przeciwnika. Właśnie dlatego teraz trzeba przejść od samej poufności do modelu szyfrowania w kanale, do założenia jawności systemu, do roli klucza oraz do zagrożeń biernych i aktywnych.

#slide 38
## layout
definition
## term
Kanał publiczny
## definition
Kanał komunikacyjny, którego bezpieczeństwo jest niewystarczające dla potrzeb jego użytkowników; może być narażony na podsłuch, modyfikację lub wstrzykiwanie wiadomości.
## teleprompter:
Pojęcie kanału publicznego jest kluczowe, bo porządkuje model zagrożeń bez przywiązywania się do fizycznej natury medium. W ujęciu Diffiego i Hellmana kanał jest publiczny nie dlatego, że każdy ma do niego formalny dostęp, lecz dlatego, że poziom jego bezpieczeństwa nie wystarcza potrzebom stron, które z niego korzystają. To ważna różnica. Ten sam kanał dla jednego zastosowania może być wystarczający, a dla innego nie. Przewód telefoniczny, łącze sieciowe czy dowolna droga transmisji nie są bezpieczne lub niebezpieczne w sensie absolutnym; ich ocena zależy od tego, jaką wartość ma przesyłana informacja i jakie działania przeciwnika trzeba uznać za realistyczne. W tym modelu trzeba założyć co najmniej trzy klasy zagrożeń. Po pierwsze, podsłuch, czyli możliwość poznania treści komunikatu. Po drugie, modyfikację, czyli nieuprawnioną zmianę przesyłanej wiadomości. Po trzecie, wstrzykiwanie wiadomości, czyli dodawanie do kanału nowych komunikatów, które mogą sprawiać wrażenie legalnych. Tak rozumiany kanał publiczny nie jest pobocznym szczegółem, ale jednym z fundamentów nowoczesnej kryptografii. To właśnie dla takiego kanału projektuje się szyfrowanie, metody uwierzytelniania i rozwiązania problemu dystrybucji kluczy. W praktyce oznacza to rezygnację z wygodnego założenia, że bezpieczeństwo zapewnia samo środowisko transmisji. Ochrona ma wynikać z własności systemu kryptograficznego, a nie z zaufania do medium.

#slide 39
## layout
bullet
## slide title
Podstawowy model komunikacji szyfrowanej
## bullets
- nadawca dysponuje tekstem jawnym
- klucz wybiera transformację szyfrującą
- przez kanał przesyłany jest szyfrogram
- odbiorca odzyskuje wiadomość przez deszyfrowanie
- przeciwnik obserwuje lub próbuje naruszyć komunikację
## teleprompter:
Najprostszy model komunikacji szyfrowanej można opisać jako uporządkowany ciąg operacji. Nadawca posiada wiadomość jawną należącą do dopuszczalnej przestrzeni wiadomości. Następnie używa klucza, który wskazuje konkretną transformację szyfrującą z rodziny transformacji określonych przez schemat. Wynikiem jest szyfrogram przesyłany przez kanał do odbiorcy. Odbiorca, dysponując odpowiednią informacją kluczową, wykonuje transformację odwrotną i odzyskuje tekst jawny. Wokół tego procesu pojawia się przeciwnik. Może jedynie obserwować przepływ danych, ale może też próbować zakłócać komunikację albo wykorzystać wiedzę o systemie do odtworzenia treści. Ten model jest prosty, lecz bardzo silny analitycznie. Pozwala oddzielić role uczestników, wskazać miejsce działania klucza, zrozumieć pojęcie poprawności oraz określić, gdzie dokładnie pojawiają się zagrożenia. W literaturze taki opis jest podstawowy, ponieważ zabezpieczenie nie dotyczy samotnej wiadomości, ale procesu komunikacji jako całości. Już sam fakt, że przez kanał nie przechodzi tekst jawny, lecz szyfrogram, nie przesądza jeszcze o bezpieczeństwie. Trzeba jeszcze zapytać, co przeciwnik wie o schemacie, jak duża jest przestrzeń kluczy, czy legalny odbiorca może niezawodnie odwrócić transformację i czy środowisko transmisji dopuszcza tylko podsłuch, czy także aktywną ingerencję.

#slide 40
## layout
definition
## term
Schemat szyfrowania
## definition
Zbiór transformacji szyfrujących i odpowiadających im transformacji deszyfrujących, powiązanych przez przestrzeń kluczy.
## teleprompter:
Schemat szyfrowania jest bardziej ogólnym pojęciem niż pojedynczy szyfr użyty w konkretnej sytuacji. Obejmuje całą rodzinę dopuszczalnych transformacji szyfrujących oraz odpowiadających im transformacji deszyfrujących. Spina je przestrzeń kluczy, która określa, jakie warianty działania są dostępne i jaką transformację wybiera się w konkretnym użyciu. Dzięki temu bezpieczeństwo można analizować nie na poziomie pojedynczej wiadomości, lecz na poziomie konstrukcji jako takiej. To bardzo ważne rozróżnienie. Gdy mówi się, że jakiś system jest mocny lub słaby, nie chodzi przecież o jeden przypadkowy szyfrogram, ale o własności całej rodziny przekształceń dostępnych dla różnych kluczy. W takim ujęciu łatwo też zrozumieć, dlaczego klucz nie jest tylko dodatkiem technicznym. Bez klucza mielibyśmy pojedynczą, stałą metodę konwersji tekstu, którą przeciwnik mógłby z czasem poznać i stale wykorzystywać. Schemat szyfrowania tworzy zatem ogólną architekturę ochrony poufności: określa, jakie są wejścia, jakie są wyjścia, jak wygląda odwracalność i które elementy pozostają jawne, a które tajne. To właśnie na tym poziomie można później mówić o szyfrowaniu symetrycznym, o różnicy między prostymi szyframi klasycznymi a późniejszymi konstrukcjami oraz o tym, dlaczego bezpieczeństwo nie powinno zależeć od ukrycia całej metody.

#slide 41
## layout
definition
## term
Warunek poprawności
## definition
Dla właściwie dobranej pary kluczy deszyfrowanie szyfrogramu ma odzyskiwać dokładnie wiadomość jawną, czyli Dd(Ee(m)) = m.
## teleprompter:
Każdy sensowny schemat szyfrowania musi spełniać podstawowy warunek poprawności. Oznacza on, że legalna strona dysponująca właściwym kluczem deszyfrującym ma być w stanie odzyskać dokładnie tę wiadomość, którą nadawca wcześniej zaszyfrował. W zapisie formalnym wyraża się to równaniem Dd(Ee(m)) = m. Ten zapis jest prosty, ale ma głębokie znaczenie. Pokazuje, że szyfrowanie nie jest dowolnym zamazaniem treści. Jest transformacją odwracalną dla strony uprawnionej. Jeżeli po legalnym odszyfrowaniu nie odzyskuje się jednoznacznie wiadomości pierwotnej, to system nie realizuje poprawnie podstawowej funkcji poufności komunikacji. Warunek poprawności jest też dobrym punktem wyjścia do myślenia o relacji między użytecznością a bezpieczeństwem. System, którego nie da się wygodnie odwrócić przez legalnego odbiorcę, nie jest po prostu „bardziej bezpieczny”; jest wadliwy. Z drugiej strony sama poprawność nic jeszcze nie mówi o odporności na przeciwnika. Można zbudować szyfr doskonale odwracalny, który będzie bardzo łatwy do złamania. Trzeba więc odróżniać dwie kwestie: poprawność dla legalnych stron i bezpieczeństwo wobec strony nieuprawnionej. Obie są konieczne, ale żadna nie zastępuje drugiej.

#slide 42
## layout
bullet
## slide title
Dlaczego potrzebny jest klucz
## bullets
- ujawnienie jednego klucza nie wymaga zmiany całego schematu
- ten sam schemat może działać w wielu niezależnych użyciach
- bezpieczeństwo ma zależeć od klucza, nie od tajności całej metody
## teleprompter:
Pytanie o sens klucza jest bardzo ważne, bo bez niego trudno zrozumieć architekturę kryptografii. Można zapytać: skoro istnieje transformacja szyfrująca i deszyfrująca, to dlaczego nie używać po prostu jednej, stałej reguły? Odpowiedź jest praktyczna i fundamentalna zarazem. Klucz pozwala korzystać z tego samego schematu wielokrotnie i niezależnie w różnych relacjach komunikacyjnych. Jeżeli ujawniony zostanie jeden konkretny klucz, nie trzeba porzucać całej konstrukcji; wystarczy zmienić parametr użycia. To odróżnia dobry system kryptograficzny od sytuacji, w której bezpieczeństwo zależy od sekretności całej metody. Klucz działa więc jak wymienialny element sterujący, który określa, która z wielu dopuszczalnych transformacji jest aktualnie używana. Taka konstrukcja ma jeszcze jedną zaletę. Umożliwia publiczną analizę i standaryzację schematu, bo tajne nie muszą być reguły systemu, lecz jedynie konkretna informacja kluczowa. Właśnie dlatego w dojrzałym podejściu kryptologicznym to klucz staje się głównym nośnikiem tajności. Sam schemat powinien pozostawać odporny nawet wtedy, gdy przeciwnik zna jego budowę, zasady działania i ogólny sposób implementacji. Bez tego bezpieczeństwo byłoby kruche i trudne do utrzymania w rzeczywistym świecie.

#slide 43
## layout
definition
## term
Szyfrowanie symetryczne
## definition
Schemat szyfrowania, w którym dla powiązanej pary kluczy łatwo wyznaczyć klucz deszyfrujący z szyfrującego i odwrotnie; w praktyce często oba są takie same.
## teleprompter:
Szyfrowanie symetryczne to podstawowy model klasycznej kryptografii poufności. Jego istota polega na tym, że klucz używany do szyfrowania i klucz używany do deszyfrowania są identyczne albo ściśle ze sobą powiązane w sposób obliczeniowo łatwy. W praktyce bardzo często mówi się po prostu o jednym wspólnym sekrecie posiadanym przez obie strony. Taki model dobrze pasuje do prostych szyfrów klasycznych i do bardzo wielu systemów współczesnych. Ma on jednak ważną konsekwencję organizacyjną. Skoro obie strony muszą znać ten sam sekret, to trzeba go najpierw bezpiecznie uzgodnić albo bezpiecznie przekazać. Sama operacja szyfrowania może być bardzo sprawna, lecz cały system nadal zależy od tego, czy udało się rozwiązać problem klucza. To właśnie dlatego szyfrowanie symetryczne bywa nazywane także szyfrowaniem konwencjonalnym lub tradycyjnym. Oferuje prosty i bardzo naturalny model matematyczny, ale nie usuwa trudności związanych z bezpiecznym rozpoczęciem komunikacji. Ta uwaga będzie miała ogromne znaczenie przy przejściu do problemu dystrybucji kluczy, który Diffie i Hellman uczynili jednym z centralnych tematów nowoczesnej kryptografii.

#slide 44
## layout
bullet
## slide title
Jawny system, tajny klucz
## bullets
- zbiory wiadomości, szyfrogramów i kluczy mogą być publicznie znane
- opis transformacji może być publiczny
- tajny ma pozostać konkretny używany klucz
## teleprompter:
Jedną z najważniejszych zasad dojrzałego myślenia kryptologicznego jest założenie, że bezpieczeństwo systemu nie powinno zależeć od ukrycia całego mechanizmu. W literaturze przyjmuje się, że przestrzenie wiadomości, szyfrogramów i kluczy, a także klasa stosowanych transformacji mogą być znane publicznie. To, co ma pozostać tajne, to konkretny klucz wybrany do danego użycia. Powód jest bardzo praktyczny. Historia pokazała, że utrzymanie w sekrecie całej konstrukcji jest trudne, a w środowisku technicznym często nierealne. Urządzenia można badać, oprogramowanie można analizować, standardy bywają publiczne, a rozwiązania komercyjne muszą współpracować między wieloma stronami. Jeżeli system traci bezpieczeństwo już wtedy, gdy jego opis staje się znany, to jest systemem kruchym. Znacznie mocniejszym założeniem jest to, że przeciwnik zna metodę, lecz nie zna aktualnego klucza. Taki sposób myślenia pozwala odróżnić trwałe bezpieczeństwo od bezpieczeństwa przez zaciemnienie. Umożliwia też otwartą analizę, porównywanie rozwiązań i wykrywanie błędów konstrukcyjnych bez niszczenia zaufania do samej idei kryptografii. W tym sensie jawność systemu nie jest słabością, ale warunkiem dojrzałej oceny jego jakości.

#slide 45
## layout
definition
## term
Przestrzeń kluczy
## definition
Zbiór wszystkich dopuszczalnych kluczy, z którego wybierany jest klucz używany w danym szyfrowaniu.
## teleprompter:
Przestrzeń kluczy określa, jak wiele różnych kluczy może zostać użytych w ramach danego schematu. To pojęcie ma bezpośredni związek z bezpieczeństwem, ponieważ przeciwnik próbujący przeszukać wszystkie możliwości działa właśnie na przestrzeni kluczy. Im mniejsza ta przestrzeń, tym łatwiej wyobrazić sobie pełne sprawdzenie wszystkich kandydatów. Im większa, tym trudniej przeprowadzić takie poszukiwanie w rozsądnym czasie. Sama liczebność przestrzeni nie rozwiązuje jednak całego problemu. Można mieć pozornie ogromny zbiór kluczy, a mimo to stworzyć system słaby z innych powodów, na przykład przez ujawnianie struktury wiadomości w szyfrogramie. Mimo to pojęcie przestrzeni kluczy jest absolutnie podstawowe, bo pozwala formalnie mówić o atakach siłowych, o zmianie klucza bez zmiany schematu i o relacji między konstrukcją systemu a kosztem jego przełamania. W prostych szyfrach historycznych przestrzeń kluczy bywa mała i łatwa do opisania, jak w szyfrze przesuwającym alfabet o kilka pozycji. W bardziej rozbudowanych systemach staje się bardzo duża, ale nadal pozostaje tym samym pojęciem: zbiorem dopuszczalnych tajnych parametrów sterujących działaniem schematu.

#slide 46
## layout
bullet
## slide title
Przeszukiwanie pełnej przestrzeni kluczy
## bullets
- przeciwnik może próbować wszystkich możliwych kluczy
- taki atak nazywa się exhaustive search
- przestrzeń kluczy ma być na tyle duża, by ten atak był obliczeniowo niewykonalny
## teleprompter:
Jednym z najbardziej naturalnych sposobów ataku na szyfr jest sprawdzenie wszystkich dopuszczalnych kluczy i wybranie tego, który prowadzi do sensownego odczytania wiadomości. Taki sposób postępowania nazywa się pełnym przeszukaniem przestrzeni kluczy. Z teoretycznego punktu widzenia jest bardzo prosty i dlatego stanowi ważny punkt odniesienia dla projektowania systemów. Jeżeli schemat można złamać szybciej niż przez pełne przeszukanie, to oznacza, że konstrukcja zdradza dodatkową słabość. Jeżeli natomiast najlepszą znaną metodą pozostaje sprawdzenie wszystkich możliwości, to bezpieczeństwo zależy od tego, czy liczba kluczy jest wystarczająco duża, by taki wysiłek był obliczeniowo nieopłacalny. To pojęcie pozwala też odróżnić systemy szkoleniowe i historyczne od systemów przeznaczonych do realnej ochrony. W prostych szyfrach klasycznych przestrzeń kluczy bywa tak mała, że atak siłowy jest trywialny. W nowoczesnej kryptografii zakłada się, że sama wielkość przestrzeni kluczy ma co najmniej uniemożliwiać ten podstawowy atak. Nie znaczy to jeszcze, że system jest automatycznie silny, ale znaczy, że nie odpada już na najprostszym teście odporności.

#slide 47
## layout
definition
## term
Schemat łamliwy
## definition
Schemat szyfrowania, w którym strona trzecia bez wcześniejszej znajomości pary kluczy może systematycznie odzyskiwać tekst jawny z odpowiadających mu szyfrogramów w odpowiednim przedziale czasu.
## teleprompter:
Pojęcie łamliwości porządkuje pytanie o to, kiedy należy uznać, że szyfr rzeczywiście został przełamany. Nie chodzi o pojedynczy przypadek szczęśliwego trafu, lecz o metodę systematycznego odzyskiwania wiadomości lub klucza w czasie, który ma znaczenie z punktu widzenia wartości chronionych danych. To ostatnie zastrzeżenie jest bardzo ważne. Informacja handlowa, która ma znaczenie przez kilka minut, i tajemnica państwowa, która ma pozostać ukryta przez dziesięciolecia, nie stawiają systemowi identycznych wymagań czasowych. Dlatego ocena łamliwości zawsze jest związana nie tylko z matematyką szyfru, lecz także z użyciem i żywotnością danych. Sama definicja przypomina również, że bezpieczeństwo nie jest pojęciem absolutnym w sensie potocznym. Można mieć schemat, który nie jest teoretycznie doskonały, ale którego przełamanie w praktycznym horyzoncie czasu pozostaje niewykonalne. Można też mieć schemat elegancki formalnie, lecz nieprzydatny operacyjnie, bo daje się przełamać zbyt szybko. To rozróżnienie będzie istotne przy przejściu od bezpieczeństwa bezwarunkowego do bezpieczeństwa obliczeniowego.

#slide 48
## layout
definition
## term
Bezpieczeństwo obliczeniowe
## definition
Własność systemu, którego przełamanie jest teoretycznie możliwe, lecz koszt obliczeniowy ataku jest zbyt duży, by był praktycznie wykonalny.
## teleprompter:
Bezpieczeństwo obliczeniowe opiera się na realistycznym założeniu, że przeciwnik nie dysponuje nieskończonym czasem ani nieskończoną mocą obliczeniową. W takim ujęciu system może być w zasadzie podatny na atak przy nieograniczonych zasobach, ale nadal pozostawać bezpieczny w praktyce, ponieważ koszt ataku jest nieakceptowalnie wysoki. To podejście dominuje w znacznej części współczesnej kryptografii. Jego siła bierze się z dopasowania do świata technicznego, gdzie zawsze istnieją ograniczenia czasu, pamięci, sprzętu i energii. Dzięki temu można budować systemy użyteczne, szybkie i możliwe do wdrożenia, nawet jeśli nie zapewniają one doskonałej tajności w sensie Shannona. Bezpieczeństwo obliczeniowe nie jest jednak wygodną wymówką dla bylejakości. Wymaga ostrożnej oceny, jakie ataki są najlepsze, jak szybko rozwija się technika i jak długo chronione dane muszą zachować poufność. System bezpieczny dziś może nie być równie bezpieczny w przyszłości, jeśli zmieni się koszt obliczeń albo pojawi się nowa metoda kryptoanalizy. Mimo tego to właśnie bezpieczeństwo obliczeniowe stało się praktycznym fundamentem większości użytecznych rozwiązań kryptograficznych.

#slide 49
## layout
definition
## term
Bezpieczeństwo bezwarunkowe
## definition
Własność systemu odpornego nawet wobec przeciwnika o nieograniczonych zasobach obliczeniowych; dla szyfrowania odpowiada jej doskonała tajność.
## teleprompter:
Bezpieczeństwo bezwarunkowe jest najsilniejszym modelem ochrony. Zakłada się w nim, że przeciwnik może mieć nieograniczone zasoby obliczeniowe, a mimo to z obserwacji szyfrogramu nie uzyskuje informacji wystarczającej do pokonania systemu. W przypadku szyfrowania taki ideał nazywa się doskonałą tajnością. Oznacza to, że po zobaczeniu szyfrogramu przeciwnik nie wie o wiadomości więcej niż wiedział przed jego zobaczeniem. Jest to kryterium niezwykle wymagające, bo nie pyta o koszt ataku, lecz o samą informacyjną możliwość uzyskania przewagi. W praktyce taki poziom bezpieczeństwa jest bardzo trudny do osiągnięcia w sposób wygodny i skalowalny. Właśnie dlatego literatura odróżnia systemy bezwarunkowo bezpieczne od systemów bezpiecznych obliczeniowo. To rozróżnienie ma duże znaczenie dydaktyczne. Pokazuje, że w kryptografii istnieją dwa różne pytania. Pierwsze brzmi: czy atak jest w ogóle możliwy przy nieograniczonych zasobach. Drugie: czy atak jest wykonalny w świecie rzeczywistym. Dopiero rozumienie obu poziomów pozwala poprawnie ocenić sens prostych szyfrów, rolę klucza i znaczenie późniejszych konstrukcji.

#slide 50
## layout
bullet
## slide title
Jednorazowy pad jako punkt odniesienia
## bullets
- jednorazowy pad jest przykładem szyfru o doskonałej tajności
- wymaga klucza losowego o długości co najmniej równej wiadomości
- praktyczna trudność leży w wytworzeniu i bezpiecznej dystrybucji takiego klucza
## teleprompter:
Jednorazowy pad zajmuje w kryptografii miejsce szczególne, ponieważ jest klasycznym przykładem systemu zapewniającego doskonałą tajność. Jego znaczenie wykracza poza samą praktykę użycia. Stanowi punkt odniesienia dla całej teorii bezpieczeństwa, pokazując, że absolutna poufność nie jest pojęciem pustym, lecz może zostać osiągnięta pod bardzo wymagającymi warunkami. Klucz musi być naprawdę losowy, musi mieć długość co najmniej równą długości wiadomości i nie może zostać użyty ponownie. Te warunki są właśnie źródłem praktycznej trudności. Problemem nie jest samo wykonanie operacji szyfrowania, lecz przygotowanie, przechowanie i bezpieczne przekazanie ogromnej ilości materiału kluczowego. Z tego powodu jednorazowy pad jest teorią graniczną bardziej niż powszechnym narzędziem codziennej komunikacji. Pozwala jednak bardzo dobrze zobaczyć napięcie między ideałem a użytecznością. Im silniejsze warunki bezpieczeństwa informacyjnego, tym trudniejsze bywa operacyjne utrzymanie systemu. Ta obserwacja prowadzi bezpośrednio do pytania, dlaczego większość praktycznych systemów opiera się na bezpieczeństwie obliczeniowym i dlaczego problem klucza staje się równie ważny jak sam algorytm szyfrowania.

#slide 51
## layout
bullet
## slide title
Problem dystrybucji kluczy w kryptografii konwencjonalnej
## bullets
- strony muszą najpierw mieć wspólny sekret
- sekret zwykle trzeba przekazać innym bezpiecznym kanałem
- koszt i opóźnienie tego procesu rosną wraz z liczbą użytkowników
## teleprompter:
W szyfrowaniu konwencjonalnym centralny problem nie kończy się na samym przekształceniu wiadomości w szyfrogram. Zanim jakakolwiek poufna komunikacja będzie możliwa, strony muszą już wcześniej posiadać wspólny sekret albo muszą go sobie bezpiecznie przekazać. To właśnie nazywa się problemem dystrybucji kluczy. W małej skali można go czasem ukryć za pomocą kontaktu osobistego, kuriera, dedykowanego łącza lub innego fizycznie bezpiecznego kanału. W dużych sieciach taka strategia szybko staje się kosztowna, powolna i organizacyjnie niewygodna. Diffie i Hellman bardzo mocno podkreślali, że właśnie ten problem staje się jedną z głównych barier dla bezpiecznej komunikacji w świecie teleprzetwarzania. Nie chodzi więc tylko o to, czy szyfr jest matematycznie elegancki, ale o to, czy system da się uruchomić między wieloma stronami, które wcześniej się nie znały i nie miały okazji wymienić sekretu poza siecią. To przesuwa punkt ciężkości z samego ukrywania treści na architekturę całego procesu bezpieczeństwa. Właśnie dlatego nowoczesna kryptografia nie mogła zatrzymać się na klasycznym modelu wspólnego klucza przekazywanego z góry osobnym kanałem.

#slide 52
## layout
title
## slide title
Od szyfrowania wiadomości do problemu klucza
## subtitle
Dlaczego sam model wspólnego sekretu nie skaluje się dobrze
## teleprompter:
W tym miejscu staje się widoczne ograniczenie tradycyjnego wyobrażenia o bezpiecznej komunikacji. Można mieć poprawny schemat szyfrowania, rozsądnie dużą przestrzeń kluczy i dobrą ochronę przed prostym podsłuchem, a mimo to cały system może okazać się niewygodny lub niewystarczający w praktyce. Powód leży w kluczu. Jeżeli każda para stron musi najpierw uzgodnić wspólny sekret w bezpieczny sposób poza głównym kanałem komunikacji, to wraz ze wzrostem liczby użytkowników rosną koszty organizacyjne, liczba relacji zaufania i ryzyko operacyjne. Diffie i Hellman pokazali, że właśnie tutaj klasyczny model przestaje dobrze odpowiadać potrzebom środowisk sieciowych. To nie jest jeszcze moment pełnego wejścia w kryptografię klucza publicznego, bo zakres tego wykładu pozostaje skupiony na podstawach, poufności i prostych szyfrach. Warto jednak już teraz uchwycić sam problem. Bezpieczna komunikacja to nie tylko odpowiedź na pytanie, jak ukryć tekst, lecz także odpowiedź na pytanie, jak zorganizować użycie kluczy wtedy, gdy kanał jest publiczny, a liczba potencjalnych partnerów komunikacji jest duża. To właśnie napięcie między teorią tajności a praktyką dystrybucji kluczy otwiera drogę do dalszego rozwoju kryptografii.

#slide 53
## layout
definition
## term
Przeciwnik pasywny
## definition
Przeciwnik zdolny wyłącznie do odczytywania informacji z niezabezpieczonego kanału.
## teleprompter:
Przeciwnik pasywny jest najprostszym, ale zarazem bardzo istotnym modelem zagrożenia. Zakłada się, że może obserwować komunikację, przechwytywać szyfrogramy i gromadzić informacje o ruchu, lecz nie ingeruje aktywnie w sam przebieg transmisji. Taki model jest szczególnie ważny dla problemu poufności, ponieważ właśnie wobec niego najczyściej formułuje się pytanie, czy szyfrogram ujawnia treść wiadomości. Przeciwnik pasywny nie musi być słaby intelektualnie ani technicznie. Może dysponować dużymi zasobami analitycznymi, może znać schemat szyfrowania i może prowadzić zaawansowaną kryptoanalizę. Ograniczenie dotyczy tylko jego relacji z kanałem: obserwuje, ale nie modyfikuje. Ten model dobrze pasuje do klasycznego obrazu podsłuchującego oponenta, który próbuje wydobyć znaczenie z zaszyfrowanych komunikatów. W dydaktyce jest to naturalny punkt startu, bo pozwala oddzielić problem tajności od problemów aktywnego fałszowania przekazu. Jednocześnie trzeba pamiętać, że wiele realnych sieci dopuszcza więcej niż sam podsłuch. Dlatego przeciwnik pasywny jest ważnym minimum, ale nie zawsze wystarcza jako pełny opis zagrożeń.

#slide 54
## layout
definition
## term
Przeciwnik aktywny
## definition
Przeciwnik, który może nie tylko obserwować, lecz także transmitować, modyfikować lub usuwać informacje w niezabezpieczonym kanale.
## teleprompter:
Przeciwnik aktywny rozszerza model zagrożeń poza sam podsłuch. Taki podmiot może nie tylko czytać komunikację, ale również na nią wpływać. Może usuwać komunikaty, dopisywać własne, zmieniać istniejące albo w inny sposób zakłócać przebieg transmisji. To prowadzi do bardzo ważnej konsekwencji: sama poufność przestaje być wystarczającą odpowiedzią na problem bezpieczeństwa. Nawet jeśli przeciwnik nie potrafi odczytać wiadomości, może próbować wymusić określone skutki przez manipulację komunikacją. W tym miejscu pojawiają się już naturalnie problemy integralności i uwierzytelnienia, bo odbiorca musi nie tylko chronić treść przed odczytem, ale też wiedzieć, czy wiadomość nie została zmieniona i czy naprawdę pochodzi od legalnej strony. Model przeciwnika aktywnego lepiej odpowiada realiom sieci komputerowych niż obraz biernego podsłuchu. Pokazuje też, dlaczego bezpieczeństwo jest własnością całego protokołu i całego kanału użycia, a nie tylko pojedynczego algorytmu szyfrującego. W praktyce każdy system projektowany dla sieci publicznych powinien być oceniany co najmniej z myślą o tym silniejszym przeciwniku.

#slide 55
## layout
bullet
## slide title
Możliwości przeciwnika w kanale niezabezpieczonym
## bullets
- odczyt wiadomości
- usuwanie wiadomości
- wstawianie nowych wiadomości
- zmiana treści lub kolejności komunikatów
## teleprompter:
Gdy kanał nie jest zabezpieczony, trzeba bardzo konkretnie nazwać możliwości przeciwnika. Nie chodzi o ogólne stwierdzenie, że „coś może się stać”, lecz o katalog działań, które należy brać pod uwagę przy ocenie systemu. Pierwszą możliwością jest odczyt, czyli klasyczny podsłuch zagrażający poufności. Drugą jest usuwanie wiadomości, co może prowadzić do utraty informacji, zaburzenia przebiegu protokołu albo wywołania błędnych reakcji po stronie odbiorcy. Trzecią jest wstawianie nowych komunikatów, a więc aktywne wstrzykiwanie treści do kanału. Czwartą jest modyfikacja lub przestawianie komunikatów, przez co przeciwnik może zmieniać sens przekazu bez konieczności pełnego zrozumienia jego treści. Taki katalog zagrożeń pokazuje, że bezpieczeństwo komunikacji jest wielowymiarowe. Nie wystarczy zapytać, czy tekst został ukryty. Trzeba też pytać, czy przeciwnik może sterować przebiegiem rozmowy, czy może tworzyć pozory legalnego ruchu i czy może doprowadzić do błędnych decyzji po stronie odbiorcy. To właśnie dlatego odruchowe utożsamianie kryptografii wyłącznie z poufnością jest zbyt wąskie.

#slide 56
## layout
definition
## term
Atak ciphertext-only
## definition
Atak, w którym przeciwnik próbuje odzyskać tekst jawny lub klucz, dysponując wyłącznie szyfrogramami.
## teleprompter:
Atak ciphertext-only jest podstawową klasą ataków na systemy szyfrowania. Przeciwnik nie zna odpowiadających wiadomości jawnych, nie może wybierać wiadomości do zaszyfrowania, nie steruje także urządzeniem deszyfrującym. Ma jedynie szyfrogramy oraz wiedzę o systemie i o statystycznych własnościach języka lub danych. Mimo pozornej słabości ten model jest niezwykle ważny. Jeżeli system przegrywa już w takiej sytuacji, należy uznać go za całkowicie niebezpieczny. Właśnie na tym poziomie łamie się wiele prostych szyfrów klasycznych. Zachowanie częstotliwości liter, typowe wzorce językowe i przewidywalne struktury wiadomości dają przeciwnikowi wystarczająco dużo informacji, by rekonstruować tekst lub odtwarzać klucz. Atak ciphertext-only dobrze pokazuje, że bezpieczeństwo nie polega na samym fakcie zakodowania wiadomości. Liczy się to, czy szyfrogram naprawdę ukrywa strukturę danych. Dla prostych szyfrów jest to moment krytyczny, bo właśnie tutaj ujawnia się ich zasadnicza słabość.

#slide 57
## layout
definition
## term
Atak known-plaintext
## definition
Atak, w którym przeciwnik dysponuje pewną liczbą par: wiadomość jawna i odpowiadający jej szyfrogram.
## teleprompter:
Atak ze znanym tekstem jawnym zakłada, że przeciwnik zna nie tylko szyfrogramy, ale także pewną liczbę odpowiadających im wiadomości jawnych. Taka sytuacja jest znacznie bardziej realistyczna, niż mogłoby się wydawać. W praktyce wiele komunikatów ma części przewidywalne, powtarzalne lub później ujawniane publicznie. Mogą to być formularze, nagłówki, standardowe komunikaty organizacyjne albo wiadomości, których treść po pewnym czasie staje się jawna. Tego rodzaju wiedza pozwala przeciwnikowi porównywać wejścia i wyjścia systemu oraz wyciągać wnioski o kluczu albo strukturze transformacji. W literaturze podkreśla się, że system uznawany za bezpieczny nie powinien załamywać się już po ujawnieniu części dawnych wiadomości. To bardzo ważna intuicja praktyczna. Gdyby każde późniejsze ujawnienie fragmentu korespondencji kompromitowało cały mechanizm, użytkownicy musieliby traktować wszystkie historyczne wiadomości jak sekrety wieczne, co w wielu zastosowaniach jest niewykonalne. Atak known-plaintext pokazuje więc, że prawdziwa odporność systemu wymaga więcej niż ochrony przed samym biernym podsłuchem.

#slide 58
## layout
definition
## term
Atak chosen-plaintext
## definition
Atak, w którym przeciwnik sam wybiera wiadomości jawne i otrzymuje odpowiadające im szyfrogramy.
## teleprompter:
Atak z wybranym tekstem jawnym jest jeszcze silniejszym modelem kryptoanalizy. Przeciwnik nie ogranicza się już do obserwacji gotowych przykładów, lecz może sam decydować, jakie wiadomości zostaną zaszyfrowane, a następnie analizować uzyskane szyfrogramy. Taki model pozwala bardzo precyzyjnie badać reakcję systemu na dobrane wejścia. Dzięki temu łatwiej wykryć reguły, zależności i słabości konstrukcyjne niż w ataku opartym wyłącznie na gotowym materiale przechwyconym z kanału. W praktyce osiągnięcie idealnego ataku chosen-plaintext bywa trudne, ale istnieją sytuacje, w których można go przybliżyć. Wystarczy, że przeciwnik potrafi skłonić legalną stronę lub system do zaszyfrowania wybranych treści. Dla prostych szyfrów klasycznych taki model jest zwykle druzgocący, ponieważ ich struktura jest zbyt regularna. W szerszym sensie ten typ ataku uczy ważnej zasady: bezpieczeństwo systemu trzeba oceniać nie tylko wobec danych zastanych, lecz także wobec sytuacji, w której przeciwnik umie aktywnie dobierać wejścia i eksperymentować z zachowaniem schematu.

#slide 59
## layout
bullet
## slide title
Co zakłada się o wiedzy przeciwnika
## bullets
- zna ogólny system szyfrowania
- zna typ danych lub język komunikacji
- może wykorzystywać statystykę i wzorce wiadomości
- nie zna konkretnego tajnego klucza
## teleprompter:
W dojrzałym modelu kryptologicznym nie traktuje się przeciwnika jak kogoś działającego w ciemno. Zakłada się raczej, że zna ogólny system, może badać urządzenia, analizować standardy i rozumie, jakiego rodzaju dane są przesyłane. Może także wykorzystywać wiedzę statystyczną o języku, o częstotliwości symboli i o przewidywalnych fragmentach wiadomości. To wszystko jest założeniem realistycznym i zarazem bardzo użytecznym metodologicznie. Dzięki niemu bezpieczeństwo nie jest oceniane na podstawie tego, że przeciwnik nic nie rozumie, ale na podstawie tego, że mimo szerokiej wiedzy nadal nie potrafi odtworzyć tajnej informacji. Jedynym elementem, którego nie powinien znać, jest konkretny klucz używany w danym przypadku. Ta zasada wiąże się bezpośrednio z przekonaniem, że tajność całego schematu nie może być fundamentem ochrony. W kontekście prostych szyfrów klasycznych takie założenie jest szczególnie oświecające, bo pokazuje, dlaczego wiele historycznych metod szybko ustępuje przed analizą statystyczną i systematycznym porównywaniem wzorców.

#slide 60
## layout
title
## slide title
Gdzie zaczynają się proste szyfry
## subtitle
Po ustaleniu modelu można przejść do podstawienia i przestawienia
## teleprompter:
Podstawowy model komunikacji jest już gotowy. Zostały uporządkowane role nadawcy, odbiorcy i przeciwnika, pojęcie schematu szyfrowania, znaczenie klucza, warunek poprawności, różnica między bezpieczeństwem bezwarunkowym a obliczeniowym, problem dystrybucji kluczy oraz podstawowe klasy ataków. Dopiero na takim tle naprawdę widać sens prostych szyfrów klasycznych. Nie są one jedynie historyczną ciekawostką ani szkolnym ćwiczeniem. Są laboratorium podstawowych idei kryptologii. Na ich przykładzie można zobaczyć, czym jest podstawienie, czym jest przestawienie, jak działa przestrzeń kluczy, jakie znaczenie ma statystyka języka i dlaczego sam fakt zaszyfrowania wiadomości nie gwarantuje bezpieczeństwa. W następnym bloku pojawią się więc najprostsze konstrukcje klasyczne: szyfry podstawieniowe i szyfry przestawieniowe. To właśnie one najczyściej pokazują zarówno intuicję szyfrowania, jak i granice tego, co da się osiągnąć bez bardziej złożonych metod. Od tego miejsca ciężar wykładu przesunie się z samego modelu na konkretne rodziny szyfrów i ich właściwości.

#slide 61
## layout
bullet
## slide title
Dwie podstawowe rodziny prostych szyfrów
## bullets
- szyfry podstawieniowe zastępują symbole innymi symbolami
- szyfry przestawieniowe zachowują symbole, ale zmieniają ich położenie
- obie rodziny należą do szyfrów blokowych w klasycznym ujęciu
## teleprompter:
W klasycznym wprowadzeniu do kryptografii bardzo szybko pojawia się podstawowy podział prostych szyfrów na dwie rodziny. Pierwsza to szyfry podstawieniowe. Ich działanie polega na zastępowaniu jednych symboli innymi symbolami albo grup symboli innymi grupami. Zmienia się więc to, co widzimy jako znaki szyfrogramu. Druga rodzina to szyfry przestawieniowe. W nich nie dochodzi do zastępowania symboli innymi wartościami, lecz do zmiany ich położenia. Materiał znakowy pozostaje ten sam, ale zmienia się jego porządek. To rozróżnienie wydaje się proste, ale jest niezwykle ważne, ponieważ porządkuje praktycznie całą historię klasycznej kryptografii. W podręcznikowym ujęciu obie rodziny są traktowane jako klasy szyfrów blokowych, czyli takich, które operują na ustalonej liczbie symboli. Dzięki temu można bardzo precyzyjnie opisać, co robi szyfr, jak wygląda jego klucz i jakiego rodzaju ślady statystyczne pozostają w szyfrogramie. Ten podział jest też znakomitym punktem wyjścia do zrozumienia nowoczesnych konstrukcji. Współczesne szyfry blokowe nie są prostymi historycznymi podstawieniami ani prostymi przestawieniami, ale łączą obie idee w bardziej złożonych rundach. Dlatego nawet bardzo dawne szyfry nie są dziś tylko ciekawostką. One pokazują dwa elementarne typy transformacji, z których później buduje się dużo silniejsze systemy.

#slide 62
## layout
definition
## term
Szyfr podstawieniowy
## definition
Szyfr blokowy, który zastępuje symbole lub grupy symboli tekstu jawnego innymi symbolami lub grupami symboli zgodnie z regułą wyznaczoną przez klucz.
## teleprompter:
Szyfr podstawieniowy polega na zamianie jednego symbolu na inny symbol albo jednej grupy znaków na inną grupę. Istotą tej rodziny jest więc sama operacja podstawienia. Nie zmieniamy miejsca znaku, lecz jego reprezentację w szyfrogramie. W najprostszej postaci jedna litera alfabetu tekstu jawnego odpowiada jednej literze alfabetu szyfrogramu, ale ogólna idea jest szersza. Można podstawiać także bloki znaków, można używać różnych permutacji alfabetu, a w bardziej rozwiniętych odmianach można nawet sprawić, że ten sam symbol tekstu jawnego nie zawsze przechodzi w ten sam symbol szyfrogramu. Z dydaktycznego punktu widzenia ta rodzina jest szczególnie ważna, ponieważ pozwala bardzo szybko uchwycić relację między kluczem a strukturą wiadomości. Szyfr podstawieniowy zwykle zachowuje wiele cech statystycznych języka, zwłaszcza gdy jest prosty i jednoalfabetyczny. To dlatego daje się często analizować metodami częstościowymi. Jednocześnie właśnie na przykładzie podstawień łatwo zrozumieć, co znaczy, że klucz wskazuje jedną z wielu dopuszczalnych transformacji. Ta rodzina pokazuje też ograniczenie samej wielkości przestrzeni kluczy. Nawet jeśli liczba możliwych podstawień wydaje się ogromna, to bezpieczeństwo może pozostać słabe, jeśli szyfrogram zachowuje zbyt dużo struktury tekstu jawnego.

#slide 63
## layout
definition
## term
Szyfr przestawieniowy
## definition
Szyfr blokowy, który zmienia pozycje symboli w bloku tekstu jawnego bez zmiany samych symboli.
## teleprompter:
Szyfr przestawieniowy działa inaczej niż szyfr podstawieniowy. Nie zastępuje znaków innymi znakami, lecz przestawia ich kolejność w obrębie bloku. Jeżeli tekst jawny zawiera określony zestaw symboli, to po zaszyfrowaniu tym typem szyfru w szyfrogramie nadal znajdują się te same symbole, ale w innym porządku. To z pozoru niewielka różnica, lecz ma bardzo poważne konsekwencje analityczne. Ponieważ przestawienie nie zmienia repertuaru symboli, wiele statystycznych własności tekstu pozostaje zachowanych bardziej bezpośrednio niż przy podstawieniu. Z tego powodu samodzielne szyfry przestawieniowe nie oferują zwykle wysokiego poziomu bezpieczeństwa. Mimo to ich znaczenie historyczne i koncepcyjne jest duże. Pozwalają uchwycić ideę rozpraszania struktury wiadomości w przestrzeni szyfrogramu. W późniejszej terminologii Shannona i podręcznikowych omówieniach nowoczesnych szyfrów to właśnie przestawienia prowadzą do intuicji dyfuzji. Kiedy elementy wiadomości zostają przemieszane, lokalne regularności tekstu jawnego przestają być skupione w jednym miejscu. Sama ta operacja nie wystarcza do budowy mocnego systemu, ale połączenie jej z podstawieniem staje się jednym z najważniejszych motywów w historii projektowania szyfrów.

#slide 64
## layout
bullet
## slide title
Co zachowuje, a co zmienia szyfr podstawieniowy
## bullets
- zmienia symbole tekstu jawnego
- nie musi zmieniać długości wiadomości
- w prostych odmianach zachowuje rozkład częstości symboli
## teleprompter:
Aby dobrze zrozumieć mocne i słabe strony szyfru podstawieniowego, trzeba oddzielić kilka poziomów opisu. Po pierwsze, taki szyfr zmienia samą postać symboli. Znak, który w tekście jawnym był literą A, może po szyfrowaniu stać się inną literą, liczbą albo całym blokiem znaków, zależnie od konstrukcji. Po drugie, bardzo wiele prostych podstawień nie zmienia długości wiadomości. Każdej literze odpowiada jedna litera, więc szyfrogram ma tę samą długość co tekst jawny. Po trzecie, i to jest najważniejsze z punktu widzenia kryptoanalizy, proste szyfry jednoalfabetyczne zachowują rozkład częstości symboli. Jeżeli w języku naturalnym pewne litery występują częściej niż inne, to po podstawieniu ich względne częstości nadal są widoczne, tylko pod innymi etykietami. To właśnie dlatego przeciwnik może próbować rozpoznawać, który znak szyfrogramu odpowiada najczęstszej literze języka, następnie literom nieco rzadszym, a potem korzystać z powtarzających się wzorców, bigramów i kontekstu słów. Stąd bierze się jedna z najważniejszych lekcji z klasycznych szyfrów: ukrycie znaków nie oznacza jeszcze ukrycia struktury. Jeżeli struktura języka pozostaje w dużej mierze zachowana, szyfrogram nadal dostarcza przeciwnikowi bardzo dużo informacji.

#slide 65
## layout
bullet
## slide title
Co zachowuje, a co zmienia szyfr przestawieniowy
## bullets
- zachowuje zestaw symboli występujących w wiadomości
- zmienia ich położenie w bloku
- pozostawia widoczne globalne częstości symboli
## teleprompter:
W szyfrze przestawieniowym obraz sytuacji jest niemal odwrotny niż w szyfrze podstawieniowym. Symbole pozostają te same, więc jeżeli w tekście jawnym pewna litera pojawiała się bardzo często, to po zaszyfrowaniu nadal będzie występowała równie często. Zmienia się jednak porządek, w jakim te symbole pojawiają się w ciągu. Taka operacja może skutecznie ukryć czytelne fragmenty słów i lokalne zależności, ale nie usuwa wielu cech statystycznych języka. Globalny rozkład znaków pozostaje bez zmian. Oznacza to, że przeciwnik nadal widzi, jak często występują poszczególne litery, choć trudniej mu od razu wskazać ich położenie w sensownych słowach. To pokazuje, dlaczego same przestawienia zwykle nie dają wysokiej odporności. One raczej przemieszczają informację o strukturze niż ją ukrywają. Z drugiej strony ta właśnie własność sprawia, że przestawienia są użyteczne jako składnik bardziej złożonego szyfru. Jeżeli połączyć zmianę wartości symboli z ich rozrzuceniem po całym bloku, wtedy przeciwnik traci jednocześnie prosty dostęp do treści i do lokalnych regularności. To już prowadzi do intuicji produktu z podstawienia i przestawienia, który stanie się ważny pod koniec tego bloku wykładu.

#slide 66
## layout
definition
## term
Szyfr przesuwający
## definition
Prosty szyfr podstawieniowy, w którym każda litera alfabetu jest zastępowana literą przesuniętą o stałą liczbę pozycji.
## teleprompter:
Szyfr przesuwający jest najprostszym i najbardziej klasycznym przykładem szyfru podstawieniowego. Działa według jednej stałej reguły: każdą literę zastępuje się literą przesuniętą o tę samą liczbę pozycji w alfabecie. Jeżeli przesunięcie wynosi trzy, to A przechodzi w D, B w E, C w F i tak dalej, z zawijaniem na końcu alfabetu. Ta konstrukcja jest cenna nie dlatego, że daje silne bezpieczeństwo, lecz dlatego, że w bardzo przejrzysty sposób pokazuje rolę klucza, przestrzeni kluczy, odwracalności i ograniczeń prostego podstawienia. Kluczem jest tu liczba przesunięcia. Deszyfrowanie polega po prostu na przesunięciu w przeciwną stronę. Dzięki temu można łatwo zobaczyć, jak działa para transformacji szyfrującej i deszyfrującej. Równocześnie natychmiast widać słabość systemu. Przestrzeń kluczy jest mała, bo liczba sensownych przesunięć jest ograniczona przez liczebność alfabetu. Dodatkowo szyfr zachowuje rozkład częstości liter, więc daje się atakować nie tylko pełnym przeszukaniem kluczy, ale też analizą statystyczną. Mimo tej słabości szyfr przesuwający pozostaje doskonałym punktem startowym dla całej kryptologii klasycznej, bo w jednej prostej konstrukcji skupia niemal wszystkie pojęcia elementarne.

#slide 67
## layout
bullet
## slide title
Szyfr Cezara jako przypadek szyfru przesuwającego
## bullets
- alfabet jest przesuwany o stałą wartość
- klasyczny przykład używa przesunięcia o 3
- deszyfrowanie cofa przesunięcie o tę samą wartość
## teleprompter:
Szyfr Cezara jest szczególnym przypadkiem szyfru przesuwającego i zarazem jednym z najbardziej rozpoznawalnych szyfrów historycznych. W jego najbardziej znanej wersji każda litera alfabetu zostaje przesunięta o trzy pozycje. Oznacza to, że tekst jawny zapisany literami alfabetu łacińskiego otrzymuje nową reprezentację, lecz zasada pozostaje jednakowa dla całej wiadomości. Właśnie ta stałość reguły sprawia, że przykład jest tak przejrzysty. Łatwo objaśnić szyfrowanie, łatwo objaśnić deszyfrowanie i łatwo pokazać, że bezpieczeństwo jest niewielkie. Przeciwnik może po prostu sprawdzić wszystkie możliwe przesunięcia. Nawet bez tego może rozpoznawać wzorce częstości liter. Gdy w szyfrogramie jakaś litera występuje wyjątkowo często, można przypuszczać, że odpowiada częstej literze języka. Szyfr Cezara pokazuje więc różnicę między odwracalnością a rzeczywistą odpornością na atak. Jest poprawny formalnie, prosty implementacyjnie i dobry do ćwiczeń, ale jako metoda ochrony informacji ma znaczenie wyłącznie historyczne i dydaktyczne. To właśnie dlatego jego rola w kursie kryptologii jest tak duża: na bardzo prostym modelu można zobaczyć zarówno sens szyfrowania, jak i natychmiastowe granice naiwnej konstrukcji.

#slide 68
## layout
bullet
## slide title
Opis algebraiczny szyfru przesuwającego
## bullets
- alfabet numeruje się zwykle od 0 do 25
- szyfrowanie można zapisać jako dodawanie modulo długość alfabetu
- deszyfrowanie jest odejmowaniem modulo długość alfabetu
## teleprompter:
Jedną z zalet szyfru przesuwającego jest to, że bardzo łatwo przejść od opisu słownego do opisu algebraicznego. Jeśli alfabet ma 26 liter, można przypisać im numery od 0 do 25. Wtedy szyfrowanie staje się prostą operacją arytmetyczną: do numeru litery dodaje się wartość klucza i wynik redukuje modulo 26. Deszyfrowanie wykonuje odwrotną operację, czyli odejmuje tę samą wartość, również modulo 26. Taki zapis jest ważny nie dlatego, że sam szyfr zyskuje przez to na bezpieczeństwie, lecz dlatego, że pokazuje sposób formalizacji kryptografii. Operacje na symbolach językowych zamieniają się w operacje na elementach pewnego zbioru liczbowego. To jest pierwszy krok do myślenia o szyfrach jako o funkcjach określonych matematycznie. Równocześnie w tym algebraicznym opisie nadal bardzo wyraźnie widać ograniczenia systemu. Dodawanie stałej do wszystkich liter zachowuje wszystkie relacje częstościowe, a przestrzeń możliwych kluczy pozostaje mała. Dzięki temu przykład ma dużą wartość porządkującą. Łączy intuicję językową, opis funkcjonalny i prostą matematykę, co będzie bardzo przydatne przy przejściu do szyfru afinicznego i dalej do bardziej ogólnych permutacji alfabetu.

#slide 69
## layout
definition
## term
Szyfr afiniczny
## definition
Szyfr podstawieniowy nad alfabetem numerowanym liczbowo, w którym szyfrowanie ma postać przekształcenia liniowego modulo długość alfabetu, przy odpowiednim doborze współczynnika odwracalnego.
## teleprompter:
Szyfr afiniczny rozszerza ideę prostego przesunięcia. Zamiast tylko dodawać stałą wartość do numeru litery, stosuje się przekształcenie liniowe modulo długość alfabetu. W praktyce oznacza to, że numer symbolu jest najpierw mnożony przez wybrany współczynnik, a potem dodawana jest druga stała. Żeby deszyfrowanie było możliwe, współczynnik mnożący musi mieć odwrotność modulo liczebność alfabetu. W przeciwnym razie różne litery mogłyby przechodzić w ten sam symbol szyfrogramu i transformacja nie byłaby odwracalna. Szyfr afiniczny jest bardzo pouczający, bo pokazuje dwa ważne fakty. Po pierwsze, nawet nieco bogatsza matematycznie postać transformacji nadal może należeć do rodziny prostych podstawień jednoalfabetycznych. Po drugie, formalnie elegantsza postać nie usuwa głównej słabości tej rodziny. Rozkład częstości liter wciąż zostaje zachowany pod permutacją symboli, więc szyfr pozostaje podatny na analizę statystyczną. W ten sposób szyfr afiniczny staje się pomostem między bardzo prostym przykładem Cezara a ogólnym pojęciem monoalfabetycznej permutacji alfabetu. Widać już więcej matematyki, ale nadal bardzo wyraźnie widać również granice bezpieczeństwa.

#slide 70
## layout
bullet
## slide title
Warunek odwracalności w szyfrze afinicznym
## bullets
- współczynnik mnożący musi mieć odwrotność modulo długość alfabetu
- nie każdy wybór parametru daje poprawny szyfr
- poprawność zależy od tego, czy transformacja jest permutacją alfabetu
## teleprompter:
W szyfrze afinicznym nie wystarczy wybrać dowolnych liczb i uznać, że otrzymano legalny szyfr. Kluczowy jest warunek odwracalności. Współczynnik użyty do mnożenia musi być taki, aby posiadał odwrotność modulo liczebność alfabetu. Dla alfabetu 26-literowego oznacza to, że ten współczynnik musi być względnie pierwszy z 26. Jeżeli ten warunek nie jest spełniony, to różne symbole tekstu jawnego mogą zostać zlane w ten sam symbol szyfrogramu, a wtedy legalny odbiorca nie będzie w stanie jednoznacznie odtworzyć wiadomości. To bardzo dobry przykład pokazujący, że poprawność schematu nie jest automatyczna. Trzeba zbudować transformację, która rzeczywiście jest permutacją alfabetu, a nie dowolnym przekształceniem liczbowym. Z punktu widzenia dydaktycznego ten warunek jest szczególnie cenny, bo jasno łączy kryptografię z pojęciem funkcji odwracalnej. Jednocześnie przypomina, że zwiększenie liczby parametrów nie musi oznaczać skoku bezpieczeństwa. Można mieć bardziej wyrafinowany zapis algebraiczny, a nadal pozostawać w klasie szyfrów, które ujawniają zbyt wiele struktury języka.

#slide 71
## layout
definition
## term
Szyfr monoalfabetyczny
## definition
Szyfr podstawieniowy, w którym jedna stała permutacja alfabetu jest używana do szyfrowania całej wiadomości.
## teleprompter:
Szyfr monoalfabetyczny uogólnia wcześniejsze przykłady przesunięcia i szyfru afinicznego. Nie ogranicza się już do specjalnej postaci matematycznej, lecz pozwala wybrać dowolną permutację alfabetu i stosować ją niezmiennie w całej wiadomości. Każda litera tekstu jawnego ma więc jeden stały odpowiednik w szyfrogramie. Jeżeli litera pojawi się w wiadomości wiele razy, za każdym razem zostanie zastąpiona tym samym symbolem. To czyni system prostym w opisie i implementacji, ale jednocześnie odsłania główną słabość. Stałość odwzorowania powoduje, że statystyka języka w dużej mierze przechodzi do szyfrogramu. Najczęstsza litera tekstu jawnego pozostaje najczęstszą literą pod inną etykietą, częste pary liter nadal manifestują się w szyfrogramie jako częste pary innych znaków, a układ słów i końcówek językowych pozostawia rozpoznawalne ślady. W rezultacie nawet ogromna liczba możliwych permutacji alfabetu nie daje praktycznie silnej ochrony, jeśli przeciwnik ma do dyspozycji umiarkowaną ilość szyfrogramu. To jeden z najważniejszych wniosków całej klasycznej kryptologii: wielka przestrzeń kluczy nie wystarcza, jeśli konstrukcja zachowuje zbyt dużo informacji statystycznej o tekście.

#slide 72
## layout
bullet
## slide title
Dlaczego wielka liczba kluczy nie ratuje prostego podstawienia
## bullets
- liczba możliwych permutacji alfabetu jest bardzo duża
- mimo to rozkład częstości liter pozostaje widoczny
- umiarkowana ilość szyfrogramu może wystarczyć do odtworzenia klucza
## teleprompter:
Na pierwszy rzut oka szyfr monoalfabetyczny może wydawać się znacznie silniejszy niż szyfr Cezara. Rzeczywiście liczba wszystkich permutacji alfabetu jest ogromna. Gdy alfabet ma 26 liter, liczba możliwych kluczy wynosi 26!, czyli bardzo dużo. Taki wynik może tworzyć wrażenie bezpieczeństwa, ale to wrażenie jest mylące. Powód jest fundamentalny. Przeciwnik nie musi traktować wszystkich kluczy jednakowo, jeśli szyfrogram zachowuje bardzo dużo struktury języka. W prostym podstawieniu najczęstsze litery pozostają najczęstsze, a typowe wzorce występowania znaków nie znikają, tylko zmieniają etykiety. To oznacza, że analiza częstości i analiza kontekstu dają przeciwnikowi ogromne skróty względem pełnego przeszukiwania przestrzeni kluczy. W praktyce umiarkowana ilość szyfrogramu może wystarczyć do systematycznego odtwarzania podstawienia. Ta obserwacja ma znaczenie wykraczające daleko poza historię. Pokazuje, że bezpieczeństwo nie może być oceniane wyłącznie przez rozmiar przestrzeni kluczy. Trzeba badać, czy konstrukcja nie ujawnia dodatkowej regularności, którą da się wykorzystać do ataku szybszego niż brutalna siła.

#slide 73
## layout
definition
## term
Analiza częstości
## definition
Metoda kryptoanalizy wykorzystująca fakt, że w językach naturalnych symbole i ich układy nie występują z jednakową częstością.
## teleprompter:
Analiza częstości jest jedną z najbardziej klasycznych metod kryptoanalizy i wynika bezpośrednio z własności języka naturalnego. W zwykłym tekście litery nie pojawiają się z jednakowym prawdopodobieństwem. Niektóre występują bardzo często, inne rzadziej, a jeszcze inne sporadycznie. Podobnie jest z parami liter, końcówkami wyrazów i innymi lokalnymi strukturami. Jeżeli szyfr zachowuje te zależności, choćby pod zmienionymi etykietami symboli, przeciwnik może zacząć budować hipotezy dotyczące odwzorowania między tekstem jawnym a szyfrogramem. To nie jest magia ani intuicja przypadkowa. To systematyczne wykorzystanie nierównomierności rozkładu językowego. W prostym szyfrze monoalfabetycznym znak najczęstszy w szyfrogramie jest naturalnym kandydatem na odpowiednik jednej z najczęstszych liter języka. Kolejne obserwacje dotyczą częstych par, typowych krótkich słów i zgodności z kontekstem. Analiza częstości pokazuje więc, że język sam w sobie bywa źródłem podatności. Jeżeli szyfr nie rozprasza skutecznie regularności tekstu jawnego, to przeciwnik otrzymuje dane statystyczne wystarczające do postępu w łamaniu. To właśnie ten rodzaj podatności odróżnia proste szyfry szkoleniowe od konstrukcji projektowanych do realnej ochrony.

#slide 74
## layout
bullet
## slide title
Jak przebiega atak na prosty szyfr monoalfabetyczny
## bullets
- zliczenie częstości znaków w szyfrogramie
- porównanie ich z częstościami języka
- sprawdzanie hipotez przez fragmenty słów i kontekst
## teleprompter:
Atak na prosty szyfr monoalfabetyczny zwykle nie zaczyna się od zgadywania całego klucza naraz. Zaczyna się od statystyki. Przeciwnik zlicza, które znaki w szyfrogramie występują najczęściej, które pojawiają się rzadko, jakie pary i trójki symboli wracają wielokrotnie oraz czy występują powtarzalne długości słów lub fragmentów. Następnie porównuje te obserwacje z właściwościami danego języka. To porównanie pozwala wysunąć pierwsze hipotezy, na przykład że określony znak szyfrogramu odpowiada bardzo częstej literze tekstu jawnego. Kolejny etap polega na sprawdzaniu spójności tych hipotez z resztą materiału. Jeżeli przypisanie daje sensowne krótkie słowa, typowe końcówki lub zgodne układy znaków, można rozwijać częściowe rozwiązanie. Jeżeli prowadzi do sprzeczności, hipotezę odrzuca się i szuka innej. W praktyce jest to połączenie obserwacji statystycznej i językowej rekonstrukcji. Dla prostego podstawienia ta metoda bywa zaskakująco skuteczna. Właśnie dlatego wielka przestrzeń kluczy nie chroni takiego szyfru przed rzeczywistym przeciwnikiem mającym do dyspozycji szyfrogram o dostatecznej długości.

#slide 75
## layout
definition
## term
Szyfr homofoniczny
## definition
Szyfr podstawieniowy, w którym jednemu symbolowi tekstu jawnego może odpowiadać więcej niż jeden możliwy symbol lub blok szyfrogramu, wybierany z rozłącznego zbioru przypisanego temu symbolowi.
## teleprompter:
Szyfr homofoniczny powstał jako próba osłabienia głównej słabości prostego podstawienia, czyli zachowywania nierównomiernych częstości znaków. Zamiast przypisywać każdej literze tylko jeden odpowiednik, przypisuje się jej cały zbiór możliwych reprezentacji szyfrogramowych. Przy szyfrowaniu wybiera się jedną z nich, zwykle w sposób losowy lub zgodny z ustaloną procedurą. Ważne jest to, że zbiory przypisane różnym symbolom tekstu jawnego są rozłączne, aby deszyfrowanie było możliwe. Ideą tej konstrukcji jest spłaszczenie statystyki szyfrogramu. Jeżeli częsta litera ma więcej możliwych reprezentacji niż litera rzadka, to częstości poszczególnych symboli szyfrogramu mogą stać się bardziej wyrównane. W ten sposób przeciwnik traci część najprostszych wskazówek statystycznych. Nie jest to jednak rozwiązanie idealne. Taki szyfr komplikuje użycie, może prowadzić do zwiększenia długości szyfrogramu i nadal nie gwarantuje bezpieczeństwa porównywalnego z nowoczesnymi metodami. Mimo to jest bardzo ważny historycznie i pojęciowo, bo pokazuje świadomą próbę walki z analizą częstości przez zmianę samego sposobu reprezentacji symboli. To już nie jest tylko prosty szyfr do ukrycia treści, lecz świadoma odpowiedź na konkretną technikę kryptoanalizy.

#slide 76
## layout
bullet
## slide title
Po co wprowadzano szyfry homofoniczne
## bullets
- aby bardziej wyrównać częstości symboli w szyfrogramie
- aby utrudnić bezpośrednią analizę częstości
- kosztem większej złożoności i często większej długości danych
## teleprompter:
Motywacja stojąca za szyfrem homofonicznym jest bardzo jasna. Proste podstawienie przegrywa z analizą częstości, bo najczęstsze litery języka pozostają najczęstsze także po zaszyfrowaniu, tylko pod innymi etykietami. Jeżeli więc chcemy utrudnić taki atak, trzeba sprawić, by częsta litera nie zawsze prowadziła do jednego i tego samego symbolu szyfrogramu. Właśnie temu służy homofonia. Jednemu symbolowi tekstu jawnego przydziela się wiele możliwych reprezentacji, a ich wybór rozprasza statystykę. Dzięki temu szyfrogram może wyglądać bardziej równomiernie i mniej zdradzać najprostsze cechy języka. To jednak nie jest darmowe wzmocnienie. Konstrukcja staje się bardziej złożona organizacyjnie, deszyfrowanie nie jest tak wygodne jak w najprostszym podstawieniu, a długość danych może rosnąć. Z perspektywy historii kryptologii najważniejsze jest jednak coś jeszcze. Szyfr homofoniczny pokazuje, że kryptografia rozwijała się jako dialog między konstrukcją a atakiem. Najpierw zauważono słabość prostego podstawienia, potem pojawiła się próba jej złagodzenia przez bardziej elastyczną reprezentację symboli. Ten ruch od prostoty do większej świadomości statystycznej bardzo dobrze przygotowuje grunt pod szyfry polialfabetyczne.

#slide 77
## layout
definition
## term
Szyfr polialfabetyczny
## definition
Szyfr podstawieniowy, w którym do kolejnych pozycji wiadomości stosuje się więcej niż jedną permutację alfabetu.
## teleprompter:
Szyfr polialfabetyczny stanowi kolejny krok w rozwoju klasycznych podstawień. Zamiast używać jednej stałej permutacji alfabetu dla całej wiadomości, stosuje się kilka różnych permutacji, zależnie od pozycji symbolu w tekście. Dzięki temu ten sam znak tekstu jawnego nie musi być zawsze szyfrowany tak samo. Jeśli litera pojawi się w różnych miejscach wiadomości, może otrzymać różne reprezentacje w szyfrogramie. To osłabia bezpośrednią skuteczność analizy częstości, bo zależność między literą a jej obrazem nie jest już stała w całym tekście. Taki szyfr nie usuwa całkowicie struktury językowej, ale rozbija ją na kilka warstw odpowiadających różnym pozycjom lub fazom użycia klucza. Z punktu widzenia teorii jest to bardzo ważna zmiana. Pokazuje, że bezpieczeństwo można wzmacniać nie tylko przez wybór bardziej złożonej pojedynczej permutacji, lecz także przez zmienność samej transformacji szyfrującej w czasie. Jednocześnie nadal pozostajemy w świecie klasycznych szyfrów, a więc nadal można mówić o ograniczeniach, powtarzalności okresu i metodach kryptoanalizy wykorzystujących tę regularność. To właśnie dlatego polialfabetyczność jest krokiem naprzód, ale nie końcem historii.

#slide 78
## layout
definition
## term
Szyfr Vigenère’a
## definition
Klasyczny szyfr polialfabetyczny, w którym kolejne pozycje tekstu są szyfrowane według cyklicznie powtarzanego zestawu przesunięć alfabetu.
## teleprompter:
Szyfr Vigenère’a jest najbardziej znanym przykładem szyfru polialfabetycznego. W jego klasycznej postaci wybiera się słowo-klucz lub, bardziej abstrakcyjnie, ciąg przesunięć alfabetu. Następnie dla kolejnych liter wiadomości stosuje się te przesunięcia cyklicznie, wracając do początku sekwencji po osiągnięciu jej końca. W efekcie ta sama litera tekstu jawnego może w różnych miejscach dawać różne litery szyfrogramu. To znacząco utrudnia prostą analizę częstości w porównaniu z szyfrem monoalfabetycznym. Zamiast jednego globalnego rozkładu podstawień powstaje kilka przeplatających się rozkładów zależnych od pozycji modulo długość klucza. Taki zabieg był przez długi czas uznawany za bardzo skuteczne wzmocnienie szyfru podstawieniowego. Z dzisiejszej perspektywy widać jednak, że kluczową słabością pozostaje okresowość. Jeżeli sekwencja przesunięć powtarza się regularnie, przeciwnik może próbować odtworzyć długość okresu, a potem rozdzielić szyfrogram na klasy pozycji szyfrowane tą samą permutacją. Wtedy problem znowu redukuje się do prostszych analiz. Mimo tej słabości szyfr Vigenère’a jest niezwykle ważny, bo bardzo jasno pokazuje ideę zmiennej transformacji szyfrującej i przygotowuje intuicję pod nowoczesne szyfry strumieniowe.

#slide 79
## layout
bullet
## slide title
Co wzmacnia szyfr Vigenère’a względem prostego podstawienia
## bullets
- ta sama litera może dawać różne litery szyfrogramu
- pojedynczy rozkład częstości nie opisuje całej wiadomości
- analiza wymaga najpierw uchwycenia okresu klucza
## teleprompter:
Najważniejszą przewagą szyfru Vigenère’a nad prostym szyfrem monoalfabetycznym jest zerwanie z zasadą jednego stałego odwzorowania dla całej wiadomości. To oznacza, że litera tekstu jawnego nie ma już jednego niezmiennego obrazu w szyfrogramie. Jej reprezentacja zależy od pozycji i od tego, która część cyklicznego klucza jest aktualnie używana. W rezultacie przeciwnik nie może od razu przyłożyć jednego globalnego modelu częstości do całego szyfrogramu. Najpierw musi zorientować się, czy szyfr ma charakter okresowy, a jeśli tak, to jaka jest długość tego okresu. Dopiero potem może rozbić materiał na warstwy odpowiadające poszczególnym pozycjom klucza i analizować je osobno jak prostsze podstawienia. To pokazuje, że Vigenère rzeczywiście stanowi postęp. Zmusza atakującego do wykonania dodatkowego kroku analitycznego. Równocześnie ten sam opis ujawnia ograniczenie systemu. Jeżeli okres istnieje i jest wykrywalny, to większa złożoność nie jest jeszcze równoznaczna z trwałym bezpieczeństwem. To raczej przesunięcie problemu na wyższy poziom, ale nadal w zasięgu systematycznej kryptoanalizy.

#slide 80
## layout
bullet
## slide title
Główna słabość szyfru Vigenère’a
## bullets
- klucz ma skończony okres i powtarza się
- po ustaleniu okresu szyfrogram można podzielić na klasy pozycji
- każda klasa zachowuje się jak prostszy szyfr podstawieniowy
## teleprompter:
Najważniejsza słabość szyfru Vigenère’a wynika nie z samej idei wielu alfabetów, lecz z ich okresowego użycia. Jeżeli ciąg przesunięć powtarza się po pewnej liczbie pozycji, to w długim szyfrogramie zaczynają pojawiać się regularności odpowiadające temu okresowi. Kiedy przeciwnik zdoła oszacować długość klucza, może podzielić szyfrogram na kilka strumieni: pierwszy zawiera symbole zaszyfrowane pierwszym przesunięciem, drugi drugim, i tak dalej. Wówczas każdy taki strumień staje się materiałem do analizy podobnej do tej, którą stosuje się wobec prostego podstawienia lub szyfru przesuwającego. Innymi słowy, złożoność systemu rozpada się na kilka prostszych problemów. To bardzo ważna lekcja. Sama zmienność transformacji szyfrującej nie wystarcza, jeśli ta zmienność ma prostą i wykrywalną strukturę okresową. Bezpieczeństwo wymaga nie tylko wielu transformacji, ale także odpowiednio trudnego do przewidzenia sposobu ich używania. Właśnie w tym miejscu historia klasycznych szyfrów zaczyna stykać się z nowoczesnym myśleniem o strumieniach klucza i generatorach pseudolosowych.

#slide 81
## layout
definition
## term
Szyfr przestawieniowy kolumnowy
## definition
Klasyczny szyfr przestawieniowy, w którym tekst zapisuje się w układzie tabelarycznym, a następnie odczytuje kolumny według porządku wyznaczonego przez klucz.
## teleprompter:
Jednym z najbardziej znanych przykładów szyfru przestawieniowego jest szyfr kolumnowy. Tekst jawny wpisuje się do tabeli w ustalonym porządku, zwykle wierszami, a następnie odczytuje w innej kolejności, na przykład kolumnami uporządkowanymi zgodnie z hasłem kluczowym. Nie następuje tu zamiana liter na inne litery. Materiał znakowy pozostaje ten sam, lecz jego rozmieszczenie w ciągu szyfrogramu zostaje zmienione. Ten przykład jest bardzo użyteczny, bo pokazuje naturę przestawienia w czystej postaci. Jeśli ktoś zna regułę permutacji kolumn, potrafi odtworzyć pierwotny układ. Jeśli nie zna, widzi ciąg tych samych liter, ale w porządku pozornie chaotycznym. Taki szyfr potrafi skutecznie zniszczyć czytelność słów i prostych fraz, lecz nadal pozostawia wiele informacji statystycznych o samych symbolach. Częste litery pozostają częste, a alfabet się nie zmienia. Z tego powodu samodzielny szyfr kolumnowy nie daje wysokiej odporności na dobrze prowadzoną analizę. Ma jednak dużą wartość jako model dyfuzji w sensie intuicyjnym: treść zostaje przemieszczona w nowe miejsca, przez co lokalne regularności przestają być widoczne tak bezpośrednio jak wcześniej.

#slide 82
## layout
bullet
## slide title
Co daje, a czego nie daje czyste przestawienie
## bullets
- ukrywa bezpośredni porządek znaków
- nie ukrywa repertuaru symboli ani ich globalnych częstości
- samo w sobie nie usuwa statystycznej struktury języka
## teleprompter:
Czyste przestawienie potrafi zrobić jedną rzecz bardzo skutecznie: rozrywa naturalny porządek znaków, z którego powstają czytelne słowa, końcówki i lokalne układy liter. To sprawia, że tekst po zaszyfrowaniu wygląda obco i nie daje się od razu przeczytać. Jednocześnie jednak przestawienie nie usuwa samych symboli. Te same litery, które były obecne w tekście jawnym, nadal znajdują się w szyfrogramie. Ich liczby wystąpień także się nie zmieniają. Oznacza to, że przeciwnik nadal ma do dyspozycji bardzo ważne informacje statystyczne. Jeśli jakaś litera była wyjątkowo częsta, pozostanie wyjątkowo częsta. Jeśli tekst miał charakterystyczny rozkład znaków, ten rozkład nadal jest obecny. Z perspektywy bezpieczeństwa oznacza to, że przestawienie samo w sobie jest raczej mechanizmem mieszającym niż ukrywającym pełną strukturę. Dobrze zaciera lokalne sąsiedztwa, ale nie eliminuje globalnych cech języka. Ta obserwacja prowadzi do naturalnego wniosku: aby uzyskać silniejszą ochronę, trzeba połączyć zmianę wartości symboli z ich przemieszczeniem. Właśnie w tym sensie podstawienie i przestawienie są wobec siebie komplementarne.

#slide 83
## layout
bullet
## slide title
Podstawienie i przestawienie jako operacje komplementarne
## bullets
- podstawienie ukrywa wartości symboli
- przestawienie rozprasza ich położenie
- razem działają silniej niż każda z tych operacji osobno
## teleprompter:
Kiedy zestawi się obok siebie szyfr podstawieniowy i przestawieniowy, od razu widać ich komplementarny charakter. Podstawienie zmienia symbole, ale samo często pozostawia wiele lokalnej i globalnej struktury statystycznej. Przestawienie nie zmienia symboli, ale skutecznie miesza ich położenie. Jeżeli zastosować tylko jedną z tych operacji, przeciwnik otrzymuje przynajmniej część regularności tekstu. Gdy jednak połączyć obie idee, sytuacja staje się znacznie trudniejsza. Podstawienie ukrywa, jakie symbole naprawdę występowały w tekście, a przestawienie rozprasza zależności między ich pozycjami. W rezultacie przeciwnik traci zarazem prosty dostęp do rozkładu treści i do lokalnego porządku. Ta intuicja jest jednym z najważniejszych pomostów między kryptografią klasyczną a nowoczesną. Pokazuje, że nawet bardzo proste operacje mogą w odpowiednim połączeniu dawać jakościowo nowy efekt. Właśnie dlatego w późniejszych konstrukcjach szyfrów blokowych pojawia się wiele rund, które łączą mechanizmy odpowiadające podstawieniu i przestawieniu lub ich odpowiednikom binarnym.

#slide 84
## layout
definition
## term
Szyfr produktowy
## definition
Szyfr otrzymany przez złożenie co najmniej dwóch transformacji, takich jak podstawienie i przestawienie, wykonywanych kolejno w rundach.
## teleprompter:
Szyfr produktowy to konstrukcja zbudowana przez składanie kilku prostszych transformacji w jedną całość. W klasycznym wprowadzeniu najważniejszym przykładem jest połączenie podstawienia i przestawienia. Najpierw można zmienić wartości symboli, a następnie przemieścić ich pozycje, albo wykonać te operacje w innej kolejności, a nawet wielokrotnie. Każde takie złożenie można traktować jako rundę albo jako część rundy, zależnie od przyjętego modelu. Istotne jest to, że bezpieczeństwo nie musi pochodzić z jednej spektakularnie złożonej operacji. Może wynikać z systematycznego nakładania na siebie kilku prostszych przekształceń, z których każde usuwa inną klasę regularności. Taka intuicja jest fundamentalna dla zrozumienia nowoczesnych szyfrów blokowych. Już na poziomie prostych szyfrów widać, że podstawienie i przestawienie osobno nie dają wysokiej odporności, ale razem mogą działać znacznie skuteczniej. Szyfr produktowy nie jest więc tylko technicznym detalem klasyfikacyjnym. Jest zapowiedzią całej filozofii projektowania systemów kryptograficznych, w której bezpieczeństwo wyrasta z kontrolowanego połączenia wielu prostych i dobrze rozumianych operacji.

#slide 85
## layout
definition
## term
Konfuzja
## definition
Własność transformacji szyfrującej polegająca na utrudnianiu uchwycenia związku między kluczem a szyfrogramem.
## teleprompter:
Pojęcie konfuzji, wprowadzone w klasycznym opisie nowoczesnych szyfrów, odnosi się do takiej własności transformacji, która zaciemnia związek między kluczem a szyfrogramem. Intuicja jest następująca. Jeżeli przeciwnik patrzy na wynik szyfrowania, nie powinien łatwo odczytać, jaki wpływ miał konkretny fragment klucza na obserwowany fragment szyfrogramu. Zależność ma być możliwie złożona, nieprzezroczysta i trudna do rozdzielenia na proste reguły. W kontekście klasycznych szyfrów najbardziej naturalnym nośnikiem konfuzji jest podstawienie. Kiedy symbole tekstu jawnego zostają zastąpione według reguły wyznaczonej przez klucz, pojawia się bezpośrednia zależność między wartością klucza a tym, co widzimy na wyjściu. Jeżeli ta zależność jest zbyt prosta, szyfr łatwo analizować. Jeśli zostaje odpowiednio skomplikowana przez kolejne operacje, bezpieczeństwo rośnie. Konfuzja nie oznacza chaosu w potocznym sensie. Oznacza kontrolowaną złożoność relacji klucz–szyfrogram. To pojęcie jest ważne, bo pokazuje, że skuteczny szyfr ma nie tylko coś ukrywać, ale ma ukrywać to w taki sposób, by zależność od klucza nie dawała się łatwo wydzielić z obserwowanych danych.

#slide 86
## layout
definition
## term
Dyfuzja
## definition
Własność transformacji szyfrującej polegająca na rozpraszaniu struktury tekstu jawnego w szyfrogramie tak, aby lokalna redundancja nie była skupiona w jednym miejscu.
## teleprompter:
Dyfuzja to druga z klasycznych idei opisujących, dlaczego połączenie prostych operacji może dawać silniejszy efekt kryptograficzny. Chodzi o takie rozmieszczenie wpływu symboli tekstu jawnego w szyfrogramie, aby lokalna struktura wiadomości została rozproszona. Jeśli w tekście jawnym istnieją powtórzenia, przewidywalne wzorce językowe albo nadmiarowość, to po szyfrowaniu nie powinny one pozostawać skupione w łatwo rozpoznawalnych fragmentach. W intuicji klasycznej nośnikiem dyfuzji jest przestawienie. Przemieszczając symbole, rozrzuca ono informacje o lokalnym sąsiedztwie po całym bloku. W nowoczesnych szyfrach dyfuzja realizowana jest dużo bardziej złożonymi metodami, ale idea pozostaje ta sama: ma być trudno prześledzić prostą drogę od lokalnej regularności tekstu jawnego do lokalnej regularności szyfrogramu. To pojęcie bardzo dobrze pokazuje, dlaczego sama poufność nie sprowadza się do zamiany liter na inne litery. Trzeba jeszcze zadbać o to, aby struktura wiadomości nie pozostawała widoczna w prosty sposób. Dyfuzja jest właśnie odpowiedzią na ten problem rozproszenia informacji.

#slide 87
## layout
bullet
## slide title
Dlaczego nowoczesne szyfry łączą konfuzję i dyfuzję
## bullets
- sama konfuzja nie usuwa całej struktury wiadomości
- sama dyfuzja nie ukrywa wartości symboli
- ich połączenie rozbija zarówno prosty związek z kluczem, jak i lokalną redundancję tekstu
## teleprompter:
Konfuzja i dyfuzja nie są dwiema rywalizującymi własnościami, lecz dwiema stronami tego samego problemu. Jeżeli szyfr wprowadza wyłącznie konfuzję, może nadal pozostawiać pewne regularności tekstu jawnego w zbyt łatwo obserwowalnej postaci. Jeżeli wprowadza wyłącznie dyfuzję, może jedynie mieszać pozycje znaków bez dostatecznego ukrycia ich wartości. Bezpieczeństwo rośnie dopiero wtedy, gdy oba mechanizmy zaczynają działać razem. Wartość symboli zostaje ukryta, a ich wpływ na szyfrogram zostaje rozproszony. To właśnie dlatego w podręcznikowym opisie nowoczesnych szyfrów blokowych pojawiają się rundy, w których działają operacje odpowiadające podstawieniu i przestawieniu. Nawet jeśli konkretne implementacje współczesnych algorytmów są nieporównanie bardziej złożone niż historyczne szyfry literowe, to ich intuicja konstrukcyjna nadal daje się opisać tym językiem. Z perspektywy wykładu o prostych szyfrach ta obserwacja jest szczególnie cenna. Pokazuje, że historia kryptologii nie jest zbiorem martwych ciekawostek. To właśnie w prostych podstawieniach i przestawieniach widać pierwsze zarysy idei, które później kształtują nowoczesne szyfrowanie.

#slide 88
## layout
definition
## term
Szyfr strumieniowy
## definition
Szyfr, w którym transformacja szyfrująca może zmieniać się dla kolejnych symboli tekstu, zgodnie ze strumieniem klucza.
## teleprompter:
Szyfr strumieniowy stanowi inne ujęcie szyfrowania niż klasyczny szyfr blokowy. Zamiast dzielić wiadomość na bloki i szyfrować każdy blok jako całość, można traktować tekst jako ciąg symboli i dla każdego kolejnego symbolu stosować transformację wyznaczaną przez strumień klucza. W podręcznikowym opisie jest to pewnego rodzaju skrajny przypadek, w którym długość bloku wynosi jeden, ale reguła szyfrująca może się zmieniać z pozycji na pozycję. Ta idea jest bardzo ważna, bo pokazuje, że polialfabetyczność można rozumieć szerzej niż tylko jako cykliczne przesunięcia alfabetu. Jeżeli kolejne transformacje są wybierane zgodnie z odpowiednim strumieniem klucza, to szyfrowanie nabiera charakteru sekwencyjnego. Z perspektywy historii pojęć to ważny pomost między klasycznymi szyframi polialfabetycznymi a późniejszymi systemami operującymi na bitach. W prostym ujęciu strumieniowym widać też, dlaczego problem generowania dobrego strumienia klucza staje się centralny. Jeżeli sekwencja jest zbyt prosta, przewidywalna lub użyta ponownie, bezpieczeństwo gwałtownie spada. To właśnie przygotowuje grunt pod przykład szyfru Vernama.

#slide 89
## layout
definition
## term
Szyfr Vernama
## definition
Szyfr strumieniowy nad alfabetem binarnym, w którym kolejne bity wiadomości łączy się z bitami klucza operacją XOR.
## teleprompter:
Szyfr Vernama jest jednym z najbardziej eleganckich przykładów szyfru strumieniowego. Działa nad alfabetem binarnym i wykorzystuje operację XOR. Każdy bit wiadomości jest łączony z odpowiadającym mu bitem klucza, a wynik tworzy szyfrogram. Deszyfrowanie jest równie proste, ponieważ ponowne zastosowanie XOR z tym samym bitem klucza odzyskuje bit wiadomości. Ta konstrukcja jest ważna z kilku powodów. Po pierwsze, pokazuje, jak bardzo kryptografia może się uprościć na poziomie operacji elementarnych. Po drugie, wyraźnie ujawnia rolę strumienia klucza. To nie sama operacja XOR jest źródłem bezpieczeństwa, lecz własności klucza, z którym jest wykonywana. Jeżeli klucz jest słaby, przewidywalny lub używany niepoprawnie, system nie będzie bezpieczny. Po trzecie, szyfr Vernama stanowi bezpośrednią drogę do pojęcia jednorazowego klucza, które prowadzi już do bezpieczeństwa bezwarunkowego w określonych warunkach. W ramach tego wykładu najważniejsze jest jednak zrozumienie samego mechanizmu: kolejna pozycja wiadomości nie musi być szyfrowana tą samą regułą co poprzednia, a bezpieczeństwo może zależeć od jakości i użycia sekwencji kluczowej.

#slide 90
## layout
bullet
## slide title
Jednorazowy klucz jako granica prostych modeli tajności
## bullets
- szyfr Vernama z losowym kluczem użytym tylko raz daje system jednorazowy
- klucz musi mieć długość co najmniej wiadomości
- praktyczna trudność przenosi się na wytworzenie, przekazanie i ochronę klucza
## teleprompter:
Kiedy szyfr Vernama zostaje użyty z prawdziwie losowym kluczem, który ma długość co najmniej równą długości wiadomości i nigdy nie zostaje użyty ponownie, otrzymuje się system jednorazowy. To szczególna granica w historii myślenia o tajności, ponieważ prowadzi do idei bezpieczeństwa idealnego, ale jednocześnie pokazuje jego praktyczny koszt. Matematycznie sytuacja wygląda bardzo atrakcyjnie: odpowiednio użyty klucz jednorazowy nie pozostawia przeciwnikowi wystarczającej informacji do odróżnienia możliwych wiadomości tylko na podstawie szyfrogramu. Operacyjnie pojawia się jednak ten sam problem, który przewijał się przez cały wykład w różnych postaciach: skąd wziąć dobry klucz, jak go bezpiecznie przekazać, jak zagwarantować jego jednorazowość i jak zarządzać nim przy większej liczbie komunikatów oraz użytkowników. W tym sensie jednorazowy klucz zamyka pewien etap. Pokazuje najczystszą odpowiedź na problem poufności, ale zarazem odsłania, że bezpieczeństwo komunikacji nie kończy się na samym szyfrowaniu. Zarządzanie kluczami pozostaje problemem praktycznym i organizacyjnym. To właśnie od tego miejsca naturalnie zaczyna się dalsza historia nowoczesnej kryptografii.

#slide 91
## layout
definition
## term
Doskonała tajność
## definition
Własność systemu szyfrowania, w którym obserwacja szyfrogramu nie daje przeciwnikowi dodatkowej informacji o tekście jawnym.
## teleprompter:
Doskonała tajność jest najmocniejszym klasycznym ideałem poufności. Jeżeli system ją spełnia, to przeciwnik po zobaczeniu szyfrogramu nie dowiaduje się o wiadomości niczego, czego nie wiedział już wcześniej. Nie chodzi więc tylko o to, że odgadnięcie pełnego tekstu jawnego jest trudne. Chodzi o coś znacznie silniejszego: sam szyfrogram nie powinien przesuwać rozkładu prawdopodobieństwa możliwych wiadomości w stronę jednej z nich. W literaturze z zakresu kryptografii ten warunek opisuje się jako brak informacyjnego zysku po stronie przeciwnika. Handbook of Applied Cryptography ujmuje to wprost jako przypadek bezpieczeństwa bezwarunkowego dla szyfrowania, a tradycja shannonowska traktuje to jako wzorzec idealny, wobec którego można porównywać rozwiązania praktyczne. To pojęcie jest bardzo ważne, ponieważ porządkuje dyskusję o granicach prostych szyfrów. Szyfr może mieć elegancki opis, może być łatwy do użycia, może nawet przez pewien czas utrudniać atak, ale jeżeli sam szyfrogram ujawnia strukturę wiadomości, to z definicji nie osiąga poziomu doskonałej tajności. Dlatego kończąc przegląd prostych szyfrów, warto zadać właśnie to pytanie: czy szyfrogram ukrywa informację całkowicie, czy tylko utrudnia jej odzyskanie. Odpowiedź prowadzi od historii szyfrów do fundamentalnego rozróżnienia między bezpieczeństwem idealnym a bezpieczeństwem praktycznym.

#slide 92
## layout
bullet
## slide title
Dlaczego proste szyfry nie dają doskonałej tajności
## bullets
- zachowują część struktury wiadomości
- pozwalają wiązać własności szyfrogramu z własnościami tekstu jawnego
- po obserwacji szyfrogramu przeciwnik zawęża zbiór sensownych hipotez
## teleprompter:
Po przejściu przez szyfry przesuwające, afiniczne, monoalfabetyczne, polialfabetyczne i przestawieniowe widać już bardzo jasno, dlaczego ta rodzina nie daje doskonałej tajności. W każdym z tych przypadków szyfrogram pozostawia ślady struktury wiadomości albo struktury języka. Czasem będzie to rozkład częstości symboli, czasem powtarzalność fragmentów, czasem zachowanie długości i układu bloków, a czasem relacje między pozycjami znaków. Właśnie dlatego przeciwnik po zobaczeniu szyfrogramu nie pozostaje w tej samej sytuacji poznawczej, w jakiej był przed jego zobaczeniem. Jego niepewność maleje. Nie musi jeszcze znać całej wiadomości, ale może zacząć odrzucać kolejne hipotezy, budować ranking prawdopodobnych odczytań, wykorzystywać statystykę języka albo odwoływać się do wiedzy o typowych formatach komunikatów. To wystarczy, by powiedzieć, że ideał doskonałej tajności nie został osiągnięty. Jest to bardzo istotne rozróżnienie. W praktyce historyczne szyfry przez pewien czas bywały użyteczne, lecz ich użyteczność nie wynikała z absolutnego ukrycia informacji, tylko z tego, że przeciwnik nie zawsze miał dość czasu, danych lub kompetencji analitycznych. Z punktu widzenia teorii trzeba jednak powiedzieć wyraźnie: proste szyfry nie eliminują związku między tekstem jawnym a szyfrogramem, a więc nie dają ochrony bezwarunkowej.

#slide 93
## layout
bullet
## slide title
Jednorazowy pad jako punkt odniesienia
## bullets
- klasyczny przykład systemu o bezpieczeństwie bezwarunkowym
- wymaga klucza losowego o długości co najmniej równej długości wiadomości
- wymaga użycia klucza tylko raz
## teleprompter:
Gdy potrzebny jest punkt odniesienia dla pojęcia doskonałej tajności, literatura niemal natychmiast prowadzi do jednorazowego padu. W Handbook of Applied Cryptography jest on wskazywany jako przykład szyfrowania o bezpieczeństwie bezwarunkowym, a Diffie i Hellman również przypominają jego szczególny status. Sens tej konstrukcji jest prosty, choć jej wymagania okazują się bardzo surowe. Klucz musi być naprawdę losowy, musi mieć długość co najmniej równą długości wiadomości i musi zostać użyty tylko jeden raz. Jeżeli te warunki są spełnione, szyfrogram nie daje przeciwnikowi podstaw do preferowania jednej sensownej wiadomości nad inną, bo dla każdej możliwej wiadomości istnieje odpowiedni klucz prowadzący do tego samego szyfrogramu. To właśnie ta wielość zgodnych wyjaśnień stoi za intuicją bezpieczeństwa bezwarunkowego. Jednocześnie jednorazowy pad bardzo dobrze pokazuje, że kryptografia nie jest tylko grą abstrakcyjnych definicji. Im silniejszy model bezpieczeństwa chcemy osiągnąć, tym ostrzejsze stają się wymagania operacyjne. Trzeba wygenerować ogromną ilość wysokiej jakości materiału kluczowego, bezpiecznie go dostarczyć obu stronom, przechować i dopilnować, by nigdy nie został użyty ponownie. Dlatego jednorazowy pad pozostaje punktem odniesienia teoretycznego i ważnym drogowskazem pojęciowym, ale nie stał się uniwersalnym rozwiązaniem codziennej komunikacji na dużą skalę.

#slide 94
## layout
bullet
## slide title
Teoria i praktyka
## bullets
- bezpieczeństwo idealne jest możliwe, ale zwykle kosztowne operacyjnie
- systemy praktyczne częściej opierają się na bezpieczeństwie obliczeniowym
- trzeba oceniać zarówno model matematyczny, jak i warunki użycia
## teleprompter:
W tym miejscu bardzo dobrze widać różnicę między tym, co możliwe w sensie teoretycznym, a tym, co daje się wygodnie stosować w praktyce komunikacyjnej. Jednorazowy pad pokazuje, że ideał poufności nie jest pustą fantazją. Bezwarunkowe bezpieczeństwo można osiągnąć. Równocześnie jednak ta sama konstrukcja pokazuje cenę takiego ideału: ogromne wymagania względem długości klucza, jego losowości, bezpiecznej dystrybucji i ścisłej dyscypliny użycia. Diffie i Hellman podkreślali, że właśnie tego rodzaju ograniczenia uczyniły klasyczne podejścia niewystarczającymi dla rosnących sieci teleprzetwarzania. Dlatego większość użytecznych systemów nowoczesnych przyjmuje model bezpieczeństwa obliczeniowego. Zakłada się w nim nie to, że atak jest logicznie niemożliwy, lecz że jest praktycznie niewykonalny przy danych zasobach czasu, pamięci i mocy obliczeniowej. To nie jest ucieczka od rygoru, tylko zmiana pytania. Zamiast pytać, czy przeciwnik absolutnie nic nie może wydedukować, pyta się, czy najlepszy znany atak mieści się w realnych możliwościach przeciwnika przez czas życia chronionej informacji. Ta różnica ma ogromne znaczenie dla inżynierii systemów. Oceniając rozwiązanie kryptograficzne, nie wolno patrzeć wyłącznie na jego wzór matematyczny. Trzeba patrzeć również na sposób generowania kluczy, kanały ich dystrybucji, założony model przeciwnika, koszt ataku oraz to, jak długo dane muszą zachować wartość poufną.

#slide 95
## layout
bullet
## slide title
Dlaczego sama poufność nie wystarcza w systemach realnych
## bullets
- przeciwnik może nie tylko czytać, ale też zmieniać wiadomości
- trzeba rozróżniać prywatność treści od autentyczności źródła
- bezpieczna komunikacja wymaga także rozwiązania problemu kluczy
## teleprompter:
Jeżeli zatrzymać się wyłącznie na poufności, łatwo przeoczyć najważniejsze zagrożenia prawdziwej komunikacji. Handbook of Applied Cryptography od początku stawia obok poufności także integralność i uwierzytelnianie, a Diffie i Hellman jeszcze mocniej pokazują, że rozwój sieci ujawnił praktyczną wagę tych problemów. Przeciwnik nie musi ograniczać się do podsłuchu. Może próbować wstrzykiwać własne wiadomości, modyfikować istniejące komunikaty, powtarzać stare transmisje albo podszywać się pod uprawnionego nadawcę. W takiej sytuacji sama nieczytelność treści nie wystarcza. Można przecież otrzymać doskonale zaszyfrowaną wiadomość, która została spreparowana przez nieuprawnioną stronę. Można też dostać poprawny technicznie komunikat, który nie pochodzi od tego nadawcy, za którego się podaje. Do tego dochodzi problem organizacji kluczy. Nawet najlepszy schemat szyfrowania nie rozwiązuje sam z siebie pytania, jak wiele stron ma wejść w bezpieczną relację, jak mają uzgadniać tajne parametry i jak mają robić to sprawnie w środowisku publicznych sieci. To jest moment, w którym kryptografia przestaje być rozumiana jedynie jako sztuka ukrywania tekstu. Staje się częścią szerszej architektury bezpieczeństwa informacji, w której poufność jest tylko jednym z koniecznych składników.

#slide 96
## layout
title
## slide title
Od teorii tajności do praktyki komunikacji
## subtitle
Dlaczego sama poufność nie wyczerpuje problemu bezpieczeństwa
## teleprompter:
Do tej pory poruszaliśmy się głównie po terenie klasycznej teorii tajności. Rozmawialiśmy o szyfrogramie, kluczu, redundancji języka, rodzinach prostych szyfrów, analizie statystycznej, przestrzeni kluczy, bezpieczeństwie bezwarunkowym i bezpieczeństwie obliczeniowym. To jest bardzo ważny fundament, ale w tym miejscu trzeba zrobić następny krok i spojrzeć na problem szerzej. W rzeczywistych systemach teleinformatycznych pytanie nie brzmi wyłącznie: czy ktoś potrafi odczytać wiadomość. Równie ważne jest to, czy wiadomość została po drodze zmieniona, czy rzeczywiście pochodzi od deklarowanego nadawcy, czy przeciwnik nie wstrzyknął nowego komunikatu do kanału i czy cała organizacja użycia kluczy jest w ogóle wykonalna przy dużej liczbie użytkowników. Diffie i Hellman bardzo wyraźnie pokazali, że rozwój komunikacji komputerowej uczynił z tych zagadnień problemy pierwszoplanowe. W klasycznym modelu zakłada się często, że strony już wcześniej mają wspólny sekret i mogą go przekazać poza systemem w sposób bezpieczny. W sieciach publicznych, przy wielu podmiotach i dynamicznych relacjach, takie założenie szybko staje się niewystarczające. Ten moment nie oznacza porzucenia klasycznej kryptografii. Oznacza raczej, że widać już granice jej mocy wyjaśniającej. Wiemy, jak opisywać tajność, wiemy, dlaczego proste szyfry ujawniają strukturę języka, wiemy też, czym różni się bezpieczeństwo idealne od praktycznego. Teraz można z tych wniosków wyciągnąć szerszą konsekwencję: bezpieczna komunikacja wymaga jednocześnie poufności, integralności, uwierzytelnienia oraz rozsądnego modelu zarządzania kluczami w środowisku, któremu nie wolno po prostu zaufać.

#slide 97
## layout
bullet
## slide title
Co zostaje po tym wykładzie jako słownik roboczy
## bullets
- kryptologia, kryptografia, kryptoanaliza
- tekst jawny, szyfrogram, klucz, przestrzeń kluczy
- poufność, integralność, uwierzytelnienie, bezpieczeństwo obliczeniowe, doskonała tajność
## teleprompter:
Po przejściu całego materiału warto zebrać słownik roboczy, który będzie wracał przez resztę kursu. Najpierw rozróżnienie między kryptologią, kryptografią i kryptoanalizą. To nie są słowa wymienne. Kryptologia obejmuje całość dziedziny, kryptografia zajmuje się konstrukcją mechanizmów ochrony, a kryptoanaliza bada sposoby ich przełamywania lub osłabiania. Następnie podstawowy język opisu szyfrowania: tekst jawny, szyfrogram, klucz, przestrzeń kluczy, szyfrowanie, deszyfrowanie i odwracalność transformacji po stronie uprawnionego odbiorcy. Dalej dochodzą pojęcia usług bezpieczeństwa. Poufność dotyczy ukrycia treści, integralność dotyczy wykrywania nieuprawnionej zmiany, a uwierzytelnienie dotyczy potwierdzenia tożsamości lub pochodzenia informacji. Wreszcie pozostają dwa poziomy mówienia o odporności systemu: bezpieczeństwo obliczeniowe i doskonała tajność. To rozróżnienie jest szczególnie cenne, bo pozwala unikać nieporozumień. Można powiedzieć, że system jest bezpieczny w praktyce, nie twierdząc zarazem, że jest informacyjnie idealny. Można też wykazać, że pewien model teoretyczny daje silniejszą ochronę, a zarazem przyznać, że jego użycie operacyjne jest uciążliwe. Ten słownik nie jest tylko zestawem definicji do zapamiętania. To zestaw pojęć, bez którego późniejsze tematy, takie jak funkcje skrótu, uwierzytelnianie wiadomości, podpisy cyfrowe czy dystrybucja kluczy, stałyby się nieczytelne.

#slide 98
## layout
bullet
## slide title
Najważniejsze wnioski techniczne
## bullets
- poprawne szyfrowanie wymaga odwracalności dla strony uprawnionej
- mała przestrzeń kluczy lub ujawnianie struktury prowadzą do praktycznej łamliwości
- siła systemu nie może zależeć od tajności samej metody
## teleprompter:
Z perspektywy technicznej można ten wykład sprowadzić do kilku bardzo mocnych wniosków. Po pierwsze, szyfr musi być odwracalny dla uprawnionego odbiorcy. To brzmi banalnie, ale właśnie ten warunek odróżnia poprawny schemat od przypadkowej transformacji symboli. Po drugie, bezpieczeństwa nie daje sama dekoracja matematyczna. Jeżeli przestrzeń kluczy jest mała, atak pełnym przeszukaniem staje się realistyczny. Jeżeli konstrukcja pozostawia statystyczne ślady języka lub inne regularności, przeciwnik może ominąć brute force i użyć lepszej kryptoanalizy. Po trzecie, jawność ogólnej metody nie powinna niszczyć bezpieczeństwa. Zarówno klasyczna zasada Kerckhoffsa, jak i nowoczesne ujęcia wprowadzające publicznie znane klasy transformacji prowadzą do tego samego wniosku: tajny ma pozostać klucz, a nie cała idea działania systemu. Po czwarte, wartość pojęć takich jak bezpieczeństwo obliczeniowe i bezpieczeństwo bezwarunkowe polega na tym, że pozwalają precyzyjnie mówić o granicach systemu, zamiast używać ogólników o tym, że coś jest po prostu mocne albo słabe. Wreszcie, analiza prostych szyfrów uczy czegoś jeszcze bardziej ogólnego: skuteczny przeciwnik korzysta z każdej struktury pozostawionej przez system. Bezpieczeństwo zaczyna się więc tam, gdzie ta struktura jest świadomie ograniczana albo ukrywana.

#slide 99
## layout
bullet
## slide title
Most do dalszej części kursu
## bullets
- dalej pojawią się mechanizmy integralności i uwierzytelniania
- pojawi się problem uzgadniania i dystrybucji kluczy
- późniejsze konstrukcje będą odpowiadały na ograniczenia prostych szyfrów
## teleprompter:
To zakończenie naturalnie prowadzi do dalszej części kursu. Skoro wiadomo już, że sama poufność nie rozwiązuje wszystkich problemów, kolejne zagadnienia będą rozszerzać obraz bezpieczeństwa komunikacji. Pojawią się mechanizmy służące integralności danych i uwierzytelnianiu pochodzenia wiadomości, a także rozwiązania odnoszące się do organizacji kluczy w środowisku publicznych kanałów. Z perspektywy tego wykładu ważne jest jednak, by zobaczyć ciągłość, a nie zerwanie. Późniejsze konstrukcje nie spadają z nieba. Są odpowiedzią na konkretne ograniczenia, które już stały się widoczne przy szyfrach prostych i przy klasycznej teorii tajności. Jeżeli prosty szyfr zachowuje zbyt dużo struktury języka, trzeba szukać konstrukcji, które tę strukturę maskują skuteczniej. Jeżeli sam szyfrogram nie rozstrzyga, czy wiadomość jest autentyczna, trzeba dodać mechanizmy uwierzytelniania. Jeżeli wspólny sekret nie może być zakładany z góry dla każdej pary komunikujących się stron, trzeba rozwiązać problem kluczy inaczej. Właśnie dlatego późniejsze tematy kursu będą czytelniejsze, jeśli zachowa się w pamięci to, co zbudowaliśmy tutaj: podstawowy słownik, model kanału publicznego, klasy ataków, ograniczenia prostych szyfrów i różnicę między ochroną idealną a praktyczną.

#slide 100
## layout
title
## slide title
Koniec wykładu 2
## subtitle
Podstawowe pojęcia kryptologii, poufność danych, terminologia, proste szyfry
## teleprompter:
Drugi wykład domyka podstawowy język kryptologii i porządkuje najważniejsze idee potrzebne do dalszej pracy. Zostały rozróżnione pojęcia kryptologii, kryptografii i kryptoanalizy. Został zbudowany model szyfrowania oparty na tekście jawnym, szyfrogramie i kluczu. Zostały uporządkowane usługi bezpieczeństwa, ze szczególnym naciskiem na poufność, ale także z wyraźnym odróżnieniem integralności i uwierzytelnienia. Przeszliśmy przez rodzinę prostych szyfrów, od podstawieniowych po przestawieniowe, i zobaczyliśmy, że ich ograniczenia nie są przypadkowe, lecz wynikają z zachowania zbyt dużej części struktury języka lub wiadomości. Pojawiło się również rozróżnienie między bezpieczeństwem bezwarunkowym a bezpieczeństwem obliczeniowym oraz klasyczny punkt odniesienia w postaci jednorazowego padu. Ostateczny wniosek jest prosty, ale bardzo ważny. Kryptografia zaczyna się od tajności, lecz nie kończy się na tajności. Bezpieczna komunikacja wymaga szerszego spojrzenia na zagrożenia, własności kanału i organizację kluczy. Z takim fundamentem można przejść do dalszych tematów bez utraty spójności pojęciowej, bo wszystkie następne narzędzia będą rozwijały właśnie te intuicje, które zostały tutaj uporządkowane.
