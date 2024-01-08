# Python morning tasks
### To create tasks:

- clone this repo;
- run `python3 -m venv venv` and activate env;
- run `pip install -r requirements.txt`;
- create new branch, implement morning task inside `task_list` directory (there should be 6 files):
  - 3 files with task description on different languages (uk, ru, en). Let's just use EN for ru because we are going to remove ru at all;
  - 1 file with tests;
  - 1 file with reference solution;
  - 1 file with initial code that students see when they open task ;
  - files naming and structure you can check in the reference PR.
- run `black <morning_task_folder>` and `flake8 <morning_task_folder>`;
- check that your reference solution passes your tests;
- make commit, push and create a PR;
- request review from [Ivan](https://github.com/IvanRamyk) and [Alex](https://github.com/Abnormaltype).


**Important**: If the task initially is created for the class on leetcode or codewars, but it could be simplified as a function, please, simplify it.

Reference PR: https://github.com/mate-academy/python_morning_tasks/pull/1
