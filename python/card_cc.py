def check_cc(card_number: str) -> int:
  # splitted_card_number = card_number.split('')
  acc = 0
  it_times = 0
  reversed_card_number = str(card_number)[::-1]
  for n in reversed_card_number:
    if ((it_times % 2) == 0):
      acc += int(n) * 1
      print(f'{n}')
    else:
      acc += int(n) + int(n) * 2
      print(f'{int(n) * 2}')
    it_times +=1
  print(it_times, acc, card_number, reversed_card_number)
  return acc % 10

print(check_cc(4028743156781887))