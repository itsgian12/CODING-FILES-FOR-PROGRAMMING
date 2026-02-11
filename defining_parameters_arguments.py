#parameters /// to define
# Default parameters
def say_hello(name='New Customer', emoji="😀"):
    print(f'hellloooo {name}{emoji}')

#arguments /// to call or invoke   
say_hello('gian', ' 😊')
say_hello('micah', ' 🥰')
say_hello()

#keyword arguments
say_hello(name='bibi', emoji='🥰')
say_hello('timmy')