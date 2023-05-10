list_Mahasiswa = [
{"NIM": "Ti001", "Nama": "Ali", "Fisika": "A", "Biologi": "A", "Matematika": "A"},
{"NIM": "Ti002", "Nama": " Budi", "Fisika": "B", "Biologi": "C", "Matematika": "B"},
{"NIM": "Ti003", "Nama": "Caca", "Fisika": "B", "Biologi": "A", "Matematika": "B"},
{"NIM": "Ti004", "Nama": "Dodo", "Fisika": "A", "Biologi": "B", "Matematika": "A"},
{"NIM": "Ti001", "Nama": "Elo", "Fisika": "A", "Biologi": "C", "Matematika": "A"} 
]

A = 4
B = 3
C = 2
D = 1
E = 0

NilaiRataRataAli = (A+A+A)/3
NilaiRataRataBudi = (B+C+B)/3
NilaiRataRataCaca = (B+A+B)/3
NilaiRataRataDodo = (A+B+A)/3
NilaiRataRataElo = (A+C+A)/3

HasilRataRata = [{"RataRata": {NilaiRataRataAli}},
                 {"RataRata": {NilaiRataRataBudi}},
                 {"RataRata": {NilaiRataRataCaca}},
                 {"RataRata": {NilaiRataRataDodo}},
                 {"RataRata": {NilaiRataRataElo}}]
for i in range (len(list_Mahasiswa)):
    list_Mahasiswa[i]["RataRata"] = HasilRataRata[i]
print(list_Mahasiswa)