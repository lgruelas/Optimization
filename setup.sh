if pip list --format columns | grep Pyoptclass;
then
	pip uninstall Pyoptclass;
else 
	echo "Instalation not found."
fi


rm -rf pyoptclass/Pyoptclass.egg-info
rm pyoptclass/pyoptclass/__init__.pyc

#install the library
cd pyoptclass
pip2 install -e .