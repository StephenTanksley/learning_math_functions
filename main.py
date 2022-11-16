def coterminal(start_angle, range_start, range_end, original_angle=None, full_rotations=0):
  """
  :param: start_angle - refers to the angle given for which the coterminal angle is sought.
  :param: range_start - refers to the starting angle, in this case 0.
  :param: range_end - refers to the ending angle, in this case 360 denoting a positive angle.
  :param: original_angle - refers to the angle which was passed in during the first iteration of the recursive function.
  :param: full_rotations - The number of full 360 degree rotations required to find coterminal angle.
    e.g. 
  """
  
  if original_angle is None:
    original_angle = start_angle
    
  if range_start <= start_angle <= range_end:
    return f"{original_angle} is coterminal with {start_angle} after {abs(full_rotations)} {'clockwise' if full_rotations < 0 else 'counterclockwise'} rotations around origin."

  if start_angle > 0:
    full_rotations -= 1
    updated_start = start_angle - 360
    print(f"{start_angle} - 360 degrees = {updated_start} degrees")
    
  elif start_angle < 0:
    full_rotations += 1
    updated_start = start_angle + 360
    print(f"{start_angle} + 360 degrees = {updated_start} degrees")

  if full_rotations != 0:
    print(f"Rotated {abs(full_rotations)} times {'clockwise' if full_rotations < 0 else 'counterclockwise'} around origin.", '\n')
  return coterminal(updated_start, range_start, range_end, full_rotations=full_rotations)


print(coterminal(-1624, 0, 360))