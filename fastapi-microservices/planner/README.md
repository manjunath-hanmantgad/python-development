1. Define models for user and events.
   a. Models will describe how data will be stored , inputed and represented.
   b. User field contains:
   [email,password,username,events]
   and event field contains:
   [title,image,desc,tags,location]

Each user will have Events field. (this will tell list of events which the user have ownership of.)

Now define the User model.

2. Now, setup routing system for API.
   a. Routing system for events and users.
   b. User route = [sign-in, sign-out,sign-up]
Authenticated user will have access for create,update,delete an event.

3. Next is to implement routes for event operations.

4. Next step is setting up database

   - Setting up SQLModel
   - CRUD operations on sql db using sqlmodel
   - setup mongodb
   - CRUD operations on mongodb using beanie

a. Setting up SQLMOdel
   - install sqlmodel library
   - Table = object for storing data (storing events)
   - Rows class which is a event
   - database transaction using session class

b. Methods used from session class
   - add() -adding db object to memory.
   - commit() - flushing transactions present in session
   - get()- takes 2 params : model and ID of document which is requested. This is used to retrieve single row from database.

5. Creating a database
   - Created using create_engine()method.
   - database url as argument