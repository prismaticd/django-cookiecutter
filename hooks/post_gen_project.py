from pathlib import Path
import shutil

install_allauth = "{{ cookiecutter.install_allauth }}" == "y"
install_behave_test = "{{ cookiecutter.install_behave_test }}" == "y"

base_dir = Path()
project_dir = Path(base_dir, "{{ cookiecutter.project_slug }}")
apps_dir = Path(project_dir, "apps")
project_static_src_dir = Path(project_dir, "static_src")
project_sass_dir = Path(project_static_src_dir, "sass")


# cookiecutter doesn't support conditional creation of files,
# so instead we delete the ones we don't want


def delete(path):
    if path.is_dir():
        shutil.rmtree(path)
    else:
        path.unlink()


if not install_allauth:
    for path in [Path(apps_dir, "myauth"), Path(apps_dir, "profile"), Path(project_sass_dir, "my_auth.scss")]:
        delete(path)

if not install_allauth or not install_behave_test:
    for path in [Path(base_dir, "features")]:
        delete(path)
