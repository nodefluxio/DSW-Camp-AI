There are some packages that you need to install on your system (macOS) before you come to DSW AI Camp by Nodeflux. 

# Anaconda Installation on MacOS
## Download Anaconda
You can download the package installer of Anaconda for macOS at the following [link](https://www.anaconda.com/download/#macos).
Get the Python 3.6 version, and go through the GUI Installation wizard with all the default option, except:
- Skip the Microsoft VScode installation

## Testing Installation
Typically, the installation will place your Anaconda at `/Applications/anaconda/` and the installer will automatically append the binaries directory to `PATH`.

Test the installation to make sure that Anaconda is installed correctly by typing the following in your terminal:
```
conda --h
```
You should see the Conda help page displayed. The output would look something like this:
```
usage: conda [-h] [-V] command ...

conda is a tool for managing and deploying applications, environments and packages.

...
```
If you get a `No command 'conda' found` error you should check you have set up your `PATH` variable correctly (you can get a demonstrator to help you do this).

## Install Python Depedencies
We will now install the dependencies for the course into the new environment:
```
conda install numpy scipy matplotlib jupyter git
conda install -c conda-forge opencv
conda install tensorflow=1.4.0
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
If you have some trouble about the installation you can email me richard@nodeflux.io.

