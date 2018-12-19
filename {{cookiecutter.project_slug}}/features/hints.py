from behave_django.environment import PatchedContext
from behave_django.testcase import BehaviorDrivenTestCase


class BehaveContext(PatchedContext):
    test: BehaviorDrivenTestCase
