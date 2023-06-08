CREATE TABLE Hewan
(
    id_hewan      INTEGER PRIMARY KEY AUTOINCREMENT,
    nama          VARCHAR(255) NOT NULL,
    jenis         VARCHAR(255) NOT NULL,
    tanggal_lahir DATE CHECK(tanggal_lahir IS strftime('%Y-%m-%d', tanggal_lahir))
);

CREATE TABLE RiwayatHewan
(
    id_riwayat  INTEGER PRIMARY KEY AUTOINCREMENT,
    id_hewan    INTEGER,
    riwayat     VARCHAR(255) NOT NULL,
    waktu_awal  DATE CHECK(waktu_awal IS strftime('%Y-%m-%d', waktu_awal)),
    waktu_akhir DATE CHECK(waktu_akhir IS strftime('%Y-%m-%d', waktu_akhir)),
    FOREIGN KEY (id_hewan) REFERENCES Hewan (id_hewan)
);

CREATE TABLE Makanan
(
    id_makanan INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_makanan VARCHAR(255) NOT NULL
);

CREATE TABLE JenisMakanan
(
    id_hewan INTEGER,
    id_makanan INTEGER,
    PRIMARY KEY (id_makanan, id_hewan),
    FOREIGN KEY (id_hewan) REFERENCES Hewan(id_hewan),
    FOREIGN KEY (id_makanan) REFERENCES Makanan(id_makanan)
);