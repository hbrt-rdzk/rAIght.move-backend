from typing import Any

from processors.base import Processor


class Pipeline:
    def __init__(self, processors: list[Processor]) -> None:
        super().__init__()
        self.propcessors = processors

    def run(self, data: Any) -> Any:
        for processor in self.propcessors:
            data = processor.process(data)
            processor.update(data)
            data = processor.data
        return data
