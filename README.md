# Starwars---Layered-Business-Logic
Técnica de Layering para desarrollo de aplicaciones.

Genera las siguientes modificaciones del código fuente:
1. Endpoint `GET /` list the Star wars movies.
  	 * Sort them by ID in ascending order.
![Snag_f0c6958](https://user-images.githubusercontent.com/131479500/233696219-c2d19f49-7ea4-46a2-9a45-baea4914d148.png)

2. Create a new Endpoint to list all character names from a movie.
  	 * You pass an ID as a URL parameter
![Snag_f0c8f4f](https://user-images.githubusercontent.com/131479500/233696249-f4529694-334b-4aec-9d34-d76476428711.png)


Refactoriza el código para dividirlo en capas (layers)
Cada layer está especificado por un módulo de python (carpeta física). 
La capa de presentación representa el código que contiene la librería de flask (los endpoints)
![Snag_f0cc9b8](https://user-images.githubusercontent.com/131479500/233696290-6b2b7836-bb20-4f37-8ea2-a4ea6491e8d8.png)

![Snag_f0cd476](https://user-images.githubusercontent.com/131479500/233696300-5dc97a05-d84f-46bd-b105-3eb0b479df6c.png)





