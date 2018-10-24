import logging
import os
import random
import sys
from collections import Counter
from typing import Union
from unittest import TestResult

from django.test.runner import RemoteTestResult

logger = logging.getLogger(__name__)


PYTHON_RANDOM_SEED = "PYTHON_RANDOM_SEED"
PYTHON_TEST_RANDOM_SEED = "PYTHON_TEST_RANDOM_SEED"
PYTHON_TEST_CLASS_RANDOM_SEED = "PYTHON_TEST_CLASS_RANDOM_SEED"


def _get_random_seed():
    seed = os.environ.get(PYTHON_RANDOM_SEED, None)

    if seed is None:
        logger.debug(f"Not seeding random (set {PYTHON_RANDOM_SEED}=random to override this)\n")
    elif seed == "random":
        seed = random.randrange(sys.maxsize)
    else:
        seed = int(seed)

    return seed


def init_random(seed=None, print_value=True):
    """

    :param seed:
    :param print_value:
    :return:
    """
    if seed is None:
        seed = _get_random_seed()

        if seed is None:
            # use system default random seed
            return

    if print_value:
        sys.stdout.write(f"random seed:\n{PYTHON_RANDOM_SEED}={seed}\n")

    random.seed(seed)

    try:
        import factory

        faker = factory.Faker._get_faker()
        faker.seed(seed)
    except ImportError:
        pass


def _get_test_result_failure_count(result: Union[TestResult, RemoteTestResult, None]):
    """
    Get the current number of test errors/failures from test result object

    TODO - this is a bit hacky, refactor to remove this?
    :param result:
    :return:
    """
    if result is None:
        return 0
    if isinstance(result, RemoteTestResult):
        event_count = Counter(e[0] for e in result.events)

        return event_count["addError"] + event_count["addFailure"]
    else:
        return len(result.errors) + len(result.failures)


class TestSeedRandomMixin:
    """
    Test mixin that re-seeds random generators at the start of each test and then prints out the seed on failure
    so that we can (in theory) reproduce test failures quickly.

    This mixin should be as close to the start of the mixin list as possible - especially before any random number generation

    TODO:
    * output the random seeds in a nicer way on failure (might require overriding test runner class(es) and / or TestResult class
      bear in mind that we're currently using 3 different test runners:
      * RemoteTestRunner when running with --parallel (eg in gitlab)
      * DiscoverRunner (django default) when running without --parallel
      * DjangoTeamcityTestRunner in PyCharm
    Maybe hold off on this until we decide if we're going to move to pytest-django (for junit compatibility with gitlab).
    """

    test_setup_random_seed = None
    test_setup_class_random_seed = None

    def shortDescription(self):
        description = super().shortDescription()
        return description

    def setUp(self):
        # if environment variable isn't set, don't do anything
        # if it is set it will have been used in app ready() with the initial value, so just re-randomise now
        env_name = PYTHON_TEST_RANDOM_SEED
        new_random_seed = None

        if os.environ.get(env_name, None):
            new_random_seed = int(os.environ.get(env_name, None))
            logger.debug(f"using {env_name}={new_random_seed}")
        elif os.environ.get(PYTHON_RANDOM_SEED, None):
            new_random_seed = random.randrange(sys.maxsize)

        if new_random_seed:
            # update random seed, but only print on failure
            self.test_setup_random_seed = new_random_seed
            init_random(new_random_seed, print_value=False)

        super().setUp()

    @classmethod
    def setUpClass(cls):
        env_name = PYTHON_TEST_CLASS_RANDOM_SEED
        new_random_seed = None

        if os.environ.get(env_name, None):
            new_random_seed = int(os.environ.get(env_name, None))
            logger.debug(f"using {env_name}={new_random_seed}")
        elif os.environ.get(PYTHON_RANDOM_SEED, None):
            new_random_seed = random.randrange(sys.maxsize)

        if new_random_seed:
            # update random seed, but only print on failure
            cls.test_setup_class_random_seed = new_random_seed
            init_random(new_random_seed, print_value=False)

        super().setUpClass()

    def get_seed_envs_str(self):
        return f"{PYTHON_TEST_RANDOM_SEED}={self.test_setup_random_seed} {PYTHON_TEST_CLASS_RANDOM_SEED}={self.test_setup_class_random_seed}"

    def shortDescription(self):
        """
        Note that this is use by the command line test runner, but not by Pycharm
        :return:
        """
        desc = super().shortDescription() or ""

        if desc:
            desc = f"{self.get_seed_envs_str()}\n{desc}"
        else:
            desc = self.get_seed_envs_str()

        return desc

    def run(self, result=None, *args, **kwargs):
        # slightly hacky way to detect if there were test failures and print them out
        orig_err_fail = _get_test_result_failure_count(result)

        result = super().run(result, *args, **kwargs)

        if orig_err_fail != _get_test_result_failure_count(result):
            # there were errors in this test

            if self.test_setup_random_seed or self.test_setup_class_random_seed:
                # note that we rely on this in PyCharm since shortDescription isn't used there
                sys.stdout.write(f"\ntest failure seeds:\n{self.get_seed_envs_str()}")

        return result
