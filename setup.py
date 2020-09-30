from setuptools import setup, find_packages
import pathlib

#here = pathlib.Path(__file__).parent.resolve()
#long_description = (here / 'README.md').read_text(encoding='utf-8')


setup(
    name='renderjson',  # Required
    version='0.2.0',  # Required
    description='Rendering JSON within IPython Notebook',  # Optional
#    long_description=long_description,  # Optional
#    long_description_content_type='text/markdown',  # Optional (see note above)

    url='https://github.com/zvasicek/renderjson',  # Optional

    # When your source code is in a subdirectory under the project root, e.g.
    # `src/`, it is necessary to specify the `package_dir` argument.
    package_dir={'renderjson': 'renderjson'},  # Optional
    packages=['renderjson'],  # Required
    python_requires='>=3.5',

    # This field lists other packages that your project depends on to run.
    # Any package you put here will be installed by pip when your project is
    # installed, so they must be valid existing projects.
    #
    # For an analysis of "install_requires" vs pip's requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['ipython'],  # Optional

)
