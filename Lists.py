bicycles = ['trek', 'redline','specialized']
print("returns all:", bicycles) # returns its representation of the list
# includes square brackets
print("returns specific:", bicycles[0]) # returns a single item with no quotation mark.
print(bicycles[0].title()) # title() capitalizes first letter.
print(bicycles[-1]) # access the last item in a list.

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
