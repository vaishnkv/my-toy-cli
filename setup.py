from setuptools import setup,find_packages

setup(
    name='toycli',
    version='0.1',
    packages=find_packages(),
    py_modules=['main'],  # Replace 'your_script' with your Python filename without the '.py' extension
    
    install_requires=[
        'Click',
    ],
    entry_points= {'console_scripts': [
            'toycli=main:toycli',  # Entry point function in main.py
        ],
    }
)
