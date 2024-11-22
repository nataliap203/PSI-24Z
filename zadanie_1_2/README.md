## Zadanie 
Komunikacja UDP
Napisz zestaw dwóch programów – klienta i serwera wysyłające datagramy UDP. Wykonaj ćwiczenie w kolejnych inkrementalnych wariantach (rozszerzając kod z poprzedniej wersji). Klient jak i serwer powinien być napisany zarówno w C jak i Pythonie (4 programy).
Sprawdzić i przetestować działanie „między-platformowe”, tj. klient w C z serwerem Python i vice versa.

Wychodzimy z kodu z zadania 1.1, tym razem pakiety datagramu mają stałą wielkość, można przyjąć np. 512B. Należy zaimplementować prosty protokół niezawodnej transmisji, uwzględniający możliwość gubienia datagramów. Rozszerzyć protokół i program tak, aby gubione pakiety były wykrywane i retransmitowane. Wskazówka – „Bit alternate protocol”. Należy uruchomić program w środowisku symulującym błędy gubienia pakietów. (Informacja o tym, jak to zrobić znajduje się w skrypcie opisującym środowisko Dockera).
## Uruchomienie
```
cd PSI-24Z/zadanie_1_2/Python
```

### Serwer Python
W miejsce `<host_ip>` i `<port>` wpisać można adres IP i port na którym ma się znajdować serwer. W przypadku pominięcia tych argumentów użyte zostaną wartości domyślne: IP 172.21.33.31 i port 8000.
```
./Sink/build.sh
./Sink/run.sh <host_ip> <port>
```

### Klient Python
W miejsce `<host_ip>` i `<port>` wpisać można adres IP i port serwera, na który klient będzie przesyłał dane. W przypadku pominięcia tych argumentów użyte zostaną wartości domyślne: IP 172.21.33.2 i port 8000.
```
./Source/build.sh
./Source/run.sh <host_ip> <port>
```
### Wprowadzenie zakłóceń
Aby włączyć symulowanie zakłóceń występujących w przypadku prawdziwych sieci należy uruchomić polecenie:
```
./Source/inject.sh
```

## Cleanup
Aby wyczyścić poprzednio uruchomione kontenery należy wykonać skrypt `cleanup.sh`

#### Serwer Python
```
./Sink/cleanup.sh
```
#### Klient Python
```
./Source/cleanup.sh
```

## Autorzy
- Krzysztof Gólcz
- Daniel Machniak
- Natalia Pieczko
