import json
import shutil
from pathlib import Path
from .registry import ModeRegistry

class TestManager:
    def __init__(self, tests_root=None, mode="default"):
        self.tests_base = Path(tests_root or "TEST_SUITE").resolve()
        self.tests_base.mkdir(parents=True, exist_ok=True)
        self.mode = mode

    def create_std_test(self, test_name: str, replace: bool = False) -> Path:
        test_dir = self.tests_base / test_name
        if replace and test_dir.exists(): 
            shutil.rmtree(test_dir)
        
        folders = ModeRegistry.get_folders(self.mode)
        for folder in folders:
            (test_dir / folder).mkdir(parents=True, exist_ok=True)

        meta_folder = next((f for f in folders if "META_CONFIG" in f), folders[2])
        
        config = {
            "std_version": "0.2.0",
            "mode": self.mode,
            "execution_meta": {
                "engine": "stdcodetest-core-v1",
                "env_requirements": self._get_env_hint()
            }
        }
        (test_dir / meta_folder / "config.json").write_text(json.dumps(config, indent=4))
        
        return test_dir

    def _get_env_hint(self):
        hints = {"vue": "node-18", "pytorch": "python-3.10", "default": "python-3.8"}
        for k, v in hints.items():
            if k in self.mode: return v
        return hints["default"]

def cli_main():
    print("stdcodetest CLI: Standardized Testing Framework for AI.")