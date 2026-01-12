class ModeRegistry:
    """
    Architecture for managing diversified standards. 
    Sequential folders ensure a logical pipeline for LLM evaluations.
    """
    _LOCAL_STANDARDS = {
        "default": ["0-INPUT", "1-USER", "2-META_CONFIG", "3-EXPECTED", "4-OUTPUT", "5-EVALUATION"],
        "vue3.2": ["0-INPUT", "1-USER", "2-META_CONFIG", "3-VITE_CFG", "4-OUTPUT", "5-EVALUATION"],
        "pytorch2.0": ["0-INPUT", "1-USER", "2-META_CONFIG", "3-WEIGHTS", "4-OUTPUT", "5-EVALUATION"]
    }

    @classmethod
    def get_folders(cls, mode):
        return cls._LOCAL_STANDARDS.get(mode, cls._LOCAL_STANDARDS["default"])

    @classmethod
    def list_modes(cls):
        return list(cls._LOCAL_STANDARDS.keys())