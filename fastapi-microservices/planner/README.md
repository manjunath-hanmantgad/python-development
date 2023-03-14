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