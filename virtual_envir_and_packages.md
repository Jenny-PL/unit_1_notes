# Using virtual environments
1. Making:
     - **python3 -m venv venv**
3. Activating:
   -  $ **source venv/bin/activate**
   - We know we are in the virtual environment(venv) because the command line changes:   
  <mark>(venv) $ project-root-folder </mark>
3. Install packages in the virtual enir:
   - **pip install -r requirements.txt**  
   - pip install <package_name> 
4. Deactivating
   - . $ **deactivate**
   - Command line will change back:   
   - <mark>$ project-root-folder</mark>  
---
# Packages 
- a package is a collection of Python modules (ie- pytest, etc)
- Module:  every .py file is a module
- Managing a package: important, to avoid breaking our code!
- pip: packaging installer for python; can use it (in terminal) to install any package in PyPI.
  - We will use <mark> pip3 </mark> to install packages to work with python3.
- PyPI: Python Packaging Index
- To list all packages on the computer: **pip3 list**

### Important concept: installing in virtual environments vs. global 
- requirements.txt will specify the packages and versions required to work collaberatively on a project.
- You can download these packages to a virtual environment so that everyone is working with the same versions/materials.
  - You will have a new virtual environment for new projects
- If a virtual environment is made w/Python3, when we're inside this activated environment, we can use **python3** or **python** as commands to mean Python3.
