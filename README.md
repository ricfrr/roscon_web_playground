
== Testing ==

=== Prerequisites ===

You will need docker installed and ghrocker.

A simple installation instructions are below. The setup of the **ghrocker venv must happen outside of the source-code directory** (e.g /home/code/ghrocker_venv must be outside /home/code/rosconxx20xx-website).

# First installation

    mkdir -p ghrocker_venv
    python3 -m venv ghrocker_venv
	source ./ghrocker_venv/bin/activate
    pip install git+https://github.com/tfoote/ghrocker.git

# Subsequent Uploads

	python3 -m venv ghrocker_venv
	source ./ghrocker_venv/bin/activate


Test locally (with the above venv activated in your shell). Sudo is no longer required to run the commands and will cause an error. 

To test the site clone this repo and then run `./test_site.bash`

And you can then find the site at http://localhost:4000



== Sponsors ==

Sponsor generation [spreadsheet can be found here.](https://docs.google.com/spreadsheets/d/15NhZjUI070CwXKXg3gLkS6yGgDoTMH_Z6cOxDxEj9Y4/edit?usp=sharing)
