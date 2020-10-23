from tornado_sqlalchemy import SessionMixin
from ..config.meta import BaseHandler
from abc import ABC
import json
from ..models.siswa import Siswa


class SiswaGetHandler(BaseHandler, SessionMixin, ABC):
    def get(self):
        try:
            with self.make_session() as session:
                siswa = session.query(Siswa).all()
                data = [{
                    'id': c.id,
                    'nisn': c.nisn,
                    'nama_siswa': c.nama_siswa,
                    'tgl_masuk': c.tgl_masuk
                } for c in siswa]

                self.set_status(200)
                self.write({'Success To Get Data Siswa list':200, 'data':data})

        except Exception as e:
            print(e)
            self.set_status(500)
            self.write({'Error To Get Siswa List':500})

class SiswaPostHandler(BaseHandler, SessionMixin, ABC):
    def post(self):
        try:
            body = (json.loads(self.request.body))
            nisn = body.get('nisn')
            nama_siswa = body.get('nama_siswa')
            kelas = body.get('kelas')
            tgl_masuk = body.get('tgl_masuk')

            with self.make_session() as session:
                siswa = Siswa()
                siswa.nisn = nisn
                siswa.nama_siswa = nama_siswa
                siswa.kelas = kelas
                siswa.tgl_masuk = tgl_masuk
                session.add(siswa)
                session.commit()

                self.set_status(200)
                self.write({'Success To Add New Siswa': 200})

        except Exception as e:
            print(e)
            self.set_status(500)
            self.write({'Error To Add New Siswa': 500})


class SiswaUpdtHandler(BaseHandler, SessionMixin, ABC):
    def put(self, **matchdict):
        try:
            body = (json.loads(self.request.body))
            id = matchdict.get('id')
            nisn = body.get('nisn')
            nama_siswa = body.get('nama_siswa')
            kelas = body.get('kelas')
            tgl_masuk = body.get('tgl_masuk')

            with self.make_session() as session:
                siswa = session.query(Siswa).filter(
                    Siswa.id == int(id)
                ).first()

                siswa.nisn = nisn
                siswa.nama_siswa = nama_siswa
                siswa.kelas = kelas
                siswa.tgl_masuk = tgl_masuk
                session.add(siswa)
                session.commit()

                self.set_status(200)
                self.write({'Succes To Edit Siswa':200})

        except Exception as e:
            print(e)
            self.set_status(500)
            self.write({'Error To Edit Siswa':500})

class SiswaDelHandler(BaseHandler, SessionMixin, ABC):
    def delete(self, **matchdict):
        try:
            id= matchdict.get('id')

            with self.make_session() as session:
                session.query(Siswa).filter(
                    Siswa.id == int(id)
                ).delete(synchronize_session=False)

                session.commit()

                self.set_status(200)
                self.write({'Success To Delete Siswa':200})

        except Exception as e:
            print(e)
            self.set_status(500)
            self.write({'Error To Delete Siswa':500})