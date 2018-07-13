{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## script to be run from terminal to validate env setup \n",
    "\n",
    "import sys\n",
    "import os\n",
    "from distutils.version import LooseVersion\n",
    "\n",
    "if sys.version_info.major < 3:\n",
    "    print('[!] You are running an old version of Python. '\n",
    "          'This tutorial requires Python 3.')\n",
    "\n",
    "    sys.exit(1)\n",
    "\n",
    "with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:\n",
    "    reqs = f.readlines()\n",
    "\n",
    "reqs = [(pkg, ver) for (pkg, _, ver) in\n",
    "        (req.split() for req in reqs if req.strip())]\n",
    "\n",
    "pkg_names = {\n",
    "    'scikit-image': 'skimage',\n",
    "    'scikit-learn': 'sklearn'\n",
    "}\n",
    "\n",
    "for (pkg, version_wanted) in reqs:\n",
    "    module_name = pkg_names.get(pkg, pkg)\n",
    "    try:\n",
    "        m = __import__(module_name)\n",
    "        status = '✓'\n",
    "    except ImportError as e:\n",
    "        m = None\n",
    "        if (pkg != 'numpy' and 'numpy' in str(e)):\n",
    "            status = '?'\n",
    "            version_installed = 'Needs NumPy'\n",
    "        else:\n",
    "            version_installed = 'Not installed'\n",
    "            status = 'X'\n",
    "\n",
    "    if m is not None:\n",
    "        version_installed = m.__version__\n",
    "        if LooseVersion(version_wanted) > LooseVersion(version_installed):\n",
    "            status = 'X'\n",
    "    print('[{}] {:<11} {}'.format(\n",
    "        status, pkg.ljust(13), version_installed)\n",
    "        )"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
