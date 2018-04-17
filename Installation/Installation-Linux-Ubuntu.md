There are some packages that you need to install on your system (macOS) before you come to DSW AI Camp by Nodeflux. 

# Anaconda Installation on Ubuntu
```
apt-get update
sudo apt-get install wget git
sudo apt-get install libgl1-mesa-glx
```

## Download Anaconda
```
wget https://repo.continuum.io/archive/Anaconda3-5.1.0-Linux-x86_64.sh
```

## Run the installer
```
sh Anaconda2-5.1.0-Linux-x86_64.sh
```
When the installer is running, there are some prompts you must filling with "yes" or "enter" option.
```
Do you accept the license terms? [yes|no]
 [no] >>>
 Please answer 'yes' or 'no':'
 >>> yes

Anaconda3 will now be installed into this location:
 /root/anaconda3

- Press ENTER to confirm the location
 - Press CTRL-C to abort the installation
 - Or specify a different location below

[/root/anaconda3] >>> **/usr/local/anaconda/**
 **PREFIX=/usr/local/anaconda**

Do you wish the installer to prepend the Anaconda3 install location
to PATH in your /root/.bashrc ? [yes|no]
[no] >>> yes

Appending source /root/anaconda3/bin/activate to /root/.bashrc
A backup will be made to: /root/.bashrc-anaconda3.bak

For this change to become active, you have to open a new terminal.

Thank you for installing Anaconda3!
```
## Testing Installation
After finished the installation you can activate it and check Anaconda correctly installed or not.
```
source ~/.bashrc
conda list
```

## Create a Conda virtual environment
Assuming Conda is working, we will now create our Conda environment:
```
conda create -n dsw-nodeflux python=3.6
```

This bootstraps a new Conda environment named `dsw-nodeflux` with a minimal Python 3.6 install. You will be presented with a 'package plan' listing the packages to be installed and asked whether to proceed: type `y` then enter.

We will now *activate* our created environment:

```
source activate dsw-nodeflux
```

If you wish to deactivate an environment loaded in the current terminal e.g. to launch the system Python interpreter, you can run `source deactivate` 

## Install Python Depedencies
We will now install the dependencies for the course into the new environment:
```
conda install numpy scipy matplotlib jupyter git
conda install -c conda-forge opencv
conda install tensorflow=1.4.1
```

Once the installation is finished, to recover some disk space we can clear the package tarballs Conda just downloaded:
```
conda clean -t
```

## Run Jupyter Notebook
Start up a Jupyter notebook server by typing this on your terminal
```
jupyter notebook
```

## Notes
If you have some trouble about the installation you can email me indra@nodeflux.io.

