from main import Dropbox
# перед виконанням треба змінювати id

def test_uploadFile():
    d = Dropbox()
    f_uploadFile = d.uploadFile()
    assert f_uploadFile == '{"name": "HomeWork1.txt", "path_lower": "/homework1.txt", "path_display": "/HomeWork1.txt", "id": "id:xvaeYKUoixkAAAAAAAAAGg", "client_modified": "2021-12-16T15:37:19Z", "server_modified": "2021-12-16T15:37:19Z", "rev": "5d34532a680478bb562e1", "size": 5, "is_downloadable": true, "content_hash": "08a610475666366a9b56ea29e3389bf01c4412499292d66a8d93e0ccaa691fbd"}'

def test_get_metadata():
    d = Dropbox()
    f_get_metadata = d.get_metadata()
    assert f_get_metadata == '{".tag": "file", "name": "HomeWork1.txt", "path_lower": "/homework1.txt", "path_display": "/HomeWork1.txt", "id": "id:xvaeYKUoixkAAAAAAAAAGg", "client_modified": "2021-12-16T15:37:19Z", "server_modified": "2021-12-16T15:37:19Z", "rev": "5d34532a680478bb562e1", "size": 5, "is_downloadable": true, "content_hash": "08a610475666366a9b56ea29e3389bf01c4412499292d66a8d93e0ccaa691fbd"}'
def test_deleteFile():
    d = Dropbox()
    f_delet = d.deleteFile()
    assert f_delet == '{"metadata": {".tag": "file", "name": "HomeWork1.txt", "path_lower": "/homework1.txt", "path_display": "/HomeWork1.txt", "id": "id:xvaeYKUoixkAAAAAAAAAGg", "client_modified": "2021-12-16T15:35:08Z", "server_modified": "2021-12-16T15:35:08Z", "rev": "5d3452ad9c82c8bb562e1", "size": 5, "is_downloadable": true, "content_hash": "08a610475666366a9b56ea29e3389bf01c4412499292d66a8d93e0ccaa691fbd"}}'




test_uploadFile()
test_get_metadata()
#test_deleteFile()