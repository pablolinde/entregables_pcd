# entregables_pcd

- El primer entregable (organizador_universidad) consiste en un sistema de gestión de usuarios de universidad que permite gestionar investigadores, profesores asociados, profesores titulares y estudiantes.

- El segundo entregable implementa un sistema de monitoreo de temperaturas en tiempo real utilizando Kafka para la comunicación entre productores y consumidores. El sistema, diseñado como un singleton, procesa las temperaturas recibidas aplicando diferentes estrategias (media, desviación estándar y cuantiles) mediante el patrón strategy, y maneja eventos específicos (umbral superado o aumento brusco) con una cadena de responsabilidad. Los tests verifican el correcto funcionamiento del singleton, el procesamiento de datos y los cálculos estadísticos.
