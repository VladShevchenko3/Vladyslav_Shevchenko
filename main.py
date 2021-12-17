import requests
import json
import pytest


class Dropbox:

  def __init__(self):
    self.key = 'abpC2vAY80YAAAAAAAAAAVdz1vaVRAopnIWT5hnPkh7e1CkWe0PDmlOLiWvM3VHU'

  def uploadFile(self):
    self.url = "https://content.dropboxapi.com/2/files/upload"
    self.payload = "text1"
    self.headers = {
    'Dropbox-API-Arg': '{"path": "/HomeWork1.txt","mode": "add","autorename": true,"mute": false,"strict_conflict": false}',
    'Content-Type': 'application/octet-stream',
    'Authorization': 'Bearer abpC2vAY80YAAAAAAAAAAVdz1vaVRAopnIWT5hnPkh7e1CkWe0PDmlOLiWvM3VHU'
}
    self.response = requests.request("POST", self.url, headers=self.headers, data=self.payload)
    return self.response

  def get_metadata(self):
    self.url = "https://api.dropboxapi.com/2/files/get_metadata"

    self.payload = json.dumps({
      "path": "/Homework1.txt",
      "include_media_info": False,
      "include_deleted": False,
      "include_has_explicit_shared_members": False
    })
    self.headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer abpC2vAY80YAAAAAAAAAAVdz1vaVRAopnIWT5hnPkh7e1CkWe0PDmlOLiWvM3VHU'
    }

    self.response1 = requests.request("POST", self.url, headers=self.headers, data=self.payload)

    return self.response1

  def deleteFile(self):
    self.url = "https://api.dropboxapi.com/2/files/delete_v2"
    self.payload = json.dumps({
      "path": "/HomeWork1.txt"
    })
    self.headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer abpC2vAY80YAAAAAAAAAAVdz1vaVRAopnIWT5hnPkh7e1CkWe0PDmlOLiWvM3VHU'
    }
    self.response1 = requests.request("POST", self.url, headers=self.headers, data=self.payload)
    return self.response1



