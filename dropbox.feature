
Feature: Dropbox test


    Scenario: Upload file
        Given  file named "HomeWork1.txt"
        When we upload file "HomeWork1.txt" to Dropbox
        Then we see file "HomeWork1.txt" uploaded

    Scenario: Get file metadata
        Given file named "HomeWork1.txt" is uploaded
        When we request metadata of file "HomeWork1.txt" by id
        Then we receive metadata for file "HomeWork1.txt"

    Scenario: Delete file
        Given we have absolute file path after file "HomeWork1.txt" was downloaded
        When we request to delete file "HomeWork1.txt"
        Then we see file "HomeWork1.txt" deleted