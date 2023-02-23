### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
  Python is a OOP language that has built-in data structures. Python could be used for back-end development. JS is a scripting language used to create inverative web sites. It is used for both front-end and back-end development.

- Given a dictionary like `{"a": 1, "b": 2}`: , list two ways you
  can try to get a missing key (like "c") _without_ your programming
  crashing.
  You can use get(key name, default value) methode. If the key is not in the dictionary then a default value will be returned.
  Use a try and except block. If the key is missing the except block will catch the error

- What is a unit test?
  Unit test is for testing a small part of the entire code. Example would be to test a function or a route.

- What is an integration test?
  Integration test involves testing multiple units to see if they work together

- What is the role of web application framework, like Flask?
  Web application framework is used to design and support development of web applications including web services, and web APIs.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

- How do you collect data from a URL placeholder parameter using Flask?
  request.args.get("")

- How do you collect data from the query string using Flask?
  Query string is part of the URL. request.arge[<key>] can be used to get the data from the query string.

- How do you collect data from the body of the request using Flask?
  request.form[""]

- What is a cookie and what kinds of things are they commonly used for?
  Cookie is a way to store small amount of data in the browser. Cookie is a key value pair which could be sent using a request header. Cookies can include information about a user's id, contents of a shopping cart or what the user clicked on.

- What is the session object in Flask?
  HTTP is a stateless protocol. Each request has no knowledge of any previous reqeusts. Sessions is used to store information related to a user across different requests.

- What does Flask's `jsonify()` do?
  jsonify() function returns a Response Object. It allows you to return JSON-formatted data from a route.
