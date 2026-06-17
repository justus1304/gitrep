import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
from uncertainties import ufloat

# ==========================================
# FUNKTIONEN FÜR FINETUNING & ABSTANDS-AUSWERTUNG
# ==========================================


def lade_und_filter_peaks(dateiname):
    """Liest die .dat Datei ein und isoliert nur die Hauptresonanzen."""
    try:
        daten = np.loadtxt(dateiname)
        frequenzen = daten[:, 0]
        amplituden = daten[:, 1]

        # --- HIER TUNEN, WENN ER IMMER NOCH ZU VIELE PEAKS NIMMT ---
        # prominence=0.5 bedeutet: Der Peak muss sich deutlich vom Untergrund abheben.
        # height=0.3 bedeutet: Absolute Mindesthöhe des Peaks.
        peak_indizes, _ = find_peaks(
            amplituden,
            height=0.3,
            prominence=3,
            distance=100,  # Erhöht den Mindestabstand zwischen Peaks
        )

        gefundene_peaks = frequenzen[peak_indizes]

        print(f"Datei '{dateiname}' erfolgreich geladen.")
        print(f"Gefundene Hauptpeaks bei: {gefundene_peaks} Hz")

        return frequenzen, amplituden, gefundene_peaks

    except IOError:
        print(f"Fehler: Datei '{dateiname}' nicht gefunden.")
        return None, None, np.array([])


def c_aus_peak_abstaenden(laenge_mm, peaks_hz, name="Zylinder"):
    """Berechnet die Schallgeschwindigkeit direkt aus den gemittelten Abständen

    der aufeinanderfolgenden Peaks: c = 2 * L * delta_f.
    """
    if len(peaks_hz) < 2:
        print(
            f"Zu wenige Peaks für {name} gefunden ({len(peaks_hz)}). Abstandsberechnung braucht mind. 2."
        )
        return None, ufloat(0, 0)

    L = laenge_mm / 1000.0  # mm in Meter

    # Berechne die Differenzen zwischen aufeinanderfolgenden Peaks (f_{n+1} - f_n)
    abstaende = np.diff(peaks_hz)

    # Mittelwert und Standardabweichung der Abstände für die Fehlerrechnung
    delta_f_mittel = np.mean(abstaende)
    delta_f_fehler = (
        np.std(abstaende, ddof=1) if len(abstaende) > 1 else 10.0
    )  # Min. 10 Hz Fehler falls nur 1 Abstand

    # Als ufloat verpacken
    delta_f_u = ufloat(delta_f_mittel, delta_f_fehler)
    L_u = ufloat(L, 0.0005)  # 0.5 mm Messunsicherheit auf den Zylinder

    # Physikalische Formel: c = 2 * L * delta_f
    c_u = 2 * L_u * delta_f_u

    print(f"--- Abstandsauswertung für {name} ---")
    print(f"Peak-Abstände (Delta f): {abstaende} Hz")
    print(f"Mittlerer Abstand: {delta_f_u} Hz")
    print(f"Berechnete Schallgeschwindigkeit c = {c_u:.2f} m/s\n")

    return abstaende, c_u


# ==========================================
# HAUPTPROGRAMM
# ==========================================

datei_50mm = "Daten/2vor1.dat"
datei_75mm = "Daten/vor1.dat"

# 1. Daten laden und nur die "großen" Peaks filtern
freq_50, amp_50, peaks_50 = lade_und_filter_peaks(datei_50mm)
freq_75, amp_75, peaks_75 = lade_und_filter_peaks(datei_75mm)

# 2. Berechnung über die Abstände
abst_50, c_50 = c_aus_peak_abstaenden(50, peaks_50, "50mm Zylinder")
abst_75, c_75 = c_aus_peak_abstaenden(75, peaks_75, "75mm Zylinder")

# ==========================================
# KONTROLL-PLOT DER ROHDATEN MIT PEAKS
# ==========================================
# Damit du sofort siehst, ob er jetzt die richtigen Peaks erwischt hat
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

if freq_50 is not None and len(peaks_50) > 0:
    ax1.plot(freq_50, amp_50, "b-", label="Spektrum 50mm Zylinder")
    # Markiere die gefundenen Peaks mit einem roten X
    ax1.plot(
        peaks_50,
        amp_50[np.isin(freq_50, peaks_50)],
        "rx",
        markersize=10,
        mew=2,
        label="Ermittelte Peaks",
    )
    ax1.set_title(f"50mm Zylinder (Ergebnis: $c = {c_50:.1fL}\\text{{ m/s}}$)")
    ax1.set_ylabel("Amplitude")
    ax1.grid(True, linestyle=":")
    ax1.legend()

if freq_75 is not None and len(peaks_75) > 0:
    ax2.plot(freq_75, amp_75, "r-", label="Spektrum 75mm Zylinder")
    ax2.plot(
        peaks_75,
        amp_75[np.isin(freq_75, peaks_75)],
        "kx",
        markersize=10,
        mew=2,
        label="Ermittelte Peaks",
    )
    ax2.set_title(f"75mm Zylinder (Ergebnis: $c = {c_75:.1fL}\\text{{ m/s}}$)")
    ax2.set_xlabel("Frequenz $f$ / Hz")
    ax2.set_ylabel("Amplitude")
    ax2.grid(True, linestyle=":")
    ax2.legend()

plt.tight_layout()
fig.savefig("build/peaks.pdf")
plt.show()