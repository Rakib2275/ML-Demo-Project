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

@dataclass
class DataTransformationArtifact:
    transformed_object_file_path:str 
    transformed_train_file_path:str
    transformed_test_file_path:str


@dataclass
class ClassificationMetricArtifact:
    f1_score:float
    precision_score:float
    recall_score:float



@dataclass
class ModelTrainerArtifact:
    trained_model_file_path:str 
    metric_artifact:ClassificationMetricArtifact
