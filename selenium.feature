Feature: OrangeHRM Demo https://opensource-demo.orangehrmlive.com/
    
    Scenario: login into OrangeHRM
        Given we have username 'Admin' 
            And password 'admin123'
        When we put username into username field
            And we put password into password field
            And we click login button
        Then we must be successfuly logged in

    Scenario: going to Admin section
        Given we are logged in sucessfully
        When we click on 'Admin' section in navbar
        Then Admin page is opened

    Scenario: opening dropdown menu
        Given we are on Admin page
        When we hover on 'Job'
        Then dropdown menu must be shown

    Scenario: going to 'Job Titles'
        Given we have 'Job' dropdown menu opened
        When we click 'Job Titles' button
        Then 'Job Titles' section is displayed

    Scenario: adding new job
        Given we are at 'Job Titles' page
        When we click 'Add' button in 'Job Titles' section
            And put 'Job' in 'Job Titles' field
            And put 'Job Description' in 'Job Description' field
            And put 'Note' in 'Note' field
            And click 'Save' button
        Then section 'Job Titles' must be displayed

    Scenario:  edit the added
        Given we are at 'Job Titles' page
        When we click  name introduced by job in 'Job Titles' section
            And clear in 'Job Titles' field
            And put 'Job' in 'Job Titles' field
            And clear in 'Job Description' field
            And put 'Job Description' in 'Job Description' field
            And click 'Save' button
        Then section 'Job Titles' must be displayed

        Scenario: delete this job
        Given we are at 'Job Titles' page
        When we click  in button near our name introduced by job in 'Job Titles' section
            And click 'Delete' button
            And click 'Ok' button
        Then section 'Job Titles' must be displayed without our job