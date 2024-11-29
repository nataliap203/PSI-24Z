## Zadanie 
Z 2 Komunikacja TCP

Napisz zestaw dwóch programów – klienta i serwera komunikujących się poprzez TCP. Transmitowany strumień danych powinien być stosunkowo duży, nie mniej niż 100 kB.


Zmodyfikuj program klienta tak, aby jednorazowo wysyłane były małe porcje danych (mniejsze od pojedynczej struktury) i wprowadź dodatkowe sztuczne opóźnienie po stronie klienta (przy pomocy funkcji sleep()). W programie serwera zorganizuj kod tak, aby serwer kompletował dane i drukował je „na bieżąco”.
## Uruchomienie
```
cd PSI-24Z/zadanie_2/Python
```

### Serwer Python
W miejsce `<host_ip>` i `<port>` wpisać można adres IP i port na którym ma się znajdować serwer. W przypadku pominięcia tych argumentów użyte zostaną wartości domyślne: IP 172.21.33.31 i port 8000.
```
./Server/build.sh
./Server/run.sh <host_ip> <port>
```

### Klient Python
W miejsce `<host_ip>` i `<port>` wpisać można adres IP i port serwera, na który klient będzie przesyłał dane. W przypadku pominięcia tych argumentów użyte zostaną wartości domyślne: IP 172.21.33.31 i port 8000.
```
./Client/build.sh
./Client/run.sh <host_ip> <port>
```
## Cleanup
Aby wyczyścić poprzednio uruchomione kontenery należy wykonać skrypt `cleanup.sh`

#### Serwer Python
```
./Server/cleanup.sh
```
#### Klient Python
```
./Client/cleanup.sh
```

## Autorzy
- Krzysztof Gólcz
- Daniel Machniak
- Natalia Pieczko
