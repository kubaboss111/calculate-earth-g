import numpy as np
from scipy.optimize import fsolve

# ==========================================
# 1. WPISZ SWOJE DANE Z EKSPERYMENTU
# ==========================================

h_zmierzone = 1      # Wysokość spadania w metrach
klatki = 90.5             # Liczba klatek zliczowych z wideo (od startu do mety)
fps = 200.0             # Klatki na sekundę Twojego telefonu
t_zmierzone = klatki / fps  # Obliczony czas lotu w sekundach

# Parametry piłki (WPISZ SWOJE)
m = 0.173               # Masa piłki w kilogramach
d = 0.032               # Średnica piłki w metrach

# Parametry środowiska (zostaw domyślne)
rho = 1.225             # Gęstość powietrza w kg/m^3
Cd = 0.47               # Współczynnik oporu dla kuli (sfery)

# ==========================================
# 2. ALGORYTM OBLICZENIOWY
# ==========================================

# Pole przekroju poprzecznego piłki
A = (np.pi * d**2) / 4.0

# Stała współczynnika oporu z wyprowadzenia matematycznego: k = (rho * Cd * A) / 2m
k = (rho * Cd * A) / (2.0 * m)

# Definiujemy funkcję, która musi równać się zero: f(g) = h_teoretyczne(g) - h_zmierzone
# h_teoretyczne to nasze: (1/k) * ln(cosh(t * sqrt(g*k)))
def rownanie_do_rozwiazania(g_guess):
    argument_cosh = t_zmierzone * np.sqrt(g_guess * k)
    h_teoretyczne = (1.0 / k) * np.log(np.cosh(argument_cosh))
    return h_teoretyczne - h_zmierzone

# Używamy fsolve do znalezienia miejsca zerowego funkcji (zgadujemy, że g jest w okolicach 9.8)
g_obliczone = fsolve(rownanie_do_rozwiazania, x0=9.81)[0]

# ==========================================
# 3. WYNIKI
# ==========================================

print("--- WYNIKI EKSPERYMENTU ---")
print(f"Czas lotu wyliczony z klatek: {t_zmierzone:.4f} s")
print(f"Stała k (opór do masy): {k:.4f} m^-1")
print(f"==========================================")
print(f"WYZNACZONE PRZYSPIESZENIE ZIEMSKIE (g): {g_obliczone:.4f} m/s^2")
print(f"==========================================")

# Opcjonalnie: Dla porównania wyliczenie z prostego wzoru na próżnię (bez oporu)
g_proznia = (2 * h_zmierzone) / (t_zmierzone**2)
print(f"Dla porównania, wynik bez oporu powietrza wyniósłby: {g_proznia:.4f} m/s^2")