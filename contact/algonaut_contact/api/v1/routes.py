from .resources.contact import Contact

routes = [
    # submit the contact form
    {'/submit' : [Contact, {'methods' : ['POST',]}]},
]
