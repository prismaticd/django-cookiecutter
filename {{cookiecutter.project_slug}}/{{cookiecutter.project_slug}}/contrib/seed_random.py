import os
import random
import sys
import logging


logger = logging.getLogger(__name__)


def _get_random_seed():
    seed = os.environ.get("PYTHON_RANDOM_SEED", None)

    if seed is None:
        logger.debug(f"Not seeding random (set PYTHON_RANDOM_SEED=random to override this)\n")
    elif seed == "random":
        seed = random.randrange(sys.maxsize)
    else:
        seed = int(seed)

    return seed


def init_random(seed=None):
    if seed is None:
        seed = _get_random_seed()

        if seed is None:
            # use system default random seed
            return

    sys.stdout.write(f"PYTHON_RANDOM_SEED={seed}\n")
    random.seed(seed)

    try:
        import factory

        faker = factory.Faker._get_faker()
        faker.seed(seed)
    except ImportError:
        pass
