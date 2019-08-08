## Script name: 
automation_tests_task

### Description:
Given an (*)input file path the script runs tests scenarios and compares the actual results with the expected results. the output of the script is two files,one is a file containing a list of usernames in which the actual results and the expected results were mismatched. and the other is the output of the tests scenarios.

### usage: 
Open the terminal and go to the script's directory.
Type: python automation_tests_task.py <Input_File_Path>
![Capture](https://user-images.githubusercontent.com/45976127/62697926-86fe3700-b9e4-11e9-9c44-b88e7a1db63f.PNG)

The script creates new text files with the names test_result and failed_usernames with the current timestamp whith the content described above and prints to the terminal the path of each file.
![Capture2](https://user-images.githubusercontent.com/45976127/62698924-fb39da00-b9e6-11e9-9908-2b3932087daf.PNG)

Note: Running the script several times in the same minute will result appending the new test results of the tests to the same files.
      If you want to change it all you need to do is to switch the comments marks between two lines like the pic here.
      ![Capture3](https://user-images.githubusercontent.com/45976127/62701098-1e1abd00-b9ec-11e9-84bd-bae06ac7ab37.PNG)

(*)input file: Is a txt file in which each line in the file is a test_scenario json.
![Capture4](https://user-images.githubusercontent.com/45976127/62701324-b2851f80-b9ec-11e9-85ec-1593ded766f6.PNG)
