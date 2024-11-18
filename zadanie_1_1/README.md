## Zadanie 
Komunikacja UDP
Napisz zestaw dwóch programów – klienta i serwera wysyłające datagramy UDP. Wykonaj ćwiczenie w kolejnych inkrementalnych wariantach (rozszerzając kod z poprzedniej wersji). Klient jak i serwer powinien być napisany zarówno w C jak i Pythonie (4 programy).
Sprawdzić i przetestować działanie „między-platformowe”, tj. klient w C z serwerem Python i vice versa.

Klient wysyła, a serwer odbiera datagramy o stałym rozmiarze (rzędu kilkuset bajtów). Datagramy powinny posiadać ustaloną formę danych. Przykładowo: pierwsze dwa bajty datagramu mogą zawierać informację o jego długości, a kolejne bajty kolejne litery A-Z powtarzające się wymaganą liczbę razy (ale można przyjąć inne rozwiązanie).  Odbiorca powinien weryfikować odebrany datagram i odsyłać odpowiedź  o ustalonym formacie. Klient powinien wysyłać kolejne datagramy o przyrastającej wielkości np. 1, 100, 200, 1000, 2000… bajtów.   Sprawdzić, jaki był maksymalny rozmiar wysłanego (przyjętego) datagramu. Ustalić z dokładnością do jednego bajta jak duży datagram jest obsługiwany. Wyjaśnić.
## Uruchomienie
```
cd PSI-24Z/zadanie_1_1
```

### Serwer Python
W miejsce `<host_ip>` i `<port>` wpisać można adres IP i port na którym ma się znajdować serwer. W przypadku pominięcia tych argumentów użyte zostaną wartości domyślne: IP 172.21.33.21 i port 8080.
```
./Python/Server/build.sh
./Python/Server/run.sh <host_ip> <port>
```

### Klient Python
W miejsce `<host_ip>` i `<port>` wpisać można adres IP i port serwera, na który klient będzie przesyłał dane. W przypadku pominięcia tych argumentów użyte zostaną wartości domyślne: IP 172.21.33.21 i port 8080.
```
./Python/Client/build.sh
./Python/Client/run.sh <host_ip> <port>
```

### Serwer C
W miejsce `<host_ip>` i `<port>` wpisać można adres IP i port na którym ma się znajdować serwer. W przypadku pominięcia tych argumentów użyte zostaną wartości domyślne: IP 172.21.33.11 i port 8080.
```
./C/Server/build.sh
./C/Server/run.sh <host_ip> <port>
```

### Klient C
W miejsce `<host_ip>` i `<port>` wpisać można adres IP i port serwera, na który klient będzie przesyłał dane. W przypadku pominięcia tych argumentów użyte zostaną wartości domyślne: IP 172.21.33.11 i port 8080.
```
./C/Client/build.sh
./C/Client/run.sh <host_ip> <port>
```
## Cleanup
Aby wyczyścić poprzednio uruchomione kontenery należy wykonać skrypt `cleanup.sh`

#### Serwer Python
```
./Python/Server/cleanup.sh
```
#### Klient Python
```
./Python/Client/cleanup.sh
```
#### Serwer C
```
./C/Server/cleanup.sh
```
#### Klient C
```
./C/Client/cleanup.sh
```

## Autorzy
- Krzysztof Gólcz
- Daniel Machniak
- Natalia Pieczko
