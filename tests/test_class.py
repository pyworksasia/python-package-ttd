# Group multiple tests in a class

# - Pytest discovers all tests following its Conventions for Python test discovery, 
# - It finds both test_ prefixed functions and class with prefix Test*. 

class Config:

    def __init__(self) -> None:
        self.APP_NAME = 'My Application'

class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_config_class(self):
        config = Config()
        assert hasattr(config, "APP_NAME")