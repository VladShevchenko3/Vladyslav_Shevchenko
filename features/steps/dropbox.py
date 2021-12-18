from behave import *
from features.main import *
import os


uploadRequest = UploadRequest()
metadataRequest = GetFileMetadataRequest()
deleteRequest = DeleteRequest()


@given(u'file named "HomeWork1.txt"')
def step_impl(context):
    assert os.path.isfile('./sample_files/file.txt')==True


@when(u'we upload file "HomeWork1.txt" to Dropbox')
def step_impl(context):
    uploadRequest.get_response()


@then(u'we see file "HomeWork1.txt" uploaded')
def step_impl(context):
    assert uploadRequest.response.status_code == 200


@given(u'file named "HomeWork1.txt" is uploaded')
def step_impl(context):
    assert uploadRequest.response.status_code == 200


@when(u'we request metadata of file "HomeWork1.txt" by id')
def step_impl(context):
    metadataRequest.get_response(uploadRequest.id)


@then(u'we receive metadata for file "HomeWork1.txt"')
def step_impl(context):
    assert metadataRequest.response.status_code == 200


@given(u'we have absolute file path after file "HomeWork1.txt" was downloaded')
def step_impl(context):
    assert metadataRequest.file_path != None


@when(u'we request to delete file "HomeWork1.txt"')
def step_impl(context):
    deleteRequest.get_response(metadataRequest.file_path)


@then(u'we see file "HomeWork1.txt" deleted')
def step_impl(context):
    assert deleteRequest.response.status_code == 200
