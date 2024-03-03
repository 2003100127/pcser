from setuptools import setup, find_packages

setup(
    name="pcser",
    version="0.0.1",
    keywords=["conda", "pcser"],
    description="Protein corona stealth effect prediction",
    long_description="Protein Corona Stealth Effect pRediction (PCSER)",
    license="GPL-3.0",

    url="https://github.com/2003100127",
    author="Jianfeng Sun",
    author_email="jianfeng.sun@ndorms.ox.ac.uk",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    python_requires='>3.9',
    install_requires=[
        'pandas',
        'numpy',
        'click',
        'matplotlib',
        'seaborn',
        'scikit-learn',
        'shap',
        'llvmlite==0.40.1',
        # 'pyfiglet', # ==0.8.post1
    ],
    # entry_points={
    #     'console_scripts': [
    #         'pcser=pcser.main:main',
    #     ],
    # }
)