FROM continuumio/miniconda3
# Variables de entorno
# ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1
# Generando un directorio de trabajo
RUN mkdir -p /codigo
WORKDIR /codigo
# Copiando la lista de requerimientos para django
COPY requirements.txt .
# Creando un entorno virtual
RUN conda create -n ende python=3.9 
RUN conda install -n ende --file requirements.txt
SHELL ["conda", "run", "-n", "ende", "/bin/bash", "-c"]
ENV PATH /opt/conda/envs/ende/bin:$PATH
RUN /bin/bash -c "source activate ende"
# Demonstrate the environment is activated:
RUN echo "Make sure django is installed:"
RUN python -c "import django"

