# Installation Anaconda on Ubuntu

There are some phase installation that required before join DSW AI Camp by Nodeflux. 
```sh
# apt-get update
# sudo apt-get install wget git
# sudo apt-get install libgl1-mesa-glx
```

## Download Installer
```sh
# wget https://repo.continuum.io/archive/Anaconda3-5.1.0-Linux-x86_64.sh
```

## Run the installer
```sh
# sh Anaconda2-5.1.0-Linux-x86_64.sh
```
When the installer is running, there are some prompt you must fill with "yes" or "enter" option.
```sh
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
```sh
# source ~/.bashrc
# conda list
```

## Install Python Depedencies
Then install some depedencies for this camp.
```sh
# conda install -c conda-forge opencv
# conda install tensorflow=1.4.1
```

## Testing Jupyter Notebook
After all you can checking the installation with running Jupyter Python Notebook.
```sh
# jupyter notebook
```

## Finally
If you have some trouble about the installation you can email me indra@nodeflux.io.

