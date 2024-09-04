def clear_fun(entry_str: str, output_value: str) -> None:
  """
  The purpose of this function is to clear the `input_entry`
  and the `output_label` of any text. It does this by setting
  the `entry_str` and the `output_value` StringVar variables
  to the value of `""`.

  Parameters: `entry_str`, the StringVar of the `input_entry`.
    `output_value`, the StringVar of the `output_label`.

  Returns: None
  """

  output_value.set("")
  entry_str.set("")