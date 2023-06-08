from datetime import date
from typing import Union


class RiwayatHewan:
    _id: int
    _riwayat: str
    _waktu_awal: Union[date, None]
    _waktu_akhir: Union[date, None]

    def __init__(self, id: int, riwayat: str, waktu_awal: Union[str, date, None], waktu_akhir: Union[str, date, None]):
        self._id = id
        self._riwayat = riwayat
        if isinstance(waktu_awal, str):
            self.waktu_awal = date.fromisoformat(waktu_awal)
        else:
            self.waktu_awal = waktu_awal

        if isinstance(waktu_akhir, str):
            self.waktu_akhir = date.fromisoformat(waktu_akhir)
        else:
            self.waktu_akhir = waktu_akhir

    @property
    def id(self):
        return self._id

    @property
    def riwayat(self):
        return self._riwayat

    @property
    def waktu_awal(self):
        return self._waktu_awal

    @property
    def waktu_akhir(self):
        return self._waktu_akhir

    @riwayat.setter
    def riwayat(self, riwayat: str):
        self._riwayat = riwayat

    @waktu_awal.setter
    def waktu_awal(self, tanggal: Union[str, date, None]):
        if isinstance(tanggal, str):
            self._waktu_awal = date.fromisoformat(tanggal)
        else:
            self._waktu_awal = tanggal

    @waktu_akhir.setter
    def waktu_akhir(self, tanggal: Union[str, date, None]):
        if isinstance(tanggal, str):
            self._waktu_akhir = date.fromisoformat(tanggal)
        else:
            self._waktu_akhir = tanggal

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, RiwayatHewan):
            return False
        return (self._id == __value.id and
                self.riwayat == __value.riwayat and
                self.waktu_awal == __value.waktu_awal and
                self.waktu_akhir == __value.waktu_akhir)

    def __ne__(self, __value: object) -> bool:
        return not self.__eq__(__value)
