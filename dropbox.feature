Feature: Dropbox test
    Scenario Outline: Upload file
        Given file named "<file>"
        When we upload file "<file>" to Dropbox
        Then we see file "<file>" uploaded
        Examples:
        |              HomeWork1.txt |
        |              home.txt      |

    Scenario Outline: Get file metadata by id
        Given file named "<file>" is uploaded
        When we request metadata of file "<file>" by id
        Then we receive metadata for file "<file>"
        Examples:
        |              HomeWork1.txt |
        |              home.txt      |

    Scenario Outline: Delete file
        Given we have absolute file path after file "<file>" was downloaded
        When we request to delete file "<file>"
        Then we see file "<file>" deleted
        Examples:
        |              HomeWork1.txt |
        |              home.txt      |

