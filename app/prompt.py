"""This module contains the function to get the prompt from a file."""


def get_prompt(
    file_path: str = 'prompt.txt'
) -> str:
    """
    Read the prompt from a file and return it. If the file is not found,
    return a default prompt.

    :param file_path: The path to the prompt file.
    :type file_path: str    found.
    :type default_prompt: str
    :return: The prompt text.
    :rtype: str
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read().strip()
    except FileNotFoundError:
        return "You are a helpful assistant, always respond in Russian."
    except Exception as e:
        raise Exception(
            f"An error occurred while reading the prompt file: {e}"
        )
