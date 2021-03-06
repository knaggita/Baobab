import unittest

from app import db, app


class ApiTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = True
        self.app = app.test_client()
        db.reflect()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.reflect()
        db.engine.execute('DELETE FROM alembic_version;')
        db.drop_all()