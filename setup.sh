# remove old versions of the library
if pip list --format columns | grep Pyoptclass;
then
	pip uninstall -y pyoptclass
else 
	echo "No previous installation found";
fi
rm -rf pyoptclass/Pyoptclass.egg-info
rm pyoptclass/pyoptclass/__init__.pyc

#install the library
cd pyoptclass
pip2 install -e .