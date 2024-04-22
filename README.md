# Talana Kombat

## Ejercicio

### Talana Kombat JRPG

Talana Kombat es un juego donde 2 personajes se enfrentan hasta la muerte. Cada personaje tiene 2
golpes especiales que se ejecutan con una combinación de movimientos + 1 botón de golpe

###  Como ejecutar

```
python3 main.py
```

### A mejorar

Dentro de los aspectos a mejorar, destaco:
* Una mejor manera de informar los golpes dados.
* Uso de test unitarios.
* Seteo de las peleas.

## Preguntas Generales

1. Supongamos que en un repositorio GIT hiciste un commit y olvidaste un archivo. Explica cómo se
soluciona si hiciste push, y cómo si aún no hiciste. De ser posible, que quede solo un commit con los cambios.
	* Si se hizo el push, esto se puede solucionar de la manera: Se agrega el archivo con **git add archivo**, se hace el commit **git commit --ammend** para cambiar el mensaje del commit si es necesario y finalmente **git push --force**.
	* En cambio, si no se ha realizado el push, se trabaja de manera normal, siguiendo con **git add archivo**, **git commit -m "archivo olvidado** y finalmente **git push**.
2. Si has trabajado con control de versiones ¿Cuáles han sido los flujos con los que has trabajado?
	* He trabajado principalmente con GitHub Flow, desde la rama master, principalmente con develop, feature y hotfix, para cambios rápidos de realizar, antes de un release de las features encontradas en develop.
3. ¿Cuál ha sido la situación más compleja que has tenido con esto?
	* Dentro de los problemas, puede ser la complejidad de comunicación entre los desarrolladores del repositorio para evitar sobrescribir archivos, e igualmente sobre el mismo tema cuando hay que devolver los cambios desplegados a producción.
4. ¿Qué experiencia has tenido con los microservicios?
	* He creado microservicios básicos en las apps de django, tales como servicios de autenticación, y sus vistas asociadas en ellas.
5. ¿Cuál es tu servicio favorito de GCP o AWS? ¿Por qué?
	* Solamente he trabajado con AWS, dentro de sus bondades destaco S3 a la hora de trabajar con almacenamiento y EC2 para la implementación de servidores.
