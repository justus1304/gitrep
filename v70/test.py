import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Konfiguration der 4 Messungen (Gleichgewichtsdrücke und die zugehörigen CSV-Dateien)
# Passe die Dateinamen hier an deine echten Pfade an!
messungen = [
    {
        "pg_titel": "0.502 mbar",
        "csv_file": "Daten/DPLR1/TPG_all_data_2026_04_20-PM04_14_00.csv",
        "pdf_name": "leckrate_0.5mbar.pdf",
    },
    {
        "pg_titel": "10 mbar",
        "csv_file": "Daten/DPLR2/TPG_all_data_2026_04_20-PM04_33_53.csv",
        "pdf_name": "leckrate_10mbar.pdf",
    },
    {
        "pg_titel": "50.1 mbar",
        "csv_file": "Daten/DPLR3/TPG_all_data_2026_04_20-PM04_53_22.csv",
        "pdf_name": "leckrate_50mbar.pdf",
    },
    {
        "pg_titel": "105 mbar",
        "csv_file": "Daten/DPLR41/TPG_all_data_2026_04_20-PM05_02_36.csv",
        "pdf_name": "leckrate_105mbar.pdf",
    },
]

# Vom Korrektor geforderter Fehler für die Fehlerbalken im Diagramm
P_FEHLER = 36.00  # mbar


def verarbeite_messung(messung):
    csv_pfad = messung["csv_file"]

    if not os.path.exists(csv_pfad):
        print(f" HINWEIS: Datei '{csv_pfad}' nicht gefunden. Pfad prüfen!")
        return None

    # 1. Daten einlesen & Spalten von \t bereinigen
    df = pd.read_csv(csv_pfad)
    df.columns = df.columns.str.strip()

    # Zeitachse berechnen (Index 'No.' * 10 Sekunden)
    t_gesamt = df["No"].to_numpy() * 10.0
    p_gesamt = df["druck"].to_numpy()

    # 2. Datenausschluss: Die ersten 2 Punkte (t=0s und t=10s) abschneiden [cite: 351, 525]
    t_fit = t_gesamt[2:]
    p_fit = p_gesamt[2:]

    # Lineare Regression mit Kovarianzmatrix für die Fehlerberechnung
    # cov=True liefert die Kovarianzmatrix (V) zurück
    p, V = np.polyfit(t_fit, p_fit, 1, cov=True)
    m, b = p
    
    # Die Diagonalelemente der Matrix enthalten die Varianzen. 
    # Die Quadratwurzel daraus liefert die Standardabweichungen (Fehler).
    m_fehler = np.sqrt(V[0][0])
    b_fehler = np.sqrt(V[1][1])

    # 3. Plot erstellen und als PDF speichern
    plt.figure(figsize=(8, 5))
    
    # Alle Messwerte mit großen Fehlerbalken (36 mbar) plotten [cite: 385, 434]
    plt.errorbar(t_gesamt, p_gesamt, yerr=P_FEHLER, fmt='o', capsize=3, 
                 elinewidth=1, color='#1f77b4', label='Messwerte')
    
    # Regressionsgerade einzeichnen
    t_gerade = np.linspace(0, max(t_gesamt) + 10, 100)
    p_gerade = m * t_gerade + b
    plt.plot(t_gerade, p_gerade, color='red', linestyle='-', 
             label=f'Fit ab t>=20s (m = {m:.4f} mbar/s)')

    plt.xlabel('t / s', fontsize=11)
    plt.ylabel('p / mbar', fontsize=11)
    plt.title(f"Leckratenmessung Drehschieberpumpe $p_g =$ {messung['pg_titel']}", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend(loc='upper left')
    plt.xlim(-5, max(t_gesamt) + 10)
    plt.ylim(min(p_gesamt) - 50, max(p_gesamt) + 100)

    plt.savefig(messung["pdf_name"], format="pdf", bbox_inches="tight")
    plt.close()

    return {
        "m": m, "m_err": m_fehler,
        "b": b, "b_err": b_fehler
    }


if __name__ == "__main__":
    print("\n" + "="*50)
    print("STARTE KORRIGIERTE VAKUUM-AUSWERTUNG MIT FEHLERN")
    print("="*50)
    
    ergebnisse = {}
    
    for m in messungen:
        res = verarbeite_messung(m)
        if res is not None:
            ergebnisse[m["pg_titel"]] = res
            
    # =========================================================================
    # ZUSAMMENFASSENDE AUSGABE IM TERMINAL (INKLUSIVE FEHLER)
    # =========================================================================
    print("\n" + "#"*65)
    print("ERHALTENE PARAMETER FÜR DEIN LATEX-DOKUMENT (INKL. STAT. FEHLER):")
    print("#"*65 + "\n")
    
    for titel, res in ergebnisse.items():
        print(f" Gleichgewichtsdruck pg = {titel}:")
        print(f"   --> Steigung m:        {res['m']:.5f} +/- {res['m_err']:.5f} mbar/s")
        print(f"   --> Achsenabschnitt b: {res['b']:.5f} +/- {res['b_err']:.5f} mbar")
        print("-" * 55)
        
    print("\nAlle PDF-Diagramme wurden erfolgreich im Ordner gespeichert!\n")