import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='coding-help',  
     version='0.1',
     scripts=['dokr'] ,
     author="Jashanpreet Singh",
     author_email="Jashanpreetsingh2502@gmail.com",
     description="A package to help for learnng coding.",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/turing-20/coding-help",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )