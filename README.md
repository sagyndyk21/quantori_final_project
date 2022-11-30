# Quantori Python Academy final project
This project implements processes as Transcription (DNA -> RNA) and Translation (RNA -> Protein). Corresponding
functions `convert_dna_to_rna` and `convert_dna_to_rna` are defined in [project/script.py](blob/main/project/script.py)
Also there is the function in ([project/gc_ratio_plot.py](blob/main/project/gc_ratio_plot.py)) plotting the
[GC-content](https://en.wikipedia.org/wiki/GC-content) of the DNA molecule.

## Run project
First get the project to your local machine:
```commandline
git clone https://github.com/sagyndyk21/quantori_final_project.git
```
[Optional] You can run project locally (Need to configure your local Postgres DB and change connection parameters
of the project):
```commandline
cd quantori_final_project
python3 -m venv venv
source ./venv/bin/activate
pip install -r ./requirements.txt
```
[Recommended] Run project with `docker-compose` (Make sure that Docker and docker-compose are installed) <br />
There are files in `project/data/inputs/` and you can add your inputs to corresponding txt files (There are
some input examples exist already) <br />
Then to start project run command in the root of the cloned project:
```commandline
docker-compose up
```
As a result docker containers will be created and run. There will be run script.py on input sequences defined in
`project/data/inputs/` and in the terminal will be printed results. Docker container of the project will continue
to work and you can enter the project via bash with the command (in the another terminal session from the project root):
```commandline
docker-compose exec project bash
```
It will start bash session for the project. There you can explore the file system and run scripts/functions/tests and etc. <br />
You can run `script.py` for your concrete example with 3 possible modes: `dna_to_rna`, `rna_to_protein`, `gc_content`.
Mode will be second argument and your input sequence as third argument. For example:
```commandline
python script.py rna_to_protein GCUAACUAACAUCUUUGGCACUGUU
```
Also it is possible to run the specific function for the input via docker-compose. To do so you can run:
```commandline
mode=<desired mode from possible options> sequence=<input sequence> docker-compose up
```
Example:
```commandline
mode=dna_to_rna sequence=CCCGTCCTTGATTGGCTTGAAGAGAAGTTT docker-compose up
```
At the end you can click Ctrl+C in the initial session or run command in another terminal session from project root:
```commandline
docker-compose down
```
