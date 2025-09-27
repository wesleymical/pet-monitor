PS C:\Users\mical\Documents\pet-monitor> tree /f
Listagem de caminhos de pasta
O número de série do volume é 08DD-217A
C:.
└───sensor_monitor
    │   docker-compose.yml
    │   iniciar_sensor_monitor.bat
    │   parar_sensor_monitor.bat
    │   README.md
    │
    ├───backend
    │       .dockerignore
    │       Dockerfile
    │       main.py
    │       requirements.txt
    │
    ├───data
    │       dados.json
    │
    └───frontend
        │   .dockerignore
        │   Dockerfile
        │   home.py
        │   requirements.txt
        │
        └───pages
                1_Monitor.py
                2_Simulator.py
                3_Dashboard.py
