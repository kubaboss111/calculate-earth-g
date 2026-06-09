# Wyznaczanie przyspieszenia ziemskiego (g) przy użyciu smartfona 

Projekt badawczy polegający na wyznaczeniu wartości przyspieszenia grawitacyjnego Ziemi ($g$) na podstawie analizy wideo spadku swobodnego, z uwzględnieniem aerodynamicznego oporu powietrza.

Projekt został zrealizowany w ramach zaliczenia przedmiotu Fizyka. Zgodnie z wytycznymi, eksperyment omija wykorzystanie wbudowanego w smartfon akcelerometru, opierając się wyłącznie na optycznej analizie poklatkowej i algorytmach numerycznych.

##  Cel projektu
Celem kodu jest numeryczne rozwiązanie równania ruchu dla spadającego obiektu (sfery), na który działają siła ciężkości oraz siła oporu powietrza (model proporcjonalny do kwadratu prędkości).

Równanie drogi od czasu dla tego modelu to równanie przestępne:
$h(t) = \frac{1}{k} \ln(\cosh(t\sqrt{gk}))$

Ponieważ wyciągnięcie $g$ z tego równania za pomocą przekształceń algebraicznych jest niemożliwe, ten skrypt rozwiązuje je numerycznie.

##  Jak działa algorytm?
Program wykorzystuje biblioteki `numpy` oraz `scipy` (konkretnie funkcję `fsolve` z modułu `scipy.optimize`). 
Algorytm szuka miejsca zerowego przekształconej funkcji, dopasowując wartość $g$ tak, aby zrównoważyć lewą i prawą stronę równania dla zmierzonego przez nas czasu lotu ($t$) z dokładnością do ułamków sekund (odczytanych z wideo nagranego w 200 FPS).
