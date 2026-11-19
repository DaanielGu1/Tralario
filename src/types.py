type NomeAluno = str
type Curso = str
type TipoCurso = str
type AnoSemestre = tuple[int, int]
type RespondeuQuestionario = bool
type DataSchemaAlunos = dict[str, tuple[NomeAluno, Curso, TipoCurso, AnoSemestre, RespondeuQuestionario]]
type DataSchemaMatric = dict[str,float]
type DataSchemaCursos = dict[str,str]