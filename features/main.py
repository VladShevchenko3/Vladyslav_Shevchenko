import requests
import json



class Dropbox():
  authorization = 'abpC2vAY80YAAAAAAAAAAVdz1vaVRAopnIWT5hnPkh7e1CkWe0PDmlOLiWvM3VHU'
  method = "POST"


class UploadRequest(Dropbox):

  def __init__(self) -> None:
    self.parameters= {
      'url': "https://content.dropboxapi.com/2/files/upload",
      'headers': {
        'Dropbox-API-Arg': '{"path": "/HomeWork1.txt","mode": "add","autorename": true,"mute": false,"strict_conflict": false}',
        'Content-Type': 'application/octet-stream',
        'Authorization': self.authorization
      }
    }

  def get_response(self):
    self.response = requests.request(
      method=self.method,
      url=self.parameters['url'],
      headers=self.parameters['headers'],
      data='This is test message for a new file'
    )
    self.id = json.loads(self.response.text)['id']


class GetFileMetadataRequest(Dropbox):

  def __init__(self) -> None:
    self.parameters = {
      'url': "https://api.dropboxapi.com/2/sharing/get_file_metadata",
      'headers': {
        'Content-Type': 'application/json',
        'Authorization': self.authorization
      }
    }

  def get_response(self, id):
    self.response = requests.request(
      method=self.method,
      url=self.parameters['url'],
      headers=self.parameters['headers'],
      data=json.dumps(
        {
          "file": f"{id}",
          "actions": []
        }
      )
    )
    self.file_path = json.loads(self.response.text)['path_display']


class DeleteRequest(Dropbox):
  def __init__(self) -> None:
    self.parameters = {
      'url': "https://api.dropboxapi.com/2/files/delete_v2",
      'headers': {
        'Content-Type': 'application/json',
        'Authorization': self.authorization
      }
    }

  def get_response(self, file_path):
    self.response = requests.request(
      method=self.method,
      url=self.parameters['url'],
      headers=self.parameters['headers'],
      data=json.dumps(
        {
          "path": f"{file_path}"
        }
      )
    )
