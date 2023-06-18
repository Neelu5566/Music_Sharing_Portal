# Music-Sharing-Portal

#### It is a website built using Django.

## The following conditions are applied on this website.

### Project Details:

* Create a website that allows users to upload music and share it with each other after logged-in.
* Users should be able to register on the platform using Email.
* Users should be able to log in to the platform using Email and password.
* Users should be able to upload music files on the platform.
* Users can upload music files as public/private/protected.
* Public Music File: Visible to all the users
* Private Music File: Visible to the user who has uploaded it
* Protected Music File: Visible to users who have access to the file using email
* Protected Music File Details:
  When user uploads any music file as a protected music file, ask him/her to add multiple email addresses.
* Check if the user with any mentioned email address is registered on the portal or not.
* If there is a user with email in allowed emails list, then show him/her that music file.
* When the user login, show him/her all the music files for which he/she has access on the homepage. (Music files that are uploaded by logged-in user, all public * music files uploaded by other users, and protected files for which logged- in user has access)
* For checking access to protected music files, use the logged-in user's email.
