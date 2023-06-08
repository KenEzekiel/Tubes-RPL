from datetime import date
from typing import Union


class Hewan:
    def __init__(self, id: int, nama: str, jenis: str, tanggal_lahir: Union[str, date]):
        self._id = id
        self._nama = nama
        self._jenis = jenis
        if isinstance(tanggal_lahir, str):
            self._tanggal_lahir = date.fromisoformat(tanggal_lahir)
        else:
            self._tanggal_lahir = tanggal_lahir

    @property
    def id(self):
        return self._id

    @property
    def nama(self):
        return self._nama

    @property
    def jenis(self):
        return self._jenis

    @property
    def tanggal_lahir(self):
        return self._tanggal_lahir

    @property
    def usia(self):
        today = date.today()
        return today.year - self.tanggal_lahir.year - ((today.month, today.day) < (self.tanggal_lahir.month, self.tanggal_lahir.day))

    @nama.setter
    def nama(self, nama: str):
        self._nama = nama

    @jenis.setter
    def jenis(self, jenis: str):
        self._jenis = jenis

    @tanggal_lahir.setter
    def tanggal_lahir(self, tanggal_lahir: Union[str, date]):
        if isinstance(tanggal_lahir, str):
            self._tanggal_lahir = date.fromisoformat(tanggal_lahir)
        else:
            self._tanggal_lahir = tanggal_lahir

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Hewan):
            return False
        return self._id == __value.id and self._nama == __value.nama and self._jenis == __value.jenis and self._tanggal_lahir == __value.tanggal_lahir

    def __ne__(self, __value: object) -> bool:
        return not self.__eq__(__value)
