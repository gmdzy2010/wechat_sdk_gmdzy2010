import setuptools


with open("README.md", "r", encoding="UTF-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wechat_sdk_gmdzy2010",
    version="0.3.2",
    author="gmdzy2010",
    author_email="gmdzy2010@126.com",
    description="The non-official sdk of wechat",
    license='MIT License',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='wechat',
    url="https://github.com/gmdzy2010/wechat_sdk_gmdzy2010",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
