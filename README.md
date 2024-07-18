# MY PROJECT

## 1 - TODO FIRST

1. Clone the template project where you want `git clone https://gitlab.par.quinten.io/albus/template_projet.git` (If you are on the Quinten AWS infra and you get an error with the previous URL you might need to use an other URL, in the previous URL replace https://gitlab.par.quinten.io/ part by  https://gitlab-datalab.quinten-saas.com/: `git clone https://gitlab-datalab.quinten-saas.com/albus/template_projet.git`)
2. Rename the project (template_projet) with the same project name as before (`mv template_projet <my_project>`)
3. Go into the project folder: `cd my_project`
4. Delete existing git tracking: `rm -rf .git`

## 2 - TODO GIT INIT

1. Init a new git tracking: `git init --initial-branch=main`
2. In gitlab interface, create a project (New project), choose 'Create blank project' and fill the blanks (Internal visibility level is OK, uncheck "
Initialize repository with a README". In "Pick a group or namespace" it's better to choose a group if you work with a team, if you work on your own project choose your pnom). Choose a project name (let's call it *my_project* here)
3. Add the remote you create in the first place (**at step 1**): `git remote add origin https://gitlab.par.quinten.io/....git` (please get the right url from the gitlab interface in the clone buton, if you are on AWS and you get an error with this url please use https://gitlab-datalab.quinten-saas.com/ instead:  `git remote add origin https://gitlab-datalab.quinten-saas.com/....git`)
4. Add all the files: `git add .` (you can check what you are about to add by running `git status` just before, which is recommended)
5. Commit the changes: `git commit -m "initial commit"`
6. Puhs (after reading warning): `git push origin master`. /!\Warning/!\: distant repository might have "main" branch instead of "master" (check on gitlab). If you want to have the same name locally rename you local "master" branch to "main" before pushing: `git branch -m master main`
7. You're done, congrats! Now follow the next todo

## 3 - TODO ADDITIONAL
1. Rename your source code folder with the name of your project (current is "src")
2. Add notebooks/* and logs/* to .gitignore file
3. If you do not use docker (e.g. in aws env), create a python environment for your project (see scoold: https://scoold.par.quinten.io/question/1247910884295053312/comment-cr%C3%A9er-un-environnement-virtuel-et-l-utiliser-dans-jupyter). You don't have to put this environment inside your project folder. If you do so your should add the folder to .gitignore file. Otherwise you can have this folder outside the project folder in a dedicated folder for instance.
4. Read FP1 as a baseline of how organizing your project [FP1](https://confluence.par.quinten.io/pages/viewpage.action?pageId=31601990)
5. Run `pip install --upgrade pip` then `pip install -r requirements`
6. You can run `python main.py` on terminal to see if you have "hello world" printed :)

## REMINDER OF GOOD PRACTICES FOR CODING
Albus coding framework is detailed here https://confluence.par.quinten.io/pages/viewpage.action?pageId=64686373 please read carefully.
On top of that (and some reminders ;)) you also need to pay attention on those items:
- **Use modular coding practice**: organise your code using modules, functions and class. Think your code in terms of pipeline "what's in what's out" 
- **Comment** your code and **document** all your functions : [FP here](https://confluence.par.quinten.io/display/ALBUS/FP+3.2+-+Commenter+et+documenter+son+code).
- **Unit test** your code the most or at least the most critical function [Ressources here](https://confluence.par.quinten.io/pages/viewpage.action?pageId=54331151#tab-Robustesse)
- Create **new branch** on git each time you develop **new feature** 
- Find a partner to **review your code**. Should be at least 2 hours (straight or 2*1h) a week on scheduled timeshifts [FP here](https://confluence.par.quinten.io/display/ALBUS/FP9+-+Code+Review)
- Follow the **google coding style** for harmonized practices at Quinten: https://google.github.io/styleguide/pyguide.html
- Use **black** (https://github.com/psf/black) to format your code automatically before commit: `black src`
- You should use **notebooks** for **exploratory analysis and testing part of your code only**. If you don't have other choice than using notebook for your project please remove notebooks folder from .gitignore file
- All your imports should start by the project source code folder's name:
```
from src.XXXX import XXXX
```
or
```
from src import XXXX
```
- Log your code: the main.py contains the logger. It can be used in any module by juste using logging api
```
import logging
logging.info("my log message")
```
- The organisation inside your source code folder (src) is not mandatory, feel free to reorganize differently. Pay attention to how intuitive the code is.
- Use this README to provide information on how to use your code for other users or developpers

## CAPITALISATION PRACTICES
Don't do the job twice! Quinten is making effort to capitalize the work done on each project in order to improve efficency on the next projects. 2 main tools are available for capitalisation of code:
- SCOOLD: https://scoold.par.quinten.io/ dedicated to on-the-flight capitalisation, it contains lot of snippets of code, answers regarding methodology questions and some domain specific Q&A. All this information is organised with tags. Please choose them carefully when you post a new question/answer
- NOTEBOOKS: https://gitlab.par.quinten.io/albus/capitalisation-notebook it gathers notebooks that explain a full pipeline dedicated to a specific task (Propensity score evaluation, how to use model interpretation tools shap and lime, benchmark of clustering)

See details of how to use those tools [here](https://confluence.par.quinten.io/display/ALBUS/Capitalisation) 

## USAGE OF THE OTHER FILES
- .gitlab-ci.yaml: TO BE COMPLETED
- requirements.txt : file that contains all the packages and their version used for the project

Dans le dossier cicd
- Dockerfile: TO BE COMPLETED
- .dockerignore: TO BE COMPLETED
- build.sh: TO BE COMPLETED
- push.sh: TO BE COMPLETED
- run_test.sh: TO BE COMPLETED
- release.sh: TO BE COMPLETED

## CODE DOCUMENTATION USING DOCSTRINGS
All detailed are provided here : https://confluence.par.quinten.io/display/ALBUS/FP+3.2+-+Commenter+et+documenter+son+code. If you want to generate code using Sphinx go to the last section of the Confluence page.
