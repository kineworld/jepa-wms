import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


class HubTests(unittest.TestCase):
    def setUp(self):
        spec=importlib.util.spec_from_file_location('hub_test',Path(__file__).resolve().parents[1]/'hubconf.py')
        self.m=importlib.util.module_from_spec(spec);spec.loader.exec_module(self.m)

    def test_explicit_path_reaches_loader_without_download(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'weights.pt';p.write_bytes(b'fixture')
            with patch.object(self.m,'_load_model_with_config',return_value='ok') as load:
                self.assertEqual(self.m.jepa_wm_pusht(checkpoint_path=p,device='cpu'),'ok')
                self.assertEqual(load.call_args.kwargs['checkpoint_path'],str(p.resolve()))

    def test_missing_path_and_unknown_keyword_fail(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(FileNotFoundError):self.m.jepa_wm_pusht(checkpoint_path=Path(d)/'missing')
        with self.assertRaises(TypeError):self.m.jepa_wm_pusht(checkpont_path='typo')

if __name__=='__main__':unittest.main()
