class DataFileError(Exception):
    """Erro no arquivo de dados."""
    pass


class DataValidationError(Exception):
    """Erro na validação dos dados."""
    pass


class ClusteringError(Exception):
    """Erro no processo de clusterização."""
    pass