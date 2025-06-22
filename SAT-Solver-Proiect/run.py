import time
import glob
import csv
import sys
import os

from src.solvers import dpll
from src.cnf_parser import parse_cnf

if __name__ == '__main__':
    DATA_DIR = 'data'
    RESULTS_DIR = 'results'

    if not os.path.exists(DATA_DIR) or not os.listdir(DATA_DIR):
        os.makedirs(DATA_DIR, exist_ok=True)
        print(f"EROARE: Folderul '{DATA_DIR}' este gol.")
        sys.exit(1)

    os.makedirs(RESULTS_DIR, exist_ok=True)
    
    instance_files = sorted(glob.glob(os.path.join(DATA_DIR, '*.cnf')))
    output_filename = os.path.join(RESULTS_DIR, 'results.csv')

    with open(output_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Instance", "Algorithm", "Result", "Time(s)"])
        
        print(f"Se rulează experimentele... (Mod Simplificat)")
        
        for filepath in instance_files:
            filename = os.path.basename(filepath)
            print(f"\nProcesare: {filename}")
            
            formula = parse_cnf(filepath)
            if formula is None: continue
            start_time = time.time()
            try:
                is_sat = dpll(formula)
                end_time = time.time()
                
                result_str = "SAT" if is_sat else "UNSAT"
                time_val = end_time - start_time
                
                writer.writerow([filename, "DPLL", result_str, f"{time_val:.4f}"])
                print(f"  -> DPLL: {result_str} în {time_val:.4f}s")

            except RecursionError:
                writer.writerow([filename, "DPLL", "RecursionError", "N/A"])
                print(f"  -> DPLL: EROARE de recursivitate!")
            except Exception as e:
                writer.writerow([filename, "DPLL", f"ERROR: {e}", "N/A"])
                print(f"  -> DPLL: EROARE: {e}")
            writer.writerow([filename, "DP", "N/A (Ignorat)", "N/A"])
            print(f"  -> DP: N/A (Ignorat)")
            writer.writerow([filename, "Resolution", "N/A (Ignorat)", "N/A"])
            print(f"  -> Resolution: N/A (Ignorat)")

    print(f"\nExperimente finalizate! Rezultatele sunt în '{output_filename}'.")