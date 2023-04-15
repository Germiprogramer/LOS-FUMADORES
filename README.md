# LOS-FUMADORES

El problema de los fumadores consiste en tres fumadores que tienen un recurso (entre papel, tabaco y fuego) y necesitan de los otros dos para fumar. Un agente externo se encarga de colocar en una mesa dos recursos al azar, recogiéndolos y poniendo otros una vez el fumador ha terminado.

Para realizar el ejercicio, vamos a crear dos clases distintas: el agente y los fumadores, quienes realizarán las tareas ya mencionadas. Tendremos cuatro hilos de ejecución, 1 agente y los tres fumadores. Para coordinar que las tareas no se bloqueen entre ellas, haremos uso de un semaforo, realizando acquire cada vez que se pongan los ingredientes y release cada vez que se quiten. Así, dos fumadores no podrán acceder a la vez a un mismo elemento de le mesa.
