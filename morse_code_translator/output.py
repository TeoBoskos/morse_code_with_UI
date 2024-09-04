def output_fun(available_characters: str, dictionary: dict, output_str: str, entry_str: str, output_value: str) -> None:
  """
  The purpose of this function is twofold. First, it loops
  through each character in the `user_input` and checks if
  it exists in the string `available_characters`. If false,
  it throws an error and breaks out of the loop.

  If true however, it moves on to the second phase. It
  translates each character of the `user_input` and gives it
  its corresponding value in the `dictionary`, after of
  course converting it to uppercase.

  It asigns each new character to the variable `output_str`
  which is set as the value of `output_value`.

  Parameters: `available_characters`, the string with the
    available characters.
    `dictionary`, a morse code dictionary.
    `output_str`, the string with the text translated to morse
    code.
    `entry_str`, the string contraining the text in
    the `input_entry`.
    `output_value`, the final result of
    the translation.

  Returns: None
  """

  user_input = entry_str.get()
  print(user_input)

  for char in user_input:
    if not char.upper() in available_characters:
      output_str = "ERROR: CHARACTER '{}' IS NOT AVAILABLE!!!".format(char)
      output_value.set(output_str)
      print("ERROR: CHARACTER '{}' IS NOT AVAILABLE!!!".format(char))
      break
    else:
      morse_code = dictionary[char.upper()]
      output_str += morse_code

  output_value.set(output_str)

  print(output_str)