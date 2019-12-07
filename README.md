Roomm8
--
This app is to manage and formalize roommates interactions. 

Progress
--
[Scrum Board](https://trello.com/b/FaETswJe/roomm8)

Build Status
--
[![Build Status](https://travis-ci.org/Willievuong/roomm8.svg?branch=master)](https://travis-ci.org/Willievuong/roomm8)

Installation Guide
--
Client
1. `cd client/`
2. `npm run install`

Backend Server 
1. `cd backend/`
2. `mkdir env` 
3. `py -m venv env`
4. `source env/bin/activate`
5. `pip install -r requirements.txt`
6. `py manage.py migrate`
7. `cd backend/scripts/`
8. `py seed.py`

Run Guide
--
Client
1. `cd client/` 
2. `npm run`

Server
1. `cd backend/`
2. `py manage runserver`

Built with
--
FrontEnd - React.js and Material UI 
BackEnd - Flask and Postgresql

Credits
-- 
Created with [create-react-app](https://github.com/facebookincubator/create-react-app/blob/master/packages/react-scripts/template/README.md)