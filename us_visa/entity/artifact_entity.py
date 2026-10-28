from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    trained_file_path: str
    test_file_path: str

    def __init__(
        self,
        trained_file_path: str = None,
        test_file_path: str = None,
        training_file_path: str = None,
        testing_file_path: str = None,
    ):
        self.trained_file_path = trained_file_path or training_file_path
        self.test_file_path = test_file_path or testing_file_path

    @property
    def training_file_path(self) -> str:
        return self.trained_file_path

    @property
    def testing_file_path(self) -> str:
        return self.test_file_path


@dataclass
class DataValidationArtifact:
    validation_status: bool
    message: str
    drift_report_file_path: str
