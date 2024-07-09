def number_in_words(n):
    if n == 1000:
        return "one thousand"

    one_nine = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    eleven_nineteen = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    hundreds = "hundred"
    a = "and"

    if n < 10:
        return one_nine[n]
    elif 10 < n < 20:
        return eleven_nineteen[n - 10]
    elif n < 100:
        tens_part = tens[n // 10]
        if n % 10 != 0:
            one_nine_part = one_nine[n % 10]
            return tens_part + one_nine_part
        else:
            return tens_part
    elif n < 1000:
        hundreds_part = one_nine[n // 100] + hundreds
        if n % 100 != 0:
            remainder = a + number_in_words(n % 100)
            return hundreds_part + remainder
        else:
            return hundreds_part

def count_letters(word):
    return len(word.replace(" ", "").replace("-", ""))

total_letters = sum(count_letters(number_in_words(i)) for i in range(1, 1001))

print(total_letters)
