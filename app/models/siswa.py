from sqlalchemy import Column, BigInteger, String
from datetime import datetime
from sqlalchemy.schema import Sequence
from ..config.meta import Base

date = datetime

class Siswa(Base):
    __tablename__ = 'siswa'

    id = Column(BigInteger, Sequence('siswa_id_seq', increment=1), primary_key=True)
    nisn = Column(BigInteger)
    nama_siswa = Column(String(100))
    kelas = Column(String(20))
    tgl_masuk = Column(String(50))
