'''
Python function that finds the length of the last word.
'''

def word_length(skaehub_string):
   initial_value = 0

   stripped_string  = skaehub_string.strip()

   for i in range(len(stripped_string)):
      if stripped_string[i] == " ":
         initial_value = 0
      else:
         initial_value += 1
   return initial_value


#invokinf the function
print(word_length("Hello Skae-hub squad!"))