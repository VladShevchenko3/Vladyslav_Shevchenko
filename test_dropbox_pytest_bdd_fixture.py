import requests
from pytest_bdd import scenario, given, when, then
import pytest
import os
from main import Dropbox


@given(u'file named "file.txt"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given file named "file.txt"')


@when(u'we upload file "file.txt" to Dropbox')
def step_impl(context):
    raise NotImplementedError(u'STEP: When we upload file "file.txt" to Dropbox')


@then(u'we see file "file.txt" uploaded')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then we see file "file.txt" uploaded')


@given(u'file named "test.txt"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given file named "test.txt"')


@when(u'we upload file "test.txt" to Dropbox')
def step_impl(context):
    raise NotImplementedError(u'STEP: When we upload file "test.txt" to Dropbox')


@then(u'we see file "test.txt" uploaded')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then we see file "test.txt" uploaded')


@given(u'file named "file.txt" is uploaded')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given file named "file.txt" is uploaded')


@when(u'we request metadata of file "file.txt" by id')
def step_impl(context):
    raise NotImplementedError(u'STEP: When we request metadata of file "file.txt" by id')


@then(u'we receive metadata for file "file.txt"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then we receive metadata for file "file.txt"')


@given(u'file named "test.txt" is uploaded')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given file named "test.txt" is uploaded')


@when(u'we request metadata of file "test.txt" by id')
def step_impl(context):
    raise NotImplementedError(u'STEP: When we request metadata of file "test.txt" by id')


@then(u'we receive metadata for file "test.txt"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then we receive metadata for file "test.txt"')


@given(u'we have absolute file path after file "file.txt" was downloaded')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given we have absolute file path after file "file.txt" was downloaded')


@when(u'we request to delete file "file.txt"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When we request to delete file "file.txt"')


@then(u'we see file "file.txt" deleted')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then we see file "file.txt" deleted')


@given(u'we have absolute file path after file "test.txt" was downloaded')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given we have absolute file path after file "test.txt" was downloaded')


@when(u'we request to delete file "test.txt"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When we request to delete file "test.txt"')


@then(u'we see file "test.txt" deleted')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then we see file "test.txt" deleted')
