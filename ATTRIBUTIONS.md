# Attributions
The successful development of the automated testing engine would not have been possible without the help from these online documentation, resources and papers.


## Online Documentation and Resources
We referenced these online documentation and resources to build the automated testing engine.

1. [Python AST Documentation](https://docs.python.org/3/library/ast.html) to view the different available node types and their attributes in order to build our modifiers in `modifier.py`.

2. [OpenAI Chat Completions API](https://platform.openai.com/docs/guides/text-generation/chat-completions-api) to learn how to make API requests to OpenAI in `openai_program_generator.py`.

3. [OpenAI Forum Post](https://community.openai.com/t/setting-request-timeout-in-openai-v1-2-2/492772) to help us in implementing a request timeout if the OpenAI model takes too long to respond, in `openai_program_generator.py`.

4. [Python requests Documentation](https://requests.readthedocs.io/en/latest/) to implement API calls to the ITS API, in `its_api_connection.py`.

5. [PynGuin Documentation](https://pynguin.readthedocs.io/en/latest/user/intro.html) to create `PynGuinArgumentGenerator` for greater branch coverage during argument generation.

6. [LeetCode Dataset by Eric Hartford and RobyBerty](https://www.kaggle.com/datasets/erichartford/leetcode-solutions) for the Kaggle dataset [`leetcode-solutions.jsonl`](datasets/leetcode-solutions.jsonl) used in `LeetCodeProgramGenerator`. The license for the dataset is [GNU Lesser General Public License](https://www.gnu.org/licenses/lgpl-3.0.html).

7. [StackOverflow Post](https://stackoverflow.com/questions/374626/how-can-i-find-all-the-subsets-of-a-set-with-exactly-n-elements) for learning how to find a powerset, used in `powerset()` of `utils.py`.

8. ChatGPT to help in improving and debugging methods
- For @eugenetangkj, ChatGPT was mainly used for the modifiers he implemented (MR03 - MR13) in `modifiers.py`. Eugene used it to help generate simple test cases to test against his modifiers. Also, he used it to get an overview of how to implement the more difficult modifiers. For example, in the `ReverseListModifier`, he used ChatGPT to learn how to track lists that have been visited. Then, he combined it with his own code (with help from the Python AST documentation) that transforms list subscripts, so only subscripts of visited lists get modified.


## Papers
We read through these papers to gain an understanding of metamorphic testing and about test case generation.

Chen, T. Y., Cheung, S. C., & Yiu, S. M. (1998). Metamorphic Testing: A New Approach for Generating Next Test Cases [Department of Computer Science, The Hong Kong University of Science and Technology]. https://arxiv.org/ftp/arxiv/papers/2002/2002.12543.pdf

Lukasczyk, S., Kroiß, F., & Fraser, G. (2023). An empirical study of automated unit test generation for Python. Empirical Software Engineering, 28(2), 36. https://doi.org/10.1007/s10664-022-10248-w
