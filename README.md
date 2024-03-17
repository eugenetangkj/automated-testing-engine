## Automated Testing Engine
### Project Overview
The _Intelligent Tutoring System_ (ITS) provides automated feedback and grading suggestions for programming assignments. As the architecture and functionality of the ITS expand, there is a need to ensure that the growing code base is maintained at high quality.

Therefore, our team has developed an automated testing engine that aims to identify existing bugs in the [ITS API](https://its.comp.nus.edu.sg/docs#/). Our solution revolves around **metamorphic testing**, where we develop metamorphic relations to identify variants of successful test cases that are potentially bug-inducing in the context of the ITS.


### Project Setup
1. Ensure that you have Python installed. Otherwise, you can download it [here](https://www.python.org/downloads/).
2. Download the packages mentioned in [`requirements.txt`](requirements.txt) using `pip install`.
3. Clone the repository to a folder of your liking.
```
git clone https://github.com/cs3213-fse-2024/automated-testing-engine-group-18.git
```
4. In the root folder, create a `.env` file. In the `.env` file, insert the following line, replacing it with your own OpenAI secret key.
```
CS3213_OPENAI_API_KEY="<OPENAI_SECRET_KEY>"
```
5. Head to `TestEngine.py` and run the program.
6. After the program finishes running, the output of the test cases can be found in the [`results`](results) folder. 