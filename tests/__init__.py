import os, signal, time, shutil
import unittest
import pyssdb


class TestCase(unittest.TestCase):
    _SSDB_PID = None

    def _mkdir_var(self):
        if not os.path.isdir('var'):
            os.mkdir('var')

    def _rmdir_var(self):
        if os.path.isdir('var'):
            shutil.rmtree('var')

    def setUp(self):
        self._mkdir_var()
        ssdb = os.getenv('SSDB', 'ssdb-server')
        self._SSDB_PID = os.spawnlp(os.P_NOWAIT, ssdb, ssdb, 'ssdb.conf')
        time.sleep(1)
        self.ssdb = pyssdb.Client()

    def tearDown(self):
        self.ssdb.disconnect()
        os.kill(self._SSDB_PID, signal.SIGTERM)
        time.sleep(0.5)
        self._rmdir_var()
        time.sleep(1)
