"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from httprunner import HttpRunner, Config, Step, RunTestCase
from <route> import <class> as <alias>


class TestCase<alias>(HttpRunner):

    config = Config("testcase description").verify(False).variables(
        **<datas>
        )

    teststeps = [
        Step(
            RunTestCase("<alias>").call(<alias>)
        ),
    ]
"""
