def insert(arr, S, N, K,LB):
  """Replaces the value at index K and decrements the previous value (if applicable).

  Args:
      arr: The array to modify.
      S: The size of the array.
      N: The current number of elements in the array.
      K: The index where replacement and decrement occur.

  Returns:
      A tuple containing:
          - The modified array (same as the input array).
          - A boolean flag indicating success (True) or failure (False).
          - An error message (optional) if failure occurs.
  """

  if N >= S:
      return arr, False, "Array is full!"
  if K < 0 or K > N:
      raise IndexError("Invalid index! Please enter a value between {} and {}".format(LB, N - 1))

  # Generate different values for each insertion
  new_value = 10 * (K + 1)  # Example value generation

  # Replace value at K and decrement previous value (if K is not the first element)
  if K > 0:
      arr[K] = new_value
      arr[K-1] -= 1  # Decrement the previous element's value
  else:
      arr[K] = new_value  # Handle first element case (no decrement)

  return arr, True, None

def main():
  """Main function to handle user interaction, array operations, and output."""

  while True:
      try:
          S = int(input("Enter the size of the array: "))
          LB = int(input("Enter the lower bound of the array: "))
          arr = [None] * S  # Initialize array with None values
          N = 0  # Number of elements currently in the array
          break
      except ValueError:
          print("Invalid input. Please enter integers only.")

  # Check for empty array and print message
  if N == 0:
      print("Array is empty.")

  # Loop for iteration and value generation
  for i in range(max(N, LB), S):
      new_arr, success, error_msg = insert(arr, S, N, i,LB)  # Use current index for value generation

      if success:
          N += 1  # Increment N after successful insertion
          print("Inserted element:", new_arr[i])
      else:
          print("Error:", error_msg)
          break  # Exit the loop on error

  # Print final array and full message (if applicable)
  print("Final array:", arr)
  if N == S:
      print("Array is full.")

if __name__ == "__main__":
  main()
