import os, signal, time, shutil

_SSDB_PID = None

def mkdir_var():
    if not os.path.isdir('var'):
        os.mkdir('var')

def rmdir_var():
    if os.path.isdir('var'):
        shutil.rmtree('var')

def setUpModule():
    global _SSDB_PID
    mkdir_var()
    ssdb = os.getenv('SSDB', 'ssdb-server')
    _SSDB_PID = os.spawnlp(os.P_NOWAIT, ssdb, ssdb, 'ssdb.conf')
    time.sleep(1)

def tearDownModule(module):
    os.kill(_SSDB_PID, signal.SIGTERM)
    time.sleep(0.5)
    rmdir_var()
    time.sleep(1)
