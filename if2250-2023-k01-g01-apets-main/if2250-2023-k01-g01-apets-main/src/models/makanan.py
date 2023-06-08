class Makanan:
    _id: int
    _nama_makanan: str

    def __init__(self, id: int, nama_makanan: str):
        self._id = id
        self._nama_makanan = nama_makanan

    @property
    def id(self):
        return self._id

    @property
    def nama_makanan(self):
        return self._nama_makanan

    @nama_makanan.setter
    def nama_makanan(self, nama: str):
        self._nama_makanan = nama

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Makanan):
            return False
        return (self._id == __value.id and
                self.nama_makanan == __value.nama_makanan)

    def __ne__(self, __value: object) -> bool:
        return not self.__eq__(__value)
