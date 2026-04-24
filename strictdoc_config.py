from strictdoc.core.project_config import ProjectConfig, ProjectFeature


def create_config() -> ProjectConfig:
    config = ProjectConfig(
        project_title="ACC Requirements Specification",
        exclude_doc_paths=["README.md", ".venv", "refs"],
        exclude_source_paths=["refs", "assets", "발표자료", "*.pdf", "*.pptx", "*.docx", "*.xlsx"],
        project_features=ProjectFeature.all()
    )
    return config
