# SAT-Solver-Comparison
## Structura Proiectului

- `data/`: Conține instanțele de test în format DIMACS CNF.
- `figures/`: Conține graficele și figurile generate pentru analiză.
- `results/`: Conține rezultatele brute ale experimentelor (ex: fișiere `.csv`).
- `src/`: Conține codul sursă al proiectului.
  - `solvers.py`: Implementarea algoritmilor SAT.
  - `cnf_parser.py`: Utilitar pentru citirea fișierelor CNF.
- `run.py`: Script principal pentru rularea experimentelor.
- `README.md`: Acest fișier.

## Manual de Utilizare

### 1. Cerințe
- Python 3.7+

### 2. Pregătirea
1.  Clonati acest repository.
2.  Adăugați instanțele de test (fișiere `.cnf`) în folderul `data/`.

### 3. Rularea Experimentelor
Pentru a rula toți algoritmii pe toate instanțele din folderul `data/`, executați comanda:

```bash
python run.py